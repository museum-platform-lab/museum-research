# Review protocol v0.1

## 1. Mục đích, câu hỏi và đơn vị

Hai hướng dùng chung thư viện nhưng có câu hỏi và tập bằng chứng được gắn nhãn riêng. Một paper có thể phục vụ cả hai, chỉ tính một work trong tổng hợp hợp nhất; bảng từng hướng phải công bố overlap.

**RQ-L1 (benchmark, tạm thời):** Các benchmark và hệ thống QA di sản/bảo tàng hiện đánh giá truy hồi, mức hỗ trợ của nguồn, trích dẫn và khả năng từ chối ra sao; còn thiếu phép đánh giá nào cho QA văn bản tiếng Việt dựa trên hồ sơ hiện vật?

**RQ-L2 (phương pháp, tạm thời):** Trên QA có nguồn bằng chứng, kiểm tra đủ bằng chứng/claim support và selective answering cải thiện lỗi trả lời không được hỗ trợ và đánh đổi accuracy–coverage như thế nào so với RAG cơ sở?

| Hướng | P | I | C cần trích xuất | O cần trích xuất |
| --- | --- | --- | --- | --- |
| Paper 1 | QA trên catalog/curatorial text và tài liệu di sản; benchmark đa phương thức dùng để đối chiếu phạm vi | Benchmark, truy hồi lexical/dense/hybrid, answer generation có nguồn | Baseline QA/RAG và biến thể truy hồi | Retrieval, answer correctness, claim support, citation correctness, answerability, subgroup coverage |
| Paper 2 | QA/RAG trên tài liệu có thể truy vết; giữ nghiên cứu ngoài bảo tàng nếu cùng bài toán bằng chứng | Sufficiency/contradiction checking, verification, attribution, abstention/calibration | RAG cơ sở, verifier/selective answering gần nhất, ablation | Unsupported-claim rate, support/attribution, accuracy–coverage, refusal errors, cost/latency |

Không coi bảng này là thiết kế thực nghiệm đã khóa. Paper 2 chưa chọn kiến trúc hoặc tuyên bố novelty; GraphRAG không mặc nhiên là đóng góp. Cần đối chiếu full-text các công trình gần như Sufficient Context, ALCE, RAGChecker, ReClaim và nghiên cứu xung đột nguồn, sau khi xác minh danh tính/phiên bản.

## 2. Phạm vi và các quyết định dự thảo

Đề xuất IC-Y từ 2016 đến ngày dừng thực tế: giữ thế hệ QA di sản trước RAG hiện đại (lead Amarna 2016 trong scoping là lý do khởi đầu, cần xác minh), đồng thời phủ giai đoạn RAG/LLM. Tác phẩm nền trước 2016 giữ BACKGROUND và snowball lead; muốn tính formal phải sửa protocol có lý do trước truy vấn liên quan. IC-L là ngôn ngữ bài báo tiếng Anh, không hạn chế ngôn ngữ corpus; tiếng Việt là bối cảnh triển khai, không phải bộ lọc bắt buộc truy vấn.

Mốc scoping hiện tại 16/11/2026, không dùng như ngày dừng formal đã hoàn thành. Ngày bắt đầu/dừng formal: PENDING; điền ngày lịch cụ thể trước khi bắt đầu, cùng khoảng cập nhật trước nộp bài. Không dùng ngày indexed/deposited thay ngày xuất bản. Nếu cover date sau cutoff nhưng online trước đó, ghi cả hai và kiểm bản thực tế theo IC-T; preprint trước cutoff không chứng minh bản journal đã đăng trước cutoff.

IC/EC chi tiết nằm ở ie_criteria.md. Không bắt buộc paper phải đo đủ mọi O, có comparator, có code hoặc đúng tiếng Việt mới được nhận; trích xuất N/A và thiếu hụt để tổng hợp. Không loại chỉ vì thiếu abstract hoặc DOI.

## 3. Nguồn, truy vấn và thời điểm khóa

Mục tiêu tối thiểu 3 CSDL chính phù hợp: IEEE Xplore, ACM DL, OpenAlex; nếu OpenAlex chưa truy cập được thì xét Scopus khi trường cấp quyền hoặc Semantic Scholar sau kiểm tra khả năng tìm/xuất. Nguồn thay thế chỉ được tính sau khi đã chạy được và log đúng truy vấn/phạm vi. Chưa có 3 nguồn hoàn tất. Scholar bổ sung; Crossref chủ yếu đối chiếu metadata; arXiv là watchlist phiên bản/novelty. Đối với NLP, ACL Anthology là nguồn chuyên ngành bổ sung đáng kiểm tra.

