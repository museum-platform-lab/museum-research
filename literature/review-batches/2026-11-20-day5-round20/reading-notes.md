# Đọc toàn văn đợt 20 ngày 20/11/2026

Đã đọc có trọng điểm N003 và N004. Chuỗi đối chiếu có 58 bài, gồm 40 bài trong catalog và 18 bài bổ sung. Ba mục ưu tiên còn lại là P027, P033 và P052. Vòng chọn bài chính thức vẫn mở.

## N003 · Cultural Faithfulness in Tourism Chatbots

Nurhidayati, Nurchayati và Sugiarto, Research Square v1. Mục 3 và Bảng 1 mô tả 61 câu dựa trên một truyện dân gian Indonesia, Ande-Ande Lumut. Có 30 câu trong phạm vi nguồn, 16 câu mơ hồ và 15 câu ngoài phạm vi. Đoạn nguồn có mã và vị trí văn bản. Ba người chấm độc lập, lưu mã lỗi và lý do, rồi họp để thống nhất các ca bất đồng hoặc lỗi nghiêm trọng. Ba nhãn trên mỗi câu tạo ra 183 phiếu cho 61 quyết định cuối. Điểm tương đồng được dùng để tìm ca cần xem xét, còn người chấm kiểm trực tiếp dữ kiện và phạm vi diễn giải được nguồn cho phép. Người chấm có thể thấy điểm tự động. Đây là một quy trình tham khảo cùng miền văn hóa với quy mô một corpus. Chưa kiểm riêng toàn bộ tệp phụ lục và chưa xác minh được bản xuất bản qua phản biện. [Preprint](https://doi.org/10.21203/rs.3.rs-8994226/v1)

## N004 · Benchmarking Large Language Models in Retrieval-Augmented Generation

Chen và cộng sự, AAAI 2024. Benchmark RGB dùng dữ liệu tiếng Anh và tiếng Trung để tách bốn khả năng: chịu đoạn nhiễu, từ chối khi thiếu bằng chứng, ghép thông tin từ nhiều đoạn và xử lý dữ kiện phản thực. Bảng 3 cho thấy cách nhận diện từ chối làm kết quả thay đổi. Với ChatGPT trên nhóm tiếng Anh, tỷ lệ là 24,67% theo quy tắc khớp và 45,00% theo bộ chấm ChatGPT. Chênh lệch chỉ ra sự nhạy với phép chấm; cần đối chiếu nhãn người để biết phép đo nào phản ánh đúng ý nghĩa câu trả lời. Bảng 5–7 cho thấy các dạng ghép nguồn và phát hiện dữ kiện sai có phép thử riêng. Với hồ sơ bảo tàng, chỉ gán một giá trị là sai khi có căn cứ xác minh. Khi nguồn thực sự bất đồng, chấm riêng cách nêu bất đồng và dẫn nguồn. [Bài hội nghị](https://doi.org/10.1609/aaai.v38i16.29728)

## Áp dụng vào pilot

- Cho người chấm xem câu hỏi, câu trả lời, hiện vật và đúng các đoạn được dẫn. Ghi nhãn độc lập và lý do trước khi đối chiếu. Giữ cả nhãn ban đầu và nhãn sau thống nhất. Nếu dùng điểm tự động để tìm ca khó, chấm độc lập trước khi xem điểm đó.
- Chấm từ chối bằng ý nghĩa câu trả lời. Ví dụ, “Hồ sơ hiện chỉ xác nhận năm tiếp nhận” có thể là phản hồi đúng khi khách hỏi ai tặng hiện vật. Cần kiểm hệ thống giữ đúng phần có nguồn và không ngụ ý đã biết người tặng.
- Báo riêng các nhóm ca nhiễu, thiếu nguồn, cần ghép nguồn và dữ kiện phản thực. Giữ mối liên hệ giữa câu gốc và các biến thể khi chia tập và tổng hợp kết quả.
