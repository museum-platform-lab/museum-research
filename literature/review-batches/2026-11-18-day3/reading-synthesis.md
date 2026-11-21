# Day 3 — Đọc và đối chiếu literature RAG

Ngày18/11/2026. Trọng tâm vẫn là text-first evidence-grounded QA cho bảo tàng. Lượt này đọc sâu và chuẩn hóa ghi chú của **Sufficient Context, ReClaim, RAGChecker và ALCE**, một số bài đã được xem ở các đợt trước. Không gọi đây là bốn ứng viên mới hoặc bốn bài lần đầu được đọc. Literature vẫn đang mở.

## Mắt xích cần làm rõ

Đợt trước phân biệt context thiếu, context sai và nguồn mâu thuẫn. Đợt này kiểm tiếp: **“trả lời đúng”, “được context hỗ trợ” và “trích đúng nguồn” có phải cùng một mục tiêu không?** Câu trả lời từ literature là cần đo riêng, vì chúng dùng những đơn vị và mẫu số khác nhau.

| Câu hỏi đánh giá | Mục tiêu/đơn vị | Nguồn đối chiếu |
|---|---|---|
| Context có đủ thông tin để trả lời không? | Question–context; chưa cần có draft answer | Sufficient Context; nối với RINSE đợt trước |
| Câu trả lời bao phủ bao nhiêu nội dung cần thiết? | Đáp án/claim bắt buộc trong gold | ALCE; ReClaim; RAGChecker |
| Claim có được một phần context hỗ trợ không? | Claim đối với retrieved context | RAGChecker |
| Đúng những nguồn gắn với câu đó có hỗ trợ câu không? | Output statement đối với attached citations | ALCE; ReClaim |
| Hệ thống từ chối bao nhiêu và trả lời đúng trên phần còn lại ra sao? | Coverage cùng selective accuracy | Sufficient Context; nối GuidelineGuard/GRAB-RAG |
| Citation có phản ánh nguồn thực sự ảnh hưởng đến generation không? | Causal attribution | Chưa được giải quyết bằng entailment score; đọc tiếp nhóm này |

Ví dụ khái niệm: một fact có trong passageB nhưng câu trả lời dẫn passageA không chứa fact đó. Claim vẫn có thể được retrieved context hỗ trợ, trong khi citation gắn với nó không đúng. Nếu mô hình nhớ đúng một fact không có trong bất kỳ passage nào, answer correctness cũng chưa chứng minh groundedness. Ngược lại, một passage chứa fact sai có thể entail một câu trả lời sai. Các trường hợp này giải thích vì sao một metric riêng lẻ không đủ mô tả chất lượng RAG.

## P050 — Sufficient Context: tín hiệu đủ bằng chứng cần đi cùng mục tiêu answering

Nguồn: [ICLR2025 proceedings PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/33dffa2e3d2ab74a783d1a8c292f66d9-Paper-Conference.pdf), §3 vàTable1, PDFtr.4–5; §5.1, tr.8–9; Fig.4/conclusion/limitations, tr.10. Header xác nhận conference paper ICLR2025; năm2024 trong catalog lịch sử là năm arXiv đầu tiên. Ghi riêng publication evidence, giữ bản catalog cũ để truy vết.

**Cách đặt vấn đề:** sufficiency xét xem từ question vàcontext có thể có một đáp án plausible hay không, thay vì kiểm entailment của một đáp án cho sẵn. §3.1 còn cho phép context chứa đáp án sai. Do đó sufficiency không chứng minh source factuality.

**Phương pháp và bằng chứng:** Table1 dùng115 instances có nhãn sufficiency của người; Gemini1.5Pro one-shot đạt accuracy0,930 vàF10,935. Đây là phân loại context đủ/thiếu, không phải93% QA accuracy. Khi làm selective generation, bài dùng FLAMe để gán nhãn sufficiency và logistic regression kết hợp nhãn này với self-rated confidence. P(True) của các mô hình mở cần20 sampled responses cùng5 lần judgment; không mặc nhiên là giải pháp ít chi phí inference.

§5.1 báo lợi ích trên một số vùng coverage, như hơn5 điểm cho Gemini/HotpotQA gần70% coverage. Nhưng Fig.4 cũng nêu Gemma27B/MuSiQue có hệ số sufficiency bằng0, hai đường confidence-only vàcombined trùng nhau. Vì vậy không kết luận thêm sufficiency luôn tốt hơn confidence.

**Giới hạn cần giữ:** autorater gold set nhỏ; khả năng chuyển sang tiếng Việt và tư liệu bảo tàng chưa được chứng minh. FLAMe xét sufficient nếu có bất kỳ chunk1600token nào sufficient, nên có thể bỏ sót bằng chứng cần ghép nhiều chunk. Đây là failure mode suy ra từ cách làm, chưa phải tỉ lệ lỗi đo được. Chi tiết chia tập/calibration cho logistic regression chưa được xác lập trong phạm vi đọc có mục tiêu này; không gán thành khẳng định paper có leakage.

