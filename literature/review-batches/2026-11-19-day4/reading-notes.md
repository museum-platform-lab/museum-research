# Day 4 · Các benchmark cho câu hỏi thiếu căn cứ và nguồn mâu thuẫn

Ngày 19/11/2026. Đọc có trọng điểm phương pháp, kết quả và giới hạn của UAEval4RAG và FaithEval từ PDF proceedings. Hai bài được theo dõi như nguồn đọc bổ sung. Tra tiêu đề, tác giả và định danh trong snapshot 101 chưa thấy bản trùng.

## UAEval4RAG · Peng và cộng sự, ACL 2025

Bài phân sáu loại yêu cầu không thể xử lý trực tiếp, gồm câu thiếu chi tiết, tiền đề sai, câu vô nghĩa, yêu cầu vượt khả năng xử lý định dạng, yêu cầu có rủi ro an toàn và câu nằm ngoài kho dữ liệu. Pipeline tự sinh và kiểm câu theo từng loại. **Acceptable Ratio** chấm phản hồi có phù hợp với loại câu hay không, còn **Unanswered Ratio** theo dõi tỷ lệ yêu cầu bị từ chối. Với câu thiếu chi tiết, hỏi lại hoặc đưa các khả năng có điều kiện có thể được chấp nhận. (§§3.1–3.3, Appendix A.5–A.6)

Trong Table 3, trên MuSiQue với cùng cấu hình truy xuất của hàng tương ứng, Prompt #2 nâng tỷ lệ phản hồi chấp nhận được ở nhóm không trả lời được từ 61,7% lên 88,0%. Tỷ lệ trả lời đúng ở nhóm có đáp án giảm từ 49,0% xuống 16,0%. Đây là đánh đổi theo cấu hình và bộ dữ liệu. Bài chủ yếu dùng câu tổng hợp và hội thoại một lượt. Các số Joint Score in trong Table 3 cho hai hàng MuSiQue Default và Prompt #1 cũng không khớp khi tính lại từ công thức 0,7 × Correctness + 0,3 × Acceptable Ratio với các cột hiển thị. Tổng hợp này dùng các cột thành phần. (Table 3, §3.3 và §6)

[Nguồn toàn văn ACL](https://aclanthology.org/2025.acl-long.415.pdf). SHA-256: 3d9895b3616ce46ed107678a0a14ccd705702740d2343c29d6175f6180c14aa4.

## FaithEval · Ming và cộng sự, ICLR 2025

Bài tạo ba điều kiện ngữ cảnh cho QA: thiếu thông tin cần thiết, tài liệu đưa ra đáp án bất nhất, và tài liệu chứa dữ kiện phản thực được tạo để kiểm model có theo ngữ cảnh hay không. Với bài toán nguồn bất nhất, chỉ dẫn yêu cầu mô hình báo xung đột. Bài báo cáo cả cách chấm khớp chặt và cách chấm chấp nhận nhiều cách diễn đạt. (§3, Figure 2, Tables 4–5)

Phi-3-medium-128k-instruct đạt 75,8% accuracy ở ngữ cảnh gốc nhưng chỉ 7,4% ở tác vụ cần nhận ra ngữ cảnh thiếu thông tin. Ở tác vụ phản thực, GPT-4o đạt 47,5% theo đáp án dựa trên ngữ cảnh được dựng. Kết quả thứ hai đo khả năng theo ngữ cảnh trong phép thử, vì vậy không thể dùng như điểm độ đúng lịch sử. (§§4.1, 4.3, Figures 4 và 6)

Trong miền bảo tàng, hai tài liệu có đáp án khác nhau còn có thể dùng quy ước niên đại khác nhau hoặc nói về hai phiên bản hiện vật. Kiểu phản hồi báo xung đột của benchmark là đối chiếu hữu ích. Xử lý bất đồng lịch sử còn đòi hỏi kiểm thực thể, nguồn và phiên bản. Đây là diễn giải cho dự án, chưa phải kết quả thực nghiệm.

[Nguồn toàn văn ICLR](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf). SHA-256: 4fca0342721af6b22847733796b621e525ec3457b76504edc2a3bf5cc46f3f39.

## Đối chiếu cho Week 6

NoMIRACL kiểm sự hiện diện của đoạn liên quan. DeclineCraft kiểm cách hệ thống phản ứng khi kho tài liệu cũ chưa đủ căn cứ. UAEval4RAG bổ sung các cách phản hồi phù hợp theo loại câu, còn FaithEval kiểm riêng ngữ cảnh bất nhất và phản thực. Với bảo tàng tiếng Việt, phần còn cần xác minh là giá trị của nhãn nguồn ở cấp từng ý, cách chấm trả lời phần có căn cứ, và tiêu chí phân biệt bất đồng nguồn với câu hỏi mơ hồ.

Chuỗi đối chiếu hiện bao phủ 20 bài. Vòng quyết định nhận bài và kiểm chéo theo Week 6 vẫn mở.
