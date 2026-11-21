# Day3, đợt2 — Citation correctness, causal faithfulness và attribution bias

Ngày18/11/2026. Tiếp tục đọc có mục tiêu3 bài P044, P032, P026; giữ literature là công việc chính. Bảng đối chiếu nối11 paper IDs của các lượt extraction chuẩn hóa, không có nghĩa11 bài mới được tìm thấy hoặc nhận chính thức.

## Mắt xích mới sau đợt trước

Đợt trước tách answer correctness, context support vàcitation support. Đợt này thêm câu hỏi: **citation được nguồn hỗ trợ có thực sự phản ánh nguồn mô hình đã dùng để sinh claim không?** Cần phân biệt điều quan sát được với cách diễn giải cơ chế của mô hình.

| Khái niệm | Bằng chứng cần có | Chưa thể suy ra chỉ từ metric này |
|---|---|---|
| Tài liệu liên quan đến câu hỏi | IR relevance labels | Tài liệu chứng minh từng claim được gắn citation |
| Citation correctness | Nguồn trích hỗ trợ statement/claim | Model thực sự dùng nguồn đó khi generation |
| Citation faithfulness theo P044 | Có support và có causal influence | Một phép perturbation đơn lẻ đủ chứng nhận mọi trường hợp |
| Attribution sensitivity/bias theo P032 | Đổi nhãn metadata, giữ nội dung để so lựa chọn citation | Nhãn provenance bảo tàng có cùng tác động hoặc bỏ metadata sẽ tốt hơn |

## P044 — Correctness is not Faithfulness

