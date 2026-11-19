# Tổng quan tài liệu v1: Trợ lý bảo tàng tiếng Việt trả lời dựa trên bằng chứng

Cập nhật 18/11/2026. Đây là bản tổng hợp có lập luận từ 14 paper IDs trong chuỗi extraction chuẩn hóa, bên cạnh catalog 101 ứng viên và hồ sơ các đợt trước. Không phải14 bài lần đầu được đọc, một tập bài đã được nhận chính thức hay systematic review đã hoàn tất. Hai đầu mối mới đã được đọc ở đợt 4 và được ghi riêng trong phần đối chiếu bổ sung. Mục tiêu hiện hành là text-first evidence-grounded RAG; KG vẫn ở vai trò đối chiếu/mở rộng tương lai.

## 1. Vấn đề nghiên cứu

Một trợ lý bảo tàng cần trả lời thông tin đúng và giúp người đọc kiểm tra được căn cứ. RAG, tức tìm tài liệu rồi dùng tài liệu để trả lời, là cách làm phổ biến. Tuy nhiên việc tìm thấy trang có cùng chủ đề không bảo đảm trang đó chứa thông tin cần thiết; một câu trả lời đúng có thể đến từ trí nhớ mô hình; một nguồn được trích có thể không chứng minh claim; và nguồn chứng minh được claim vẫn có thể chứa thông tin sai.

Vì vậy bản review tổ chức theo ba câu hỏi:

1. Dữ liệu hiện có ghi lại câu hỏi, đáp án và bằng chứng ở mức nào? Những trường hợp cần nhiều nguồn, thiếu thông tin hoặc nguồn khác nhau được thể hiện ra sao?
2. Các nghiên cứu tìm cách chọn đủ bằng chứng, sinh câu có nguồn, kiểm từ ng ý và quyết định trả lời/từ chối như thế nào?
3. Các phép đánh giá thực sự đo điều gì: đáp án đúng, bao phủ đủ ý, được context hỗ trợ, dẫn đúng nguồn hay phản ánh nguồn ảnh hưởng đến generation?

Một claim là một ý có thể kiểm chứng, chẳng hạn niên đại của một hiện vật. Context là các đoạn tài liệu hệ thống nhận được. Citation là chỉ dẫn nối một ý trong câu trả lời với nguồn. Ba khái niệm này cần được giữ riêng khi đọc kết quả.

## 2. Dữ liệu gần nhất: ViCH-QA và SACR

