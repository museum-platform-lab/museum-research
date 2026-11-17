# Scope correction theo người dùng —17/11/2026

Trigger: người dùng hỏi vì sao không tập trungRAG và yêu cầu tiếp bước đối chiếu baseline BM25/dense/hybrid,SACR,verification,abstention. Quyết định hiện tại: text-first evidence-grounded RAG là core; KG/GraphRAG về comparator hoặc mở rộng tương lai. Không khóa KG thành Paper2, cũng không khóa Paper2 thành một verifier cụ thể khi chưa có error analysis.

Affected records: graph-specific architectural comparators P005/P006/P009/P035/P036/P038/P039/P041/P042/P083/P086/N007/N012 được gắn reading roleBACKGROUND trong active priority view. P070 claim-graph verifier vẫn có thể thuộc core RAG-verification literature vì graph unit là claims, không đồng nhất mọi paper có graph với triển khai heritage KG. Đây là prioritization, không đổi inclusion evidence hoặc xóa nearest work.

S4/v0.2 trial ở batch3–4 được giữ bất biến như scoping history và không là active deployment plan. V0.1 labels63/30/8 không đổi. Không lấy70 trial relevance làm formal included hoặc tập core RAG mới. literature/CURRENT_FOCUS.md là chỉ dẫn phạm vi hiện hành để agent sau đọc trước các draft cũ.

Không có formal searches, inclusion adjudication, model runs hoặc claim novelty mới trong đợt này. Existing literature-review readiness(nguồn/RQ/reviewer/lock) còn cần xử lý, tách khỏi experimental-design readiness(corpus/gold/compute).
