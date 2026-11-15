# Backlog

Checkbox chưa đánh dấu nghĩa là chưa triển khai; có tài liệu không có nghĩa tính năng đã hoàn thành.

## P0 — bắt đầu ngay

- [ ] T00: Chọn bản mã chính ở museum-platform, xác nhận quyền dùng mã và corpus cũ. Xong khi có ghi chép quyết định.
- [ ] T01: Chọn một bộ sưu tập và mô tả người dùng mục tiêu trong 5 dòng.
- [ ] T02: Lập 10 hồ sơ kèm source, passage và quyền dùng; không cần ảnh.
- [ ] T03: Viết 10 câu hỏi, ít nhất 3 câu nhiều bước và 2 câu không trả lời được.
- [ ] T04: Đọc 3–5 công trình liên quan, lập bảng điểm giống/khác và giới hạn; chưa tuyên bố novelty.
- [ ] T05: Sao lưu database và mã trước khi sửa cấu trúc.

## P1 — MVP

- [ ] T10: Database riêng và schema nguồn/chứng cứ. Phụ thuộc T00, T02, T05.
- [ ] T11: API tác phẩm và adapter frontend. Xong khi search/detail đọc corpus mới.
- [ ] T12: Nhập 30–50 hồ sơ, giữ ID ổn định và evidence liên kết được.
- [ ] T13: Vector RAG với citation và run log. Phụ thuộc T10, T12.
- [ ] T14: Entity linking và graph retrieval. Phụ thuộc T12.
- [ ] T15: Evidence ranking và abstention. Phụ thuộc T13, T14.
- [ ] T16: Giao diện câu trả lời/nguồn/đường liên hệ. Phụ thuộc T15.

## P2 — nghiên cứu

- [ ] T20: Benchmark và hướng dẫn chấm; freeze dev/test.
- [ ] T21: Baseline B1/B2/B3 cùng ngân sách và generator.
- [ ] T22: Ablation và phân tích chi phí.
- [ ] T23: Review người, khoảng tin cậy, phân tích lỗi.
- [ ] T24: Kiểm tra chuyển collection nếu dữ liệu đủ; không gắn nhãn LODO cho protocol khác.
- [ ] T25: Báo cáo và quyết định loại bài dựa trên kết quả.

## P3 — mở rộng sau

- [ ] Trích xuất graph bằng nhiều mô hình, đánh giá riêng chất lượng annotation.
- [ ] Motif explorer hoặc tìm kiếm đa phương thức.
- [ ] Đăng nhập, đóng góp và quản trị sau khi quyền backend được bảo vệ.

Trong tuần đầu chỉ lấy T00–T04. Tránh đổi tên toàn bộ entity và làm UI mới trước khi xác nhận corpus đủ để thực hiện câu hỏi nghiên cứu.
