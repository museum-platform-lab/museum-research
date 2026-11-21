# Protocol amendment v0.2 — DRAFT, NOT LOCKED

Đây là đề xuất sau scoping, chưa thay protocol v0.1, chưa đăng ký RQ hoặc được xác nhận học thuật. Lý do thay đổi và record bị ảnh hưởng được giữ để không lựa chọn scope im lặng sau khi thấy results. Các nguồn discovery/pilot vẫn không hồi tố thành formal records.

## A01 — General KG cho Paper2

Trước: S2 nhận KG-QA trong heritage; S3 ngoài heritage tập trung verification/sufficiency/attribution/abstention. Vì vậy general GraphRAG chỉ benchmark QA vẫn pending.

Đề xuất thêm S4: source-conditioned multi-hop/document QA với graph/hypergraph tổ chức quan hệ giữa entities, evidence units và original sources; intervention retrieval/path construction/graph grounding có empirical comparison liên quan QA hoặc complete evidence retrieval. Record S4 có thể phục vụ method Paper2 và background benchmark Paper1, không tự là primary domain Paper1. EC-O bổ sung pure node classification/link prediction hoặc recommender không QA; global QFS-only không có evidence-QA target; graph visualization không empirical QA.

Affected: P035/P036/P038/P039/P041/P042/N012. Khi criteria được xác nhận, relevance đề xuất chuyển đọc tiếp Paper2; vẫn phải kiểm IC-L/T/E/Y/pages và published version. Không chỉ chọn paper có kết quả thuận lợi cho KG, không thay đổi historical v0.1 labels.

## A02 — Secondary studies

Đề xuất empirical evidence table chính lấy primary experiments/benchmarks có kết quả và task phù hợp. Secondary review/survey vào BACKGROUND và snowball, không cộng số primary included. Nếu paper review có thí nghiệm validation riêng, chỉ phần đó được xét theo cùng criteria, đánh dấu evidence independence.

Affected: P010/P024/P025/P028/P029/P031/P048/P067. Chưa tự chuyển8 bài thành EXCLUDE; cần đọc đúng phần empirical nếu có. Vai trò background không có nghĩa bỏ khỏi bibliography hoặc novelty watchlist.

## A03 — Boundary/background

P002: có test harness chưa đủ nếu không có QA experiment. P016: semantic query processing phải có QA/evidence target mới vào stream. P011: visitorUX không thay QA evaluation. P076: atomic factuality metric là nền cần cite dù primary scope hẹp. N008: SciFact retrieval/fact verification không tự thành conversational QA; xét explicit QA adaptation nếu có.

P063/P064/P066/N009: retrieval/language study làm baseline; chỉ primary S3 nếu có intervention/evaluation về evidence support, sufficiency/abstention/attribution theo RQ. P075: tool/library dùng implementation; empirical part xét riêng. Không thêm tiếng Việt như tiêu chí đủ để nhận.

## Gates trước formal

Chốt RQ/PICO và year window, người phụ trách/independent reviewer, native query/export ở≥3 CSDL, lịch formal và lock commit. Mọi thay đổi search blocks/filters ghi amendment và rerun requirement. A01 có thể cần graph/hypergraph/traversal terms ở method stream; chưa chạy formal queries hoặc ghi native syntax như đã kiểm.
