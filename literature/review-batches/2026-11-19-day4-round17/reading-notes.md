# Đọc toàn văn đợt 17 ngày 19/11/2026

Đã đọc có trọng điểm P034 và P079 từ bản hội nghị. Chuỗi đối chiếu hiện có 52 bài, gồm 34 bài trong catalog và 18 bài bổ sung. Còn 9 ứng viên ưu tiên chưa thấy ghi chú đọc toàn văn. Vòng chọn bài chính thức vẫn mở.

## P034 · Self-RAG

Asai và cộng sự, ICLR 2024. Mục 3 và Bảng 1 mô tả các tín hiệu mà mô hình học qua huấn luyện. Retrieve quyết định có cần tìm đoạn mới, IsRel chấm đoạn liên quan, IsSup chấm mức đoạn hỗ trợ phần trả lời, còn IsUse chấm tính hữu ích. Khi sinh, các tín hiệu này tham gia chọn phương án cho từng phần câu trả lời. Bảng 2 trên ASQA báo cáo precision/recall trích dẫn của bản 13B là 70,3/71,3, còn Ret-ChatGPT là 65,1/76,6. Hai chỉ số có thể đi theo hai hướng. Phần Ethical Concerns lưu ý Self-RAG vẫn sinh nội dung có trích dẫn chưa đủ hỗ trợ. Quyết định có truy xuất và tín hiệu hỗ trợ trong bài là tiền lệ gần cho cơ chế kiểm trong lúc sinh. Pilot bảo tàng cần phép chấm riêng cho quyết định trả lời, trả lời một phần hoặc dừng khi nguồn vẫn thiếu. Nếu dùng prompt để mô phỏng bước tự kiểm, ghi rõ đây là đối chứng lấy cảm hứng từ Self-RAG. Việc gọi tên Self-RAG đầy đủ cần mô hình và cấu hình phản tư đã huấn luyện tương ứng. [Bản hội nghị](https://proceedings.iclr.cc/paper_files/paper/2024/hash/25f7be9694d7b32d5cc670927b8091e1-Abstract-Conference.html)

## P079 · RAGAS

Es và cộng sự, EACL System Demonstrations 2024. Mục 4 tách ba chỉ số: mức câu trả lời được ngữ cảnh hỗ trợ, mức trả lời đúng trọng tâm, và mức ngữ cảnh liên quan. Để tính faithfulness, mô hình tách câu trả lời thành các mệnh đề rồi kiểm từng mệnh đề có suy ra được từ ngữ cảnh đã cung cấp hay không. Bảng 4 báo cáo mức đồng ý 0,95 với người chấm cho faithfulness trong phép so sánh theo cặp trên WikiEval. Số này thuộc thiết lập với dữ liệu tiếng Anh của bài, chưa xác lập độ chính xác khi chấm mệnh đề tiếng Việt. Mệnh đề có thể được một đoạn trong ngữ cảnh hỗ trợ, trong khi đoạn mà câu trả lời thực sự dẫn lại nói về hiện vật khác. Do đó cần chấm riêng cặp mệnh đề–đoạn trích cụ thể bên cạnh điểm hỗ trợ chung. Ghi phiên bản thư viện, tên metric và mô hình chấm để tái lập. [Bản hội nghị](https://aclanthology.org/2024.eacl-demo.16/)

## Áp dụng vào pilot

- Giữ cùng câu hỏi, đoạn đầu vào và mô hình sinh khi so RAG cơ sở với cấu hình prompt có bước tự kiểm. Ghi riêng ca tìm thêm nếu thay đổi đầu vào. Chấm từng dữ kiện và tỷ lệ từ chối nhầm khi có đủ nguồn.
- Với một mẫu có nhãn người, chấm từng mệnh đề hai lần: có đoạn nào trong tập truy xuất hỗ trợ, và đoạn thực sự được dẫn có hỗ trợ. Ví dụ, một đoạn xác nhận niên đại hiện vật A nhưng câu trả lời dẫn hồ sơ B. Điểm hỗ trợ chung có thể đạt, còn điểm trích dẫn phải ghi lỗi.
- Khi hồ sơ chỉ đủ một phần, kiểm mô hình giữ thông tin đã xác nhận và nêu rõ phần còn thiếu. Kiểm sai lệch của bộ chấm tự động trên tên hiện vật, mã hồ sơ, niên đại và mệnh đề cần ghép nguồn trước khi dùng điểm này để so hệ thống.
