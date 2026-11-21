# Nhật ký nguồn đợt 3

Mục đích: exact-record abstract recovery và kiểm phiên bản cho pilot, không phải broad formal database search. Chọn 24 ID trước đọc abstract, có chủ đích cho boundary cases; 77 chưa lọc. Chỉ dùng title/abstract cho suggestions; chưa review Table/Figure/full-text evidence.

24 request trực tiếp tới URL primary/repository/registry, tối đa 4 đồng thời, timeout 25s; log raw/fetch timestamp/HTTP/URL/SHA256 trong fetch_log.json. Kết quả HTTP không thành công: P002 429, P014 403. Chi tiết trong fetch_log.json. Không bypass rate limit/paywall. Abstract P002/P014 dùng snapshot audit có provenance, không khẳng định fetch mới thành công.

4 supplement request: P050 official ICLR proceedings, P083 SIGWEB conference TOC, P090 ACM publisher, N008 publisher landing. P050/P083/N008 thành công, P090 403. P090 vẫn UNSURE, không EC-A. Kiểm publication P050 qua title, proceedings và authors; chưa so byte/full-text giữa versions.

Hai lượt web lookup, mỗi lượt 4 exact-title queries:
- MuseumQA Abstract; Evaluating a Radius-based Pipeline; Claim-Aware Scientific RAG; DeclineCraft.
- MuseumQA exact title + abstract dataset 23149; Sufficient Context exact title + ICLR2025; RAGChecker abstract fine-grained; VISCOUNTH abstract.

Web chỉ chỉ đường đến primary sources. Không dùng hit counts làm PRISMA/nguồn native DB. Không lấy số 23149 trong câu query như kết quả đã kiểm. P083 dùng abstract SIGWEB, không lấy trích đoạn PDF search thành full-text review. P050 dùng official ICLR page, không dựa riêng vào search snippet. N008 dùng Crossref abstract cho scope; publisher/registry khác cách ghi tên venue/DOI cần kiểm kỹ trước nhận IC-T, không suy quality từ DOI.

Nguồn excerpt chính xác có trong source_evidence_index.csv, tối đa 18 từ mỗi paper trong CSV public. Raw pages/abstract đầy đủ chỉ trong gói Drive. Agent không đồng bộ/ghi Zotero bằng API; không dùng token nào. Agent không gửi tin hoặc cấp thêm quyền chia sẻ.
