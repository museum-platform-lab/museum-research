# Đọc toàn văn đợt 9 ngày 19/11/2026

Đợt này tập trung vào bước tìm hồ sơ trước khi sinh câu trả lời. MIRACL đã có trong catalog dưới mã P077. EntityQuestions là đầu mối bổ sung, chưa thấy bản ghi theo tên hoặc định danh trong catalog 101. Hai bài chưa xuất hiện trong các ghi chú đọc và bảng trích xuất trước của chuỗi đã rà, nâng số bài đối chiếu trong chuỗi lên 36. Vòng chọn bài chính thức vẫn đang mở.

## EntityQuestions

Sciavolino và cộng sự, EMNLP 2021. Bộ câu hỏi theo mẫu được tạo từ các dữ kiện Wikidata và đánh giá truy xuất trên Wikipedia tiếng Anh. Bảng 1 báo cáo top-20 retrieval accuracy là 71,2% cho BM25, 49,7% cho DPR huấn luyện trên Natural Questions và 56,7% cho DPR huấn luyện trên nhiều tập. Thứ tự đảo chiều trên Natural Questions, nơi hai cấu hình DPR đều vượt BM25. Số 71,2% lấy từ bản xuất bản ACL Anthology. Bản arXiv v3 báo cáo 72,0% cho BM25 cùng dòng. Mục 4.1 và Hình 1 cho thấy kết quả DPR giảm ở thực thể ít xuất hiện, với số liên kết Wikipedia làm chỉ dấu. Mức chênh phản ánh các mô hình, kho và câu hỏi của bài. Với bảo tàng, mã hiện vật và tên riêng thường là tín hiệu từ khóa hữu ích, còn tên gọi khác có thể cần đối sánh theo ngữ nghĩa hoặc bảng tên đã kiểm chứng. Hai trường hợp này cần được đo riêng trên dữ liệu của mình. [Bài báo và toàn văn](https://aclanthology.org/2021.emnlp-main.496/)

## MIRACL

Zhang và cộng sự, TACL 2023. Mục 3, Bảng 2 và Mục 6 mô tả bộ truy xuất 18 ngôn ngữ, với câu hỏi và đoạn Wikipedia cùng ngôn ngữ, có nhãn liên quan do người gán. Tiếng Việt vắng mặt trong danh sách. Bảng 5 báo cáo Recall@100 trung bình trên tập phát triển là 0,772 với BM25, 0,790 với mDPR và 0,880 với phương án kết hợp hai điểm sau khi chuẩn hóa. Trên tiếng Indonesia, BM25 đạt 0,904 so với 0,768 của phương án kết hợp, cho thấy kết quả trung bình cần đọc cùng kết quả theo nhóm. Mục 5.2 cho biết phiên bản cuối loại các câu mà người gán nhãn chưa nhận diện được đoạn liên quan trong các cặp được cung cấp. Vì vậy, cách so sánh bộ truy xuất có thể tham khảo từ bài, còn ca thiếu căn cứ và đánh giá từ chối cần được xây dựng riêng. [Bài báo và toàn văn](https://aclanthology.org/2023.tacl-1.63/)

## Áp dụng vào RAG bảo tàng

- Chạy BM25, truy xuất theo ngữ nghĩa và kết hợp hai cách trên cùng tập đoạn tiếng Việt. Giữ cố định cách chia đoạn và số đoạn được chuyển cho mô hình. Chọn cấu hình trên tập phát triển và báo cáo kết quả trên tập kiểm thử.
- Tạo cặp câu hỏi cùng hiện vật và thuộc tính. Một câu dùng mã hoặc tên chuẩn, câu kia dùng tên gọi khác đã xác minh. Đánh dấu riêng các ca có tên dễ nhầm với hiện vật khác. Nếu có nhiều câu cho cùng hiện vật, giữ chúng cùng một phần dữ liệu khi chia tập.
- Trên nhóm có đáp án, báo cáo tỷ lệ câu mà ít nhất một đoạn nguồn chuẩn được đưa vào top-k. Với câu cần nhiều nguồn, báo cáo thêm tỷ lệ có đủ các đoạn bắt buộc. Sau đó chấm câu trả lời và trích dẫn khi mô hình đã nhận đủ nguồn. Cách này nối với đợt 8, vốn giữ bằng chứng trong ngữ cảnh và kiểm lỗi ở bước đọc.
- Chỉ dùng tên gọi khác có nguồn xác nhận và tách ca thiếu căn cứ khỏi mẫu số của chỉ số tìm thấy đoạn chuẩn. Độ bao phủ và lựa chọn mô hình vẫn cần kiểm bằng kho hồ sơ thực tế.
