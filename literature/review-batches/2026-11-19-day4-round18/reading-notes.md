# Đọc toàn văn đợt 18 ngày 19/11/2026

Đã đọc có trọng điểm P068 và N005. Chuỗi đối chiếu hiện có 54 bài, gồm 36 bài trong catalog và 18 bài bổ sung. Còn 7 ứng viên ưu tiên chưa thấy ghi chú đọc toàn văn. Vòng chọn bài chính thức vẫn mở.

## N005 · When Abstention Gates Overtrust Noisy Evidence

Patel, bản preprint v1 trên Research Archive of Rising Scholars. Mục 3 tạo bốn ngữ cảnh cho mỗi câu hỏi gốc của HotpotQA: đủ hai đoạn, chỉ có một đoạn cần thiết, hai đoạn trùng từ khóa nhưng thiếu bằng chứng chuẩn, và nhiễu ngẫu nhiên. Tác giả lưu ý các biến thể của cùng câu là quan sát phụ thuộc. Theo Bảng 1B, lỗi đánh giá nhầm nguồn thiếu thành đủ tập trung vào ca thiếu một phần và ca trùng từ khóa. Bảng 3 báo cáo cùng tập kiểm thử: ngưỡng hiệu chỉnh chỉ bằng nhiễu ngẫu nhiên cho tỷ lệ đánh giá nhầm tổng thể 65,17%, còn ngưỡng hiệu chỉnh bằng ca thiếu một phần và ca trùng từ khóa cho 5,33%. Các số đo chỉ áp dụng cho thiết lập nhân tạo của bài, và ngưỡng nghiêm hơn cũng làm bỏ qua nhiều ca đủ nguồn. Bài chưa chạy mô hình sinh để đo lỗi câu trả lời. Mức đồng ý 96,5% trong audit nhỏ là giữa quy tắc tạo ca và bộ chấm tự động, chưa phải mức đồng ý giữa hai người chấm. [Bản preprint](https://doi.org/10.58445/csk35g23)

## P068 · Evaluating Open-Source LLMs in RAG Systems

Antal và Buza, Acta Universitatis Sapientiae, Informatica, 2025. Mục 3 mô tả 227 bản tóm tắt luận văn tiếng Anh và 122 câu hỏi có thể trả lời, tạo bằng GPT-4o rồi rà thủ công. Mục 5.2–5.3 và Bảng 7–8 so việc đưa sẵn đúng bản tóm tắt gốc với việc đưa năm tài liệu truy xuất đã xếp hạng lại. Llama3 giảm điểm faithfulness do Ragas chấm từ 0,82 xuống 0,76 giữa hai điều kiện. Điều kiện thay đổi cả việc có nguồn đúng và số tài liệu đầu vào, nên chênh lệch đo hiệu quả của hai thiết lập. Bộ thử loại câu không thể trả lời. Vì vậy, kết quả hữu ích khi thiết kế đối chứng có nguồn chuẩn, còn hành vi từ chối cần bộ ca và nhãn người riêng. [Bài báo](https://doi.org/10.1007/s44427-025-00006-3)

## Áp dụng vào pilot

- Tạo ca thiếu một đoạn bắt buộc và ca trùng từ khóa ở hồ sơ của hiện vật khác. Xác minh người chấm vẫn kết luận thiếu căn cứ khi đối chiếu cả tên gọi khác và các đoạn còn lại. Giữ các biến thể cùng câu hỏi trong cùng phần dữ liệu.
- Hiệu chỉnh ngưỡng trên tập phát triển có ca khó và báo riêng tỷ lệ nhận nhầm nguồn thiếu thành đủ ở từng nhóm. Báo song song tỷ lệ từ chối nhầm khi nguồn đủ và hiệu quả thực tế trên câu trả lời cuối.
- Đo với hai điều kiện có nguồn chuẩn và nguồn truy xuất, giữ số đoạn hoặc ngân sách ngữ cảnh tương đương khi mục tiêu là tách lỗi tìm nguồn khỏi lỗi đọc. Dùng nhãn người để kiểm điểm tự động, đặc biệt khi một mệnh đề cần ghép nhiều đoạn.