Nguồn: [bảnPDF do tác giả lưu](https://mariaheuss.com/assets/correctness.pdf), ICTIR2025, DOI10.1145/3731120.3744592. Đọc §§3–7, PDFtr.4–9; đã xem trực tiếp Fig.6 ởtr.8. Metadata hội nghị/DOI/tác giả khớp catalog; đây không phải binary tải từ ACM.

Bài định nghĩa citation correctness là source hỗ trợ claim; citation faithfulness còn đòi claim chịu ảnh hưởng nhân quả từ source. Hai output nhìn giống nhau có thể chưa cho biết generation thực sự dựa vào context hay parametric memory.

Phép kiểm dùng Command-R+104B quantized4-bit và1.444 câu NQ. Tác giả chèn span ngắn từng được model sinh vào tài liệu khác, regenerate và kiểm model có dẫn tài liệu bị chèn cho span cũ hay không. Fig.6 cho nhóm relevant-but-uncited có273/476 trường hợp còn khớp span cũ dẫn tài liệu bị sửa, xấp xỉ57,4%; tập tạo ban đầu có702 trường hợp. Nhóm random là116/936; nhóm cited-for-other-reasons290/525. Đây là các tỷ lệ **có điều kiện trên span khớp**, không phải tỷ lệ citation giả trong toàn bộ RAG thông thường. Khớp span cũng không có nghĩa cả answer giữ nguyên.

Kết quả cho thấy một failure mode đáng lưu ý. Tuy nhiên tác giả chỉ kiểm một necessary condition, không quan sát toàn bộ internal provenance. Adversarial-only context đôi khi vẫn giúp recover span; cueing, useful content hoặc model memory còn là các khả năng. Vì vậy giữ riêng observed behavior và cách tác giả diễn giải là post-rationalization. Không coi pass/fail một probe là chứng nhận causal faithfulness hoàn chỉnh.

## P032 — Attribution Bias trong Generator-Aware RAG

Nguồn: [ACL2025 officialPDF](https://aclanthology.org/2025.findings-acl.1087.pdf), §3, PDFtr.3–5; §4–5/Tables1–5, tr.5–8; Limitations tr.9; AppendixA tr.13.

Bài đổi nhãn Human/LLM trong input và giữ passage text để kiểm ảnh hưởng của authorship information. Mixed mode còn giữ actual authorship giống nhau giữa các documents, giúp tách nội dung được viết lại khỏi nhãn được thông báo cho generator.

Table4 trên NQ với toàn bộ actual text do người viết: Llama3 có attribution precision45,7 hoặc57,4 tùy cách gắn nhãn relevant/non-relevant passages; Table5 báo CAB+11,7. Kết quả chỉ ra model nhạy với nhãn tác giả trong cấu hình thử. Precision ở đây đếm citation tới tài liệu IR-relevant, không phải entailment của từng câu.

**Một trùng tên cần sửa trong cách tổng hợp:** CAS của bài này là Counterfactually-estimated Attribution Sensitivity, tức mean absolute change của metric khi thêm authorship labels. CAS của ReClaim là Correct Attribution Score. Chúng không thể đặt cùng một cột “CAS” rồi so cao/thấp.

Giới hạn:500 câu mỗi benchmarkNQ/MSMARCO, chỉ giữ câu có đúng một relevant document trong top-k; English,3 models. AppendixA có2 expert annotators kiểm synthetic relevant passages; non-relevant preservation chỉ kiểm mẫu10% queries. Bài không có claim-support adjudication đầy đủ hoặc mitigation đã kiểm nghiệm. Hiệu ứng của tên bảo tàng/nhãn “nguồn chính thức” vẫn là câu hỏi chuyển miền, chưa phải kết quả đã được chứng minh; không có cơ sở khuyên bỏ provenance metadata.

## P026 — RAGE và fine-tuning citation

Nguồn: [KONVENS2024 officialPDF](https://aclanthology.org/2024.konvens-main.6.pdf), §§3–4/Tables1–2, PDFtr.2–4; §4.5/§6, tr.5. Bài8 trang; đợt này đọc main evaluation, fine-tuning vàlimitations, chưa đọc toàn bộ appendices.

RAGE tạo mixture relevant/irrelevant/seemingly-relevant documents từ IR labels. Citation precision đếm relevant citations trong toàn bộ citations; recall đếm distinct relevant documents đã cite trong số relevant documents được cung cấp. Đây là document-selection proxy, khác ALCE citation recall trên output statements được nguồn chứng minh.

Bài dùng SFT với syntheticGPT3.5 data vàPPO với reward là trung bình precision/recall, cóKL penalty. Table2 cho Llama2-7B F1 tăng0,47→0,70 khi dùngSFT+PPO. Nhưng với Mistral7B, PPO-onlyF10,72 cao hơnSFT+PPO0,70; phối hợp có precision0,74 thay vì0,65 nhưng recall0,66 thay vì0,80. Không thể kết luận phối hợp thắng ở mọi mục tiêu.

SFT có3.201 examples; PPO10.347 examples từNQ/HotpotQA; kết quả chính dùng250 câu NQ giữ lại. Citation gains theo relevance labels chưa chứng minh từng cited source entail claim, answer factuality, abstention quality hoặc causal use. §6 thừa nhận rõ citation quality tăng có thể đi cùng chất lượng khác giảm.

## Kết nối với các bài đã đọc

ALCE/ReClaim giúp kiểm đúng attached source; RAGChecker giúp chẩn đoán support ở toàn context. P044 đặt thêm yêu cầu về ảnh hưởng của source vào generation; P032 kiểm một nguyên nhân khác làm source selection đổi: metadata labels. RAGE cung cấp optimization từ document relevance nhưng đo ở mức khác claim entailment.

Do đó cần ghi metric bằng tên đầy đủ, đơn vị vàmẫu số. `metric-dictionary6.csv` tách3 cặp dễ nhầm: CAS củaReClaim vớiCAS củaP032; citation recall củaRAGE vớiALCE; faithfulness củaRAGChecker vớicausal faithfulness củaP044. Các điểm này là kết quả đối chiếu literature, chưa phải experimental protocol hoặc architecture được chốt.

**Novelty vẫn chưa được xác nhận.** Counterfactual citation tests, authorship-bias tests vàcitation fine-tuning đều đã có tiền lệ trực tiếp. Không thể chỉ lấy một trong các block đó đưa vào museum chatbot rồi gọi là phương pháp mới. Cũng chưa đủ cơ sở kết luận toàn bộ nearest work trong bảo tàng tiếng Việt chưa làm các việc này.

Lượt kế tiếp nên nối nhóm mechanistic/internal attribution(P022/P047, kiểm publication status trước) với bằng chứng miềnViCH/SACR. Không mở rộng sang xây KG hoặc chạy benchmark chỉ vì đã có các ý tưởng kiểm chứng.

## Trạng thái hồ sơ

Thêm3 phiếu extraction,18 ghi chú có locator, bảng11 IDs vàtừ điển6 mục metric. Ba nguồnPDF đều tải thành công, không truncated; giữ raw/text vàảnhFig.6 trong archive dữ liệu. Kết quả số là tác giả báo cáo; phần tính57,4% là tính lại từ số đếmFig.6, không phải inference của dự án.

Danh mục101 vànhãn v0.1(63/30/8) không đổi. Không có ứng viên mới, formal inclusion mới, independent human crosscheck hoặc model run trong lượt này. Formal search vàeligibility vẫn mở; literature chưa kết thúc.
