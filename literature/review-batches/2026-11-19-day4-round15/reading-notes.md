# Đọc toàn văn đợt 15 ngày 19/11/2026

Đã đọc có trọng điểm hai bài ưu tiên P056 và P057 từ bản hội nghị. Chuỗi đối chiếu hiện có 48 bài, gồm 30 bài trong catalog và 18 bài bổ sung. Còn 13 ứng viên ưu tiên chưa thấy ghi chú đọc toàn văn. Vòng chọn bài chính thức vẫn mở.

## P056 · Astute RAG

Wang và cộng sự, ACL 2025. Mục 4.2–4.4 tạo thêm đoạn từ kiến thức mô hình, sau đó tổng hợp các đoạn sinh và truy xuất. Phương pháp giữ nhãn nguồn, nhóm các đoạn tương thích, giữ riêng các nhóm bất đồng và so độ đáng tin trước khi chọn câu trả lời. Bảng 1 và Mục 5 thử các chất lượng bằng chứng trên bốn mô hình. Phần Limitations lưu ý rằng phương pháp phụ thuộc vào khả năng làm theo hướng dẫn và suy luận của mô hình. Với hệ thống bảo tàng, có thể dùng bước nhóm các đoạn theo dữ kiện để làm đối chứng. Đoạn do mô hình sinh có thể gợi cách tìm hồ sơ. Dữ kiện gửi cho khách và đoạn trích dẫn cần dựa vào hồ sơ kiểm được. [Bản hội nghị](https://aclanthology.org/2025.acl-long.1476/)

## P057 · Rich Knowledge Sources Bring Complex Knowledge Conflicts

Chen, Zhang và Choi, EMNLP 2022. Mục 4–5 so các can thiệp tổng hợp với các dạng khác biệt có ý nghĩa từ AmbigQA và SituatedQA. Mục 5 dùng quy tắc nhị phân: chỉ chấp nhận đáp án khi khớp đáp án chuẩn và tập bằng chứng không xung đột. Bảng 9 cho thấy bộ hiệu chỉnh học trên ca thay thực thể đạt 98,60% trong điều kiện cùng dạng, còn trên AmbigQA là 13,62%. Bộ học kết hợp ba dạng đạt 72,46% trung bình theo bốn tập trong bảng, với kết quả khác nhau giữa các nhóm. Các con số là độ chính xác của quyết định nhị phân trên bộ đánh giá của bài. Bài cung cấp bằng chứng về hạn chế khi chuyển sang kiểu bất đồng khác. Việc trình bày hai cách hiểu hoặc nêu bất đồng kèm nguồn cần được chấm riêng. AmbigQA và SituatedQA đã được đọc trong các đợt trước, nên không tính lại là hai bài mới. [Bản hội nghị](https://aclanthology.org/2022.emnlp-main.146/)

## Áp dụng vào pilot

- Với mỗi ca, ghi hiện vật, thuộc tính, mốc hiệu lực, giá trị và mã nguồn của từng đoạn. Nhóm các đoạn cùng hỗ trợ một giá trị. Kiểm xem khác biệt do cách gọi, mốc thời gian, hay hai hồ sơ thực sự bất đồng về cùng dữ kiện.
- Chọn cách phản hồi dựa trên căn cứ có thể kiểm. Nếu một hồ sơ ghi rõ việc đính chính, có thể nêu dữ kiện đã được đính chính và dẫn nguồn. Nếu hai niên đại đều có hồ sơ hỗ trợ và chưa biết hồ sơ nào có hiệu lực hơn, nêu cả hai kèm nguồn. Nếu thiếu dữ kiện cho mọi cách hiểu, nói rõ phần chưa xác nhận.
- Hiệu chỉnh quy tắc trên tập phát triển rồi kiểm riêng hai nhóm: ca chỉnh có kiểm soát và bất đồng có thật trong hồ sơ. Đảo thứ tự cặp nguồn ở cả hai nhóm theo đợt 14, chấm độ ổn định bên cạnh độ phù hợp của cách trả lời. Điểm của ca tổng hợp có thể cao trong khi quy tắc vẫn xử lý kém hồ sơ thật.
