"""Run a bounded access/search pilot, recording payloads and actual returned counts."""
import csv
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

directory = Path(__file__).resolve().parent
raw = directory / "search-pilot"
raw.mkdir(exist_ok=True)
date_filter = "from_publication_date:2016-01-01,to_publication_date:2026-11-21"
subjects = {
    "domain": '(museum OR "cultural heritage") AND "question answering"',
    "sufficiency": '"retrieval augmented generation" AND ("sufficient context" OR "evidence sufficiency" OR abstention)',
    "citation": '"retrieval augmented generation" AND ("citation accuracy" OR "evidence attribution" OR "claim verification")',
}
jobs = [
    (f"OA-{key}", "OpenAlex", term, "search", date_filter,
     "https://api.openalex.org/works?" + urlencode({
         "search": term, "filter": date_filter, "per_page": 10,
         "select": "id,doi,display_name,publication_year,primary_location",
     }), "openalex")
    for key, term in subjects.items()
]
jobs.extend([
    ("S2-domain", "Semantic Scholar", "museum cultural heritage question answering", "paper/search query", "year=2016-2026",
     "https://api.semanticscholar.org/graph/v1/paper/search?" + urlencode({
         "query": "museum cultural heritage question answering", "year": "2016-2026",
         "limit": 10, "fields": "paperId,title,year,externalIds,url",
     }), "semantic"),
    ("IEEE-domain", "IEEE Xplore", subjects["domain"], "queryText", "Chưa áp bộ lọc",
     "https://ieeexplore.ieee.org/search/searchresult.jsp?" + urlencode({"queryText": subjects["domain"]}), "html"),
    ("ACM-domain", "ACM DL", subjects["domain"], "AllField", "Chưa áp bộ lọc",
     "https://dl.acm.org/action/doSearch?" + urlencode({"AllField": subjects["domain"]}), "html"),
])

def run(job):
    identifier, source, query, field, filters, url, kind = job
    started = datetime.now(timezone(timedelta(hours=7))).isoformat(timespec="seconds")
    counts = ("", "")
    notes = ""
    seeds = []
    try:
        request = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; academic metadata pilot)"})
        with urlopen(request, timeout=14) as response:
            status = response.status
            data = response.read(750_000)
    except HTTPError as error:
        status = error.code
        data = error.read(100_000)
    except (URLError, TimeoutError) as error:
        status = "CONNECT_ERROR"
        data = str(error).encode()
    filename = f"{identifier}.{'html' if kind == 'html' else 'json'}"
    if status != 200:
        filename = f"{identifier}.error.txt"
        notes = "Chưa xác minh tìm kiếm và xuất metadata."
    elif kind == "html":
        notes = "Có phản hồi HTML; cần kiểm giao diện kết quả và quyền xuất. Chưa xác nhận record."
    else:
        value = json.loads(data)
        if kind == "openalex":
            hits = value["meta"]["count"]
            records = value["results"]
        else:
            hits = value["total"]
            records = value["data"]
        counts = hits, len(records)
        seeds = [row.get("display_name") or row.get("title") for row in records]
        notes = "Chỉ lấy trang đầu để thử kết nối và xem khả năng trả metadata. Không dùng số hit làm số đã lọc."
    (raw / filename).write_bytes(data)
    return {
        "run_id": identifier, "stage": "PRE_LOCK_PILOT", "database": source,
        "exact_query": query, "fields": field, "filters": filters, "run_at": started,
        "request_url": url, "http_status": status, "reported_hits": counts[0],
        "exported_sample_records": counts[1], "raw_file": f"search-pilot/{filename}",
        "sha256": hashlib.sha256(data).hexdigest(), "notes": notes,
    }, seeds

with ThreadPoolExecutor(max_workers=4) as pool:
    output = list(pool.map(run, jobs))
with (directory / "query-runs.csv").open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=output[0][0])
    writer.writeheader()
    writer.writerows(row for row, _ in output)
for row, titles in output:
    print(row["run_id"], row["http_status"], row["reported_hits"], row["exported_sample_records"])
    if titles:
        print(titles[:5])
