# Đợt đọc literature RAG — 17/11/2026

**Literature review vẫn đang làm. Đợt này đọc sâu các phần phương pháp, kết quả và hạn chế của 4 bài về sufficiency, verification, abstention và conflict; chưa chuyển sang làm benchmark hoặc chạy mô hình.** Đây là tổng hợp có trích vị trí nguồn, không phải kết luận review cuối cùng hay tuyên bố novelty.

Danh mục vẫn có 101 ứng viên. Không thêm ứng viên hoặc đổi nhãn relevance v0.1 trong đợt này; các nhãn 63 đọc tiếp / 30 chưa rõ / 8 ngoài phạm vi không phải số bài được nhận chính thức. Bốn bài dưới đây là phạm vi đọc của đợt, không mặc nhiên là bốn bài mới hoàn toàn chưa từng được xem.

## 1. Vì sao đọc bốn bài này cùng nhau?

Câu hỏi chung của mình là: **một trợ lý bảo tàng dùng RAG làm thế nào để trả lời dựa trên bằng chứng, nhận ra phần chưa đủ căn cứ và tránh trả lời quá mức?** Cần tách các mắt xích sau để đọc đúng literature:

| Mắt xích | Điều cần biết | Bài đối chiếu chính trong đợt |
|---|---|---|
| Context liên quan → context đủ căn cứ | Nguồn có trả lời được mọi phần cần thiết của câu hỏi không? | RINSE |
| Context đủ thông tin → thông tin đáng tin | Nguồn có thể cung cấp một đáp án rất rõ nhưng sai không? | GRAB-RAG |
| Draft có citation → claim được nguồn hỗ trợ | Verifier kiểm được gì và loại nhầm những câu nào? | GuidelineGuard |
| Nguồn khác nhau → cách xử lý thích hợp | Khác nhau do entity ambiguity, thông tin sai hay nhiều diễn giải hợp lệ? | MADAM-RAG / RAMDocs |

Các bài đo những mục tiêu khác nhau; không xếp hạng chúng bằng cách đặt các con số PA, answer rate, MCQ accuracy và set-EM lên cùng một thang.

## 2. P023 — RINSE: kiểm đủ bằng chứng trước khi sinh đã có tiền lệ trực tiếp

