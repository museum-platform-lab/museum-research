# Ngày2 đợt4 — thử scope v0.2, giữ v0.1 bất biến

Ngày17/11/2026 Asia/Saigon. Thực hiện thử streamS4 general KG và role primary/secondary trên các record đã có. Không chốt protocol/RQ, không hồi tố formal search, không human validation hoặc model experiment. Đây là trial relevance/role view, không phải tập included chính thức.

## Kết quả có thể kiểm tra

-7 KG candidates đều đủ liên quan dưới S4 dự thảo để tiếp tục đọc Paper2: HyperSU, HippoRAG, StepChain, Query-Aware Spreading Activation, GFM-RAG, adaptive-pruning DuP-RAG, HyperReCo. Đã đọc các phần method/empirical evaluation liên quan từ PDF/HTML; không tuyên bố full extraction mọi appendix, code hoặc data. Publisher/arXiv versions và formal IC-T/IC-E/pages vẫn cần kiểm riêng.
-8 reviews được gắn BACKGROUND_SECONDARY_PROVISIONAL theo abstract/prior publisher evidence, không mới full-text read cả8 và không kết luận chắc chắn không có original validation. P025/framework cần chú ý component validation.
-5 task boundaries có3 background-provisional (ArtiFact, ARtour, FActScore) và2 pending (ATLAS429; N008 SciFact/task-source chưa rõ). ARtour không đánh giá content accuracy có hệ thống theo main text, nên không lấy UX score làm QA accuracy. ArtiFact có data-management/semantic queries khác QA support target. FActScore vẫn là metric foundation quan trọng.

Trial v0.2 toàn101:70 continue relevance,11 background-provisional,12 pending,8 outside-current-primary.11 background không bị xóa khỏi thư viện hoặc novelty evidence.12 pending gồm5 access-missing(P033/P043/P052/P055/P090),2 task/access(P002/N008),4 language-method(P063/P064/P066/N009),1 tool/benchmark(P075). View v0.1 vẫn63/30/8. Hai hệ status không cộng trộn;70 không phải formal included hoặc70 đều đọc full-text.

## Thứ tự baseline KG nên khảo sát

HippoRAG/PPR và query-aware gate là hai comparator có cơ chế đối chiếu rõ nếu corpus/stack phù hợp; không mặc định Neo4j đang có hoặc các baseline này rẻ nhất trên máy user. Thử matched text baseline trước rồi graph/no-graph và query-gate ablation. StepChain cần kiểm retrieval rounds/LLM budget. HyperSU cần kiểm corpus-driven construction và mapping sources. GFM-RAG/HyperReCo là learned graph/hypergraph references, checkpoint/training/transfer cần budget riêng; không gọi zero-shot transfer là không có chi phí đào tạo. Adaptive pruning cần giữ calibration/tuning tách finaltest.

Không xếp hạng các method bằng số score cross-paper khác dataset/generator/protocol. Không chốt KG thành Paper2 chỉ từ danh sách này. Cần dữ liệu/query lỗi cụ thể và fair evidence/path/provenance evaluation để quyết định.

## Hồ sơ và giới hạn

kg_trial7.csv ghi mechanism/evidence/limits/locator/feasibility. secondary_roles8.csv và task_boundary5.csv ghi rõ read level. v02_trial_view101.csv giữ nguyên nhãn v0.1 và thêm shadow status; v02_pending12.csv là queue tiếp theo. fetch-log.json có11 request,10 thành công vàATLAS429; HTTP200 không thay cho đánh giá full-text/quality. P042 phải lấy div.html-p vì parser p-only bỏ mất prose; text recovery được giữ trong raw bundle. Các số author-reported không được tái lập.

Nguyên liệu raw/documents và script có ở gói Drive, Git chỉ metadata/tổng hợp, không private Drive IDs, raw PDF hoặc gated rows. Đợt tiếp nên xử lý5 language/tool pending bằng targeted full-text và2 task pending theo nguồn hợp pháp, đồng thời đóng gói protocol v0.2 để xác nhận RQ/owner/date/source access trước formal run. Không cần mua Elicit để làm các bước này.
