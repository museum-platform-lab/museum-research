# Day 3, đợt 5 · Nhận ra thiếu bằng chứng và biết khi nào nên dừng

Ngày 18/11/2026. Đọc có trọng điểm phần thiết kế, kết quả và hạn chế của NoMIRACL và DeclineCraft. Cả hai giúp làm rõ cách chấm khi thông tin cần thiết vắng mặt. Kết luận về nguồn chỉ áp dụng cho kho tài liệu hoặc ngữ cảnh được bài xác định.

## NoMIRACL · Findings of EMNLP 2024

- **Đơn vị đánh giá.** Với câu hỏi và các đoạn lấy từ Wikipedia, mô hình nhận định có đoạn liên quan hay không. Nhóm non-relevant gồm các câu mà toàn bộ đoạn được cung cấp đều bị người gán nhãn đánh giá là không liên quan. Nhóm relevant có ít nhất một đoạn liên quan. Table 1 có 13.903 và 17.737 mục test tương ứng. Bài bao phủ 18 ngôn ngữ với hai tập dev/test, và danh sách trong Table 1 chưa có tiếng Việt. (§3, Table 1, tr. 12514)
- **Kết quả minh họa.** Trong phân tích phản hồi tiếng Anh ở Table 2, hàng trả lời “Yes” trên nhóm non-relevant là 42,4% với GPT-4 và 8,0% với Mistral 7B. Trên nhóm relevant, hàng trả lời “No” lần lượt là 4,8% và 60,8%. Đây là các hàng trong phân tích loại phản hồi tiếng Anh, nên cần giữ nguyên mẫu số và không chuyển các số này thành tỷ lệ hallucination chung của mọi ngôn ngữ. (Table 2)
- **Giới hạn đo lường.** “Hallucination rate” trong tác vụ này là tỷ lệ dương tính giả khi nhận định sự hiện diện của đoạn liên quan. “Error rate” là tỷ lệ âm tính giả. Bài đánh giá mức liên quan của các đoạn, vì vậy kết quả không trực tiếp đo độ đúng của một đáp án tự do, đoạn nguồn hỗ trợ từng claim, hoặc quyết định khi các nguồn mâu thuẫn. (§3 và §10)

[PDF chính thức](https://aclanthology.org/2024.findings-emnlp.730.pdf). DOI 10.18653/v1/2024.findings-emnlp.730. SHA-256 fc3f554b3664302cba134767083c8602f0a3e7183edf36299dea95bf248d0998. Tra theo tiêu đề và ID ACL chưa thấy bài trong danh mục 101. Theo dõi như nguồn bổ sung đã đọc để xét ở vòng formal screening.

## DeclineCraft · N011, arXiv v1

- **Đơn vị đánh giá.** 700 câu có thể trả lời và 300 câu thiếu căn cứ theo thiết lập được tạo từ lịch sử cập nhật Minecraft Wiki. Hệ truy xuất chỉ nhận tài liệu trước mốc 31/03/2025. Dữ kiện đích của câu thiếu căn cứ nằm ở tài liệu sau mốc. Tác giả kiểm khả năng mô hình từng tiếp xúc với dữ kiện bằng cách yêu cầu trả lời khi không truy xuất. Cách kiểm này là một tín hiệu về khả năng mô hình đã biết dữ kiện. (§§3.1–3.3, Figure 1)
- **Kết quả.** Với truy xuất lặp, Correct Abstention Rate thấp hơn có ý nghĩa thống kê so với truy xuất một lượt ở 30/40 cấu hình được so sánh. Accuracy của đáp án chỉ thay đổi nhẹ, từ 68,5% lên 69,3%. Đọc hai kết quả cùng nhau vì một hệ thống có thể trả lời thêm mà đồng thời thừa nhận thiếu căn cứ ít hơn. Một số kết luận về chế độ reasoning và ngày phát hành thay đổi khi quy tắc chấm chấp nhận cả lời phủ định tiền đề. (Tóm tắt, §4 và Appendix I)
- **Giới hạn.** “Nguồn hiện tại chưa xác nhận X” được chấm khác với “X không tồn tại” nếu mô hình không có bằng chứng cho lời phủ định. Các câu chịu ảnh hưởng của một miền Wiki, dữ liệu được xây dựng và đánh giá với nhiều LLM, còn phần đối chiếu với người chỉ có 100 mục chung. Khả năng chuyển kết quả sang dữ liệu bảo tàng cần được xác minh. (§6 và Appendix I)

[Bản arXiv v1 đọc ngày 18/11/2026](https://arxiv.org/pdf/2610.28340). SHA-256 5768c9f865cecbf3cf4838e044c57d9ea432b10be86414c017000eb40e7798cd. Chưa xác minh được bản hội nghị hoặc tạp chí. Giữ kết quả ở phần đối chiếu tính mới theo tiêu chí IC-T của Week 6.

## Hàm ý đối với review

NoMIRACL cung cấp tiền lệ cho việc cho mô hình xem toàn đoạn không liên quan rồi chấm nhận định về đoạn. DeclineCraft cung cấp tiền lệ cho cách tạo trường hợp thiếu căn cứ theo phiên bản tài liệu và tách từ chối đúng khỏi phủ định thiếu căn cứ. Kết hợp với ViCH-QA/SACR, ba đơn vị cần phân biệt là mức liên quan của đoạn, mức đủ căn cứ để trả lời và mức hỗ trợ của nguồn trích cho từng claim. Câu hỏi còn mở là các bộ dữ liệu gần nhất có nhãn chi tiết đến đâu cho hỗ trợ một phần, bằng chứng mâu thuẫn và nguồn cần ghép lại.

Chuỗi ghi chú đối chiếu hiện bao phủ 18 bài. DeclineCraft đã ở danh mục với ID N011. NoMIRACL là mục bổ sung theo dõi riêng. Quyết định nhận chính thức và kiểm chéo Week 6 còn mở.
