# Đọc toàn văn đợt 13 ngày 19/11/2026

Đã đọc có trọng điểm hai bài ưu tiên P085 và P078. Chuỗi đối chiếu tăng lên 44 bài, gồm 26 bài trong catalog và 18 bài bổ sung. Còn 17 ứng viên ưu tiên chưa thấy ghi chú đọc toàn văn. Vòng chọn bài chính thức vẫn mở.

## P085 · Corrective Retrieval Augmented Generation (CRAG)

Yan và cộng sự. Mục 4.3–4.4 dùng điểm liên quan của các đoạn truy xuất với hai ngưỡng. Nếu có đoạn vượt ngưỡng trên, hệ thống lọc nội dung từ nguồn đã tìm. Nếu tất cả đoạn dưới ngưỡng dưới, hệ thống viết lại truy vấn và tìm trên web. Ở vùng trung gian, hệ thống kết hợp hai nguồn. Nhãn Ambiguous ở đây mô tả độ không chắc về kết quả truy xuất. Trong bộ đánh giá bảo tàng, sự mơ hồ về hiện vật hoặc ý định của khách là một tình huống riêng. Bảng 1 báo cáo cải thiện trên các tác vụ nguồn với những cấu hình cụ thể. Mục 5.7 và Bảng 5 còn so với cách bổ sung tìm web cho mọi câu. Việc một đoạn liên quan chưa đảm bảo có đủ dữ kiện để trả lời. Cần đo riêng khả năng từ chối khi lượt tìm bổ sung vẫn không có căn cứ. Đã đối chiếu bản arXiv. [Toàn văn](https://arxiv.org/abs/2401.15884)

## P078 · RARR

Gao và cộng sự, ACL 2023. Mục 2–3 bắt đầu từ bản nháp, tạo truy vấn để tìm bằng chứng cho từng ý, đối chiếu đoạn tìm được với nội dung đang viết và sửa khi thấy bất đồng. Bài đo cả mức câu được nguồn hỗ trợ bằng AIS và mức giữ lại ý định hay cách diễn đạt của bản nháp. Trong Bảng 1, trên đầu ra PaLM cho Natural Questions, điểm AIS do người chấm tăng từ 35,4 lên 43,4 sau RARR. EFEC đạt AIS 48,3 trong cùng nhóm, còn điểm kết hợp giữ nội dung của RARR cao hơn (83,1 so với 10,4). Mục 8 thảo luận giới hạn của việc sửa hoặc xóa câu khi khó tìm được nguồn. Hai loại điểm giúp phát hiện việc chỉnh sửa quá tay. Chúng chưa trực tiếp đo tỷ lệ từ chối đúng khi hồ sơ bảo tàng thiếu thông tin. [Bản hội nghị](https://aclanthology.org/2023.acl-long.910/)

## Áp dụng vào pilot

- Dùng cùng mô hình sinh và cùng kho hồ sơ được duyệt. So ba cấu hình: RAG một lượt, tìm bổ sung khi lượt đầu thiếu bằng chứng, và kiểm rồi sửa bản nháp theo từng dữ kiện. Giới hạn một lượt tìm bổ sung trong pilot để đo thời gian và chi phí theo cùng một ngân sách.
- Tách ca nguồn đúng có trong kho nhưng chưa tìm thấy khỏi ca kho chưa đủ để trả lời. Ví dụ giả định: hồ sơ hiện vật có tên người tặng dưới mã cũ, nên lượt hai có thể tìm bằng mã thay thế đã xác minh. Nếu vẫn chỉ tìm thấy năm tiếp nhận thì trả lời phần có nguồn và nói rõ hồ sơ chưa xác nhận người tặng.
- Chấm việc tìm được đoạn còn thiếu, dữ kiện sau sửa có đúng và được nguồn hỗ trợ, ý đã đúng có bị sửa sai hay bỏ mất, và phản hồi khi nguồn vẫn thiếu hoặc mâu thuẫn. Báo riêng số lượt tìm và thời gian để xem lợi ích đến từ tìm thêm hay bước sửa.
- Hai bài là tiền lệ cho việc tìm thêm và sửa theo nguồn. Đóng góp dự kiến cần được đánh giá bằng nhãn trạng thái bằng chứng và chất lượng phản hồi trên hồ sơ bảo tàng tiếng Việt.
