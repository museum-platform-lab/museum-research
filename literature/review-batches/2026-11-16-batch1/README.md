# Đợt 1 — Rà metadata, phiên bản và lead discovery

Ngày: 16/11/2026. Đầu vào là snapshot discovery 90 bản ghi và 254 lượt nguồn phụ trợ. Đây là đợt làm sạch danh mục trước protocol/screening, không phải tìm kiếm rộng đợt 2.

## Kết quả

- Giữ đủ 90 bản ghi gốc trong metadata_audit_all90.csv; gom 2 cặp thành 88 nhóm phiên bản thư mục. Không xóa bản preprint hoặc khẳng định các thí nghiệm giữa hai bản giống hệt nhau.
- P044/P045: Correctness is not Faithfulness..., preprint 2024 và bản ICTIR 2025, cùng bốn tác giả và nội dung abstract tương ứng. P049/P051: Google Research liên kết trực tiếp arXiv:2506.08500; cùng tác giả, tên hiển thị thay đổi. Bằng chứng và giới hạn trong version_decisions.csv. Đây là quyết định hỗ trợ bởi AI, còn chờ kiểm chéo con người.
- Kiểm 61 DOI có sẵn: 61 trả HTTP 200 sau retry có giới hạn. So khớp title gồm subtitle và chuẩn hóa cụm Retrieval-Augmented Generation/RAG; registry resolution không chứng minh chất lượng nghiên cứu. 29 mục gốc không có venue DOI đã xác minh.
- 65/90 mục có metadata venue; 25 chưa có. Không gán peer-reviewed từ việc có DOI hoặc venue.
- Rà toàn bộ 254 lượt nguồn / 241 URL khác nhau. Nhận diện 10 tên bài qua Crossref và 3 mã arXiv, bổ sung 13 ứng viên; xem new_candidates_from_leads.csv.
- Danh mục hiện tại: 88 nhóm gốc + 13 ứng viên bổ sung = 101 bản ghi trong master_catalog_batch1.csv. Đây chưa phải số nghiên cứu độc lập hoặc số included.
- Ngày: cả 90 bản ghi gốc có bằng chứng metadata cho một phiên bản công khai không sau 16/11/2026. Có trường hợp chỉ xác định được theo khoảng năm/tháng; không tự tạo ngày chính xác. Không đồng nghĩa mọi phiên bản venue đã công bố trước ngày chốt.
- Phân biệt cover date và online date: ví dụ P010/P011/P067/P070 có citation date 12/2026 nhưng Crossref cho ngày online trước 16/11. P020 có venue date chỉ tháng 11/2026; ghép đúng title/tác giả với preprint arXiv:2608.22228 để xác nhận có phiên bản trước mốc chốt. Chi tiết từng nguồn/ngày trong metadata_audit_all90.csv.
- Không screening title/abstract, không đọc full-text để trích xuất kết quả, chưa chạy kiểm chéo độc lập và chưa có included chính thức. Abstract chỉ được đối chiếu để nhận diện hai nhóm phiên bản, không dùng để xác nhận gap.

## Trạng thái lead theo 241 URL

| Trạng thái | Số URL |
|---|---:|
| NEW_CANDIDATE_IDENTIFIED_FROM_OLD_LEAD | 13 |
| EXISTING_PAPER_REPRESENTATION | 51 |
| UNRESOLVED_DOCUMENT_TITLE | 7 |
| PAPER_LEAD_UNRESOLVED | 15 |
| INDEX_TOOL_OR_AUTHOR_PAGE | 15 |
| CODE_DATA_OR_MODEL_RESOURCE | 48 |
| EXISTING_PAPER_LEAD_TRUNCATED_TITLE | 16 |
| CONTEXT_OR_DISCUSSION_SOURCE | 62 |
| SECONDARY_GUIDE_OR_BIBLIOGRAPHY | 10 |
| THESIS_OR_LONG_FORM_DOCUMENT | 3 |
| OTHER_RESOURCE_REQUIRES_REVIEW | 1 |

Các mục unresolved/resource vẫn được giữ; không coi đây là quyết định EXCLUDE. Mỗi lượt trong 254 dòng vẫn có ID/URL/trạng thái/lý do. Loại nguồn là triage, không phải đánh giá chất lượng hay tiêu chí môn đã khóa.

## File

- master_catalog_batch1.csv: danh mục làm việc 101 mục, giữ ID Pxxx; Nxxx là ứng viên phục hồi từ lead cũ.
- metadata_audit_summary90.csv: tóm tắt rà metadata 90 mục gốc.
- metadata_audit_all90.csv: đầy đủ bằng chứng ngày và source URL; cùng raw API responses nằm trong archive trên Drive nếu không có cạnh README trong Git.
- version_decisions.csv: hai nhóm phiên bản, nguồn và giới hạn quyết định.
- lead_triage_all254.csv: toàn bộ lượt lead và cách xử lý.
- new_candidates_from_leads.csv: 13 ứng viên bổ sung, chưa đánh giá mức liên quan.
- zotero_batch1.ris / references_batch1.bib: bản nhập thư viện đã gom nhóm phiên bản; không import chồng toàn bộ cả bản 90 và 101 vào cùng collection nếu chưa xử lý trùng.
- batch1_stats.json / validation_batch1.json: số đếm và kiểm tra nhất quán.
- raw/: API metadata response, mã HTTP, URL và thời điểm truy cập. Không dùng indexed/created/deposited của Crossref làm ngày công bố.

## Giới hạn và việc còn lại

Bằng chứng ở mức metadata; không xác nhận toàn văn truy cập được, tính đúng của claim nghiên cứu hoặc quyền dùng dataset. Dữ liệu registry có thể sai/backdate; cần đối chiếu bản gốc khi đọc full-text. Các ngày giữ precision và loại online/print/preprint. Ba nhóm ngày không rõ: khoảng thời gian bao trùm mốc chốt, cover date sau mốc mà chưa biết online date, hoặc metadata thiếu; không loại âm thầm.

Các ứng viên mới được giữ bất kể venue/chủ đề có vẻ phù hợp hay không, chờ protocol và screening. DOI của preprint không chứng minh đã bình duyệt. Không gọi 101 mục là corpus review cuối hoặc tạo PRISMA từ số đếm này.

Đợt tiếp theo: soạn protocol và IC/EC v0.1 theo hai hướng paper, chốt nguồn/năm/cú pháp truy vấn và cách kiểm chéo; sau đó mới screening và truy vấn bổ sung theo khoảng thiếu. Không tự đánh dấu protocol đã được giáo viên duyệt.

## Bản lưu trong Git

Đây là kết quả mới, không ghi đè snapshot discovery 90 mục ngày 16/11. File đầy đủ `metadata_audit_all90.csv`, `raw/` và script có trong ZIP trên Drive; xem external-data-manifest.json. Danh mục 101 mục là view mới ở đợt 1, không phải thay đổi ngược số liệu của đợt discovery.

Hai cặp được gom ở cấp nhóm phiên bản thư mục để tránh đếm đôi, không tuyên bố hai bản có mọi kết quả thực nghiệm giống nhau. Mọi mục vẫn NOT_SCREENED. Khi protocol/IC/EC được chốt, cần quyết định bản nào là bản chính và cách xử lý bản mở rộng.
