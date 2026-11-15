# Định hướng nghiên cứu và paper

## Câu hỏi chính

Với cùng corpus, mô hình sinh và ngân sách context, truy xuất đường quan hệ có chứng cứ có cải thiện độ đầy đủ của nguồn và tính đúng của câu trả lời nhiều bước so với vector RAG không?

Giả thuyết H1: đường quan hệ giúp truy xuất đủ chứng cứ cho câu hỏi cần nối nhiều thực thể. H2: quyết định từ chối dựa trên mức đủ chứng cứ giảm câu trả lời không được nguồn hỗ trợ. H3: lợi ích vẫn xuất hiện khi đánh giá trên bộ sưu tập khác.

Các giả thuyết phải được kiểm chứng; kết quả không cải thiện cũng cần báo cáo.

## Phương pháp ứng viên

1. Nhận diện thực thể trong câu hỏi và liên kết với node.
2. Truy xuất đoạn văn bằng vector hoặc từ khóa.
3. Mở rộng graph tối đa 2–3 cạnh ở giai đoạn thử nghiệm.
4. Xếp hạng đường đi theo mức liên quan, chứng cứ hỗ trợ và độ dài.
5. Chọn tập chứng cứ trong ngân sách token cố định.
6. Sinh câu trả lời với trích dẫn tới đoạn nguồn; từ chối nếu không đủ.

Các đặc trưng, trọng số và ngưỡng chỉ điều chỉnh trên dev. Đường graph thể hiện quan hệ, không tự chứng minh một diễn giải nghệ thuật hoặc quan hệ nhân quả.

## Đóng góp có thể theo đuổi

- Benchmark nhỏ, có nguồn và nhãn câu hỏi nhiều bước trong nghệ thuật Việt Nam.
- Phương pháp chọn chứng cứ theo đường quan hệ, nếu khác biệt rõ với công trình trước.
- Phân tích khi graph giúp hoặc làm hại truy xuất, nhất là dưới dịch chuyển bộ sưu tập.

“Dùng GraphRAG cho nghệ thuật” và “ghép nhiều LLM” chưa tự chứng minh tính mới. Cần đọc nghiên cứu liên quan trước khi chốt tuyên bố đóng góp.

## Điều kiện quyết định viết paper

Sau pilot: có baseline hoạt động, dữ liệu có thể đánh giá hợp lệ và phương pháp có điểm khác biệt cụ thể. Sau thí nghiệm: có kết quả kèm độ bất định, ablation và phân tích lỗi. Chọn loại bài và venue theo kết quả thực tế, quyền phát hành dữ liệu và hướng dẫn venue tại thời điểm nộp.

30–50 tác phẩm đủ thử MVP, chưa đủ để khẳng định benchmark mạnh. Chỉ mở rộng số lượng sau khi kiểm tra câu hỏi không lặp, độ đa dạng và khả năng chú giải.

Outline bản thảo: vấn đề → related work → dữ liệu → phương pháp → protocol → kết quả → phân tích lỗi → giới hạn. Bắt đầu viết protocol trước khi chạy test cuối.
