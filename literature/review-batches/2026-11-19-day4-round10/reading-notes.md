# Đọc toàn văn đợt 10 ngày 19/11/2026

Đợt này xem cách đánh giá câu trả lời khi một câu hỏi có nhiều cách hiểu. AmbigQA và ASQA chưa có bản ghi theo tên hoặc định danh trong catalog 101 đã đối chiếu. Chuỗi ghi chú hiện bao phủ 38 bài. Vòng chọn bài chính thức vẫn đang mở.

## AmbigQA

Min và cộng sự, EMNLP 2020. Mục 3 định nghĩa hai đầu ra: tìm những đáp án hợp lý và viết lại câu hỏi sao cho mỗi cách viết xác định một cách hiểu. Mục 4 và Bảng 2 mô tả AmbigNQ với 14.042 câu hỏi gốc từ NQ-Open được gán nhãn. Bảng 1 minh họa các dạng mơ hồ, gồm thực thể được nhắc tới, dạng đáp án và mốc thời gian. Bảng 3 chấm độ bao phủ đáp án và chất lượng viết lại. Một câu hỏi viết lại để mô tả một cách hiểu khác với câu hỏi làm rõ gửi cho người dùng để chọn giữa các cách hiểu. Bài cung cấp mẫu cho bước gán nhãn từng cách hiểu. [Bài báo và toàn văn](https://aclanthology.org/2020.emnlp-main.466/)

## ASQA

Stelmakh và cộng sự, EMNLP 2022. Mục 3 và Bảng 1 mô tả 6.316 câu hỏi lấy từ tập con mơ hồ của AmbigQA, với câu trả lời dài giải thích các cách hiểu và các đoạn Wikipedia hỗ trợ. Hai bộ có quan hệ kế thừa về câu hỏi, nên cần nhận diện trùng nếu dùng cùng nhau. Mục 4 tách độ giống văn bản với câu trả lời chuẩn khỏi mức bao phủ từng cách hiểu. Disambig-F1 dùng một mô hình đọc câu trả lời dài để xem có rút được đáp án cho từng câu hỏi đã làm rõ không. Phần chấm thủ công cũng kiểm việc này. Các phép đo ở Mục 4 cho biết câu trả lời đã bao phủ bao nhiêu cách hiểu, còn việc mỗi mệnh đề được đoạn trích dẫn chứng minh cần một phép chấm độc lập. [Bài báo và toàn văn](https://aclanthology.org/2022.emnlp-main.566/)

## Áp dụng vào RAG bảo tàng

- Gán nhãn từng cách hiểu khả dĩ bằng hiện vật hoặc thực thể, thuộc tính, mốc thời gian nếu cần và đoạn nguồn tương ứng. Ca minh họa: “Ai tặng chiếc bình men lam?” khi cùng bộ sưu tập có hai chiếc bình phù hợp với mô tả. Lưu mã và tên hiển thị của mỗi chiếc để kiểm nhầm nguồn.
- So hai cách phản hồi khi hồ sơ xác nhận rõ cả hai hiện vật: nêu kết quả theo từng chiếc kèm nguồn, hoặc hỏi một chi tiết phân biệt mà khách có thể cung cấp, chẳng hạn mã trên nhãn trưng bày. Khi xác định được hiện vật nhưng hồ sơ thiếu dữ kiện được hỏi, chấm phản hồi có nói rõ phần thiếu. Khi hai nguồn có dữ kiện khác nhau về cùng hiện vật và cùng mốc, dùng nhãn bất đồng nguồn của đợt 6.
- Với câu trả lời có nhiều phương án, chấm đúng thực thể và đúng nguồn cho từng phương án. Với câu hỏi làm rõ, chấm chi tiết được hỏi có phân biệt được các phương án hay không. Nếu thử hội thoại hai lượt, sau câu trả lời của khách, chấm lại đáp án cuối và đoạn nguồn.
- Đây là thiết kế pilot. Hai bài nguồn kiểm phần nhận diện và trình bày các cách hiểu. Việc hỏi lại người dùng, từ chối và hiệu quả trên hồ sơ bảo tàng tiếng Việt cần được kiểm trực tiếp.

