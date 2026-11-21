# Ngày2 đợt2 — phục hồi abstract và đọc có trọng tâm

Ngày17/11/2026 Asia/Saigon. Đây là scoping/targeted reading; chưa formal database search, independent human review, full extraction toàn101 hoặc xác nhận novelty. Không ghi đè nhãn/snapshot đợt trước. Candidate KG Paper2 vẫn mở.

## Kết quả xử lý nhóm thiếu

Tổng13 record thiếu abstract từ đợt1 (12 trong77 mới và MuseumQA từ pilot). Phục hồi8 nguồn đủ xem relevance: P003,P017,P026,P034,P041,P048,P072,N002. Sáu record chuyển union UNSURE→INCLUDE V1 để đọc tiếp; GFM-RAG giữ UNSURE do scope KG và P048 giữ UNSURE/background review. Còn5 record thiếu nguồn đủ tin cậy: P033,P043,P052,P055,P090. Publisher search snippet không được giả làm abstract hoàn chỉnh; HTTP200/redirect cũng không tự chứng minh có full-text.

Ledger mới101:63 đọc tiếp,30 UNSURE,8 ngoài phạm vi sơ bộ. Tất cả vẫn chưa human-validated/formal included. Việc có abstract/PDF không tự xác nhận IC-T/IC-E/pages. Trong30 UNSURE có5 missing, còn lại cần scope/boundary hoặc full-text; không khẳng định đã giải quyết mọi bất đồng.

## Tác động của đọc sâu

Đã đọc có trọng tâm4 bài: CultureBot, HeriKGQA, RAG-RewardBench, ALCE. Dossier có task/data/intervention/metric/result/limits và locator; không tuyên bố đã kiểm toàn bộ appendix, code, source data hoặc tái lập số liệu. Các con số là tác giả báo cáo.

- CultureBot trực tiếp đối chiếu graph-guided/no-graph trên cultural collection. Expert rubric không cùng thang với QA accuracy;55 authored queries khác250 evaluation sessions. Bổ sung KG vào museum assistant đơn thuần chưa đủ novelty.
- HeriKGQA chủ yếu giải quyết sensor identity/time/quantity và tính toán bằng SPARQL/deterministic grounding.99% accuracy không thể dùng làm mục tiêu trực tiếp cho prose/citation QA; cần tách KG benefit khỏi công cụ tính toán và schema exposure.
- RAG-RewardBench đã bao gồm citation/multi-hop/abstention/conflict trong reward-model preference setting; gom các nhãn này lại không tự đủ mới. Cần phân biệt preference ranking với gold support của một assistant answer.
- ALCE đã định nghĩa citation recall/precision với joint support từ nhiều passages và correctness riêng. Đổi tên hoặc áp thẳng metric sang domain khác chưa phải đóng góp metric mới.

## Việc tiếp theo

1. Đọc đủ P017 (benchmark5 cấp bằng chứng) và các công trình sufficiency/conflict gần để kiểm khác biệt benchmark dự kiến; abstract đã phục hồi nhưng chưa full extraction.
2. Xử lý30 UNSURE bằng2 queue riêng: access5 và scope/boundary25. Clarification KG/secondary reviews cần được ghi thành draft amendment trước formal screening, không sửa theo kết quả một cách im lặng.
3. Xây nearest-work matrix cho từng claim đóng góp Paper1/Paper2, ghi cả phần đã giải quyết. Chưa chốt graph architecture hoặc kết luận khoảng trống.

## Nguồn và giới hạn

3 nhóm exact-title lookups (12 queries),1 nhóm lookup bổ sung3 queries và4 primary-page open attempts; chỉ phục hồi record/nguồn đã có. Direct fetch16 sources và1 publisher PDF N002, logs/checksums trong ZIP. ScienceDirect shell/web open403; không vượt paywall hoặc dùng proxy không chính thức. Không liên hệ tác giả, không yêu cầu quyền thay người dùng, không chạy model/API inference. P006 HTML tải được nhưng chưa lập deep dossier trong đợt này. Không thêm candidate mới vào101 từ các lead phụ của websearch.
