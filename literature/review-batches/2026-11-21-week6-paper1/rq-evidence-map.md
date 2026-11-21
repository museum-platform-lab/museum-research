# Week 6 · Bản đồ bằng chứng cho câu hỏi nghiên cứu Paper 1

Cập nhật 21/11/2026. Đây là bản dự thảo để xác nhận phạm vi, lập bảng quyết định và kiểm phản chứng ở Week 7. Căn cứ hiện có nằm trong [bảng bằng chứng gộp dự thảo](evidence-table-merged.md).

## Câu hỏi ứng viên

Trên bộ câu hỏi tiếng Việt về hiện vật và hồ sơ bảo tàng, khi dùng cùng mô hình sinh và cùng các đoạn truy xuất, việc kiểm tra ngữ cảnh đã đủ căn cứ trước khi trả lời có giảm tỷ lệ dữ kiện thiếu hỗ trợ từ đoạn được trích, đồng thời giữ được tỷ lệ câu hỏi nhận câu trả lời hữu ích, so với RAG cơ sở có yêu cầu dẫn nguồn hay không?

| Thành phần | Phạm vi ứng viên | Bài làm nền | Cần kiểm để chốt |
|---|---|---|---|
| **P · Dữ liệu** | Câu hỏi tiếng Việt về hồ sơ bảo tàng. Đơn vị thử là câu hỏi và tập đoạn cấp cho mô hình, có mã hồ sơ và vị trí đoạn gốc. Gồm ca đủ, thiếu một phần, không đủ, và bất đồng khi có hồ sơ xác minh. | P008 đã có QA di sản tiếng Việt, thẩm định chuyên gia và câu nhiều tài liệu. P001, P004 có QA bảo tàng hoặc tác phẩm. P017, N004 có thiết kế nhóm bằng chứng. | Chọn corpus đọc được và quyền sử dụng. Kiểm phiên bản, trường và nhãn thực tế của ViCH-QA trước khi phát biểu về phần còn thiếu. Phân biệt kho hồ sơ thiếu dữ kiện với bộ truy xuất bỏ sót đoạn. |
| **I · Can thiệp** | Bước kiểm đủ bằng chứng ở cấp câu hỏi và tập đoạn trước khi sinh. Nhãn trạng thái và quyết định trả lời ghi riêng. Với ca mơ hồ hoặc bất đồng, trước mắt dùng để phân tích lỗi và kiểm định tính khả thi của nhãn. | P055 so bộ kiểm trước khi sinh. P050 dùng tín hiệu đủ cùng độ tự tin. N006 thêm ngưỡng từ chối. P052 tách trạng thái–hành động. | Chọn một can thiệp chính và ghi rõ input, output, ngưỡng và quy tắc cho ca đủ một phần. Đọc toàn văn P052 và P033. Chỉ đưa thêm hành động hỏi lại nếu corpus và đánh giá hai lượt đủ khả thi. |
| **C · Đối chứng** | RAG cơ sở có yêu cầu trích nguồn, giữ nguyên tập đoạn, thứ tự, mô hình và ngân sách sinh giữa hai cấu hình. Đối chứng từ chối ngẫu nhiên ở cùng tỷ lệ trả lời để kiểm bước chọn ca. | P055 có RAG luôn trả lời và đối chứng ngẫu nhiên khớp tỷ lệ trả lời. N006 giữ đoạn và bộ trích cụm từ trong so sánh. P084 cung cấp cấu hình sinh có nguồn. P008 cung cấp đối chiếu truy xuất cùng miền. | Chốt bộ truy xuất riêng trước so can thiệp. Chạy đối chứng cùng dữ liệu và cùng điều kiện. Nếu thử SACR, log thay đổi ở lớp truy xuất và kiểm link về hồ sơ gốc. |
| **O · Kết quả** | Chỉ số chính ứng viên là tỷ lệ dữ kiện thực tế đã nêu thiếu hỗ trợ trong đoạn được dẫn. Báo song song tỷ lệ có phản hồi hữu ích, tỷ lệ từ chối nhầm ở ca đủ và tỷ lệ trả lời thiếu căn cứ trong ca không đủ. | P084/P046 đo trích dẫn, P018/P079 đo hỗ trợ trên toàn ngữ cảnh, P055/P050 đo chất lượng theo tỷ lệ trả lời, P017/N004 đo hành vi ở ca thiếu nguồn. | Gán nhãn tiếng Việt bằng người chấm độc lập trên mẫu. Chọn ngưỡng cải thiện và giới hạn mất tỷ lệ hữu ích ở Week 7 khi có nguồn số liệu phù hợp hoặc mini-pilot. Chốt trước khi chạy tập chính thức. |

