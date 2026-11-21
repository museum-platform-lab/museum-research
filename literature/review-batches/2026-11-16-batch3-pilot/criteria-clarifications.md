# Clarifications đề xuất sau pilot — chưa sửa protocol v0.1

| ID | Tình huống quan sát | Clarification cần chốt | Ảnh hưởng |
| --- | --- | --- | --- |
| C01 | P010 scoping review có số liệu tổng hợp nhưng không phải primary QA experiment | Nêu rõ empirical set là primary studies hay gồm secondary empirical reviews; BACKGROUND không tự tính included | Giữ UNSURE, không dùng EC-N tự động cho mọi survey |
| C02 | P076 atomic factuality trên biography generation, có retrieval-augmented model | S3 nhận evaluator trên source-grounded generation rộng đến đâu? Giữ citation nền kể cả formal exclude | Không tự mở S3 sau khi thấy FActScore; nhãn hiện tại UNSURE |
| C03 | N008 SciFact fact retrieval và proxy hallucination | Có đáp ứng document QA hay chỉ task adjacent? Nguồn liên quan phải được giữ ngay cả khi formal scope hẹp | Không đồng nhất no-relevant-abstract proxy với unsupported claims |
| C04 | P016 semantic query processing | Quy định natural-language query/query engine khi nào là QA benchmark, cần gold answer/evidence gì | UNSURE, tránh nhận mọi museum dataset |
| C05 | P058 có từ over-refusal nhưng là safety-trigger | EC-O của S3 phải giữ ranh giới nguyên nhân refusal; có thể cite background | Không gom safety refusal với insufficient-evidence abstention |
| C06 | P050 catalogue venue trống nhưng có ICLR2025 proceedings | Venue UNKNOWN khác preprint-only; tìm published version trước FAIL_IC-T | Lưu update riêng, bảo toàn audit snapshot |
| C07 | N001 visitor UX có số liệu nhưng không xác lập QA task | UX/recommendations không đủ IC-P; có thể xét lại nếu full-text cho evidence evaluation | Đề xuất EC-O ở pilot, không phán không có QA tuyệt đối |

Các clarification là đề xuất cần người nghiên cứu xác nhận, chưa có amendment sau khóa vì protocol chưa khóa. Không cần giảng viên duyệt chỉ để chuẩn bị draft; yêu cầu kiểm chéo người thật và xác nhận RQ vẫn chưa được đáp ứng. Dùng pilot này để có ví dụ cụ thể khi thống nhất, không giả định AI suggestions là ground truth.
