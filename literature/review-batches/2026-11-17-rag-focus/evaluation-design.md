# Thiết kế đánh giá RAG — draft, chưa chạy

## 1. Câu hỏi cần trả lời

E1: retriever nào lấy được đủ bằng chứng gốc cho câu hỏi museum? E2: SACR có giúp khi giữ cùng retriever/reranker/budget? E3: với cùng retrieved context và cùng draft response, claim verification và sufficiency/confidence gates thay đổi correctness/support/coverage như thế nào?

Không gộp đánh giá retriever với chính sách response thành một “RAG tốt hơn” duy nhất. Chưa chốt Paper2 là phương pháp nào hoặc xác nhận gap. Core text-first; KG chỉ future comparator nếu lỗi baseline chứng minh cần structured relations.

## 2. Retrieval trước

12 arms trong retrieval_matrix12.csv: BM25/dense/hybridRRF × ORIGINAL/SACR × rerank OFF/ON. Giữ corpus snapshot, original chunk boundaries, segmenter, source IDs và relevance labels. Fix returned top-k, candidate-pool k_before_rerank và tổng generator token budget trên dev; chưa điền số tùy tiện như đã chốt. Reranker chỉ reorder/truncate cùng candidate pool trong cặp tương ứng; hybrid fusion weights/k_RRF pin rõ. Dense checkpoint/revision và segmenter version pin sau feasibility check, không mặc định model mới nhất hoặc lớn nhất tốt nhất.

SACR: một summary/document, lưu original/summary riêng, prompt/model/length/seed/version, index augmented chunks với stable original IDs. Không thay gold source spans thành summary. So cả fixed generator-token budget và số context units thực sự fit; top-k bằng nhau chưa đủ fairness khi summary làm context dài hơn. Summary generation không được đọc QA/gold answer. Đo riêng offline calls/tokens/time/index storage và online latency; ít LLM calls chưa tự bằng giảm cùng tỷ lệ chi phí.

Metrics: document Hit/Recall/MRR/nDCG cho baseline compatibility; gold-span recall và complete-evidence-set coverage để đo thực chất đủ bằng chứng. Chỉ có document labels thì báo document-level và ghi span metric NOT_AVAILABLE, không giả thành chunk-support accuracy. Tính riêng single/multi-source và corpus/context answerability.

## 3. Generation và ablation

G1 BM25 original/noRR; G2 dense original/noRR; G3 hybrid original/noRR; G4 hybrid original/RR; G5 SACR hybrid/RR. Same generator/checkpoint, language, decoding/prompt, context token cap và câu hỏi. G5 là fixed comparison anchor đã chọn vì là nearest SACR configuration, không gọi là winner khi chưa đo; nếu kết quả thua phải báo. Retrieval arms khác vẫn có thể được dùng nghiên cứu sau, không cherry-pick test winner.

Trên G5 dùng 2×4 arms: verifier OFF/ON × gate NONE/CONFIDENCE_ONLY/SUFFICIENCY_ONLY/SUFFICIENCY_PLUS_CONFIDENCE. NONE+OFF chính làG5; tổng unique generator/policy configs là5+8−1=12. Đây là paired diagnostic, dùng cùng draft+context hash mỗi query-condition, không generate draft khác cho mỗi gate rồi quy gain cho gate.

Sufficiency chỉ nhìn question+context trước answer; confidence baseline đọc cùng draft/context, self-report không coi là probability đúng đã hiệu chuẩn. Combined gate fit/calibrate trên dev/calibration riêng rồi freeze trước sealedtest. Nếu reimplement Sufficient Context, ghi rõ khác biệt prompting/confidence method so với paper; không gọi một cosine threshold là sufficiency proof.

Verifier kiểm atomic claims của draft với ORIGINAL source spans và citations, phân biệt entail/contradict/not-supported/uncertain. Stage đầu deterministic removal/retain hoặc fallback policy, không generate repair text mới rồi xem là cùng draft. Nếu dùng rewrite/RARR/ReClaim, đó là arm riêng và chi phí riêng. Retained claims có thể không đủ trả lời, phải kiểm lại required answer slots/completeness theo rubric sau verification; runtime slots chỉ được suy từ question/context, không đọc gold; gold completeness chỉ dùng để chấm; tránh gate cho draft đầy đủ nhưng output cuối thiếu phần quan trọng.