### Quy tắc đối chiếu mức gần

Chữ hoa là khớp trực tiếp theo định nghĩa trong bản này. Chữ thường ghi tiền lệ gần nhưng thiếu một thành phần cốt lõi. P cần cùng dạng dữ liệu và tác vụ QA hồ sơ bảo tàng tiếng Việt. I cần bước kiểm đủ căn cứ tác động đến việc trả lời trước khi sinh. C cần so bước kiểm với RAG cơ sở trong thiết lập giữ mô hình sinh và đoạn đầu vào. O cần đo mức hỗ trợ của đoạn thực sự được dẫn cùng độ hữu ích hoặc độ bao phủ. Không cộng chữ thường vào số trùng trực tiếp. Khi RQ hoặc nhãn được xác nhận, cần cập nhật các dòng tương ứng trong CSV.

| Bài | Khớp trực tiếp | Gần một phần | Khác biệt cần xác minh |
|---|---|---|---|
| P008 · ViCH-QA/SACR | 0/4 | p | QA di sản tiếng Việt rất gần miền. Bài đánh giá truy xuất ở đơn vị tài liệu và hiệu quả theo đáp án tham chiếu. Cần kiểm đúng bản và schema. |
| P001 · MuseRAG++ | 0/4 | p c o | Có QA bảo tàng và chấm tới dữ kiện. Nhiều thành phần đổi đồng thời, thiếu xác minh phép chấm khi cả kho không đủ. |
| P004 · Context or Retrieval? | 0/4 | p c | Có dữ liệu tác phẩm và nhóm đối chứng truy xuất. So sánh khác đầu vào và quy trình sinh. |
| P055 · Sufficiency-Gated RAG | I C (2/4) | o | Gần nhất ở can thiệp và phép thử có đối chứng. Tác vụ đa bước tiếng Anh và đơn vị thiếu hỗ trợ cấp đáp án, theo ngữ cảnh. |
| P050 · Sufficient Context | I (1/4) | c o | Chấm độ đủ và đánh giá theo tỷ lệ trả lời. Chính sách kết hợp độ tự tin và không có phép chấm đoạn trích cụ thể trong kết quả đối chiếu. |
| N006 · Evidence-Calibrated RAG | I (1/4) | c o | Giữ cùng đầu vào nhưng dùng bộ trích cụm từ. Kết quả answerability và từ chối chưa có chấm mệnh đề trích dẫn. |
| P017 · ESB | 0/4 | i o | Điều kiện bằng chứng và hành động có nhãn trước. Đánh giá theo lựa chọn nhị phân và chuỗi đáp án chuẩn. |
| P034 · Self-RAG | 0/4 | i c o | Mô hình học tự kiểm trong lúc sinh. Trích dẫn được đo riêng trong ASQA. Cần phân biệt đối chứng prompt với mô hình huấn luyện gốc. |
| P018 · RAGChecker | 0/4 | o | Tách mệnh đề và chấm hỗ trợ trong toàn ngữ cảnh. |
| P046 · ReClaim | 0/4 | i o | Đặt bằng chứng trước mệnh đề khi sinh. Không đồng nhất với can thiệp chọn trả lời dựa vào độ đủ. |
| P084 · ALCE | 0/4 | c o | Có tiền lệ yêu cầu dẫn nguồn và đo hỗ trợ theo trích dẫn. Cần kết hợp với phép đo trả lời hữu ích khi có quyền từ chối. |
| P079 · RAGAS | 0/4 | o | Chấm hỗ trợ trong ngữ cảnh. Chưa xác nhận độ đúng khi chấm tiếng Việt. |
| N004 · RGB | 0/4 | o | Có kịch bản thiếu nguồn và phép chấm từ chối. Tiếng Anh/Trung và không chấm từng đoạn trích cho mệnh đề. |
| P078 · RARR | 0/4 | i o | Sửa nháp hậu kỳ theo nguồn; chấm giữ nội dung gốc. |
| P052 · EPRAG | Chờ toàn văn | i o | Đã có hành động hỏi lại hoặc từ chối dựa trên trạng thái. Gói tái lập đủ để đối chiếu lựa chọn hành động, còn phạm vi đánh giá trích dẫn và đối chứng cần rà toàn văn. |
| P033 · SC-RAG | Chờ toàn văn | i | Mô tả công khai có truy xuất và tự sửa theo nguồn. Chờ kiểm cách chấm và thiết lập đối chứng. |

