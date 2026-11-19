# Đọc toàn văn đợt 16 ngày 19/11/2026

Đã đọc có trọng điểm hai bài ưu tiên P055 và N006 từ bản tạp chí. Chuỗi đối chiếu hiện có 50 bài, gồm 32 bài trong catalog và 18 bài bổ sung. Còn 11 ứng viên ưu tiên chưa thấy ghi chú đọc toàn văn. Vòng chọn bài chính thức vẫn mở.

## P055 · Sufficiency-Gated Retrieval-Augmented Generation

Shishir và cộng sự, Computers, Materials & Continua, 2026. Mục 3 so bốn cách đánh giá độ đủ của ngữ cảnh trước khi sinh, gồm quy tắc đơn giản, chấm từng đoạn, chấm chung tập đoạn và dùng chính mô hình sinh để chấm. Mục 5 và Bảng 7–8 báo cáo tỷ lệ trả lời, tỷ lệ thiếu hỗ trợ trong số câu đã trả lời và độ đúng trên toàn tập. Đối chứng từ chối ngẫu nhiên giữ cùng số câu được trả lời. Trong thiết lập chính, chỉ cách dùng mô hình sinh để chấm vượt đối chứng này trên cả HotpotQA và MuSiQue. Trên HotpotQA, cấu hình đó trả lời 57,0% số câu và có 17,2% câu thiếu hỗ trợ trong nhóm đã trả lời, so với 26,2% ở RAG luôn trả lời. Độ khớp chính xác trên toàn tập giảm từ 32,0% xuống 25,0% khi chấm từ chối là sai. Mục 6.3 lưu ý phép đo hỗ trợ dựa trên bộ suy luận ngôn ngữ tự động và nhãn đủ bằng chứng dựa trên việc tìm được dữ kiện chuẩn. Hai phép đo có giới hạn khi câu trả lời cần ghép nhiều đoạn hoặc diễn đạt khác. [Bài báo](https://doi.org/10.32604/cmc.2026.088937)

## N006 · Evidence-Calibrated RAG for Unanswerable Question Answering

Zhong và cộng sự, Journal of Technology Informatics and Engineering, 2025. Mục III–IV so bộ luôn trả lời với bộ có thêm ngưỡng từ chối trên SQuAD 2.0, giữ nguyên đoạn truy xuất và bộ trích cụm từ. Hai cấu hình dùng cùng nguồn đầu vào nên có thể xem riêng ảnh hưởng của ngưỡng. Tác giả báo cáo AUROC 0,5475 khi dùng điểm bằng chứng để phân biệt câu có và không có đáp án, gần mức 0,5 của xếp hạng ngẫu nhiên. Các bảng cho thấy thay ngưỡng làm thay đổi cả tỷ lệ từ chối và chất lượng trên nhóm có đáp án. Thiết lập dùng đáp án trích xuất. Chỉ số đại diện cho lỗi của bài cần được đọc theo tác vụ này. Việc xác minh nguồn cho từng dữ kiện trong câu trả lời tiếng Việt cần nhãn riêng. [Bài báo](https://doi.org/10.51903/jtie.v4i2.536)

## Áp dụng vào pilot

- Giữ nguyên bộ truy xuất, các đoạn nguồn và mô hình sinh khi so RAG luôn trả lời với RAG có bước kiểm đủ bằng chứng. Chọn ngưỡng trên tập phát triển và báo cáo điểm trên tập kiểm thử.
- So thêm đối chứng từ chối ngẫu nhiên với cùng tỷ lệ trả lời. Báo cả tỷ lệ trả lời, tỷ lệ câu thiếu căn cứ trong nhóm đã trả lời và tỷ lệ từ chối nhầm khi nguồn đủ. Với câu cần nhiều đoạn, nhờ người chấm kiểm cả tập đoạn và đoạn trích cho từng dữ kiện.
- Ghi riêng trường hợp kho có nguồn nhưng bộ truy xuất bỏ sót và trường hợp hồ sơ chưa có dữ kiện. Nếu thử trả lời một phần, chấm dữ kiện có nguồn đã được giữ lại và phần chưa xác nhận đã được nói rõ. Cấu hình và ngưỡng cho tiếng Việt vẫn cần kiểm trên dữ liệu dự án.
