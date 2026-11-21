# Phạm vi Paper 1 và kế hoạch hoàn tất Week 6

Ngày 21/11/2026. Phạm vi và tiêu chí dưới đây là đề xuất cần xác nhận trước khi khóa protocol. Hồ sơ hiện có 101 ứng viên từ giai đoạn thăm dò, 59 bài đã có ghi chú đọc toàn văn, gồm 41 bài trong danh mục và 18 bài bổ sung. Kết quả tìm kiếm chính thức, số bài nhận cuối và số kiểm chéo độc lập còn chờ xác nhận. [Ghi chú đợt 21](https://github.com/museum-platform-lab/museum-research/blob/research/literature-discovery-2026-11-16/literature/review-batches/2026-11-20-day5-round21/reading-notes.md) · [Ghi chú đợt 22](https://github.com/museum-platform-lab/museum-research/blob/research/literature-discovery-2026-11-16/literature/review-batches/2026-11-20-day5-round22/reading-notes.md)

## Phạm vi đề xuất

Tập trung Paper 1 vào hỏi đáp tiếng Việt dựa trên hồ sơ hiện vật và văn bản thuyết minh có thể truy về nguồn gốc. Phần tổng quan đối chiếu các bộ câu hỏi và hệ thống QA bảo tàng có đánh giá, cùng các phương pháp có liên hệ trực tiếp với việc kiểm đủ bằng chứng, dẫn nguồn và quyết định cách trả lời. Ghi vai trò mỗi bài theo nhiệm vụ và dữ liệu của bài. Bài đa phương thức có thể cung cấp đối chiếu cùng miền. GraphRAG và câu hỏi Paper 2 giữ ở hồ sơ đối chiếu hoặc hướng tương lai.

**Câu hỏi dẫn đường cho tổng quan.** Các bộ đánh giá hiện có kiểm thế nào việc tìm đúng đoạn, việc trích dẫn hỗ trợ từng dữ kiện và việc trả lời khi hồ sơ thiếu hoặc mâu thuẫn? Phép đánh giá nào có thể áp dụng cho hồ sơ bảo tàng tiếng Việt?

| Yếu tố | Phạm vi đề xuất |
| --- | --- |
| P · Đối tượng | Câu hỏi về hiện vật dựa trên hồ sơ gốc tiếng Việt và đoạn nguồn có mã. Đánh dấu câu có đủ nguồn, thiếu một phần, thiếu toàn bộ hoặc nguồn bất đồng. |
| I · Can thiệp | Bước kiểm độ đủ của bằng chứng trước quyết định trả lời. Ghi yêu cầu và kiểu phản hồi chuẩn cho từng tình huống trong pilot. |
| C · Đối chứng | RAG cơ sở cùng tập câu hỏi, kho hồ sơ, đoạn truy xuất, mô hình sinh và ngân sách ngữ cảnh. Đối chiếu thêm SACR nếu có thể mô tả và tái lập đúng cấu hình chuẩn. |
| O · Kết quả | Ứng viên chỉ số chính là tỷ lệ dữ kiện trả lời thiếu hỗ trợ từ đoạn được dẫn. Báo riêng tỷ lệ trả lời, từ chối nhầm khi bằng chứng đủ và cách phản hồi với nguồn bất đồng. Chốt đơn vị chấm và mẫu số trước pilot. |

P/I/C/O này để đối chiếu tài liệu và chuẩn bị kiểm tra khả thi. Nếu kết quả rà nguồn cho thấy can thiệp, thước đo hoặc dữ liệu rất gần một bài đã có, ghi bằng chứng trùng và sửa câu hỏi nghiên cứu sau khi trao đổi. ViCH-QA/SACR, MuseRAG++, EPRAG và Sufficiency-Gated RAG là nhóm cần đối chiếu trực tiếp. [ViCH-QA/SACR](https://ctujs.ctu.edu.vn/index.php/ctujs/article/view/3152) · [MuseRAG++](https://doi.org/10.1038/s41598-026-55700-9) · [EPRAG](https://doi.org/10.1016/j.knosys.2026.116929) · [Sufficiency-Gated RAG](https://doi.org/10.32604/cmc.2026.088937)

## Tiêu chí nhận và loại dự kiến

Các mã kế thừa từ protocol v0.1. Áp dụng cùng tiêu chí cho bản ghi tìm mới và ứng viên được dẫn lại từ bài khác.

| Mã | Quy tắc và chứng cứ cần ghi |
| --- | --- |
| IC-P, IC-I | Nhận bài có đánh giá QA bảo tàng hoặc di sản, hoặc bài QA dùng nguồn tài liệu và đánh giá trực tiếp ít nhất một yếu tố gồm độ đủ, độ hỗ trợ, trích dẫn, mâu thuẫn hoặc từ chối khi thiếu nguồn. Ghi stream cùng miền hoặc đối chiếu phương pháp. |
| IC-L, IC-T, IC-Y | Bài tiếng Anh, có bản tạp chí hoặc hội nghị xác minh được. Đề xuất khoảng năm từ 2016 đến ngày dừng chính thức, chờ xác nhận ngày. Bài tiền ấn phẩm gần đề tài giữ để kiểm khoảng trống và tìm bản xuất bản. |
| IC-E | Có kết quả thực nghiệm hoặc đánh giá benchmark định lượng trong bảng hoặc hình, với vị trí, thiết lập và mẫu số kiểm được. Ghi thiếu comparator hoặc code vào bảng, nếu có. |
| EC-O, EC-N | Loại khỏi tập thực nghiệm chính nếu tác vụ ngoài phạm vi hoặc thiếu đánh giá thực nghiệm. Ví dụ gồm nhận dạng ảnh đơn thuần, trải nghiệm khách tham quan thiếu phép đánh giá QA, khảo sát tổng quan thuần mô tả. Giữ tài liệu nền trong thư mục tham khảo khi phù hợp. |
| EC-D, EC-S | Ánh xạ các bản trùng hoặc các phiên bản về cùng mã nghiên cứu trước khi đếm. Ghi lý do khi chọn bản đầy đủ. Theo tiêu chí học phần, kiểm riêng bài dưới bốn trang, abstract và poster. |
| EC-A | Chỉ quyết định sau khi đã thử các đường truy cập hợp pháp theo protocol và ghi kết quả. Khi đang chờ, dùng trạng thái chờ toàn văn và giữ DOI. |

P033 và P052 hiện chờ toàn văn. Tóm tắt và tài liệu tái lập của P052 thích hợp cho bảng đối chiếu phương pháp. Trước quyết định toàn văn, cần kiểm bản xuất bản hoặc bản tác giả hợp lệ qua thư viện, kho cơ quan hoặc tác giả. [P033](https://doi.org/10.1016/j.ipm.2025.104369) · [P052](https://doi.org/10.1016/j.knosys.2026.116929) · [Kho tái lập EPRAG](https://zenodo.org/records/21592366)

## Trình tự hoàn tất Week 6

1. **Khóa protocol sau xác nhận.** Chốt P/I/C/O của Paper 1, ngày bắt đầu và ngày dừng, tiêu chí nhận và loại, nguồn chính có thể tìm và xuất kết quả, người phụ trách tìm kiếm, lọc, kiểm chéo. Protocol v0.1 đề xuất IEEE Xplore, ACM DL và OpenAlex, với ACL Anthology làm nguồn bổ sung chuyên ngành. Kiểm khả năng truy vấn và xuất kết quả trước khi ghi bộ nguồn cuối. Ghi phiên bản và commit. Lưu truy vấn nguyên văn, trường tìm kiếm, bộ lọc, thời gian, số kết quả nguồn báo và số thực xuất cho từng nguồn.
2. **Tìm và lọc có nhật ký.** Chạy các truy vấn đã khóa trên các nguồn có thể kiểm tra, lưu tệp xuất gốc, nối bản ghi nguồn với DOI hoặc mã nghiên cứu, lọc tiêu đề/tóm tắt rồi đọc toàn văn. Tận dụng 59 ghi chú làm nguồn trích xuất dự thảo khi có đường truy xuất chính thức tương ứng. Ghi lý do loại, trạng thái chờ toàn văn và một lượt lần tham chiếu từ bài hạt giống theo protocol.
3. **Kiểm chéo và nộp các sản phẩm D1.** Người kiểm chéo độc lập gán nhãn trước khi xem nhãn cũ. Tách kiểm chéo quyết định lọc khỏi kiểm chéo các ô trích xuất. Tạo bảng bằng chứng gộp, bảng đếm PRISMA từ cùng CSV và bản đồ RQ–bằng chứng P/I/C/O. Theo hướng dẫn học phần, mục tiêu bảng gộp là ít nhất 12 bài đủ tiêu chí. Mỗi yếu tố P/I/C/O cần nguồn đối chiếu hoặc ghi rõ còn thiếu. Các số đếm thăm dò và số đếm chính thức có nhật ký riêng.
4. **Chuẩn bị bước Week 7.** Từ bảng bằng chứng, xác định công trình có thể đã giải quyết khoảng trống dự kiến, kiểm khả thi trên một ít hồ sơ tiếng Việt được phép dùng và chốt một câu hỏi chính, một đối chứng, một chỉ số. Dựa vào nguồn phù hợp hoặc mini-pilot 5–10 mục để chọn ngưỡng. Ghi cấu hình và giả thuyết vào proposal trước pilot chính.

### Quyết định cần xác nhận

- Phạm vi Paper 1 và vai trò bài nền ngoài bảo tàng. Chốt trước khi khóa truy vấn và tiêu chí.
- Các nguồn tìm kiếm, ngày dừng và người kiểm chéo độc lập. Xác nhận quyền và khả năng xuất kết quả theo từng nguồn.
- Danh mục hồ sơ bảo tàng tiếng Việt có quyền dùng, cách gán mã nguồn, tiêu chí xác minh dữ kiện, cách đánh dấu tình huống thiếu hoặc mâu thuẫn và mẫu số của chỉ số chính. Các quyết định này cần cho nghiên cứu thực nghiệm và đề xuất Week 7.
