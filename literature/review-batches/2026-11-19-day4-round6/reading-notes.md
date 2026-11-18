# Day 4, đợt 6 · Trùng tên, khác thời điểm và bất đồng nguồn

Ngày 19/11/2026. Đọc các phần phương pháp và kết quả của AmbigDocs và ConflictBank. Tra tên, mã arXiv và tên phương pháp trong danh mục 101 chưa thấy bản trùng. Hai bài được theo dõi như nguồn đối chiếu bổ sung.

## AmbigDocs · Lee, Ye và Choi, COLM 2024

Bộ dữ liệu dùng trang phân biệt tên trên Wikipedia để thu thập tài liệu về nhiều thực thể cùng tên rồi tạo câu hỏi và tập đáp án gắn với từng thực thể. Bài báo có 36.098 ví dụ, trung bình 2,92 đáp án mỗi câu. Trong 100 ví dụ do tác giả kiểm thủ công, 2% có một tài liệu nói về nhiều thực thể cần phân biệt và 4% có đáp án do mô hình sinh bị sai. Đây là kiểm mẫu của dữ liệu tổng hợp. (§3, Table 1, Appendix B.3)

Trong thiết lập chỉ cấp tài liệu chuẩn, GPT-4 đạt Answer Recall 0,632 nhưng Entity-Answer Recall là 0,473 và Disambig-F1 là 0,289. Khi chỉ dùng năm tài liệu truy xuất, Entity-Answer Recall giảm còn 0,265 trong thiết lập của bài. Phép chấm gắn đáp án với đúng thực thể cho thấy một hệ thống có thể nhắc đúng dữ kiện nhưng ghép nhầm đối tượng. Các điểm này dựa trên bộ tham chiếu và quy tắc chấm của AmbigDocs. (§§4–5, Table 2)

Áp dụng vào hồ sơ hiện vật, trước khi ghi hai đoạn là mâu thuẫn cần kiểm tra chúng có cùng nói về một hiện vật, cùng phiên bản và cùng thuộc tính hay không. Trường hợp tên trùng có thể cần câu hỏi làm rõ hoặc đáp án theo từng đối tượng.

[Bản COLM trên OpenReview](https://openreview.net/attachment?id=mkYCfO822n&name=pdf) · [Bản đã đọc](https://arxiv.org/pdf/2404.12447). SHA-256 9f65c60e119cf0aa5b83748bf45f46fa0dd7362c4b02102a29883d8d0308c197.

## ConflictBank · NeurIPS 2024

Bài bắt đầu từ các dữ kiện Wikidata, xây tình huống thông tin sai, thay đổi theo thời gian và khác biệt ngữ nghĩa, rồi sinh đoạn bằng chứng theo ba phong cách văn bản. Pipeline dùng kiểm suy diễn tự động và các bước lọc. Bản NeurIPS báo 7,45 triệu cặp nhận định–bằng chứng và 553 nghìn cặp QA. Quy mô này gồm dữ liệu được tạo cho phép thử. Không thể xem đó là số bất đồng tự nhiên đã được chuyên gia kiểm. (§2 và Appendix B)

Thử nghiệm §3.2 so hai chế độ: chỉ cấp bằng chứng đối lập với câu trả lời gốc, hoặc cấp hai bằng chứng cho cả đáp án gốc và đáp án đối lập. Table 6 báo GPT-4o ở nhóm thời gian có Memorization Ratio 5,55% và 67,74% tương ứng. MR là tỷ lệ đáp án gốc trong hai nhóm đáp án gốc và đáp án đối lập được đếm, theo công thức OAR/(OAR+CAR). Các tỷ lệ này mô tả lựa chọn giữa hai loại đáp án trong thiết lập có kiểm soát. Chúng chưa đo nhận diện bất đồng, hỏi lại hoặc tỷ lệ câu trả lời đúng lịch sử. (§§3.1–3.2, Table 6)

Với bảo tàng, một hồ sơ ghi nơi lưu giữ năm 2010 và hồ sơ ghi nơi lưu giữ hiện nay có thể đều đúng. Cần giữ mốc thời gian và phạm vi mỗi nguồn để phân biệt thay đổi trạng thái với bất đồng về cùng một trạng thái.

[PDF chính thức NeurIPS](https://papers.nips.cc/paper/2024/file/baf4b960d118f838ad0b2c08247a9ebe-Paper-Datasets_and_Benchmarks_Track.pdf). SHA-256 e0d407f2e90f87e3ec39097c18d4a526455cb78268a648d413d4070e7795d634.

## Đối chiếu cho review

AmbigDocs làm rõ ca trùng tên. ConflictBank làm rõ khác biệt theo thời gian và cách phản ứng với bằng chứng được kiểm soát. Đặt cùng FaithEval và RAMDocs, có thể xác định tiền lệ cho việc kiểm nhiều cách hiểu, bất đồng và thông tin sai. Câu hỏi mở của dự án là những nhãn nào đã tồn tại trong dữ liệu bảo tàng gần nhất và cách kiểm từng ý khi hồ sơ thiếu mốc thời gian hoặc thiếu thông tin nhận dạng. Hồ sơ đối chiếu hiện bao phủ 30 bài. Quyết định nhận bài và kiểm chéo theo Week 6 còn mở.
