# Đợt 3 — pilot title/abstract, 16/11/2026

Trạng thái: PILOT_SCOPING, đề xuất của AI theo protocol v0.1 DRAFT, chưa có người xác nhận/kiểm chéo độc lập. Chưa chạy formal database search, chưa tạo formal included hoặc PRISMA. Full-text review/extraction chưa thực hiện; việc tải HTML có nội dung bài để lấy abstract không có nghĩa đã đọc/kiểm full-text.

Chọn có chủ đích 24/101 ứng viên để thử tiêu chí: 12 domain, 9 method/metric và 3 lead phục hồi; không phải mẫu ngẫu nhiên, không ước lượng tỷ lệ liên quan của cả thư viện. 77 mục chưa vào pilot. selection-before-screening.json giữ danh sách và lý do chọn trước khi đọc abstract. Mỗi bản ghi có nhãn riêng cho hai hướng; union chỉ lấy nhãn tiến xa nhất và không cộng trùng.

Kết quả đề xuất V1 của union: **15 INCLUDE để đọc tiếp, 6 UNSURE, 3 EXCLUDE khỏi phạm vi thử**. INCLUDE V1 chỉ là phù hợp sơ bộ, chưa đạt IC-T/IC-E/số trang hoặc được chọn chính thức. Preprint/venue thiếu được giữ kiểm bản published, không tự tính như formal included. Ba mục EXCLUDE vẫn giữ background trong thư viện: COVER (safety-trigger refusal), GraphRAG global QFS, và visitor-UX study.

File chính: pilot_decisions_24.csv có lý do, thông tin thiếu, nguồn và excerpt ≤18 từ; catalogue_progress_101.csv chỉ theo dõi tiến độ pilot; source_evidence_index.csv ghi provenance abstract; coverage-and-next-batch.md nêu điều cần kiểm và kế hoạch tiếp; criteria-clarifications.md nêu các chỗ chưa rõ của protocol. Snapshot discovery/audit/protocol v0.1 không bị ghi đè.

**Phát hiện cần ưu tiên:** Vichat/ViCH-QA (P008) đã có benchmark QA di sản tiếng Việt và đối chiếu lexical/dense/hybrid theo abstract gốc. Không dùng “QA di sản tiếng Việt + RAG” như novelty đã được chứng minh. Sufficient Context (P050) có bản proceedings ICLR 2025; thiếu venue trong catalogue cũ không có nghĩa preprint-only. P090 MuseumQA thiếu abstract gốc sau registry lookup và publisher 403, giữ UNSURE thay vì suy từ mô tả Elicit hoặc gán EC-A.

Các con số, chất lượng và gap từ full-text vẫn chưa kiểm. Không có người reviewer thứ hai nên không báo agreement hoặc coi AI là kiểm chéo. Các đề xuất clarification chưa sửa/khóa protocol. Đợt tiếp nên mở rộng lọc sơ bộ 77 mục còn lại, ưu tiên lấy abstract thiếu và kiểm các công trình gần; chỉ tìm formal sau khi đủ gate trong protocol.

Trong Git chỉ lưu metadata, đề xuất, diễn giải và excerpt ngắn. Raw HTML/registry và abstract đầy đủ dùng để kiểm trong gói làm việc Drive; không đưa toàn bộ bài/PDF vào repo public. Không thêm link/ID Drive riêng tư trong payload Git.