**Liên hệ:** bài tối ưu chọn câu có khả năng đúng, kể cả khi context thiếu. Nếu dự án yêu cầu mọi câu trả lời có căn cứ trong nguồn, phải giữ riêng tiêu chí support; không sao chép chính sách answer/abstain chỉ vì answer accuracy cao hơn.

## P046 — ReClaim: chọn reference trước claim đã có tiền lệ rõ

Nguồn: [Ground Every Sentence](https://aclanthology.org/2025.findings-naacl.55.pdf), §§3.2–3.5, PDFtr.3–5; Tables2–3, tr.6–7; §4.6, tr.7–8; Limitations, tr.9; AppendixC.3, tr.14–15.

**Cách làm:** dữ liệu fine-tuning có reference–claim pairs được lọc bằng NLI; bản interleaving dùng ReferModel chọn reference vàClaimModel viết claim từ các reference/claim trước. Prefix-tree decoding giữ reference là câu có thật trong supplied passages. Bản Unified chỉ dùng một model không đạt attribution tốt bằng bản interleaving trong bảng chính.

**Đọc kết quả cùng các cột:** với Llama3-8B, Table2 so ALCE với ReClaimIG trênASQA cho CAS54,7→92,1 nhưng EMrecall55,2→53,5. TrênELI5, CAS42,8→89,9 còn claimrecall20,5→17,8; trênEXPERTQA, CAS51,4→90,1 còn claimrecall20,2→14,0. Đây là so sánh hệ thống trong bài, không phải ước lượng tác động riêng của interleaving khi mọi yếu tố khác đã được giữ bằng nhau.

CAS tương ứng tỷ lệ answer clauses được citations hỗ trợ, gần ALCE citation recall. Nó khác answer recall, vốn hỏi có trả lời đủ thông tin cần thiết không. Table3 cho reference consistency vàattribution ratio có thể đạt100% trong khiCAS ởTable2 vẫn dưới100%: citation được sao chép đúng nguồn và có mặt bên cạnh câu chưa bảo đảm entailment.

**Giới hạn:** cách làm đã có trước cho evidence-first sentence generation; chưa thể gọi block tương tự là novelty. Bài thừa nhận hạn chế với multi-source/multi-hop, thêm quote làm output dài hơn và tăng thời gian generation. Faithfulness trong§4.6 là RAGAS trên toàn context, không phải kiểm causal influence của citation. Chưa xác lập independent human claim-support validation từ các phần được đọc; không coi NLI-filtered training vàNLI evaluation là human gold.

## P018 — RAGChecker: chẩn đoán hữu ích, cần đọc đúng phạm vi metric

Nguồn: [NeurIPS2024 proceedings PDF](https://papers.nips.cc/paper_files/paper/2024/file/27245589131d17368cccdfa990cbf16e-Paper-Datasets_and_Benchmarks_Track.pdf), §3, PDFtr.3–6; §4.2/Table2, tr.6–7; AppendixC, tr.16–17; AppendixH, tr.22.

**Cách làm:** tách response thành claims và kiểm entailment với gold answer cùng retrieved chunks. Từ đó có metrics cho toàn hệ thống, retrieval vàgeneration. Đây là evaluator/diagnostic framework; sử dụng nó không tự tạo ra generation-time verifier hoặc answerability policy đã hiệu chỉnh.

**Điểm định nghĩa rất quan trọng:** faithfulness kiểm support ở bất kỳ retrieved chunk nào. Claim đúng nhưng không được context hỗ trợ nằm ở self-knowledge; claim sai và không được context hỗ trợ mới thuộc hallucination; claim sai nhưng được source hỗ trợ thuộc noise sensitivity. “Hallucination” ở đây không cùng định nghĩa với mọi bài selective answering, nên không so trực tiếp các phần trăm mang cùng tên.

**Bằng chứng về evaluator:** benchmark có4.162 questions ở10 domains; meta-evaluation280 response pairs, mỗi cặp có2 annotators. Table2 báo overall Pearson0,6193 vàSpearman0,6090, cao hơn RAGASAnswerSimilarity0,4831/0,5723. Tuy vậy, completeness Spearman củaRAGChecker0,5811 thấp hơnRAGAS0,6135. Không viết “thắng trên mọi metric”. Các số tương quan này cũng không phải độ chính xác kiểm entailment từng claim.

**Đọc cách có human evidence:** AppendixC nói annotators được xem GPT-4-generated critiques trong lúc gán nhãn; một số long-form gold answers cũng được mở rộng bằngGPT-4. Đây vẫn là human preference data, nhưng không phải hoàn toàn unaided/blinded claim-level adjudication. Cần ghi rõ sự hỗ trợ này khi nhận xét độ mạnh của validation.

**Giới hạn tác giả nêu:** AppendixH gộpNeutral vàContradiction thànhnon-entailment; English text-only. Chỉ riêng tín hiệu không-entailment chưa cho biết nguồn không đề cập hay chủ động phủ định claim. Một gold answer chưa đầy đủ còn có thể khiến fact bổ sung đúng bị tính như lỗi. Entailment overlap cũng chưa đủ chứng minh model thực sự dùng passage đó để sinh câu.

## P084 — ALCE: citation recall khác answer recall

Nguồn: [Enabling Large Language Models to Generate Text with Citations](https://aclanthology.org/2023.emnlp-main.398.pdf), §§2–3, PDFtr.2–5; §6/Tables8–9, tr.8–9; Limitations, tr.10.

**Đơn vị đánh giá:** ALCE tách fluency, correctness vàcitation quality. Citation recall lấy tỷ lệ output statements được toàn bộ cited passages đi kèm hỗ trợ; correctness recall hỏi response chứa được bao nhiêu gold answer/claim cần có. Vì vậy câu trả lời rất ngắn có thể có citations tốt nhưng bỏ sót phần lớn câu hỏi.

Citation precision kiểm citation không liên quan. §3.3 nói rõ không đòi bộ citation tối thiểu. Một claim cần nhiều nguồn kết hợp vẫn có thể hợp lệ; không được bắt từng citation riêng rẽ chứng minh toàn bộ claim. Đồng thời metric yêu cầu joint full support trước khi cho precision1, vàbinary NLI có hạn chế với partial support.

**Validation và giới hạn:** §6 cho Cohenκ0,698 với citation recall và0,525 với precision. Khi dùng human labels làmgold, accuracy tương ứng85,1% và77,6%; đây không phải accuracy của hệ thống QA. Table8 còn có ASQArerank automatic recall83,9 so với human79,3, cho thấy tối ưu metric và độc lập kiểm bằng người có thể lệch nhau.

§3.4 chỉ ra cách sao chép passage có thể gần hoàn hảo ở citation scores nhưng yếu về correctness/utility. Limitations nhắc MAUVE nhạy với độ dài/style, ELI5 generated claims chưa đầy đủ vàNLI không xử lý partial support tốt. Do đó không thay human checking bằng một evaluator score, cũng không dùng citation score đơn lẻ để khẳng định câu trả lời đáng tin.

## Nối với đợt trước và phạm vi còn phải đọc

Hai đợt chuẩn hóa hiện có8 paper IDs trong `cross-paper-matrix8.csv`; đây không phải8 lần đọc đầu tiên hoặc8 formal included studies.

- RINSE vàSufficientContext cung cấp hai cách xem evidence sufficiency, với khác biệt về scorer, nhãn vàđích selective answering.
- GRAB-RAG cho thấy đủ thông tin có thể vẫn sai; không dùng sufficiency thay source reliability.
- ReClaim vàGuidelineGuard cho thấy hai cách ràng buộc generation bằng evidence, đều có trade-off về nội dung được trả lời hoặc coverage.
- RAGChecker kiểm context-level claim support; ALCE kiểm citation-specific support. Cần cả hai khi so sánh nearest work.
- MADAM-RAG nhắc rằng apparent conflict còn có thể do ambiguity hợp lệ; gộp mọi conflict thành refuse làm mất thông tin.

**Điều đã đủ cơ sở:** sufficiency gate, evidence-first reference–claim generation, independent verifier vàcitation metrics đều có prior work trực tiếp. Không đề xuất lại chúng như một novelty độc lập.

**Điều chưa đủ cơ sở:** chưa chứng minh không có benchmark/method kết hợp các mục tiêu này trong museum QA tiếng Việt; chưa chốt novelty, venue hoặc hai paper chắc chắn. Cần đọc tiếp citation correctness với causal faithfulness(P044), accurate citation generation(P026) vàattribution bias(P032), đồng thời đối chiếu miền Việt Nam/SACR theo cùng khung extraction. Đây là hàng đợi literature, chưa phải lựa chọn architecture.

Danh mục101 vànhãn relevance v0.1(63/30/8) không đổi. Tìm nguồn theo protocol, eligibility adjudication vàindependent human crosscheck chưa hoàn tất. Mọi số liệu ở đây là tác giả báo cáo, chưa tái lập; không có model run của dự án hoặc dữ liệu benchmark mới trong lượt này.

## Hồ sơ kèm theo

`reading-extraction4.csv` ghi phạm vi đã đọc, phương pháp, kết quả, hạn chế vàpublication evidence. `evidence-ledger20.csv` chứa20 nhận định có source locators. `cross-paper-matrix8.csv` nối hai lượt đọc; `publication-evidence-delta.csv` tách năm arXiv củaP050 với publication year. Source access log vàarchive giữ bảnPDF/text để kiểm lại. Public repo chỉ chứa metadata, paraphrase vàscholarly links.
