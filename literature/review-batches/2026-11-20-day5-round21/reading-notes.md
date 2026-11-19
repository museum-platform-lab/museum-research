# Đợt 21 ngày 20/11/2026. Nén ngữ cảnh và rà ba bài ưu tiên cuối

Đã đọc có trọng điểm toàn văn P027. Chuỗi đối chiếu có 59 bài, gồm 41 bài trong catalog và 18 bài bổ sung. Hai mục ưu tiên còn chờ toàn văn là P033 và P052. Đã rà truy cập của cả hai theo tiêu đề và DOI. ScienceDirect trả 403 khi mở bằng công cụ web, và OpenAlex chỉ liệt kê trang xuất bản cho hai DOI. Kết quả tìm công khai trong đợt này chưa cho thấy bản toàn văn thay thế. Vòng quyết định chọn bài Week 6 vẫn mở.

## P027 · The Attribution-Compression Frontier in Retrieval-Augmented Generation

Mody, arXiv v1. Bài so các cách giảm ngữ cảnh trên ASQA và QASPER với một mô hình sinh cố định. Mục phương pháp tách việc đoạn rút gọn hỗ trợ câu trả lời khỏi việc lần được về đoạn hồ sơ gốc hỗ trợ cùng mệnh đề. Theo Bảng 1 và tóm tắt, ở một cấu hình tóm tắt kiểu RECOMP trên ASQA, tỷ lệ token giữ lại thực tế là 0,08 dưới ngân sách đặt trước 0,25. Điểm precision trích dẫn là 0,86 khi chấm theo đoạn tóm tắt và 0,12 khi chấm theo đoạn gốc tìm lại. Mục 9 nêu rằng cùng một mô hình suy luận ngôn ngữ được dùng để tìm lại đoạn và chấm hỗ trợ trong cấu hình chính, với tập đoạn ứng viên giới hạn và chưa có đối chiếu độc lập bằng nhãn người. Điểm thấp theo đoạn gốc có thể phản ánh mất dấu nguồn, tìm lại sai hoặc lỗi bộ chấm. Phép thử đo khả năng truy về nguồn và sự hỗ trợ của nguồn theo quy trình của bài. [Toàn văn](https://arxiv.org/abs/2609.14245)

## P033 · SC-RAG

Li và cộng sự, Information Processing & Management, 2026. Đã xác minh DOI và nội dung mô tả công khai của nhà xuất bản. Mô tả cho biết bài kết hợp truy xuất theo ngữ nghĩa và theo khía cạnh, cùng một bước tự sửa theo bằng chứng để xử lý khác biệt giữa kiến thức mô hình và nguồn ngoài. Giữ ở trạng thái chờ toàn văn để kiểm thiết lập đối chứng và kết quả. [Nhà xuất bản](https://doi.org/10.1016/j.ipm.2025.104369)

## P052 · EPRAG

Kinalioglu, Knowledge-Based Systems, 2026. Đã đọc mô tả công khai và README của repo tác giả. Repo tách nhận diện trạng thái bằng chứng khỏi chọn hành động, gồm tổng hợp để trả lời, ưu tiên nguồn để trả lời, hỏi làm rõ, từ chối vì không đủ căn cứ và từ chối theo chính sách. Bản lưu Zenodo công bố mã, cấu hình và kết quả đánh giá, đồng thời ghi rõ gói lưu không chứa bản thảo. Cần giữ EPRAG là đối chiếu gần khi viết về tính mới của cơ chế chọn hành động. Chờ toàn văn để kiểm định nghĩa nhãn, các đối chứng và kết quả của bài. Đợt này chưa chạy mã tái lập. [Nhà xuất bản](https://doi.org/10.1016/j.knosys.2026.116929) · [Bản lưu tái lập](https://zenodo.org/records/21592366) · [README](https://github.com/ihakkikinali/EPRAG_v1.0.0)

## Áp dụng vào pilot

- Khi dùng tóm tắt để lập chỉ mục hoặc chọn đoạn, giữ mã tài liệu, vị trí đoạn gốc và liên kết về hồ sơ. Nếu mô hình dùng bản rút gọn để tạo câu, vẫn chấm đoạn gốc có xác nhận đúng hiện vật, thuộc tính, mốc và giá trị hay không.
- Nếu thử nén, dùng cùng câu hỏi và mô hình sinh. Báo tỷ lệ token giữ lại thực tế, tỷ lệ lần được về đoạn gốc và tỷ lệ đoạn gốc hỗ trợ dữ kiện. Ghi cả trường hợp bản tóm tắt đúng nhưng không tìm lại được đoạn gốc.
- Với cơ chế hỏi lại hoặc từ chối, kiểm khách có thể cung cấp chi tiết giúp tìm ra nguồn phù hợp hay kho hồ sơ vẫn thiếu dữ kiện. Việc tách trạng thái bằng chứng và hành động đã có tiền lệ ở EPRAG. Đóng góp dự kiến cần được đánh giá trên các ca hồ sơ bảo tàng tiếng Việt và trích dẫn ở cấp dữ kiện.
