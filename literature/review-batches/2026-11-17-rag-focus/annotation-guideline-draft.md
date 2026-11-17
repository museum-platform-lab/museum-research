# Annotation draft cho evidence-grounded museum RAG

Mỗi question có ID, source snapshot, required facts, alternative sufficient evidence sets và corpus-answerability(ANSWERABLE/UNANSWERABLE/AMBIGUOUS/UNKNOWN). Mỗi returned-context condition có sufficiency riêng(FULL/PARTIAL/NONE/CONFLICT/UNKNOWN) và action được phép(FULL_ANSWER/PARTIAL_WITH_CAVEAT/QUALIFIED_ANSWER/CLARIFY/ABSTAIN). Không bắt tất cả conflict dùng cùng action nếu evidence authority/time khác nhau.

Mỗi answer claim lưu text, original-source span IDs/offsets và labels ENTAILED/CONTRADICTED/NOT_SUPPORTED/UNCERTAIN; answer correctness và source support chấm riêng. Claim đúng theo external knowledge nhưng không có trong permitted sources vẫn unsupported theo source-constrained task. Evidence citation ở document-level chưa thay gold span. Summary-derived assertions phải trace về original, không tự là primary evidence.

Human annotators làm độc lập trước adjudication; lưu hai nhãn, guideline version và resolution. Agent có thể đề xuất claim split/labels nhưng không ghi như người đã xác nhận. Pilot2–3 papers/extraction và course crosschecks vẫn áp dụng khi làm formal literature review; benchmark annotation cần kế hoạch riêng phù hợp sample. Chưa có human labels/IAA trong đợt này.

Ví dụ giả định, không là gold record: hỏi năm công nhận+địa phương mà context chỉ có năm → PARTIAL, chỉ trả phần có support nếu policy cho phép và nêu thiếu địa phương. Hai mốc năm của cùng tên lễ hội ở hai tỉnh khác nhau có thể là facts tương thích; phải normalize entity/location trước labelCONFLICT. Hai diễn giải curatorial có nguồn khác nhau có thể cần qualified answer, không tự coi một bên sai.
