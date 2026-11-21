# Đọc toàn văn đợt 19 ngày 20/11/2026

Đã đọc có trọng điểm P070 và N010. Chuỗi đối chiếu hiện có 56 bài, gồm 38 bài trong catalog và 18 bài bổ sung. Còn 5 ứng viên ưu tiên chưa thấy ghi chú đọc toàn văn. Vòng chọn bài chính thức vẫn mở.

## P070 · FreeGuard

Wang và Zhao, Discover Computing, 2026. Mục phương pháp mô tả việc tách bản nháp thành dữ kiện nhỏ và dùng quan hệ giữa các dữ kiện để ưu tiên chỗ cần kiểm. Bước kiểm tìm cả bằng chứng hỗ trợ lẫn phản bác, rồi thử thay đổi tập bằng chứng để xem kết luận nào phụ thuộc vào một nguồn. Bảng 10 báo cáo trên RAGTruth, F1 phát hiện bằng chứng phản bác là 73,6 với cấu hình đầy đủ và 66,8 khi bỏ bước kiểm phản thực. Đây là kết quả của hai cấu hình trên bộ thử của bài. Mục 5 lưu ý hệ thống phụ thuộc vào chất lượng tách dữ kiện, truy xuất và phân loại quan hệ. Thí nghiệm qua nhiều mô hình tập trung vào tiếng Anh. Đồ thị trong bài biểu diễn quan hệ giữa mệnh đề và bằng chứng trong quá trình kiểm một câu trả lời. Đối với pilot bảo tàng, có thể thử tìm cả đoạn xác nhận và đoạn phản bác trên cùng hiện vật, thuộc tính và mốc thời gian bằng bảng ghép dữ kiện với đoạn nguồn. [Bài báo](https://doi.org/10.1007/s10791-026-10667-z)

## N010 · Evidence-Bound Factual Repair

Rajendran và Singaravelu, preprint v1. Bài tách vai trò chỉ ra chỗ cần sửa và chọn câu nguồn khỏi thao tác tạo văn bản thay thế. Theo Mục 5, mô hình chọn vị trí và mã bằng chứng. Quy tắc cố định kiểm ánh xạ trước khi thay bằng nội dung có trong nguồn. Những ca ánh xạ chưa giải quyết có thể giữ văn bản cũ, nên đầu ra sau bước sửa vẫn cần nhãn trạng thái. Bảng 7 báo cáo trên 32 câu trả lời RAGTruth đã được gắn lỗi, phương pháp bỏ được lỗi ở 14 ca, còn sinh lại tự do bỏ được lỗi ở 15 ca. Hai tỷ lệ lỗi mới trong cùng bảng dùng mẫu số khác nhau, 2/885 và 1/98, nên chỉ so mô tả. Mục 10 lưu ý số cặp đổi trạng thái ít và mô hình sinh với mô hình định vị thuộc cùng họ. [Bản preprint](https://doi.org/10.20944/preprints202609.0490.v1)

## Áp dụng vào pilot

- Tách ba bước: tìm chỗ cần kiểm, xác minh đoạn nguồn, và quyết định giữ, sửa hay nói rõ phần chưa xác nhận. Với mã hoặc niên đại có một giá trị được nguồn xác nhận rõ, thử thay đúng trường dữ kiện bằng nội dung từ hồ sơ và giữ mã đoạn trích.
- So sửa theo nguồn với sinh lại tự do trên cùng câu hỏi, cùng đoạn và cùng số ca. Chấm lỗi cũ đã sửa, lỗi mới phát sinh, ý đúng bị mất và phần còn thiếu được thông báo. Ghép kết quả theo từng câu thay vì so tỷ lệ từ hai nhóm khác nhau.
- Nếu hai nguồn còn bất đồng và chưa có căn cứ phân xử, chấm cách nêu bất đồng và nguồn của từng giá trị. Nếu không thể xác minh, ghi trạng thái chưa xác minh để tránh coi việc giữ nguyên câu cũ là đã kiểm xong.
