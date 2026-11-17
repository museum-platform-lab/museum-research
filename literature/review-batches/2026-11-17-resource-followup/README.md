# Resource follow-up — 17/11/2026 (Asia/Saigon)

Tiếp bước người dùng yêu cầu: tìm dataset/code ViCH-QA, kiểm schema và đối chiếu nearest work. Đây là follow-up tài nguyên và đọc các phần liên quan, không phải broad formal search, formal included, full reproduction hoặc hoàn thành lọc 77 mục còn lại. Catalogue 101 giữ nguyên. User-facing date theo Asia/Saigon; access-log giữ UTC thực tế.

Kết quả quan trọng:

1. Tìm được ứng viên rất gần ViCH-QA: `quockhangdev/vietnamese-cultural-rag-benchmark`, metadata có 4719 QA, 494 chunks, 159 summaries, 159 knowledge_graphs. Người sở hữu có tên trùng đồng tác giả và dấu vết VICH collection; chưa có xác nhận trực tiếp release/commit trùng paper. Corpus metadata có 174 hàng, khác 159 tài liệu trong PDF, cần giải thích trước tái lập.
2. Hai repo HF QA/RAG đều gated=manual; metadata API đọc được nhưng raw README và dataset-server trả401. Không đọc được data rows, không vượt gate, không gửi yêu cầu truy cập hoặc email thay người dùng. Chưa xác minh nguồn của từng QA, join filename, gold span, nội dung graph hay chất lượng nhãn.
3. QA config của RAG candidate chỉ khai báo question/answer/type/source(list[string]); không khai báo trường claim span/sufficiency/abstention ở top-level schema. Đây là quan sát metadata, không khẳng định mọi nội dung/annotation không có trong dữ liệu bị gated.
4. KG cần được giữ mở nhưng không coi là miền trống: PDF Vichat không có thực nghiệm KG; tài nguyên liên quan đã liệt kê KG. Chưa biết representation/triples/provenance hoặc hệ thống có dùng KG hay không.
5. Sufficient Context/ReClaim/RAGChecker đã bao phủ lần lượt sufficiency-selective generation, sentence attribution, atomic claim evaluation. Các khái niệm này riêng lẻ không đủ novelty. DeclineCraft và NoMIRACL bổ sung đối chiếu abstention/relevance với hạn chế tài nguyên riêng.

Đọc `findings-and-next-actions.md` để thấy các việc còn làm; `vich_resources_schema.csv`, `nearest_work_matrix.csv` và `baseline_candidates.csv` là deliverable chính. `annotation-schema-draft.json` là schema mới đề xuất cho dự án, không phải schema đã thấy trong ViCH-QA. Không có inference/training hoặc paid API call nào được chạy.

Git chỉ lưu tổng hợp/metadata/schema đề xuất; raw papers/docs/metadata liên quan ở gói làm việc Drive. Không đưa tài liệu Drive riêng tư, token, PDF hoặc dữ liệu gated vào public repo. Mọi snapshot trước giữ nguyên; không đổi prototype KG thành hướng đã chốt.
