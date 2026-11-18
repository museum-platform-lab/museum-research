# Day 4, đợt 3 · Bằng chứng ở cấp đoạn và câu hỏi cần ghép nguồn

Ngày 19/11/2026. Hai bài được đọc có trọng điểm từ bản PDF proceedings. Phần này nối kết quả về hỗ trợ từng ý của FActScore và ALCE với cách xây bộ câu hỏi có nhiều đoạn bằng chứng.

## MuSiQue · Trivedi và cộng sự, TACL 2022

**Dữ liệu và cách chấm.** MuSiQue-Ans có 24.814 câu cần 2–4 bước suy luận. Mỗi ngữ cảnh có 20 đoạn gồm các đoạn hỗ trợ của từng bước và các đoạn gây nhiễu. MuSiQue-Full ghép mỗi câu với một ngữ cảnh đối chứng vẫn dùng nguyên câu hỏi, nhưng được xây sao cho không tìm thấy đáp án của một bước cần thiết. Phép chấm theo cặp cho 0 điểm nếu mô hình nhận định sai mức đủ thông tin ở một trong hai ngữ cảnh. Nếu nhận định đúng cả cặp, điểm lấy từ kết quả đáp án hoặc đoạn hỗ trợ của bản đủ thông tin. (§5, bước S6–S8, Table 2 và §7.1)

**Kết quả.** Table 5 báo EX(SA) đạt Answer F1 49,0 và Support F1 80,6 trên MuSiQue-Ans. Trên MuSiQue-Full, điểm kết hợp với nhận định đủ thông tin lần lượt là 32,2 và 44,3. Cách chấm và đơn vị tính khác nhau giữa hai bộ, nên chênh lệch chưa cô lập ảnh hưởng của việc bỏ một bước. Mô hình chỉ nhìn câu hỏi đạt 4,6 Answer F1 ở Ans và 0,0 điểm đáp án kết hợp ở Full trong phép thử của tác giả.

**Liên hệ với bảo tàng.** Kiểu cặp giữ nguyên câu hỏi giúp kiểm mô hình có thay đổi hành vi khi dữ kiện cần thiết vắng mặt. Nhãn hỗ trợ của MuSiQue đặt ở cấp đoạn cho bước suy luận. Nếu đánh giá một đáp án dài có nhiều ý, vẫn cần kiểm ý nào được đoạn trích hỗ trợ. Đây là bộ đọc hiểu với ngữ cảnh cung cấp sẵn, nên điểm của bài chưa đo khả năng truy xuất nguồn trong cả kho bảo tàng.

[PDF TACL](https://aclanthology.org/2022.tacl-1.31.pdf). SHA-256 c0d8b89636bcbca4972b55ab68f014eb20f74c4b9a4fcf126ca68d7f2ec1e753. Tra theo tiêu đề, tác giả và mã ACL trong snapshot 101 chưa thấy bản trùng. Theo dõi như nguồn bổ sung để rà độ phù hợp với RQ khi chốt vòng toàn văn.

## Bộ Amarna · Sheng, Van Gool và Moens, LT4DH 2016 · P012

**Dữ liệu và nhãn.** Bài thu thập 805 câu hỏi ảnh–văn bản bằng tiếng Anh cho 16 hiện vật. Table 2 ghi 204 tài liệu, 101 tài liệu liên quan và 139 đoạn được liên kết. Ba người tham gia gắn nhãn đoạn, trong đó một người phân xử khi hai người còn lại bất đồng. Các đoạn liên quan được xác định theo URL tài liệu và vị trí từ trong HTML, với 0–6 đoạn liên kết mỗi câu. Tác giả báo 55% câu hỏi có thể trả lời chỉ bằng bộ tài liệu liên quan. (§3.2–3.3, Fig. 3 và Table 2)

**Giới hạn.** Những câu còn lại có thể cần xử lý hình ảnh, thiếu kiến thức lịch sử hoặc đặt câu hỏi khó xác định. Vì vậy 45% còn lại chưa thể dùng làm tập nhãn “phải từ chối”. Bài mô tả và phân tích bộ dữ liệu. Gắn nhãn đến cụm từ trong đoạn hoặc vùng ảnh được nêu như hướng mở rộng. Scope đã đọc chưa thấy thực nghiệm so sánh hệ QA hay thước đo hỗ trợ từng ý của đáp án sinh. (§§4–5)

**Ghi chú Week 6.** Giữ P012 làm tiền lệ dữ liệu cùng miền. Khi áp tiêu chí IC-E và EC-N, cần phân biệt số liệu mô tả corpus với kết quả thực nghiệm. Trạng thái đề xuất là đối chiếu nền, chờ quyết định chính thức.

[PDF proceedings](https://aclanthology.org/W16-4003.pdf). SHA-256 94afb4e16ccbd7b61abbebb5b547adc8f034fee58e876bc8efb43be377503f14.

## Đối chiếu với ViCH-QA

ViCH-QA đã có nhãn nguồn ở cấp tài liệu và câu hỏi đa nguồn. Amarna đã có gắn đoạn trong miền di sản. MuSiQue đã có cặp ngữ cảnh đủ và thiếu dữ kiện cho cùng câu hỏi. Các tiền lệ này thu hẹp tuyên bố tính mới. Phần đáng kiểm tiếp là liệu một bộ QA bảo tàng tiếng Việt có thể đánh giá đồng thời đoạn nguồn cho từng ý, ý đã trả lời hoặc còn thiếu, và mức đủ căn cứ khi phải ghép nhiều đoạn hay không. Khả năng đối chiếu nhãn với ViCH-QA vẫn phụ thuộc vào dữ liệu có thể truy cập.

Chuỗi đối chiếu hiện bao phủ 24 bài. Vòng quyết định nhận bài và kiểm chéo Week 6 còn mở.
