# Day 4, đợt 2 · Đánh giá từng ý và mức trả lời đầy đủ

Ngày 19/11/2026. Đọc có trọng điểm các phần định nghĩa, phương pháp, kết quả và giới hạn liên quan của FActScore (P076) và Attributed Question Answering. Bài thứ hai được theo dõi như nguồn bổ sung sau khi dò tiêu đề và mã arXiv trong danh mục 101.

## FActScore · Min và cộng sự, EMNLP 2023

FActScore tách câu trả lời thành các ý kiểm chứng được, sau đó tính tỷ lệ ý được kho tham chiếu hỗ trợ. Một câu nêu cả năm chế tác và tên nghệ nhân có thể chứa hai ý với hai mức hỗ trợ khác nhau. Cách chấm nhị phân ở từng ý cho phép ghi nhận phần có căn cứ mà không cần đặt một tỷ lệ tùy ý cho cả câu. (§3.1)

Điểm lấy trung bình trên các lượt mô hình có trả lời. Các lượt từ chối nằm ngoài mẫu số, và điểm đo độ chính xác trên các ý đã nêu. Với tiểu sử dựa trên Wikipedia, ChatGPT đạt FActScore do người chấm là 58,3% và trả lời 85,8% lượt. Table 1 trình bày hai đại lượng riêng. Table 6 minh họa một câu trả lời có factual precision cao nhưng còn thiếu thông tin quan trọng. (§3.3, Table 1, Limitations và Table 6)

Bài giả định các ý có trọng số ngang nhau và kho tham chiếu đủ nhất quán để xét hỗ trợ. Với dữ liệu bảo tàng có nguồn bất đồng, cần ghi phạm vi của nguồn và tình trạng bất đồng trước khi chấm đúng sai. Việc kho tham chiếu hỗ trợ một ý và việc đoạn được chatbot trích hỗ trợ ý đó là hai quan hệ khác nhau.

[PDF hội nghị](https://aclanthology.org/2023.emnlp-main.741.pdf). DOI 10.18653/v1/2023.emnlp-main.741. SHA-256 8486fe22a15aaf3fe2e1d7043d169000600205dde9c601c9fd31c0dd6f7380e9.

## Attributed Question Answering · Bohnet và cộng sự, arXiv

Với một câu hỏi, hệ thống đưa ra đáp án ngắn và một đoạn nguồn. Người chấm kiểm xem đầu ra có thể hiểu được và toàn bộ thông tin trong đáp án có được đoạn đó hỗ trợ hay không. Thử nghiệm dùng Natural Questions và bản Wikipedia ngày 13/10/2021. Chấm AIS trên 1.000 câu lấy ngẫu nhiên và dùng đa số trong 5 người chấm cho mỗi câu. (§§3.1, 5.1–5.2)

Trong Table 1, hệ retrieve-then-read đạt AIS 65,5 và Exact Match 41,1. Hệ tìm nguồn sau khi sinh đạt AIS 55,6 và Exact Match 49,5. Xếp hạng đảo chiều vì hai thước đo hỏi hai câu khác nhau: đáp án có khớp chuỗi tham chiếu và đáp án có được đoạn chỉ định hỗ trợ. AutoAIS có tương quan Pearson 0,96 với AIS ở cấp hệ thống trong phân tích được báo cáo. Tác giả ghi nhận biến thể chọn nguồn bằng AutoAIS lệch khỏi xu hướng đó, nên kết quả tổng hợp chưa đủ để dùng điểm tự động thay phán đoán con người cho từng bản ghi. (§5.3, Table 1 và §5.5, Figure 3)

Đây là thiết lập đáp án ngắn, một đoạn nguồn. Cần thêm đối chiếu khi một ý phụ thuộc nhiều đoạn hoặc câu hỏi có nhiều điều kiện. Nguồn công khai đã xác minh là arXiv năm 2022, vì vậy kết quả được giữ ở phần đối chiếu tiền lệ trong khi trạng thái xuất bản theo IC-T còn mở.

[PDF đã đọc](https://arxiv.org/pdf/2212.08037). SHA-256 0b493430aaf8a448b1d17d1132ae3f2e0c0fd0655d570f0ea46c924397959502.

## Hàm ý cho review

FActScore đã đặt tiền lệ cho chấm ở cấp từng ý. Attributed QA đã kiểm trực tiếp khả năng hỗ trợ của đoạn được dẫn. ALCE còn cho phép xét các nguồn trích kết hợp với nhau. Với câu hỏi bảo tàng như “Chiếc bình này được làm khi nào và do ai?”, cần ghi riêng ý về niên đại, ý về nghệ nhân, đoạn nguồn hỗ trợ từng ý và phần thông tin được hỏi nhưng chưa trả lời. Nếu hai nguồn bất đồng, người chấm cần biết bất đồng nằm ở ý nào. Giá trị của cách gán nhãn này so với các bộ gần nhất vẫn cần đối chiếu trên dữ liệu có thể truy cập.

Chuỗi đối chiếu chuẩn hóa hiện bao phủ 22 bài. FActScore đã có ID P076 trong danh mục. Quyết định nhận bài và kiểm chéo theo Week 6 còn mở.