Diagnostic có thể phải generate cả những draft mà pre-generation gate sẽ chặn để paired comparison công bằng. Các calls này vẫn tính actual study compute. Production-call savings từ pre-gate chỉ là counterfactual estimate, phải label rõ, cần confirm bằng online run riêng; chưa báo savings như đo được. Tách generator, confidence, sufficiency, verifier và evaluator costs.

## 4. Evidence conditions và gold actions

Từ câu hỏi có source traceable tạo matched conditions: full support, partial support, irrelevant, empty, conflict. Đây là conditions, không áp một ordinal expected-action cho mọi câu. Corpus-answerability độc lập với sufficiency của returned context; retrieval failure không chứng minh câu hỏi không trả lời được trong corpus.

Partial: ghi required facts nào thiếu, partial answer có được phép và caveat nào cần. Conflict: kiểm cùng entity/time/version/claim trước khi gọi contradiction; có thể gold action là qualified answer, clarify hoặc abstain. Một tài liệu thẩm quyền mới thay bản cũ khác hai nguồn ngang quyền chưa giải quyết. Annotation guideline phải chốt trước đánh giá; không mặc định mọi conflict cần refuse hoặc mọi partial vẫn trả lời đầy đủ.

Negative context cần kiểm semantic leakage, paraphrase, answer equivalence, lexical/position artifacts; giữ query-cluster IDs. Cùng question có nhiều conditions vẫn là một cluster khi split/bootstrap. Shuffle order bằng predetermined seeds, log permutation; không tùy chọn order cho kết quả tốt.

## 5. Generation metrics

- Answer correctness/completeness: human rubric theo required facts; Token-F1 là secondary comparability với ViCH, không là source-support proof.
- Atomic support: supported claims / evaluable emitted claims, và contradiction/unsupported rates riêng. Answer-level unsupported incidence báo riêng, không thay claim denominator. Từ chối không có claims thì support ratio là N/A, không tự chấm100%.
- Citation correctness và coverage: ALCE-style recall/precision, allow joint support; annotate original cited sources. Đúng câu trả lời, đúng citation và causally-used citation khác nhau; không tuyên bố causal faithfulness từ entailment score.
- Selective risk/coverage: full-answer coverage và partial-answer rate riêng; selective correctness và selective correctness+support risk theo denominator rõ; false refusal trên answerable/full-context; false commitment ở contexts không đủ. All-refuse có full-answer coverage0 và selective accuracy N/A, không coi perfect system.
- Báo latency p50/p95, token/call counts và storage nếu đo; threshold comparison ở matched coverage và giữ threshold frozen cho finaltest. Confidence ECE chỉ khi có probabilities/labels phù hợp; ESB-style B-ECE là behavioral-policy mismatch, báo tên đúng.

## 6. Thực thi theo giai đoạn

P0: kiểm corpus/data rights/provenance và manifest, lập annotation pilot nhỏ có người kiểm độc lập. Không lấy synthetic examples làm gold thật. Ở lần kiểm trước dataset ViCH candidate bị gated; chưa có raw rows được phép dùng hoặc xác nhận exact release trong task này.
P1: retrieval-only12 arms trên pilot, kiểm evidence recall/complete coverage và context formatting trước generator calls.
P2:5 plain RAG generation controls với một generator khả thi và fixed budget; chạy sample plan theo pilot/log, không claim powered sample size chưa tính.
P3:paired8 policy arms trên G5; judges calibrate bằng human labels tiếng Việt và freeze policy. Mở rộng model/dataset sau khi pilot cho thấy khả thi.

Chưa chọn checkpoint, top-k, số QA, threshold hoặc budget như các thông số đã duyệt. Không chạy API trả phí tự động. Open-source library miễn phí không đồng nghĩa inference không cần compute. Data acquisition, human validation và compute access là các pending facts phải điền trong manifest.
