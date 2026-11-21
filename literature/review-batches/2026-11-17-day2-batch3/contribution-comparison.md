# Contribution stress-test — dự thảo

| Đề xuất dễ nêu | Đã có công trình gần | Điều phải chứng minh thêm |
| --- | --- | --- |
| QA di sản tiếng Việt và lexical/dense/hybrid RAG | ViCH-QA/Vichat | Evidence unit/coverage/task và useful validated labels khác biệt, không chỉ số câu hoặc đổi domain |
| Five evidence conditions và answer/abstain | ESB P017, GRAB-RAG, RGB, RAG-RewardBench | Không chỉ đổi tên states; gold policy và causal/error-analysis question cụ thể |
| Sentence/claim citation support | ALCE, ReClaim, RAGChecker, RAGTruth | Provenance/gold calibration/language validity hoặc method/analysis khác có bằng chứng |
| Cultural QA bằng knowledge graph | CultureBot, dual-layer heritage KG, HeriKGQA; general KG methods | Lỗi relation/provenance cụ thể, fair no-KG ablation, đủ bằng chứng và cost; giữ task sensor vs catalog riêng |
| Pairwise contradiction detector rồi refuse | ESB future-work proposal và conflict/abstention methods | Nearest-method coverage, method novelty hoặc empirical contribution đáng kể, không chỉ implementation proposal |

Lựa chọn nên nghiên cứu tiếp: benchmark kết nối original catalog source spans, alternative evidence sets, answerability theo corpus/context, support của claims và expected actions có điều kiện. Partial answer/clarification/qualified disagreement cần nhãn human cùng guideline. Đây là hướng ứng viên, không phải xác nhận first/novel. Paper2 có thể dùng KG để chọn evidence/provenance tốt hơn nếu error analysis chỉ ra nhu cầu; chưa khóa architecture.

Đầu ra đợt này là stress-test và draft criteria để người nghiên cứu xem được, không phải chốt gap thay người dùng/giảng viên. Không có annotation người thật hoặc thực nghiệm sinh mới.