Nguồn: [Relevance Is Not Sufficient Evidence](https://arxiv.org/pdf/2609.37469), đặc biệt §3; §4/Fig.2, tr.6–7; §5/Tables4–5, tr.8–9; §6/Table6, tr.10. Số trang là vị trí trang PDF, tính từ1. Bản lấy về ghi **Preprint. Under review**.

**Vấn đề:** một passage có cùng chủ đề chưa chắc chứa thông tin cần để trả lời. Nếu chỉ dùng relevance hoặc confidence của câu trả lời thì có thể bỏ qua khoảng thiếu này.

**Cách làm:** RINSE kết hợp ba bộ đọc: mức phủ các phần của câu hỏi; một extractive reader so đáp án dạng span với no-answer; và một bộ đọc latent xét nhiều passage cùng nhau. Điểm được hiệu chỉnh theo kích thước evidence set, chuẩn hóa bằng training fold và cộng với trọng số bằng nhau. Đây không phải chỉ thêm một câu prompt “hãy kiểm tra đủ thông tin”.

**Bằng chứng:** Table4 báo cáo pairwise accuracy trung bình0,837, so với0,746 của Self-RAG và0,784 của API Sufficient Context. PA đo khả năng xếp evidence đủ cao hơn evidence thiếu trong một cặp/nhóm, có ties tính0,5. Nó không có nghĩa hệ thống trả lời đúng83,7% câu hỏi. RINSE cũng không thắng mọi nơi: trên SQuAD2.0, nó đạt0,684, thấp hơn Self-RAG0,752.

Table5 dùng3.149 cặp output BM25 và dense retrieval, chọn những cặp mà một bên chứa đủ annotated supporting passages và bên kia không đủ. PA trung bình là0,813 cho RINSE và0,800 cho API. Đây là kiểm tra bổ sung ngoài các cặp được tạo bằng cách xóa/thay evidence, nhưng vẫn phụ thuộc độ đầy đủ của nhãn support.

Khi dùng làm gate cho12 generator, tỉ lệ trả lời trên context thiếu giảm0,636→0,511, đồng thời tỉ lệ trả lời trên context đủ cũng giảm0,861→0,783 (§5, sau Table5). Như vậy gate có ích nhưng có chi phí từ chối nhầm.

**Đọc phản biện:** tác giả có kiểm các shortcut như số passage và lexical overlap; điều này không chứng minh mọi artifact đã biến mất. Các thành phần không đóng góp đồng đều: content reader riêng đạt0,799 trên NeoQA, cao hơn tổng hợp0,773; span reader gần chance ở đây. Không có kiểm chứng cho QA bảo tàng tiếng Việt. Latency36,5ms là số đo tác giả trên A100, không phải cam kết chạy trên máy mình.

**Hệ quả cho literature của mình:** không thể lấy “thêm sufficiency gate trước generation” làm novelty độc lập. Bài này phải có trong bảng nearest work. Theo tiêu chí dự thảo ưu tiên bài đã xuất bản, hiện giữ ở novelty watchlist; chưa nhận vào formal included set.

## 3. P020 — GRAB-RAG: thiếu bằng chứng khác với có bằng chứng sai

Nguồn: [Prompt-Based Abstention Fails Under Misleading Context](https://aclanthology.org/2026.aacl-long.153.pdf), §§3–4/Fig.1, PDF tr.3–6; §5/Tables1–3, tr.6–7; §6 và Limitations, tr.8–9. PDF thuộc proceedings trong metadata hiện có; chưa quyết định formal eligibility độc lập.

**Vấn đề:** mô hình biết từ chối khi không tìm thấy thông tin có đồng nghĩa với việc biết từ chối khi passage cung cấp thông tin sai rất trôi chảy không?

**Cách kiểm:** cùng câu hỏi được đặt vào context có đủ gold passage(Q100), giảm support(Q50), chỉ còn hard negatives(Q0), và một passage bị thay đáp án kèm bốn hard negatives(QC). Có1.000 câu hỏi ban đầu; chỉ202 NQ và330 HotpotQA đáp ứng điều kiện tạo swap QC. Không được gọi64.980 output rows là64.980 câu hỏi độc lập.

**Bằng chứng:** trên sáu ô model×dataset, thêm yêu cầu từ chối rõ ràng(P1) vẫn để lại QC answer rate41,6%. Dùng closed-book agreement gate(P3) giảm xuống13,3%, nhưng Q100 answer rate cũng giảm79,3%→33,4%; FAC@Q100 tăng từ0 theo cách xây capable set P1 lên49,8%(Table2). P4 dùng NLI lấy lại một phần coverage, nhưng vẫn dựa vào closed-book answer và không giải quyết được trường hợp memory và context cùng sai.

**Cẩn thận với metric:** HwSA ởQC tính bất kỳ lần trả lời nào là failure, kể cả tình cờ trả về gold answer. Do đó không được diễn giải41,6% thành “41,6% câu trả lời có claim hallucination”. Tác giả chủ động đo chính sách từ chối context không đáng tin.

**Giới hạn:** mô hình nhỏ3,8B–8B, frozen, quantized; English extractive QA; swap tạo bằng rule và thiên về factoid dễ. QC không phải xung đột tự nhiên giữa hai tài liệu. P3/P4 được giới thiệu là diagnostic baselines, không phải giải pháp triển khai đã hoàn chỉnh.

**Hệ quả:** RINSE hỏi “context có đủ không”; GRAB-RAG cho thấy context có thể đủ để suy ra một đáp án nhưng đáp án sai. Hai bài bổ sung nhau. Không được coi NLI entailment là bằng chứng về sự thật ngoài đời.

## 4. P030 — GuidelineGuard: kiểm claim có thể tăng độ chọn lọc và đồng thời loại nhiều câu đúng

Nguồn: [publisher HTML](https://www.mdpi.com/2079-3197/14/9/210), §§3.4,3.6–3.10; Table3; §§4.8,4.12/Tables12–13; §6. DOI:10.3390/computation14090210. Đọc HTML; chưa kiểm số trang publisher PDF để hoàn tất tiêu chí length.

**Cách làm:** Planner tách câu hỏi, hybrid retrieval lấy câu evidence, Clinician viết claim kèm source ID. Auditor chỉ thấy claim và câu evidence, rồi gán Entails/Partially/Not. Synthesizer dùng phần qua gate; standard mode còn cho fallback Partially khi không có Entails. “Claim được một auditor duyệt” không đồng nghĩa mọi output đều đã được chứng minh đầy đủ.

**Bằng chứng quan trọng hơn abstract quảng bá:** ở GG-Bench200, no-auditor đúng191/200 với192 commitments; có auditor đúng185/200 với186 commitments. Gate loại thêm6 commitment đúng và không loại commitment sai nào(§4.12/Table12). Bộ200 này mở rộng từ60 câu do tác giả viết bằng140 câu template, dùng chung corpus73 câu; không phải200 trường hợp lâm sàng độc lập được bác sĩ kiểm định.

Trên PubMedQA500, no-auditor có operational accuracy0,638, coverage0,896 và selective accuracy0,712. Có auditor, ba số tương ứng là0,550;0,736;0,747(Table13). Trong496 trường hợp xác minh cùng observable pre-audit state, gate loại36 commitment sai và45 commitment đúng. Bốn trường hợp còn lại bị regenerate sau quota interruption; không gộp chúng vào phép so sánh gate paired496.

**Đọc phản biện:** selective accuracy cao hơn đi cùng coverage thấp hơn và tổng số câu đúng thấp hơn. Original Citation Faithfulness được đo bằng các evaluator khác nhau giữa hệ thống, nên không phải so sánh ngang hoàn toàn. Table3 còn cho empty cases đóng góp0 vào macro CF; metric đó trộn coverage với support. Citation ID tồn tại hoặc trùng gold ID chỉ là reference alignment, không phải human-adjudicated entailment. NLI crosscheck chỉ là một model đối chiếu; không thay được chuyên gia độc lập và không bảo đảm hết bias.

Một điểm cần hỏi lại khi kiểm raw artifacts: các đoạn original report dùng những mẫu số claim khác nhau(§3.10 nêu45/70; §4.8 nêu68 audited pairs cho8B), và §4.11 mô tả refusal khi chỉ còn Partially khác với fallback ở§3.4. Chưa tự giải thích thay tác giả; ưu tiên số expanded case-level có mẫu số rõ, giữ các điểm này là unresolved. Chưa tải/chạy lại Zenodo package để adjudicate.

**Hệ quả:** “tách verifier khỏi generator”, “kiểm từng claim–sentence” và “có abstention” đã có tiền lệ trực tiếp. Nếu sau này chọn hướng này, lập luận nghiên cứu phải vượt qua bằng chứng phản biện trên; hiện chưa chốt phương pháp.

## 5. P054 — MADAM-RAG/RAMDocs: conflict không có một cách xử lý duy nhất

Nguồn: [Retrieval-Augmented Generation with Conflicting Evidence](https://arxiv.org/pdf/2504.13079), §3 tr.4–5; §4 tr.5–6; §5/Table1 tr.6–8; §6/Fig.3 tr.9; AppendixD/Table2 tr.17. PDF ghi COLM2025; catalog cũ còn arXiv-only, cần đối chiếu proceedings/version trước formal eligibility.

**Vấn đề:** hai nguồn nêu hai năm sinh cho “Michael Jordan” có thể nói về hai người khác nhau. Giữ cả hai đáp án kèm phân biệt entity có thể đúng; coi một bên sai hoặc tự động từ chối thì mất thông tin. Điều đó khác với passage bị sửa năm sinh cho chính một người.

**Cách làm:** RAMDocs có500 truy vấn, trung bình2,20 valid answers và5,53 documents/truy vấn; support count biến thiên và thêm misinformation/noise. MADAM-RAG gán một agent cho mỗi document, cho tranh luận và aggregator tổng hợp, tối đa3 vòng với early stopping.

**Bằng chứng:** với Llama3.3-70B, strict set-EM trên RAMDocs tăng32,60→34,40% so với concatenated prompt(Table1). Đây là1,80 điểm phần trăm, không phải mức cải thiện rất lớn; EM yêu cầu có đủ mọi gold answer và không thêm answer sai. Trên FaithEval, tăng27,30→43,10%; không chuyển mức tăng ở đây sang khẳng định cho mọi loại conflict.

Đã xem trực tiếp Fig.3 trên ảnh render của PDF tr.9: accuracy RAMDocs có aggregator qua1/2/3 vòng là37,8/36,8/34,4%. Vì vậy không thể rút ra “thêm vòng debate luôn tốt”; biểu đồ cho thấy trade-off precision/recall và trường hợp accuracy giảm. Table2 AppendixD báo trung bình input/output tokens3.186,45/1.547,18 so với822,69/126,25 cho plain prompt; đây là token usage, không phải latency.

**Giới hạn:** misinformation vẫn được tạo bằng answer swap; supporting chunks được chọn theo answer; không có gold claim–citation entailment cho museum QA tiếng Việt. Thiết kế debate không bảo đảm “được nhiều agent đồng ý” thì đúng. Không thấy một mục Limitations riêng ở main text; các giới hạn chuyển miền trên là đánh giá của lượt đọc, không gán nguyên văn cho tác giả.

## 6. Điều literature đã làm rõ và điều còn mở

**Đã có cơ sở từ nguồn để thu hẹp novelty:** sufficiency gate; kiểm claim với source sentence; selective answering; conflict-aware multi-agent aggregation đều đã có tiền lệ. Chỉ ghép các block này vào một museum chatbot chưa đủ chứng minh đóng góp phương pháp mới.

**Mắt xích còn phải đọc tiếp:** cần đối chiếu các kết quả trên với SACR/ViCH-QA trong miền tiếng Việt, Sufficient Context về sufficiency–confidence, ReClaim/ALCE về cited evidence và RAGChecker về claim diagnostics. Một số bài đã được xem ở đợt trước; bước tiếp là hoàn thiện extraction cùng khung, tìm các phản ví dụ và nguồn gần hơn, không tuyên bố chúng chưa từng được đọc. Phải phân biệt support của câu trả lời, mức đúng của source, và causal faithfulness của citation; lượt này chưa giải quyết hết cả ba.

**Khoảng trống chưa được xác nhận:** từ bốn bài này chưa chứng minh rằng không có nghiên cứu nào đánh giá đồng thời các mục tiêu trên cho museum QA tiếng Việt. Đó là câu hỏi tiếp tục tra cứu, không phải kết luận “mình là đầu tiên”. Chưa có căn cứ chốt chất lượng venue hay tách chắc chắn thành hai paper.

**Literature chưa đóng:** tìm nguồn theo protocol còn chưa hoàn tất; eligibility toàn văn chưa adjudicate; extraction chưa được người thứ hai đối chiếu; tổng hợp nearest work còn đang mở. Không tăng formal included count từ lượt đọc này. Không có model run, benchmark creation hoặc inference score của dự án trong báo cáo.

## 7. Hồ sơ đọc để kiểm lại

- `reading-extraction4.csv`: câu hỏi, cách làm, dữ liệu, metric, kết quả, hạn chế, read scope và trạng thái eligibility cho4 bài.
- `evidence-ledger22.csv`:22 nhận định có source URL và section/table/page locator. Đây là đơn vị ghi chú, không phải22 phát hiện mới.
- `source-access.json`:log lấy4 nguồn gốc và SHA256 tại thời điểm tải; không phải xác minh nội dung tự động.
- Bản archive trên kho dữ liệu dự án giữ PDF/HTML, text extract và ảnh Fig.3 để kiểm tra lại. Repo chỉ chứa paraphrase, metadata và liên kết scholarly công khai.

Mọi kết quả số là tác giả báo cáo, chưa được tái lập. Đây là AI-assisted critical extraction; independent human check chưa thực hiện. File scope hiện hành đặt literature reading/extraction/synthesis là ưu tiên; experimental design trước đây chỉ còn là draft tham khảo.
