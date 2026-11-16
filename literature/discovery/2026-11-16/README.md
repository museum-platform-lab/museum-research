# Literature discovery — Museum Platform

Ngày: 16/11/2026. Trạng thái: danh mục ứng viên để chuẩn bị literature review cho hai paper; CHƯA SCREENING, CHƯA INCLUDED, CHƯA XÁC NHẬN GAP.

## Kết quả đợt này

- 26 truy vấn web theo sáu nhóm và các lượt bổ sung seed/exact-title.
- 405 dòng nguồn trong hồ sơ thu nhận: 386 kết quả web trả về, 10 seed có sẵn và 9 metadata match từ Crossref. Đây là dòng nguồn, không phải số paper hay số PRISMA.
- 114 biểu diễn bibliographic candidate sau chuẩn hóa URL; gộp 24 biểu diễn trùng DOI hoặc title chuẩn hóa chính xác, còn 90 bản ghi ứng viên.
- 90 bản ghi có title/metadata lấy từ trang nguồn hoặc Crossref. Điều này không xác nhận nội dung khoa học, quyền dataset, chất lượng venue hay sự liên quan cuối cùng.
- 2 cặp cần xem lại quan hệ preprint/bản xuất bản; KHÔNG coi 90 bản ghi là chắc chắn 90 nghiên cứu độc lập.
- 254 lượt nguồn phụ trợ được giữ nguyên trong auxiliary_sources.csv: có mirror, repository, trang tác giả, tin tức và lead chưa xác định. Không coi toàn bộ nhóm này là paper bị loại. Có thể còn công trình mới cần nhận diện từ đây.
- Có DOI ở 61 bản ghi; có trường abstract/description ở 78 bản ghi. Abstract tự động có thể là description của trang, cần đối chiếu khi screening.
- Thiếu authors: 0; thiếu year: 0. Metadata tác giả/năm chưa được người kiểm chéo; year có thể là năm preprint, không phải năm venue cuối.
- 43 bản ghi có ngày đủ chi tiết không sau 16/11/2026; 47 bản ghi cần kiểm ngày/version (nhiều trang chỉ nêu năm/tháng). Không suy ra ngày công bố từ ngày crawl của web search.
- 0 full-text đã được review; 0 paper included chính thức. Không tạo evidence table đầy đủ hay PRISMA từ số discovery này.

## Sáu nhóm chủ đề

| Tag | Chủ đề | Số bản ghi có tag |
|---|---|---:|
| T1 | Heritage/museum QA | 23 |
| T2 | Benchmark/dataset/evaluation | 42 |
| T3 | Retrieval/hybrid/multi-hop/graph | 66 |
| T4 | Claim verification/citations/attribution | 18 |
| T5 | Sufficiency/abstention/conflict | 14 |
| T6 | Vietnamese/multilingual consistency | 12 |

Tags được gợi ý từ nhóm truy vấn và title, có thể chồng lấn hoặc sai. Đây không phải kết quả screening; không cộng các số thành tổng paper.

## File nên mở

1. master_paper_list.csv: bảng chính, UTF-8 BOM để mở Excel/Sheets. Có paper_id, title, authors, year, DOI/link, metadata source, dates, topic tags và trạng thái.
2. zotero_import.ris: nhập Zotero bằng File → Import. Dùng loại RIS GEN khi chưa chốt publication type, tránh tự gán journal/conference. Tags chủ đề được giữ.
3. references.bib: bản BibTeX tương ứng để trao đổi/trích dẫn; metadata vẫn cần xác nhận trước khi viết bài. Nếu đã nhập RIS thì không nhập tiếp toàn bộ BibTeX vào cùng collection để tránh tạo trùng.
4. search-log.md và raw/search_*.json: query nguyên văn, ngày, nguồn và kết quả web nhận được.
5. raw_hits.csv, auxiliary_sources.csv: toàn bộ lượt nguồn, kể cả lead chưa nhận diện được; không mất dữ liệu khi gom.
6. dedup_log.csv: gộp DOI/title chính xác; possible_duplicates.csv: hàng đợi kiểm tra version/cặp tương tự.
7. raw/metadata/ và raw/crossref_*.json: metadata response, lỗi truy cập và provenance để đối chiếu. Không chứa full-text PDF.
8. build_catalog.py, enrich_seeds.py, package_results.py, stats.json, validation.json: cách chuẩn hóa, enrich, đóng gói và kiểm tra bookkeeping. Có thể tái dựng từ log/cache; chạy script không tái tạo hoàn toàn xếp hạng web ở thời điểm khác.

