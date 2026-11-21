# Ngày2 — điều chỉnh về trọng tâm RAG

Hoàn tất đối chiếu các RAG baseline và thiết kế đánh giá theo chỉ dẫn mới nhất của người dùng. KG/GraphRAG được chuyển về comparator/future extension trong priority view, không đổi historical relevance labels. Không cần thêm paper KG để triển khai core plan hiện tại.

Đầu ra: baseline_evidence_matrix.csv; retrieval_matrix12.csv; generation_controls5.csv; policy_ablation8.csv; evaluation-design.md; annotation-guideline-draft.md; experiment-manifest.json; rag_priority_view101.csv. `CURRENT_FOCUS.md` là bản sao ghi nhận scope, bản Git ở literature/CURRENT_FOCUS.md là điểm vào cho agent về sau.

Thiết kế có12 retrieval-only configurations (3 retrievers×2 representations×2 rerank states). Generation:5 plain RAG controls và8 policy arms dùng G5, trong đó1 arm chính làG5 →12 unique configurations, không phải13 hoặc12×8. Triển khai từng giai đoạn, không chạy toàn grid theo mọi model ngay. Mọi trạng thái NOT_RUN; corpus/checkpoint/budget/annotation pilot chưa có xác nhận thực tế.

V0.1 counts63/30/8 giữ nguyên. Reading priority view mới không phải formal screening. Draft KG stream/v0.2 trial trước được giữ lịch sử; không âm thầm coi streamKG là trọng tâm Paper2 nữa. Không có paid API calls, gold labels hoặc metrics kết quả được tạo.
