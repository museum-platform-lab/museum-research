# Day 4, đợt 4 · Tìm đủ bằng chứng và dùng đúng bằng chứng

Ngày 19/11/2026. Đọc có trọng điểm phương pháp và kết quả của IIRC và HotpotQA từ bản proceedings. MuseumQA được kiểm truy cập riêng.

## IIRC · Ferguson và cộng sự, EMNLP 2020

IIRC có 13.441 câu hỏi và 5.698 đoạn mở đầu. Người viết câu hỏi nhìn thấy đoạn mở đầu và tiêu đề của các trang được liên kết, còn người trả lời có thể mở nội dung trang. Với câu có đáp án, người gán nhãn ghi các đoạn trích tối thiểu cần thiết. Câu thiếu thông tin được ghi nhãn không có đáp án trong các nguồn của tác vụ. Chia dev/test dùng ba người và giữ câu có ít nhất hai người đồng ý về đáp án. (§§2.2–2.3, Table 2)

Trên test, mô hình đạt answer F1 31,1. Khi cấp liên kết chuẩn, F1 đạt 32,5. Khi cấp cả liên kết và ngữ cảnh chuẩn, F1 đạt 70,3. Người chấm đạt 88,4 trên một tập con 200 câu test, nên đối chiếu với người cần ghi khác biệt mẫu số. So sánh trong cùng pipeline cho thấy chọn đúng đoạn sau khi theo liên kết là một điểm nghẽn đáng kể. (§4.3, Table 3)

Table 6 còn ghi F1 58,1 khi chỉ nhìn câu hỏi trong tác vụ nhận diện câu không có đáp án trên dev. Đây là dấu hiệu có thể đoán một phần nhãn qua cách đặt câu. Nếu xây bộ đánh giá bảo tàng, đối chứng chỉ nhìn câu hỏi có thể giúp phát hiện dấu hiệu tương tự. IIRC dò nguồn trong phạm vi các trang liên kết, nên cần ghi rõ phạm vi khi so với hệ tra cứu toàn kho.

[PDF EMNLP](https://aclanthology.org/2020.emnlp-main.86.pdf). SHA-256 c4a45b1c3d267328373b8d67847c429f5241824e9e24298c46d9b3fbe7592800. Tra theo tiêu đề và ID ACL/arXiv trong snapshot 101 chưa thấy bản trùng.

## HotpotQA · Yang và cộng sự, EMNLP 2018 · P088

Bộ câu hỏi Wikipedia gắn nhãn câu hỗ trợ cho suy luận nhiều bước. Trong thiết lập distractor, hệ thống nhận hai đoạn chuẩn và tám đoạn gây nhiễu. Trong full wiki, hệ thống tự tìm nguồn trong Wikipedia. Bài báo cáo riêng điểm đáp án và điểm câu hỗ trợ, cùng Joint EM và Joint F1. Joint EM yêu cầu cả đáp án lẫn tập câu hỗ trợ đều khớp. (§§3.3, 5.2, Tables 1 và 4)

Baseline test đạt Answer F1 58,99 và Joint F1 41,37 trong distractor. Ở full wiki, hai số tương ứng là 34,40 và 17,85. Hai thiết lập dùng tập test riêng. Vì vậy số chênh lệch cho thấy mức khó của hai bài kiểm tra, và chưa cô lập tác động của truy xuất cho cùng câu. Nhãn câu hỗ trợ theo đáp án chuẩn là tiền lệ quan trọng. Đánh giá nguồn hỗ trợ từng ý phát sinh trong câu trả lời tự do cần một phép kiểm khác.

[PDF EMNLP](https://aclanthology.org/D18-1259.pdf). SHA-256 4ac04d526dfdf4a2549e4a7fcebe0c55a8ff0071b61ea53615e49c3a778f907c.

## MuseumQA · P090 · Chờ toàn văn

Xác nhận hồ sơ ACM 221–226 và DOI 10.1145/3639479.3639525. Ngày hội nghị trong hồ sơ là 2023 và ngày xuất bản trực tuyến Crossref ghi 28/02/2024. URL PDF ACM trả HTTP 403 trong lần kiểm này. OpenAlex trỏ về cùng URL và chưa cho thấy bản toàn văn trong kho lưu trữ. Đã tìm theo tiêu đề, DOI và tác giả. Trạng thái yêu cầu thêm toàn văn qua các đường hợp lệ trước khi quyết định Week 6. Chưa dùng số lượng câu hỏi hoặc cấu trúc nhãn từ mô tả thứ cấp làm bằng chứng.

[Nguồn ACM theo DOI](https://doi.org/10.1145/3639479.3639525) · [Hồ sơ OpenAlex](https://api.openalex.org/works/https://doi.org/10.1145/3639479.3639525)

## Đối chiếu cho review

IIRC và HotpotQA đã có nhãn bằng chứng chi tiết hơn cấp tài liệu. Hai bài cung cấp tiền lệ cho việc tách đáp án, chọn bằng chứng và kiểm phần đọc hiểu khi đã có cung cấp nguồn chuẩn. Với QA bảo tàng, phép đối chiếu cần thêm nhãn phần được hỏi, ý mô hình thực sự nêu, và nguồn hỗ trợ từng ý, đồng thời kiểm các bộ cùng miền khi có toàn văn và dữ liệu. Chuỗi đối chiếu hiện có 26 bài đã đọc có trọng điểm. MuseumQA vẫn chờ toàn văn và nằm ngoài con số này. Quyết định nhận và kiểm chéo Week 6 còn mở.
