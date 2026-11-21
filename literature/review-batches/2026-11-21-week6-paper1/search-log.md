# Nhật ký thử tìm kiếm Paper 1

Ngày 21/11/2026. Các lượt dưới đây thử kết nối và lấy metadata trước khi khóa protocol. Ngày 21/11 dùng để thử bộ lọc OpenAlex. Ngày dừng chính thức vẫn chờ xác nhận.

| Nguồn | Đã thử | Kết quả và giới hạn |
| --- | --- | --- |
| OpenAlex | 3 truy vấn chủ đề qua API works, có khoảng ngày thử | Cả ba trả HTTP 429. Phản hồi ghi hết ngân sách ẩn danh trên IP dùng chung. Chưa xuất được bản ghi. |
| IEEE Xplore | Mở trực tiếp URL tìm kiếm với queryText | HTTP 200 cho trang tìm kiếm. Phản hồi HTML chưa xác nhận được số kết quả hay bản ghi xuất. |
| ACM Digital Library | Gửi truy vấn AllField tới giao diện tìm kiếm | HTTP 403, nhận trang kiểm tra truy cập. Chưa xuất được bản ghi. |
| Semantic Scholar | Truy vấn API paper/search cho QA bảo tàng và di sản | HTTP 200, API báo 2.275 kết quả. Đã lấy 10 bản ghi trang đầu để kiểm khả năng xuất metadata. Mẫu có câu hỏi di sản, QA đa phương thức và cả kết quả lệch phạm vi. Cú pháp tìm từ khóa ở lượt thử khác với chuỗi Boolean đề xuất. |

Chuỗi nguyên văn, URL, thời gian, phản hồi và SHA-256 được ghi ở [query-runs.csv](query-runs.csv). Mẫu 10 dòng và cột khớp catalog có ở [pilot-records.csv](pilot-records.csv). Phản hồi gốc nằm trong thư mục search-pilot của gói Drive. Độ phủ trên các bài hạt giống chưa được xác lập từ một trang đầu. Không dùng 2.275 hit và 10 dòng mẫu làm số PRISMA.

## Chuyển sang tìm kiếm chính thức

- Chạy thử giao diện IEEE và ACM qua quyền trường hoặc thư viện. Với OpenAlex, dùng phương án truy cập được lập danh trong protocol và xác minh kết quả trả về có thể xuất theo quy trình đầy đủ. Semantic Scholar là phương án thay thế có điều kiện, cần log khác biệt cú pháp và thử phân trang trước khi đưa vào danh sách nguồn chính.
- Chốt bộ truy vấn theo cùng khái niệm và khoảng ngày, lưu chuỗi thực tế từng nguồn. Kiểm vài seed đã biết và lý do bỏ sót. Ghi người phụ trách, phiên bản protocol và ngày khóa trước lượt chính thức.
- Xuất toàn bộ bản ghi theo phạm vi đã công bố, khử trùng theo DOI và nhóm phiên bản, lọc hai vòng và ghi nhánh lần trích dẫn riêng. Lưu số nguồn báo và số thực xuất bằng hai trường khác nhau.
- P033 và P052 vẫn chờ toàn văn. Một lượt tìm công khai trước đã xác minh DOI, trang xuất bản và tình trạng truy cập. EPRAG có gói tái lập cho đối chiếu phương pháp. Nếu quyền thư viện hoặc bản tác giả hợp lệ chưa được xác minh, giữ trạng thái chờ. [P033](https://doi.org/10.1016/j.ipm.2025.104369) · [P052](https://doi.org/10.1016/j.knosys.2026.116929) · [Đợt 22](https://github.com/museum-platform-lab/museum-research/blob/research/literature-discovery-2026-11-16/literature/review-batches/2026-11-20-day5-round22/reading-notes.md)
