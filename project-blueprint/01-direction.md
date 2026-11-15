# Định hướng sản phẩm

## Vấn đề muốn giải quyết

Người yêu nghệ thuật có thể tìm thấy nhiều mô tả tác phẩm, nhưng khó đối chiếu quan hệ giữa nghệ sĩ, chất liệu, giai đoạn và nguồn tư liệu. Sản phẩm giúp khám phá những liên hệ đó và kiểm tra căn cứ của câu trả lời.

Người dùng chính: người học và người yêu nghệ thuật Việt Nam muốn tìm hiểu có dẫn nguồn. Chưa đặt mục tiêu phục vụ nghiên cứu giám định, định giá hoặc xác thực tác phẩm.

## Hành trình sử dụng

1. Tìm tác phẩm theo tên, nghệ sĩ hoặc chất liệu.
2. Xem hồ sơ tác phẩm và nguồn của từng thông tin.
3. Hỏi câu hỏi liên quan đến một hoặc nhiều tác phẩm.
4. Xem câu trả lời, đoạn nguồn hỗ trợ và chuỗi quan hệ được dùng.
5. Nhận thông báo thiếu chứng cứ nếu dữ liệu không đủ.

Ví dụ câu hỏi phụ thuộc dữ liệu: “Hai tác phẩm này dùng chung chất liệu nào?”, “Những tác phẩm nào cùng nghệ sĩ và cùng giai đoạn?”, “Nguồn nào xác nhận chất liệu của tác phẩm X?”.

## MVP

- 30–50 tác phẩm trong một bộ sưu tập có nguồn hợp lệ.
- Danh sách, tìm kiếm và trang chi tiết tác phẩm.
- Quan hệ tác phẩm–nghệ sĩ–chất liệu–giai đoạn, có chứng cứ.
- Hỏi đáp văn bản bằng tiếng Việt, hiện trích dẫn và đường quan hệ.
- Lưu log truy xuất để đánh giá; trạng thái trả lời hoặc thiếu chứng cứ.

Ảnh là tùy chọn: được dùng ảnh dự phòng. Kiến thức phiên bản đầu lấy từ văn bản, không suy luận phong cách hoặc mô típ từ ảnh chưa được chú giải.

## Để sau MVP

Tìm kiếm bằng ảnh, nhận diện mô típ, trích xuất graph bằng nhiều LLM, cộng đồng đóng góp, ứng dụng điện thoại và đa ngôn ngữ. Tập trung một hướng nghiên cứu chính trước khi thêm các nhánh này.

## Tiêu chí sản phẩm hoàn thành

Người dùng mở được hồ sơ từ database mới, kiểm tra được nguồn, và hiểu vì sao hệ thống trả lời hoặc từ chối. Demo có thể chạy lại theo hướng dẫn và không phụ thuộc ảnh Drive của dự án cũ.

Hứng thú nghệ thuật xác định chủ đề; kinh nghiệm KG xác định cách truy xuất; kinh nghiệm ghép mô hình là hướng mở rộng; kinh nghiệm LODO giúp thiết kế đánh giá khi chuyển bộ sưu tập.
