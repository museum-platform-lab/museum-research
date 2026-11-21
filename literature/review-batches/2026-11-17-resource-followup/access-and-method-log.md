# Phạm vi, nguồn và điều chưa làm

Ngày báo cáo17/11/2026 Asia/Saigon; timestamp raw giữ UTC tại lúc request. Follow-up nối tiếp pilot24, không phải formal database search. Đã đọc toàn PDF Vichat ở lượt trước; lượt này đối chiếu phần methods/evaluation liên quan trong Sufficient Context, ReClaim, RAGChecker và README/code/metadata. Không tuyên bố đã full-text review mọi benchmark trong matrix.

Exact queries đã dùng: ViCH-QA dataset/github; Vichat SACR github; Ground Every Sentence ReClaim github; Sufficient Context github RAGChecker; quockhangdev VICH github; vietnamese-cultural-qa-benchmark; DeclineCraft github dataset; ViCHat SACR code repository; vietnamese-cultural-rag-benchmark knowledge_graphs; NoMIRACL official dataset. Web chỉ discovery chỉ đường; findings dựa vào registry public, bài gốc và repo official, không dựa search hit count. Không thêm paper formal hoặc dựng flow từ queries này.

HTTP status/logs nằm ở access-log-initial.json và access-log-supplement.json. Metadata HF200; protected README/viewer401. Không dùng cache/proxy để vượt gate. Public code được đọc dưới dạng văn bản, không thực thi script remote hoặc gửi dataset tới judge/API.

File inventory đã quan sát: sufficientcontext main chỉ README+5 images; ReClaim có train/generate/evaluation; RAGChecker có package, examples và benchmark instructions; DeclineCraft có pipeline scripts và annotation tooling. README external data link của ReClaim chưa kiểm download. Không ghi token/auth vào log.

NoMIRACL là resource lead được xác minh website/metadata; chưa thêm catalogue101, chưa formal-screen. Mọi bản ghi cũ giữ nguyên. Data-use permission/license của từng release phải kiểm riêng; không suy article license sang dataset. Raw bundle không có gated data rows và không có model outputs mới.
