# Ngày 2 — hoàn tất scoping 77 mục còn lại (17/11/2026)

Đã xem title/abstract khả dụng của đủ77 mục; nhãn là đề xuất AI, chưa người xác nhận, chưa full-text review hoặc formal included. Truy vấn ở đợt này chỉ nhằm phục hồi abstract các record đã có, không phải formal database search mới. Catalogue101 không thêm/xóa paper.

77 mục: {'UNSURE': 30, 'INCLUDE': 42, 'EXCLUDE': 5}. Hợp nhất24pilot+77: {'INCLUDE': 57, 'UNSURE': 36, 'EXCLUDE': 8}. INCLUDE V1 nghĩa đọc tiếp, không phải đã đạt IC-T/IC-E/số trang. Tổng101 là union mỗi work, không cộng số Paper1+Paper2. Có12 mục trong đợt77 chưa lấy được abstract đáng tin cậy; tất cả UNSURE, không tự loại hoặc xem teaser/bibliography là abstract.

Đã thử phục hồi35 abstract thiếu/bibliographic từ URL record/registry,25 trả được abstract trước kiểm teaser. Hai đoạn chỉ là publisher teaser bị hạ lại missing. Các abstract từ audit được giữ provenance, không tuyên bố đều mới fetch hoặc mọi metadata/metric đã xác minh. Không dùng số liệu abstract để kết luận superiority/quality.

Knowledge graph được giữ trong Paper2 chưa chốt: CultureBot(P005), dual-layer heritage KG(P006), HeriKGQA(P009) là đối chiếu domain trực tiếp. HippoRAG(P036), HyperSU(P035), StepChain(P038), query-aware traversal(P039), adaptive-pruning graph(P042), HyperReCo(N012) được giữ KG candidate/UNSURE do S3 v0.1 chưa bao trùm general KG QA. Chưa tự sửa protocol để nhận tất cả graph papers. N007 SCMRAG và P070 claim-level graph verification là giao điểm KG/verification cần đọc; claim graph khác entity KG.

Nhóm benchmark/verification cũng có nearest work cần ưu tiên: RAG-RewardBench(P019), GRAB-RAG(P020), RINSE(P023), RAMDocs/MADAM-RAG(P054), ALCE(P084), RAGTruth(P087), RGB(N004); domain-near Cultural Faithfulness(N003), LongHisDoc(P082), cùng ViCH-QA đã đọc trước. Không thể coi thiếu/misleading/conflict contexts, source support, sentence citations hoặc human adjudication riêng lẻ là novelty đã chứng minh.

Các survey/secondary synthesis giữ UNSURE/background chờ clarification C01. General IR/encoder hoặc QAG ngoài scope vẫn được lưu làm background/resource, không xóa thư viện. Không dùng preprint label hoặc thiếu venue để loại khi chưa kiểm published version.

File: screening77.csv có rationale/next check/nguồn; screening_progress101.csv bảo toàn24 nhãn pilot cũ; missing_abstract_queue.csv và kg_priority_queue.csv là hai hàng chờ đọc. Snapshot discovery/audit/protocol/pilot cũ không thay. Mục tiêu đợt1 ngày2 là làm xong ledger, chưa giải quyết mọi UNSURE. Đợt tiếp: xử lý missing/boundary, đọc nearest work theo hai hướng và đề xuất amendment KG/secondary study trước khóa formal.
