# Trọng tâm nghiên cứu hiện tại — cập nhật17/11/2026

**TEXT-FIRST, EVIDENCE-GROUNDED RAG CHO QA BẢO TÀNG.** Đây là điều chỉnh theo chỉ dẫn mới nhất của người dùng sau khi nhánh KG được mở rộng quá sớm.

- Paper1 dự kiến: benchmark và phân tích retrieval, source support/citations, answerability/abstention trên museum QA. Chưa xác nhận novelty hoặc chốt dataset size.
- Paper2 dự kiến: phương pháp cải thiện RAG được chọn từ lỗi baseline, chưa chốt architecture. Claim verifier hoặc sufficiency gate riêng lẻ không mặc nhiên mới.
- BM25/dense/hybrid, SACR, source verification và selective answering là trọng tâm hiện tại. KG/GraphRAG giữ comparator/future extension; không phải deployment được chốt, không có graph experiment bắt buộc trong core plan.

V0.1 ledger63/30/8 giữ để truy vết. V0.2 KG trial70/11/12/8 là hồ sơ thử scope lịch sử, **không phải active selection/experiment plan** sau steering này. Không dùng70 như số RAG papers included. Các graph papers vẫn cần cite nếu gần contribution, không bị xóa hoặc relabel ngoài phạm vi chỉ do đổi ưu tiên.

Active reading view: `review-batches/2026-11-17-rag-focus/rag_priority_view101.csv`. Active experiment draft: cùng thư mục, `evaluation-design.md`. Đây là planning/scoping, chưa khóa protocol, formal included, human validation hoặc chạy inference.
