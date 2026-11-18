# Đọc toàn văn đợt 8 ngày 19/11/2026

Hai bài bổ sung phép thử cho bước mô hình đọc các đoạn mà RAG đã truy xuất. Hai đầu mối chưa có bản ghi trùng theo tên hoặc định danh trong catalog 101 ứng viên đã đối chiếu. Chuỗi ghi chú hiện bao phủ 34 bài. Vòng chọn bài chính thức vẫn đang mở.

## Lost in the Middle

Liu và cộng sự, TACL 2024. Mục 2 và Hình 5 dùng câu hỏi NaturalQuestions-Open, một đoạn Wikipedia chứa đáp án và các đoạn truy xuất có liên quan nhưng không chứa đáp án đã gán nhãn. Khi di chuyển đoạn chứa đáp án, nhiều cấu hình đạt kết quả cao hơn ở đầu hoặc cuối và giảm khi đoạn này nằm giữa. Phụ lục A kiểm tra lại trên nhóm câu hỏi ít mơ hồ hơn. Mục 5 và Hình 11 chạy hệ truy xuất–đọc thực tế, trong đó độ bao phủ của bộ truy xuất còn tăng sau khi mức cải thiện độ chính xác của bộ đọc đã chậm lại. Bài đo độ đúng của đáp án và độ bao phủ truy xuất. Việc kiểm đoạn trích thực sự chứng minh từng mệnh đề cần một phép chấm riêng. [Bài báo và toàn văn](https://aclanthology.org/2024.tacl-1.9/)

## NoLiMa

Modarressi và cộng sự, ICML 2025. Mục 3 xây dựng bài kiểm tra tổng hợp, giấu một dữ kiện có ít từ trùng với câu hỏi trong văn bản dài. Câu hỏi có thể yêu cầu nối địa danh với công trình hoặc địa điểm qua một hay hai bước liên hệ. Mục 4.4.4, Hình 5 và Phụ lục D bổ sung một câu chứa từ khóa của câu hỏi nhưng không cung cấp đáp án. Hiệu năng giảm khi thêm câu gây nhiễu ở hai mô hình được thử trong cấu hình này. Ở kết quả chính, 11 trong 13 mô hình xuống dưới một nửa điểm nền ngữ cảnh ngắn của chính chúng tại 32 nghìn token. Hai kết quả dùng câu hỏi tiếng Anh và dữ kiện cài vào văn bản, nên cần kiểm lại trên hồ sơ bảo tàng tiếng Việt và độ dài ngữ cảnh mà hệ thống thực sự dùng. [Bài báo và toàn văn](https://proceedings.mlr.press/v267/modarressi25a.html)

## Áp dụng vào bộ đánh giá RAG bảo tàng

- Với cùng câu hỏi và cùng tập đoạn, đặt đoạn chuẩn lần lượt ở đầu, giữa và cuối, giữ nguyên nội dung và độ dài. Chấm đáp án và đoạn trích dẫn cho từng vị trí.
- Với cùng bằng chứng chuẩn và vị trí, thay một đoạn phụ bằng đoạn gần độ dài có nhiều từ khóa trùng nhưng mô tả hiện vật khác. Ví dụ giả định: câu hỏi hỏi về chiếc bình A, hồ sơ chuẩn gọi nó bằng mã hiện vật, còn đoạn gây nhiễu lặp cụm “bình gốm men lam” về chiếc bình B. Chỉ dùng ca mà người gán nhãn xác nhận được mã và tên cùng chỉ một hiện vật.
- Chạy thêm cấu hình truy xuất thông thường. Ghi riêng bằng chứng chuẩn có nằm trong tập đoạn đưa cho mô hình hay không. Trong các ca đã có đoạn chuẩn, chấm đáp án và đoạn trích có hỗ trợ đáp án không. Khi bỏ đoạn chuẩn để tạo ca thiếu bằng chứng, kiểm mọi đoạn còn lại rồi mới chấm khả năng từ chối hoặc nói rõ thiếu thông tin.
- Giữ ngân sách ngữ cảnh và thứ tự đoạn nhất quán khi so các biến thể ngoài yếu tố đang thử. Chọn độ dài theo phân bố hồ sơ và cấu hình thực tế, rồi mới so số lượng đoạn hoặc bộ sắp xếp lại kết quả.

Hai bài cung cấp cách kiểm soát thí nghiệm. Các kết quả trên benchmark nguồn chưa cho biết mức lỗi của hệ thống bảo tàng.
