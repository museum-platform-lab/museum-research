# Nguồn và quyền truy cập — as of 16/11/2026

Đây là trạng thái từ scoping/audit trước, không phải kiểm tra kết nối mới trong đợt 2.

| Nguồn | Vai trò dự kiến | Bằng chứng/trạng thái hiện có | Việc cần trước formal |
| --- | --- | --- | --- |
| IEEE Xplore | Primary DB 1 | Chưa xác minh native query/export | Pilot đúng giao diện, lưu syntax/filters, export metadata; full-text tùy quyền |
| ACM DL | Primary DB 2 | Chưa xác minh native query/export | Pilot field search/export, kiểm đầy đủ trang và quyền đọc |
| OpenAlex | Primary DB 3 dự kiến | Anonymous search đã trả 503 trong discovery; chưa cấu hình key | Thử đường miễn phí được hỗ trợ, kiểm Boolean/cursor/export; không ghi là nguồn đã harvested |
| Scopus | Thay thế có điều kiện | Chưa biết trường có quyền | Xác minh quyền và strategy, ghi amendment nếu thay |
| Semantic Scholar | Thay thế/bổ sung có điều kiện, citation tracing | Chưa harvested native | Kiểm search dialect/quota/export; chỉ tính nguồn đã chạy thực tế |
| ACL Anthology | Chuyên ngành NLP bổ sung | Chưa tìm native | Kiểm query/export và coverage, không thay 3 DB im lặng |
| Google Scholar/web search | Bổ sung discovery/coverage | Đã có 26 web queries ở discovery, không đồng nghĩa native Scholar | Log prompt/query và paper mở; formal ingress qua query/snowball hợp lệ |
| Crossref | Metadata/version check | Audit 61 DOI thành công sau retry | Không coi metadata enrichment là formal topic search |
| arXiv | Watchlist, phiên bản mới | Có exact-ID lead trong discovery/audit | Tìm bản published; preprint-only không đạt IC-T |
| Zotero | Thư viện, PDF, cite/export | Có RIS 101 mục để người dùng import | Không có API sync agent đã cấu hình; không dùng key lộ trong chat |

Miễn phí không đồng nghĩa toàn bộ full-text miễn phí. Dùng publisher OA, institutional/author repository và quyền thư viện hợp pháp; ghi access attempts trước EC-A. Chưa đủ 3 primary DB hoạt động, nên readiness formal vẫn PENDING.
