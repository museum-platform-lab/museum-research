# Trọng tâm nghiên cứu hiện tại — cập nhật18/11/2026

**TEXT-FIRST, EVIDENCE-GROUNDED RAG CHO QA BẢO TÀNG.** Đây là điều chỉnh theo chỉ dẫn mới nhất của người dùng sau khi nhánh KG được mở rộng quá sớm.

- Paper1 dự kiến: benchmark và phân tích retrieval, source support/citations, answerability/abstention trên museum QA. Chưa xác nhận novelty hoặc chốt dataset size.
- Paper2 dự kiến: phương pháp cải thiện RAG được chọn từ lỗi baseline, chưa chốt architecture. Claim verifier hoặc sufficiency gate riêng lẻ không mặc nhiên mới.
- BM25/dense/hybrid, SACR, source verification và selective answering là trọng tâm hiện tại. KG/GraphRAG giữ comparator/future extension; không phải deployment được chốt, không có graph experiment bắt buộc trong core plan.

V0.1 ledger63/30/8 giữ để truy vết. V0.2 KG trial70/11/12/8 là hồ sơ thử scope lịch sử, **không phải active selection/experiment plan** sau steering này. Không dùng70 như số RAG papers included. Các graph papers vẫn cần cite nếu gần contribution, không bị xóa hoặc relabel ngoài phạm vi chỉ do đổi ưu tiên.

**Ưu tiên công việc ngay lúc này: tiếp tục literature review — đọc toàn văn có phạm vi rõ, trích bằng chứng kèm section/table/page, đối chiếu nearest work và tổng hợp phản biện. Literature chưa hoàn tất; chưa chuyển sang tạo benchmark, xây corpus thí nghiệm hoặc chạy mô hình.** Đây là điều chỉnh theo nhắc lại của người dùng “literature chưa xong mà?” / “không đọc tiếp hả”.

Active reading view: `review-batches/2026-11-17-rag-focus/rag_priority_view101.csv`. Bản tổng quan liền mạch hiện tại: `LITERATURE_REVIEW_DRAFT.md` (v1), tổng hợp14 paper IDs trong chuỗi extraction chuẩn hóa; chưa phải systematic review hoàn tất hoặc formal included set. Đợt mới nhất: `review-batches/2026-11-18-day3-round3/`, gồm P022/P047/P008,20 ghi chú có locator và9 đối chiếu dữ liệu ViCH/SACR. P022 có published ECIR2026 family nhưng numeric read-version alignment còn mở. ContextCite vàFACTUM là2 leads mới chưa đọc toàn văn, chưa merge vào catalog101. Các đợt cũ vàv0.1 ledger được giữ nguyên.

`review-batches/2026-11-17-rag-focus/evaluation-design.md` và các experiment matrices chỉ là draft tham khảo, không phải bước thực hiện ưu tiên hiện tại. Chưa khóa protocol/search, eligibility, human validation, novelty hay chạy inference.
