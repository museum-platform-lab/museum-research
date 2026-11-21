# Đọc toàn văn đợt 11 ngày 19/11/2026

Đã đọc có trọng điểm toàn văn hai bài ưu tiên trong catalog, P001 và P004. Chuỗi đối chiếu tăng từ 38 lên 40 bài, gồm 22 bài trong catalog và 18 bài bổ sung. Hàng đợi ưu tiên còn 21 mục chưa thấy có ghi chú đọc toàn văn theo cách đếm đã dùng sau đợt 10. Quyết định chọn bài chính thức vẫn đang mở.

## P001 · MuseRAG++

Yifan Hu, Scientific Reports, 2026. Phần Dataset mô tả kho chính về đèn Trường Tín gồm 188 bài nghiên cứu và 5 video tài liệu. Phần Cross-artifact generalization analysis báo cáo thêm ba bộ theo nhóm hiện vật. Hệ thống mô hình hóa ý định, kết hợp truy xuất từ khóa và ngữ nghĩa, kết hợp nguồn đa phương thức và sinh câu trả lời gắn nguồn. Phần Evaluation metrics tách Recall@k ở cấp đoạn, precision/recall ở cấp dữ kiện và accuracy ở cấp câu trả lời. Precision đòi dữ kiện đúng và có hỗ trợ trong bằng chứng truy xuất. Bảng 1 báo cáo Recall@10 và F1 của hệ thống đầy đủ lần lượt là 83,1 và 79,6, so với 77,8 và 74,2 của BGE-M3 + ChatGLM4-9B-Chat. Bảng 3 báo cáo điểm người chấm về mức có bằng chứng và khả năng lần về nguồn. Bảng 4 bỏ từng thành phần để so hiệu quả. Các mục đánh giá đã rà chưa cho thấy một phép đo riêng về quyết định trả lời hay từ chối khi hồ sơ thiếu hoặc mâu thuẫn. [Bài báo](https://www.nature.com/articles/s41598-026-55700-9)

Repo bài báo trỏ tới truy cập được. README của bản công khai ghi rõ đây là triển khai tối giản, dùng BGE-M3 để tìm theo ngữ nghĩa, yêu cầu model chèn mã nguồn và đo tỷ lệ câu có mã. Mô hình hóa ý định, kết hợp sparse–dense và phối hợp đa phương thức được ghi là phần có thể bổ sung. Tỷ lệ câu có mã nguồn cho biết độ bao phủ trích dẫn về hình thức. Cần kiểm riêng đoạn được dẫn có chứng minh dữ kiện hay không. Đợt này đã kiểm danh mục tệp và README, chưa chạy mã hoặc xác minh toàn bộ nhãn dữ liệu. [Repo công khai](https://github.com/Alkaid-Hu/MuseRAG-/tree/main/MuseRAGpp)

## P004 · Context or Retrieval?

Ramos-Varela và cộng sự, IWSDS 2025. Mục 3–5 mô tả 1.020 tác phẩm với hồ sơ và mô tả ảnh do mô hình sinh. GPT-4-Turbo tạo 12.240 cặp hỏi–đáp, trong đó khoảng 1.200 cặp được kiểm thủ công. Cấu hình ngữ cảnh đầy đủ đưa toàn bộ mô tả và thông tin của tác phẩm tương ứng cho LLaMA 3.1-8B. Bảng 3 báo cáo cosine similarity trung bình 0,879 cho cấu hình này và tối đa 0,698 cho nhóm RAG, với ModernBERT và chia đoạn theo câu. Mục 5–6 nói kết quả RAG được đo trên đầu ra trực tiếp của pipeline truy xuất, không qua bước tạo hoặc mở rộng đáp án. So sánh này thay đổi cả nguồn đầu vào sẵn có và cách tạo đầu ra. Điểm đo là độ gần với đáp án tham chiếu tổng hợp, chưa đo độ đúng của từng dữ kiện hay đoạn trích. [Bài báo](https://aclanthology.org/2025.iwsds-1.10/)

## Hàm ý cho RAG bảo tàng

- Đưa MuseRAG++ vào bảng nghiên cứu gần nhất ở cùng miền. Đóng góp dự kiến cần cụ thể hơn việc kết hợp truy xuất và gắn nguồn, vì bài đã làm cả hai và đo ở cấp dữ kiện.
- Dùng cùng mô hình sinh và cách chấm để so ba điều kiện: các đoạn tập hợp qua truy xuất, các đoạn chuẩn do người gán nhãn cung cấp, và hồ sơ đầy đủ của hiện vật đã biết nếu vừa ngân sách ngữ cảnh. Điều kiện biết sẵn hiện vật giúp phân tích lỗi, còn cấu hình truy xuất thông thường đo tác vụ thực tế.
- Giữ các phép chấm tìm đúng đoạn, nguồn trích hỗ trợ từng dữ kiện, và trả lời hoặc từ chối khi thiếu căn cứ. Chạy trên hồ sơ tiếng Việt đã gán nhãn để kiểm đóng góp dự kiến. Các khác biệt với hai bài là căn cứ thiết kế đánh giá; tính mới vẫn cần đối chiếu với các bài ưu tiên còn lại.