search-strings.md giữ các khối khái niệm và thiết kế 6 truy vấn. Chuyển cú pháp theo từng giao diện thực tế, ghi nguyên văn chuỗi đã chạy, trường tìm, filter và mọi giới hạn. Không giả định API/giao diện nào hỗ trợ đầy đủ Boolean, không gọi web search có site: là native database search. Trường đích Title/Abstract/Keywords nếu nguồn hỗ trợ; mọi lệch trường ghi rõ.

Trình tự: pilot truy vấn/tiêu chí → ghi sửa đổi → khóa bản có ngày, người chịu trách nhiệm và Git commit → formal search → screening. Snapshot discovery đã có là scoping trước protocol; không viết lại lịch sử thành tìm kiếm đã đăng ký trước. Nếu dùng một paper discovery trong formal set, cần đường truy xuất từ formal query hoặc snowball hợp lệ. Lead chưa truy xuất được ở lại watchlist.

Mỗi formal query lưu raw export bất biến, checksum local, query ID, thời gian/timezone, URL, tổng hit nguồn báo, số xuất, giới hạn trang/xếp hạng, raw filename và map source ID→record ID→work ID. Nếu chỉ xuất một phần phải báo coverage partial; không lấy số hit nguồn báo làm số record đã thu. Không cắt top-k tùy tiện rồi gọi đầy đủ.

## 4. Phân công và vai trò AI

Người dùng: chủ nhiệm dự thảo, xác nhận RQ và quyết định học thuật. Người kiểm chéo độc lập: CHƯA PHÂN CÔNG. Giảng viên: xác nhận yêu cầu học phần/phạm vi khi cần; chưa ghi là đã duyệt. Agent: chuẩn bị truy vấn, normalize, đề xuất nhãn có dẫn chứng, quản lý log; không đại diện cho người thứ hai. Người phụ trách từng CSDL: CHƯA PHÂN CÔNG, ghi tên và quyền truy cập trước formal search.

Không gửi tin/email hoặc cấp quyền chia sẻ mới. Không đưa token, PDF có hạn chế phân phối hoặc dữ liệu cá nhân vào repo public. Lưu PDF hợp pháp trong thư viện/Drive theo quyền; repo lưu metadata, quyết định và đoạn trích ngắn cần thiết.

## 5. Dedup, lọc và full-text

Giữ source occurrences trước dedup. DOI chuẩn hóa là khóa đầu; thiếu DOI dùng title chuẩn hóa+year, kiểm thêm authors. Mỗi work có ID bền vững và mọi alias discovery; không đánh lại ID qua vòng lọc. Một preprint và bản published cùng nghiên cứu thuộc version family; bản journal mở rộng có kết quả mới được liên kết và đánh giá đóng góp riêng, không gộp mù hoặc đếm là bằng chứng độc lập.

Vòng 1: title/abstract INCLUDE, EXCLUDE, UNSURE theo từng hướng/stream. Thiếu thông tin dùng UNSURE và nêu thiếu gì. INCLUDE vòng 1 chỉ có nghĩa chuyển full-text. Vòng 2 kiểm bài gốc, IC-T, số trang, kết quả, liên quan; final INCLUDE mới vào evidence table. Giữ tất cả quyết định trước/sau adjudication, lý do có mã và locator. EC-A chỉ sau các đường hợp pháp đã thử và log; lỗi truy cập một lần chưa đủ.

## 6. Kiểm chéo và chất lượng

Pilot trích xuất 2–3 bài do hai người đọc độc lập trước trích xuất hàng loạt. Kiểm chéo vòng 1 khoảng 20% record, chọn ngẫu nhiên có seed 20261116, gồm cả nhận và loại; nếu cần stratify để cả hai có mặt, ghi thiết kế và tỷ lệ từng tầng, không gọi là simple random. Người thứ hai chưa xem nhãn ban đầu. Ghi n kiểm, n bất đồng, agreement=n đồng thuận/n kiểm và cách xử lý. Không có người thứ hai thì ghi NOT_MET, không coi AI rerun là kiểm chéo.

