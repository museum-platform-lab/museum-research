# Đọc toàn văn đợt 7 ngày 19/11/2026

Hai bài bổ sung cách thiết kế ca kiểm thử theo thời gian cho trợ lý bảo tàng tiếng Việt. Cả hai được đối chiếu với catalog hiện tại và chưa có bản ghi trùng theo tên hoặc DOI. Tổng số bài đã đối chiếu trong chuỗi ghi chú là 32. Số này ghi nhận tiến độ đọc và đối chiếu, còn quyết định đưa vào tổng quan chính thức theo tiêu chí chọn bài vẫn đang mở.

## SituatedQA

Michael J.Q. Zhang và Eunsol Choi, EMNLP 2021. Bài phân biệt câu hỏi có đáp án ổn định với câu hỏi có đáp án thay đổi theo thời gian hoặc địa điểm. Một câu hỏi có thể được đánh giá ở nhiều mốc với đáp án khác nhau. Mục 5, Bảng 5–6 và Mục 6 đối chiếu đáp án khớp với đúng ngữ cảnh được hỏi và đáp án khớp với bất kỳ ngữ cảnh nào đã gán nhãn. Bảng 5 báo cáo 23,0% exact match trên nhóm thời gian cho cấu hình truy xuất tốt nhất trong bảng. Các thí nghiệm đo khớp đáp án và phân tích lỗi sai ngữ cảnh. Việc trích đoạn nguồn đủ để chứng minh mốc thời gian cần phép đo riêng trong bộ đánh giá của mình. [Toàn văn](https://aclanthology.org/2021.emnlp-main.586.pdf)

## TempReason

Qingyu Tan, Hwee Tou Ng và Lidong Bing, ACL 2023. Mục 3 phân biệt ba dạng câu hỏi: tính toán giữa hai mốc, tìm sự kiện hoặc trạng thái ứng với một mốc, và suy ra quan hệ giữa các sự kiện. Dữ liệu cho hai dạng sau dựa trên sự kiện có thời gian trong Wikidata. Ở chế độ Reasoning QA, mô hình nhận danh sách dữ kiện đúng chủ đề ở dạng cấu trúc. Ở chế độ open-book QA, mô hình nhận các đoạn văn truy xuất. Bảng 4 báo cáo TempT5 đạt 88,9 F1 và 36,3 F1 tương ứng ở hai chế độ cho nhóm thời gian–sự kiện. Đây là kết quả theo hai cấu hình của bài, với dữ kiện cấu trúc được cung cấp sẵn ở cấu hình đầu. Bài đo F1 và exact match của đáp án. Bằng chứng cho từng mệnh đề và cách xử lý khi hồ sơ thiếu mốc cần gán nhãn riêng. [Toàn văn](https://aclanthology.org/2023.acl-long.828.pdf)

## Áp dụng vào bộ đánh giá

- Tạo cặp câu hỏi về cùng hiện vật và thuộc tính, chỉ thay mốc được hỏi. Ví dụ giả định là “Hiện vật A được trưng bày ở đâu vào năm 2019?” và cùng câu hỏi cho năm 2023. Ghi đoạn nguồn và khoảng thời gian mà mỗi đoạn xác nhận.
- Phân biệt mốc trong câu hỏi, thời gian sự kiện hoặc hiệu lực của dữ kiện, và ngày công bố hoặc cập nhật tài liệu. Một bài viết năm 2024 có thể mô tả đợt trưng bày năm 2019. Nếu đoạn nguồn chỉ nói “hiện đang trưng bày” và chưa đủ thông tin về thời điểm áp dụng, đánh dấu thiếu căn cứ cho câu hỏi về năm 2019.
- Khi chấm, ghi riêng đáp án đúng mốc, nguồn thực sự hỗ trợ mốc, và phản hồi khi thiếu căn cứ. Một đáp án có thể trùng đáp án chuẩn trong khi trích dẫn chỉ chứng minh cho năm khác.
- Chỉ gán mâu thuẫn khi hai nguồn nói về cùng hiện vật, thuộc tính và khoảng thời gian chồng lấp. Hai vị trí trưng bày tại hai thời kỳ khác nhau có thể đồng thời đúng. Thiết kế này nối trực tiếp với phân loại mâu thuẫn và nhiều cách hiểu đã ghi ở đợt 6.

Hai bài cung cấp mẫu để thiết kế ca kiểm thử. Mức độ áp dụng và số ca khả thi phụ thuộc vào các hồ sơ bảo tàng thực tế có mốc thời gian kiểm chứng được.
