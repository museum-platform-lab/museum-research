# Đọc toàn văn đợt 12 ngày 19/11/2026

Đã đọc có trọng điểm P069 và P021, hai bài trong danh sách ưu tiên. Chuỗi đối chiếu tăng lên 42 bài, gồm 24 bài trong catalog và 18 bài bổ sung. Còn 19 ứng viên ưu tiên chưa thấy ghi chú đọc toàn văn. Vòng chọn bài chính thức vẫn mở.

## P069 · ARES

Saad-Falcon và cộng sự, NAACL 2024. Mục 3 tách ba câu hỏi chấm RAG: đoạn truy xuất có liên quan không, câu trả lời có được các đoạn hỗ trợ không, và câu trả lời có đúng trọng tâm câu hỏi không. ARES tạo dữ liệu tổng hợp để huấn luyện bộ chấm. Sau đó phương pháp suy luận dựa trên dự đoán (PPI) dùng một mẫu có nhãn người để hiệu chỉnh sai lệch của bộ chấm khi ước lượng điểm tổng hợp và khoảng tin cậy. Bảng 1, Phụ lục Bảng 3 và Mục 7 cho thấy kết quả phụ thuộc vào tập dữ liệu và số nhãn của người chấm. Khoảng 150–300 mẫu ở bài là quy mô dùng hoặc thảo luận cho thiết lập của tác giả. Việc chọn cỡ mẫu cho dữ liệu bảo tàng cần dựa vào mức sai lệch và độ chính xác mong muốn. Các tiêu chí ARES hữu ích để phát hiện lỗi từng tầng, còn chấm đoạn trích hỗ trợ từng dữ kiện và quyết định từ chối cần nhãn riêng. [Bản hội nghị](https://aclanthology.org/2024.naacl-long.20/)

## P021 · Cited but Unused

Abbas, Zia và Windridge, bản arXiv đọc ngày 19/11/2026. Mục 3–5 dùng phép thử thay một giá trị trong các đoạn truy xuất rồi hỏi lại. Nếu câu trả lời đổi theo giá trị mới, đầu ra nhạy với thay đổi bằng chứng trong phép thử. Nếu vẫn giữ giá trị cũ, bài gán nhãn vận hành là nguồn gốc từ tham số mô hình. Bài loại các ca có giá trị trong câu hỏi và các ca đầu ra chứa cả hai giá trị hoặc không chứa giá trị nào theo quy tắc chính. Với phép thay giá trị gần nhất của Bảng 2, bài báo cáo tỷ lệ theo nhãn này là 4,6% và 8,5% trên Qwen2.5-7B và 14B trong thiết lập ASQA. Các tỷ lệ phụ thuộc cách chọn giá trị, tập ca đủ điều kiện và cách đọc đầu ra. Mục Limitations và phân tích thao tác thay giá trị bàn về khớp chuỗi, biến thể biểu đạt và thay đổi tính hợp lý. Kết quả giữ nguyên có thể cần xem kỹ phản hồi hoặc nguồn khác trước khi suy luận về cơ chế. Chưa xác minh được bản xuất bản qua phản biện. [Bản arXiv](https://arxiv.org/abs/2611.17161)

## Áp dụng vào pilot

- Chấm độc lập ba tầng: tìm đúng đoạn, từng dữ kiện được đoạn trích dẫn chứng minh, và phản hồi phù hợp với mức đủ bằng chứng. Với tiếng Việt, dùng một tập nhãn người để kiểm bộ chấm tự động, chú ý tên riêng, số liệu và mốc thời gian.
- Trên một tập chẩn đoán nhỏ tách khỏi dữ liệu trả lời thật, tạo cặp chỉ đổi một giá trị trong tất cả đoạn hỗ trợ liên quan. Giữ câu hỏi và cấu hình sinh cố định, kiểm tính nhất quán của đoạn đã chỉnh và lưu riêng ba dạng đầu ra: thay theo nguồn, giữ giá trị ban đầu, hoặc không xác định. Dùng bản gốc để chấm độ hỗ trợ của citation, dùng bản chỉnh để đo độ nhạy khi nguồn thay đổi.
- P021 nối phép kiểm can thiệp nguồn của các đợt trước với một quy tắc gán nhãn cụ thể. ARES cung cấp cách hiệu chỉnh điểm tổng hợp bằng nhãn người. Hai bài bổ sung phương pháp đối chiếu. Điểm của bộ chấm và độ nhạy với bằng chứng vẫn cần kiểm trên dữ liệu dự án.
