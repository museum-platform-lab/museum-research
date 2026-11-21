# Day 4, đợt 5 · Phân biệt thiếu bằng chứng và mâu thuẫn

Ngày 19/11/2026. Đã đọc các phần liên quan về phương pháp, nhãn, kết quả và giới hạn trong hai PDF proceedings. RAGTruth đã có ID P087 trong danh mục. RefChecker được ghi riêng để xét ở vòng toàn văn vì tra theo tiêu đề, tên phương pháp, ID ACL và mã arXiv chưa thấy bản trùng.

## RefChecker · Hu và cộng sự, EMNLP 2024

RefChecker tách đầu ra thành các ý theo cấu trúc thực thể, quan hệ và thực thể. Mỗi ý được chấm với nguồn tham chiếu theo ba nhãn: được hỗ trợ, bị nguồn bác bỏ hoặc chưa đủ thông tin để xác minh. KnowHalBench có khoảng 11.000 ý trong 2.100 câu trả lời. Tác giả báo 23% số ý được gán nhãn hai lần và mức đồng thuận 95% trên phần đó. Bộ bài chọn ca khó qua một bộ kiểm ở cấp câu trả lời, nên thống kê không đại diện cho tỷ lệ lỗi thường gặp ngoài thực tế. (§§3–5)

Table 6 báo biến thể RepC-LE-nn đạt trung bình accuracy 81,27% và macro-F1 60,80 trên ba điều kiện. Kết quả thay đổi đáng kể theo điều kiện, chẳng hạn macro-F1 47,56 ở nhóm ngữ cảnh nhiễu. Bài dùng phép gộp nghiêm, trong đó một ý mâu thuẫn có thể quyết định nhãn của cả đáp án. Do đó cần giữ nhãn từng ý nếu muốn chấm phần trả lời đúng bên cạnh phần sai. (§6, Table 6)

Tác giả nêu rằng biểu diễn ba thành phần có thể làm mất điều kiện thời gian, và bộ kiểm đôi khi dựa vào kiến thức sẵn có để đổi nhãn “chưa đủ thông tin”. Với bảo tàng, một nhận định về niên đại hoặc quy thuộc cần giữ cả mốc thời gian, đối tượng và phạm vi nguồn khi trích thành các ý nhỏ. (Limitations)

[PDF EMNLP](https://aclanthology.org/2024.emnlp-main.395.pdf). SHA-256 0aa0637a8a1aabbeaf2bf8172285cd0854661fdebcf6135bfc6271d75a59651b.

## RAGTruth · Niu và cộng sự, ACL 2024 · P087

Corpus có 17.790 câu trả lời trên ba tác vụ. Riêng QA có 989 đầu vào và 5.934 câu trả lời từ các mô hình. Người gán nhãn đánh dấu vị trí lỗi trong **đầu ra**. Bài phân biệt mâu thuẫn với ngữ cảnh và thêm thông tin thiếu căn cứ, mỗi nhóm có dạng rõ rệt và dạng khó nhận ra. Đây là nhãn vị trí lỗi trong câu sinh. Nhãn đoạn nguồn có thể dùng để chứng minh từng ý là một cấu trúc dữ liệu khác. (§3 và Table 2)

Trong phần QA, Llama-2-13B đã tinh chỉnh đạt F1 68,2 khi phát hiện câu trả lời chứa lỗi và 58,2 khi định vị phần lỗi. Đây là điểm của bộ phát hiện trên hai đơn vị chấm khác nhau. Các điểm này chưa đo mức trả lời đủ ý, độ đúng lịch sử hoặc khả năng áp dụng sang tiếng Việt. Tác giả cũng ghi việc kiểm tra khả năng chuyển sang dữ liệu khác là hướng còn mở. (Tables 5–6 và §8)

[PDF ACL](https://aclanthology.org/2024.acl-long.585.pdf). DOI 10.18653/v1/2024.acl-long.585. SHA-256 17afb377ca5ea8cf672efa9a95fca5889713e94c6fd0355f89f8e01651ddfd4d. Bản proceedings 2024 xác nhận trạng thái xuất bản của P087, trước đó danh mục dẫn arXiv.

## Đối chiếu cho review

RefChecker và RAGTruth đã có tiền lệ trực tiếp cho việc phân biệt thiếu căn cứ với mâu thuẫn và đánh dấu lỗi ở mức nhỏ hơn cả câu trả lời. Hai bài tập trung vào các ý mô hình đã nêu. Với câu hỏi “Chiếc bình được làm khi nào và do ai?”, trường hợp chỉ trả lời đúng niên đại còn cần một kiểm riêng về phần nghệ nhân bị bỏ sót. Mâu thuẫn giữa hai tài liệu cũng cần ghi riêng với mâu thuẫn giữa lời đáp và đoạn tài liệu dùng để kiểm. Các phân biệt này giúp rà dữ liệu bảo tàng hiện có, trong khi tính mới của nhãn theo từng ý và khả năng kiểm nhãn ViCH-QA vẫn còn mở.

Chuỗi ghi chú đối chiếu bao phủ 28 bài. Quyết định nhận bài và kiểm chéo Week 6 còn mở.