[ViCHat/SACR(P008)](https://ctujs.ctu.edu.vn/index.php/ctujs/article/view/3152) là prior work trực tiếp về QA di sản tiếng Việt. Bài mô tả159 tài liệu,494 chunks và 4.719 QA:2.959 single-hop,1.580 câu tổng hợp nhiều phần trong cùng tài liệu,180 câu cần nhiều tài liệu. Có track thủ công và track LLM-assisted kết thúc bằng chuyên gia kiểm duyệt; câu đa tài liệu dùng2–4 nguồn. Do đó “QA di sản tiếng Việt”, “có chuyên gia kiểm” và “câu hỏi nhiều nguồn” đều đã có tiền lệ(§3, printed p.80).

SACR tạo một summary chung cho mỗi tài liệu rồi ghép và o các child chunks trước indexing. Điều đáng chú ý là lựa chọn metric: retrieved chunk được xem relevant theo việc parent document có thuộc gold source set không(§4,p83). Đó là gold ở mức tài liệu, chưa đồng nghĩa mỗi chunk retrieved chứa đúng fact hoặc chứng minh từ ng claim.

Bài có kết quả phản biện cho cách hiểu “ranking tốt hơn là đủ”: trên nhóm cross-document, NDCG@10 tăng0,6371→0,6461, nhưng Complete-Hit@10 giảm0,6056→0,5778 và All-EvidenceRecall@10 giảm0,7921→0,7819(§5.1,p85). Việc tập trung nguồn relevant ở vị trí đầu có thể đi cùng giảm mức thu đủ các nguồn cần thiết. Tác giả còn ghi rõ generation metrics là reference-based, chưa phải direct context-faithfulness audit(§6,p88).

Public registry của [ứng viên HF liên quan](https://huggingface.co/datasets/quockhangdev/vietnamese-cultural-rag-benchmark) tiếp tục khai báo4.719 QA,494 chunks và 159 summaries. QA schema hiển thị question/answer/type/source; dataset vẫn gated=manual. Metadata không đủ chứng minh exact release khớp bài hoặc thiếu toàn bộ nhãn chi tiết trong dữ liệu. Corpus174 rows so với 159 documents còn chưa giải thích. Vì vậy chưa được viết “ViCH-QA không có gold spans/abstention/conflict labels” như một sự thật đã xác nhận. `domain-evidence9.csv` phân biệt paper-reported, metadata-declared và unknown.

**Hệ quả đối với đóng góp dữ liệu:** số lượng QA và tên miền tiếng Việt chưa đủ tạo khác biệt. Một đóng góp có thể nằm ở đơn vị bằng chứng, tình huống đánh giá hoặc chất lượng kiểm nhãn; nhưng phải kiểm bộ dữ liệu hiện có và chứng minh nhu cầu chưa được đáp ứng. Bản review này chưa kiểm kê corpus riêng của dự án và chưa tạo dữ liệu benchmark mới.

Bộ Amarna đã liên kết câu hỏi ảnh–văn bản về hiện vật với đoạn nguồn do người gán nhãn. MuSiQue-Full giữ nguyên câu hỏi nhiều bước và ghép hai ngữ cảnh đủ hoặc thiếu dữ kiện. Hai tiền lệ giúp phân biệt nhãn đoạn liên quan với nhãn đủ căn cứ để trả lời và nhãn nguồn hỗ trợ cho từng ý đã sinh. [Ghi chú đọc đợt 3 ngày 19/11](review-batches/2026-11-19-day4-round3/reading-notes.md).

MuseRAG++ (P001) là đối chiếu gần về QA bảo tàng. Bài kết hợp truy xuất lai và sinh gắn nguồn, đồng thời chấm hỗ trợ ở cấp dữ kiện. Repo công khai hiện mô tả bản tối giản dùng truy xuất ngữ nghĩa và đo tỷ lệ câu có mã trích dẫn. Context or Retrieval? (P004) so ngữ cảnh đầy đủ của tác phẩm tương ứng với đầu ra truy xuất qua độ giống đáp án tham chiếu. Hai bài củng cố lý do dùng cùng mô hình sinh khi so các điều kiện ngữ cảnh, đồng thời chấm riêng nguồn hỗ trợ từng dữ kiện và hành vi khi thiếu căn cứ. [Ghi chú đọc đợt 11 ngày 19/11](review-batches/2026-11-19-day4-round11/reading-notes.md).

## 3. Context liên quan khác context đủ để trả lời

[Sufficient Context(P050)](https://proceedings.iclr.cc/paper_files/paper/2025/file/33dffa2e3d2ab74a783d1a8c292f66d9-Paper-Conference.pdf) đặt câu hỏi context có đủ thông tin để hình thành một đáp án plausible hay không, trước khi có candidate answer. Bài kết hợp sufficiency và self-rated confidence cho selective answering. Đây là prior work trực tiếp cho ý tưởng “đánh giá đủ bằng chứng rồi quyết định trả lời”. Tuy nhiên lợi ích không đồng đều: Fig. 4 cho Gemma27B/MuSiQue hai đường combined và confidence-only trùng nhau.

[RINSE (P023)](https://arxiv.org/pdf/2609.37469) dùng ba bộ đọc cho coverage của câu hỏi, evidence dạnganswer span và joint-context evidence. PA trung bình0,837 là xếp sufficient evidence cao hơn insufficient evidence trong cặp/nhóm, không phải83,7% answer accuracy(Table 4). Đây hiện là fulltext preprint under review trong hồ sơ, vẫn cần dùng khi đối chiếu novelty nhưng không tự chuyển thành formal included published study.

Hai bài cho thấy độ tương đồng chủ đề, đủ căn cứ và model confidence là những tín hiệu khác nhau. Sufficient Context còn cho phép source chứa một đáp án sai mà vẫn sufficient theo định nghĩa. Một gate đủ thông tin không kiểm được mọi vấn đề về độ đúng của source.

[GRAB-RAG(P020)](https://aclanthology.org/2026.aacl-long.153.pdf) làm rõ điều này qua context thiếu và context bị sửa để hỗ trợ đáp án sai. Gate chặt hơn giảm trả lời ở misleading context nhưng có thể mất nhiều câu đúng ở context tốt. HwSA của bài là answer rate khi chính sách yêu cầu abstain, kể cả gold-correct overrides; không được gọi đó là claim-hallucination rate. Phạm vi là các mô hình nhỏ, English extractive QA và constructed swaps.

NoMIRACL đánh giá liệu các đoạn cung cấp có đoạn liên quan hay không, với hai nhóm do người gán nhãn và 18 ngôn ngữ trong Table 1. DeclineCraft kiểm từ chối khi dữ kiện cần thiết nằm ngoài kho tài liệu ở một mốc thời gian, đồng thời chấm riêng lời phủ định tiền đề thiếu căn cứ. Hai bài giúp làm rõ đơn vị đánh giá cho câu hỏi thiếu nguồn trong miền bảo tàng. [Ghi chú đọc đợt 5](review-batches/2026-11-18-day3-round5/reading-notes.md).

UAEval4RAG tách phản hồi phù hợp theo loại câu khỏi tỷ lệ từ chối. FaithEval cung cấp điều kiện riêng cho ngữ cảnh thiếu, bất nhất và phản thực. Hai bài bổ sung tiêu chí đọc dữ liệu cho các tình huống hỏi lại, báo bất đồng và xác minh phiên bản nguồn trong QA bảo tàng. [Ghi chú đọc ngày 19/11](review-batches/2026-11-19-day4/reading-notes.md).

IIRC và HotpotQA cung cấp tiền lệ cho nhãn bằng chứng ở cấp đoạn trích hoặc câu. IIRC kiểm riêng pipeline khi được cấp liên kết và ngữ cảnh chuẩn. HotpotQA báo riêng đáp án, câu hỗ trợ và điểm kết hợp. MuseumQA còn chờ toàn văn nên chưa đối chiếu được cấu trúc nhãn cùng miền. [Ghi chú đọc đợt 4 ngày 19/11](review-batches/2026-11-19-day4-round4/reading-notes.md).

Lost in the Middle cho thấy chuyển đoạn chứa đáp án vào giữa ngữ cảnh có thể làm giảm độ đúng dù đoạn đó vẫn được đưa cho mô hình. NoLiMa minh họa một lỗi khác: đoạn nhiễu trùng từ khóa có thể lấn át bằng chứng dùng cách diễn đạt khác. Với RAG bảo tàng, nên chấm riêng việc truy xuất có đưa được đoạn chuẩn vào ngữ cảnh và việc mô hình có dùng đúng đoạn đó để trả lời. Một phép thử giữ nguyên tập đoạn và đổi vị trí nguồn chuẩn. Phép thử khác giữ nguyên nguồn chuẩn và vị trí rồi thay đoạn phụ bằng hồ sơ của hiện vật khác có từ khóa tương tự. [Ghi chú đọc đợt 8 ngày 19/11](review-batches/2026-11-19-day4-round8/reading-notes.md).

EntityQuestions cho thấy thứ hạng BM25 và DPR có thể đảo chiều giữa câu hỏi về thực thể và tập QA thông dụng. MIRACL cung cấp đối chứng BM25, mDPR và kết hợp trên 18 ngôn ngữ. Kết quả thay đổi theo ngôn ngữ, và bộ này chưa có tiếng Việt. Với hồ sơ bảo tàng, so ba cấu hình trên cùng tập đoạn và cùng số đoạn đầu ra, rồi tách kết quả cho câu hỏi dùng mã hoặc tên chuẩn và câu hỏi dùng tên gọi khác đã xác minh. Đo tỷ lệ tìm được nguồn chuẩn trước khi chấm đáp án và trích dẫn. [Ghi chú đọc đợt 9 ngày 19/11](review-batches/2026-11-19-day4-round9/reading-notes.md).

## 4. Sinh với bằng chứng và kiểm từ ng ý

[ReClaim(P046)](https://aclanthology.org/2025.findings-naacl.55.pdf) chọn reference trước rồi sinh claim, dùng constrained decoding để reference khớp nguồn cung cấp. Đây là tiền lệ cho evidence-first sentence generation. Nhưng citation membership không bảo đảm entailment. Table 2 còn cho citation support tăng trong khi answer recall giảm ở một số bộ dữ liệu: cùngLlama3-8B, ELI5CAS42,8→89,9 còn claimrecall20,5→17,8. Khả năng trả lời đủ nội dung cần được đọc cùng mức hỗ trợ của phần đã trả lời.

[GuidelineGuard(P030)](https://www.mdpi.com/2079-3197/14/9/210) có Auditor chỉ xem claim và candidate evidence sentence. Trên GG200, gate loại6 commitment đúng và 0 sai so với paired no-auditor draft. Trên PubMedQA, selective accuracy tăng nhưng coverage và operational accuracy giảm(§4.12/Tables12–13). Verifier có thể là selective gate hữu ích trong một số điều kiện; không được mặc định nó cải thiện mọi chất lượng.

[RAGE(P026)](https://aclanthology.org/2024.konvens-main.6.pdf) tối ưu citation selection từ IR relevance labels bằng SFT/PPO. Recall ở đây đếm relevant documents được cite, không phải tỷ lệ output statements được nguồn chứng minh nhưALCE. Gains trên metric này chưa đủ xác nhận claim-level support; chính tác giả nêu citation improvement có thể đi cùng chất lượng khác giảm(§6).

Các nghiên cứu này làm yếu đi tuyên bố “thêm verifier, evidence-first hoặcfine-tuning citation là phương pháp mới”. Chúng còn cho thấy answer completeness, source support và refusal cost phải được đọc cùng nhau.

CRAG (P085) dùng điểm liên quan để quyết định lọc đoạn đã tìm hay tìm thêm. RARR (P078) kiểm và sửa bản nháp theo nguồn, đồng thời đo mức giữ lại ý định ban đầu. Với hồ sơ bảo tàng, có thể so RAG một lượt, tìm thêm trong kho đã duyệt và sửa theo từng dữ kiện. Chấm riêng đoạn mới tìm được, dữ kiện sau sửa, ý đúng bị mất và phản hồi khi nguồn vẫn thiếu. [Ghi chú đọc đợt 13](review-batches/2026-11-19-day4-round13/reading-notes.md).

## 5. Các evaluator và những tên metric dễ nhầm

[ALCE(P084)](https://aclanthology.org/2023.emnlp-main.398.pdf) phân biệt fluency, correctness và citation quality. Citation recall hỏi mỗi output statement có được joint cited evidence hỗ trợ không. Citation precision loại nguồn không liên quan và không bắt mọi citation riêng lẻ chứng minh toàn bộ câu. Đây là nền tảng để tránh loại nhầm trường hợp cần kết hợp nhiều nguồn. NLI vẫn có hạn chế với partial support.

[RAGChecker(P018)](https://papers.nips.cc/paper_files/paper/2024/file/27245589131d17368cccdfa990cbf16e-Paper-Datasets_and_Benchmarks_Track.pdf) tách claims và kiểm với gold answer cùngretrieved context. Faithfulness mặc định xét support ở bất kỳ retrieved chunk nào, chưa kiểm đúng attached source. Neutral và Contradiction bị gộp thànhnon-entailment theo limitation của bài. Human preference validation cũng cóGPT-4critiques hỗ trợ; không nên mô tả thành hoàn toàn unaided claim-level adjudication.

`metric-dictionary6.csv` của đợt trước tách những trùng tên quan trọng: CAS củaReClaim làCorrect Attribution Score, còn CAS của [Attribution Bias(P032)](https://aclanthology.org/2025.findings-acl.1087.pdf) làCounterfactually-estimated Attribution Sensitivity. “Recall” có thể dùng mẫu số làgold answers, output statements hoặcrelevant documents. “Faithfulness” có thể chỉsource entailment hoặcđòi hỏi causal influence. Một bảng so sánh phải ghi đơn vị, mẫu số và gold/judge trước khi đặt các score cạnh nhau.

FActScore đo tỷ lệ ý được kho tham chiếu hỗ trợ trên các lượt có trả lời. Attributed QA kiểm toàn bộ đáp án ngắn với đoạn được dẫn. Với dữ liệu bảo tàng, cần đọc song song mức hỗ trợ của từng ý, độ bao phủ những phần được hỏi và cách hệ thống xử lý khi nguồn bất đồng. [Ghi chú đọc đợt 2 ngày 19/11](review-batches/2026-11-19-day4-round2/reading-notes.md).

RefChecker phân biệt ý được nguồn hỗ trợ, ý bị nguồn bác bỏ và ý chưa đủ căn cứ. RAGTruth đánh dấu vị trí lỗi trong đầu ra và phân biệt mâu thuẫn với thông tin thêm thiếu căn cứ. Cả hai là tiền lệ cho kiểm đáp án chi tiết. Đánh giá câu hỏi bảo tàng còn cần đo phần được hỏi nhưng bị bỏ sót và ghi rõ khi các nguồn bất đồng với nhau. [Ghi chú đọc đợt 5 ngày 19/11](review-batches/2026-11-19-day4-round5/reading-notes.md).

ARES (P069) tách mức liên quan của ngữ cảnh, mức câu trả lời được ngữ cảnh hỗ trợ và mức đúng trọng tâm. Bài dùng nhãn người để hiệu chỉnh ước lượng điểm tổng hợp của bộ chấm tự động. Với RAG bảo tàng tiếng Việt, cần kiểm bộ chấm trên nhãn người trong miền và giữ phép chấm nguồn ở cấp từng dữ kiện. [Ghi chú đọc đợt 12](review-batches/2026-11-19-day4-round12/reading-notes.md).

## 6. Citation hỗ trợ được claim chưa chứng minh model đã dùng nguồn

[Correctness is not Faithfulness(P044)](https://mariaheuss.com/assets/correctness.pdf) phân biệt source support và causal dependence. Phép chèn span và o tài liệu khác cho thấy một vulnerability, nhưng con số57% là273/476 matched-span cases ở một điều kiện; không phải tỷ lệ mọi citation củaRAG. Bài thừa nhận một sốadversarial documents có thể trở thành cue và phép probe không quan sát đầy đủ internal process.

[How Do LLMs Cite?(P022)](https://arxiv.org/pdf/2606.28358) can thiệp các tín hiệu tính toán trung gian để nghiên cứu quyết định phát citation củaLlama3.1-8B. “Activation patching” ở đây là thay một phần trạng thái tính toán bằng trạng thái ở lần chạy khác rồi quan sát thay đổi. Kết quả arXiv cho thấy thay đổi citation emission, nhưng không lập được toàn bộ đường truyền tạoanswer và citation.69% suppression là9/13 selected failures. Trên6.808 HotpotQA examples, strict citation rate0,001→0,024; relative gain lớn vẫn đi cùng absolute success thấp(§§4–5).

[Publisher](https://link.springer.com/chapter/10.1007/978-3-032-21324-2_35) xác nhận P022 là conference paperECIR 2026, online 24/03/2026,pp458–473. Fulltext được đọc làarXiv 18 pages, chưa đối chiếu byte/text với chapter 16 pages. Không xếp published family thànhpreprint-only; cũng không gán các numeric results củaread version cho một version chưa kiểm.

[MIRAGE(P047)](https://aclanthology.org/2024.emnlp-main.347.pdf) tìm answer tokens nhạy với context, sau đó tìm context cues ảnh hưởng đến prediction bằng gradient attribution. Có142 calibration/1.144 test examples ởmatched subset, với 5 ngôn ngữ chưa cótiếng Việt. Calibrated variant đạt86,7% human agreement, còn uncalibrated 83,4%;NLI+translation 84,2%(Table 2), với yêu cầu tài nguyên khác nhau. ELI5 dùngNLIproxy vì thiếuhuman attribution gold;Llama2 recall tăng nhưngprecision giảm(Table 3).

Hai hướng internals làprior work cần biết để diễn giải citation claims. Chúng chưa được chọn làm architecture bắt buộc cho dự án bảo tàng. Agreement với human/NLI hoặcđiều khiển được citation token cũng chưa tự tạo chứng nhận causal faithfulness phổ quát.

ContextCite bổ sung cách ước lượng ảnh hưởng của nguồn bằng phép bỏ các tổ hợp câu khỏi ngữ cảnh. FACTUM dự đoán khả năng nguồn trích hỗ trợ câu từ tín hiệu bên trong mô hình. Đối chiếu hai bài giúp tách ảnh hưởng của nguồn lên đầu ra khỏi việc nguồn có chứng minh được câu hay không. Các kết quả và giới hạn về nguồn trùng lặp, chi phí và cảnh báo nhầm nằm trong [ghi chú đợt 4](review-batches/2026-11-18-day3-round4/reading-notes.md).

Cited but Unused (P021, bản arXiv) thay một giá trị trong các đoạn nguồn rồi hỏi lại để đo độ nhạy của câu trả lời. Phép thử bổ sung cho việc kiểm nguồn gốc có hỗ trợ câu trả lời hay không. Khi áp dụng vào pilot, cần ghi cả các ca không xác định và xem lại cách thay giá trị trước khi suy luận về nguồn gốc dữ kiện. [Ghi chú đọc đợt 12](review-batches/2026-11-19-day4-round12/reading-notes.md).

## 7. Mâu thuẫn, ambiguity và metadata

[MADAM-RAG/RAMDocs(P054)](https://arxiv.org/pdf/2504.13079) phân biệt câu hỏi mơ hồ có nhiều đáp án hợp lệ với thông tin sai và noise. Một tên người có thể chỉ nhiều người; câu trả lời có điều kiện hoặcphân biệt entity có thể phù hợp hơn việc tự động từ chối. Debate nhiều vòng cũng không luôn tăngaccuracy theoFig.3.

P032 cho thấy đổi Human/LLM labels có thể đổi lựa chọn citation khi nội dung giữ nguyên. Đây làmetadata sensitivity trong cấu hình thử, không phải bằng chứng tên bảo tàng hoặcnhãn “nguồn chính thức” sẽ có cùng hiệu ứng. Không suy ra nên loại bỏ thông tin provenance có thật.

AmbigDocs kiểm trường hợp nhiều thực thể trùng tên và xem đáp án có đi với đúng thực thể không. ConflictBank kiểm riêng thông tin sai, khác biệt thời gian và khác biệt ngữ nghĩa. Khi đối chiếu tài liệu bảo tàng, cần xác định hiện vật, thuộc tính và mốc thời gian trước khi chấm hai nguồn là bất đồng. [Ghi chú đọc đợt 6 ngày 19/11](review-batches/2026-11-19-day4-round6/reading-notes.md).

SituatedQA đánh giá đáp án ở đúng mốc được hỏi. TempReason tách bài toán tìm dữ kiện khỏi việc chọn trạng thái đúng mốc trong các cấu hình thí nghiệm. Với hồ sơ bảo tàng, có thể tạo cặp câu hỏi về cùng hiện vật và thuộc tính, chỉ đổi năm, rồi chấm riêng đáp án đúng mốc, đoạn nguồn hỗ trợ mốc và phản hồi khi thiếu căn cứ. Cần phân biệt mốc trong câu hỏi, thời gian hiệu lực của dữ kiện và ngày công bố hoặc cập nhật tài liệu. [Ghi chú đọc đợt 7 ngày 19/11](review-batches/2026-11-19-day4-round7/reading-notes.md).

AmbigQA gán các đáp án vào từng cách hiểu bằng câu hỏi viết lại. ASQA dùng một tập con từ AmbigQA để chấm câu trả lời dài có bao phủ được từng cách hiểu hay không. Với RAG bảo tàng, mỗi cách hiểu cần mã hiện vật và đoạn nguồn riêng. Khi hồ sơ phân biệt được hai hiện vật, có thể thử nêu cả hai khả năng hoặc hỏi khách một chi tiết phân biệt. Khi hiện vật đã rõ nhưng nguồn thiếu dữ kiện, câu trả lời cần nêu phần thiếu. Chấm riêng đáp án, đoạn trích và khả năng phân biệt của câu hỏi làm rõ. [Ghi chú đọc đợt 10 ngày 19/11](review-batches/2026-11-19-day4-round10/reading-notes.md).

DRAGged into Conflicts (P049) chấm riêng việc phản hồi phù hợp với loại bất đồng, độ bao phủ đáp án và tính nhất quán với nguồn. When Evidence Conflicts (P053) dùng cùng hai đoạn theo hai thứ tự và thấy mô hình có thể đổi đáp án. Với hồ sơ bảo tàng, nên gán nhãn hành vi phù hợp trước, rồi đảo thứ tự và đo riêng lỗi đổi dữ kiện hoặc đổi cách phản hồi. Với bất đồng chưa phân xử được, chấm việc nêu từng cách diễn giải và dẫn đúng nguồn tương ứng. [Ghi chú đọc đợt 14](review-batches/2026-11-19-day4-round14/reading-notes.md).

## 8. Định hướng và novelty sau review

| Ý tưởng đã bàn | Prior work trực tiếp | Vị trí hiện tại |
|---|---|---|
| QA di sản tiếng Việt, cóchuyên gia/nhiều nguồn | ViCH-QA | Đã có tiền lệ; size/domain alone không đủ |
| Summary-augmented retrieval | SACR | Candidate comparator; chưa reproduce |
| Sufficiency và confidence gate | Sufficient Context,RINSE | Không mới nếu chỉghépblock |
| Claim verifier/evidence-first generation | GuidelineGuard,ReClaim | Cótrade-off; chưa chọn thànhmethod |
| Citation-support metrics | ALCE,RAGChecker,RAGE | Cần chuẩn hóa định nghĩa,không đặt score cùng tên cạnh nhau |
| Counterfactual/internal citation attribution | P044,P022,MIRAGE | Đã có tiền lệ; còn nearest work phải đọc |

Khả năng đóng góp dữ liệu/đánh giá cần tiếp tục kiểm ở những đơn vị bằng chứng và tình huống màbenchmark hiện có chưa đáp ứng: chẳng hạn support của từ ng ý, câu thiếu căn cứ, bằng chứng bất đồng hoặcgánh nặng từ chối nhầm. Đây làcác giả thuyết còn mở, không phải xác nhận bộhiện có đều thiếu nhãn.

Mục tiêu hai paper có thể giữ như định hướng: một đóng góp dữ liệu/đánh giá có giá trị độc lập, và một đóng góp phương pháp được chọn sau khi có căn cứ vềlỗi cụ thể. Hiện chưa có đủ bằng chứng đểcam kết cảhai, chốt architecture, hoặcđặt KG thànhpaper 2. Thêm một block cósẵn hoặcđổi ngôn ngữ không tự chứng minh novelty.

## 9. Những việc ngăn kết luận “literature đã hoàn tất”

1. Chưa hoàn tất search coverage theo protocol/primary sources và screening adjudication cho catalog 101. Không có formal search saturation hoặcPRISMA counts được xác nhận.
2. ContextCite và FACTUM đã được đọc có trọng điểm ở đợt 4. Hai đầu mối vẫn được theo dõi riêng trong khi chờ quyết định vòng toàn văn theo protocol. [Ghi chú đọc và vị trí trong nguồn](review-batches/2026-11-18-day3-round4/reading-notes.md).
3. Cần căn chỉnh P022 read version với published chapter; review vẫn phân biệt publication evidence và version-specific results.
4. ViCH candidate còn manual gate và exact-release/count/schema uncertainty. Chưa raw-row audit, chưa kết luận nhãn nào không tồn tại.
5. Extraction và eligibility chưa được người thứhai kiểm độc lập; không gọi AI-assisted reading làindependent reviewer.

Bản v1 đã nối bằng chứng thành một lập luận nghiên cứu. Nó chưa chốt gap, quy môdataset, targetvenue hoặcdeployment. Các kết quả số làtác giảbáo cáo; không cómodel experiment của dự án trong lầncập nhật này.

## Hồ sơ đi kèm

Đợt hiện tại có`reading-extraction3.csv`,`evidence-ledger20.csv`,`cross-paper-matrix14.csv`,`domain-evidence9.csv`,`publication-evidence-delta.csv`,`unreviewed-leads2.csv` và source/progress/validation metadata tại`review-batches/2026-11-18-day3-round3/`. Các ledger cũ được giữ nguyên đểtruy vết. Raw PDFs/text nằm trongarchive dữ liệu, không được đưa và o public Git.