Kiểm chéo trích xuất ceil(20% số paper), tối thiểu 3, ưu tiên near_rq≥3 yếu tố. Nếu tổng dưới 3 kiểm tất cả và ghi chưa đáp ứng mức tối thiểu. Đếm số ô thực sự đối chiếu; >10% ô bất đồng thì rà lại toàn bộ bảng của người trích xuất. Giữ giá trị hai người và kết quả thống nhất; không thống nhất được chuyển người phụ trách/giảng viên. Kiểm chéo vòng 1 không thay kiểm chéo trích xuất.

Rubric chất lượng 4 câu yes/no: thiết kế rõ? có dataset và N? có baseline? định nghĩa metric? High=3–4, medium=2, low=0–1. Ghi locator từng câu; chưa đủ thông tin dùng UNKNOWN, chưa chấm tổng cuối. Chất lượng dùng diễn giải độ tin cậy, không thêm tiêu chí loại hậu nghiệm.

## 7. Trích xuất và tổng hợp

Giữ 10 nhóm Evidence Table của giảng viên: Paper, Tool/LLM, Dataset, Metric, Comparator, Results, Code, Limitations, Near-RQ(P/I/C/O), Reliability; schema CSV tách các ô để có thể kiểm tra. Mọi kết quả có page/section/table/figure, excerpt ngắn, đơn vị, split, setting, N và tác giả đánh giá. Không suy diễn citation correctness thành causal faithfulness; benchmark có relevant paragraph chưa tự có claim-level labels. Không gộp support, citation precision/recall, correctness và abstention thành một metric.

Tổng hợp narrative theo task/data/evidence unit, retrieval, metric, answerability/conflict và ngôn ngữ. So sánh số chỉ khi cùng dataset/split/metric/setting; tránh pooling khác thang đo hoặc lấy nhiều version của một study làm nhiều bằng chứng. Báo missingness và chất lượng. Ít nhất 12 included là mốc học phần của bảng gộp, không chứng minh đủ literature hoặc đủ novelty cho hai paper.

Lập nearest-work matrix riêng cho mỗi hướng: claim đóng góp dự kiến, 2–3 đối thủ gần nhất đã đọc, P/I/C/O overlap, dataset/metric, phần đã giải quyết và phần còn thiếu. ≥3 paper gợi ý khoảng trống hoặc near_rq≥3 chỉ là ưu tiên kiểm tra phản chứng, không phải bằng chứng novelty. Ghi cả kết quả phủ định gap.

## 8. Snowball, dừng và đếm

Sau full-text chọn seed từ formal INCLUDE gần RQ: trước mắt 1 seed/hướng, nếu trùng thì giữ 1 và chọn seed bổ sung theo near_rq cao, phá hòa citation vừa phải rồi năm gần hơn; log citation count tại ngày chọn. Mỗi seed 1 lượt backward và forward, không đệ quy seed mới. Với >200 citations, lọc tiêu đề theo từ P hoặc I và công bố số đã lướt/giới hạn theo hướng dẫn tuần 7. Nếu dịch vụ không cho xem hết phải báo thiếu. Forward chú ý 12 tháng gần nhất, không có thì ghi rõ.

Snowball qua cùng 2 vòng/IC-EC; source/seed bắt buộc, dedup với main set. Phễu chính chốt riêng trước snowball; final union khử trùng main+snowball, báo overlap. Đếm từ CSV cùng snapshot, không dùng 386 web hits/90 hoặc101 discovery làm PRISMA formal. Mọi record query chính thức phải được lọc; không có quy tắc dừng sớm theo xếp hạng AI. Chỉ dừng khi đã xử lý hết export trong phạm vi công bố và một vòng snowball định trước, đến ngày dừng đã khóa; đây không phải chứng minh hoàn toàn đầy đủ.

## 9. Giới hạn và sửa đổi

Giới hạn: chỉ tiếng Anh; IC-T bỏ preprint/thesis dù watchlist vẫn cần; nguồn/quyền truy cập có thể thiếu; EC-A và thiếu abstract ảnh hưởng coverage; reviewer chưa sẵn sàng; phạm vi tiếng Việt có thể thiếu chuẩn gold; tiêu chí cần khớp RQ được đăng ký. Báo số EC-A và agreement thực tế khi có, không điền số 0 thay chưa làm.

Mọi đổi RQ, năm, khối từ, nguồn, trường tìm hoặc cách lọc sau khóa phải có ngày, trước/sau, lý do, ảnh hưởng record và có cần rerun. Không sửa protocol để hợp với kết quả đã thấy mà thiếu log. Không có tìm kiếm formal trong đợt 2.