## Giới hạn và quy tắc dùng

Đây là discovery, không phải tìm hết mọi paper. Search engine trả danh sách có xếp hạng và giới hạn; chỉ ghi số đã nhận, không giả định tổng kết quả cơ sở dữ liệu. OpenAlex anonymous search trả 503 nên chưa harvest từ nguồn đó. Chưa chạy tìm kiếm có hệ thống trên IEEE/ACM/Scopus hoặc Semantic Scholar; các link nhà xuất bản trong kết quả web không tương đương một lượt search database chính thức.

Crossref dùng để kiểm metadata, không dùng điểm relevance của nó làm quyết định INCLUDE. DOI arXiv và DOI venue có thể khác nhau; bản arXiv không tự bị loại ở discovery. Hai cặp đang chờ xem lại: Correctness is not Faithfulness... và DRAGged...; cần xác nhận version và chọn cách biểu diễn trong review trước khi tính số nghiên cứu.

Không dùng bản tổng hợp AI hoặc NLI để chứng nhận gold. Không tự xem presence của DOI/abstract là quality gate. Chưa có human crosscheck trong đợt này. Không tự thêm dữ liệu vào Zotero qua API, không dùng key đã gửi trong ảnh và không thay đổi source repo.

## Việc tiếp theo

- Duyệt lead chưa nhận diện và hai cặp version; kiểm ngày/venue/preprint; sửa metadata khi có bằng chứng.
- Chốt review questions, phạm vi, IC/EC và protocol trước lượt tìm chính thức. Dùng discovery để kiểm độ phủ từ khóa, không đổi discovery thành formal included bằng cách đổi nhãn.
- Chạy tìm theo nguồn thích hợp; lưu exports gốc. Sau đó title/abstract screening hai người trên mẫu, full-text screening, snowball và evidence extraction có page/section/table.
- Nhập RIS vào collection riêng; chưa tải PDF hàng loạt trước khi biết quyền truy cập và mức liên quan.

## Bảo mật và phạm vi lưu trữ

Gói này chỉ có metadata, log và script; không có API key, credential, PDF trả phí hoặc dữ liệu hội thoại. Không kết luận quyền phân phối của dataset từ license của metadata. Mọi claim nghiên cứu và số liệu bài báo phải được kiểm tra từ nguồn gốc khi đọc full-text.

## Vị trí của snapshot trong Git

Các file CSV/BibTeX/RIS, log tìm kiếm, dedup, thống kê và validation nằm cạnh README này. Các đường dẫn raw/, raw_hits.csv, auxiliary_sources.csv và script được nhắc phía trên nằm trong gói ZIP trên Drive, không được commit vào snapshot này. Manifest cạnh đây ghi file ID, URL, số byte và SHA-256 của từng bản đã upload. SHA-256 là giá trị tính từ bản local; Drive mới được kiểm tra bằng ID/tên/số byte, chưa tải lại để đối chiếu SHA-256.

Để kiểm tra hoặc tái dựng: tải ZIP theo manifest, giải nén vào thư mục làm việc riêng; chạy `python build_catalog.py` rồi `python package_results.py`. Script dùng cache/log của đợt discovery; nếu chạy lại trên mạng, metadata có thể thay đổi. So sánh kết quả với stats.json và validation.json đã commit. Không suy ra một review mới đã hoàn tất từ việc script chạy thành công.