## Cách đọc các điểm số

- **Thiếu hỗ trợ ở cấp dữ kiện.** Mẫu số là số dữ kiện kiểm chứng được mà hệ thống đã nêu. Nhãn ghi đủ hỗ trợ, thiếu hỗ trợ, bị nguồn phản bác, hoặc chưa xác định. Nếu hệ thống nêu dữ kiện mà thiếu đoạn dẫn, ghi nguyên nhân riêng. Với dữ kiện cần ghép, lưu tập đoạn tối thiểu giúp kiểm.
- **Tỷ lệ trả lời hữu ích.** Mẫu số là toàn bộ câu theo nhóm. Chốt rubric cho câu trả lời đầy đủ hoặc một phần, phần chưa xác nhận, và câu hỏi làm rõ thực sự cần thiết. Ghi riêng độ bao phủ theo ca đủ và ca thiếu. Đừng tính phản hồi rỗng là từ chối đúng.
- **Từ chối nhầm.** Mẫu số là ca có đủ bằng chứng trong tập đoạn được cấp. Báo riêng với thất bại tìm nguồn trong kho. Hai cấu hình có thể có tỷ lệ trả lời khác nhau, vì vậy đối chiếu thêm ở cùng mức bao phủ.
- **Bất đồng nguồn.** Ghi cùng hiện vật, thuộc tính, mốc và thẩm quyền nguồn. Giữ nhãn đối với khác mốc hiệu lực, bổ sung cho nhau và mâu thuẫn chưa phân xử. Chấm phản hồi khi đảo thứ tự cùng hai đoạn nếu có đủ ca kiểm.

## Ưu tiên phản chứng và kiểm khả thi ở Week 7

Trong bảng dự thảo, P055 có I và C khớp trực tiếp, với O gần; P001 có P, C và O gần; P034 có I, C và O gần. Đây là các bài cần kiểm trước vì nhiều thành phần trùng về mục đích và thiết kế. Chưa có kết luận 3/4 hay 4/4 đã được kiểm chéo. Bổ sung P008 và P052 dù mức khớp còn bất định vì lần lượt là đối chiếu sát miền và sát quyết định hành động.

| Nhóm rà | Mã và đường truy vết | Cần quyết định từ toàn văn/dữ liệu | Người thực hiện |
|---|---|---|---|
| Dữ liệu cùng hoặc gần miền | P008, P001, P004, N003 qua danh mục dự án, DOI và ghi chú đọc | Nhãn cấp đoạn và cấp dữ kiện, ca thiếu nguồn, vai trò của thẩm định chuyên gia. | Người tiến hành review và người kiểm chéo độc lập, chờ phân công. |
| Can thiệp và đối chứng | P055, P050, N006, P017, P034; P052 từ DOI và gói tái lập, P033 từ DOI | Điều kiện cố định đầu vào, sự khác nhau giữa phát hiện thiếu nguồn và sửa câu, mẫu số theo mức bao phủ. | Người tiến hành review và người kiểm chéo độc lập, chờ phân công. |
| Phép đo và điều kiện thử | P018, P084, P046, P079, N004; P049 và P027 trong danh sách theo dõi | Đo toàn ngữ cảnh hay đoạn được dẫn, cách chấm ca ghép nguồn, mức chuyển giao sang tiếng Việt. | Người tiến hành review và người kiểm chéo độc lập, chờ phân công. |

Ưu tiên gom các bằng chứng sát RQ trước, kiểm lại toàn văn và truy theo trích dẫn khi đã ghi nguồn và quy trình. Sang Week 7, kiểm corpus và các trường nhãn có dùng được, sau đó chọn chỉ số chính, mức cải thiện đáng quan tâm và giới hạn từ chối nhầm. Khi chưa có số tương đương để đặt ngưỡng, mini-pilot 5–10 ca có thể giúp kiểm rubric và độ khả thi. Kết quả pilot cần tách khỏi tập đánh giá cuối. Hướng Paper 2 phụ thuộc lỗi thực nghiệm và đóng góp phương pháp có thể kiểm độc lập.
