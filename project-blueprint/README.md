# Art Evidence Graph — hồ sơ định hướng dự án

Ngày lập: 02/10/2026. Trạng thái: đề xuất để bắt đầu pet project; chưa xác nhận tính mới nghiên cứu.

Mục tiêu: xây một công cụ khám phá nghệ thuật Việt Nam, trả lời câu hỏi kèm nguồn và đường liên hệ giữa tác phẩm, nghệ sĩ, chất liệu và giai đoạn. Dùng sản phẩm làm môi trường thử nghiệm cho nghiên cứu truy xuất chứng cứ bằng đồ thị.

Tên Art Evidence Graph là tên làm việc. Bộ tài liệu lấy hướng này làm giả định từ cuộc trao đổi, có thể điều chỉnh trước khi triển khai.

## Đọc theo thứ tự

| Tệp | Nội dung |
|---|---|
| [01-direction.md](01-direction.md) | Người dùng, giá trị sản phẩm và giới hạn MVP |
| [02-research.md](02-research.md) | Câu hỏi nghiên cứu, giả thuyết và điều kiện viết paper |
| [03-architecture.md](03-architecture.md) | Kiến trúc và cách tái sử dụng hệ thống hiện tại |
| [04-data.md](04-data.md) | Schema, nguồn dữ liệu, chú giải và quyền sử dụng |
| [05-evaluation.md](05-evaluation.md) | Baseline, phân chia dữ liệu và tiêu chí đánh giá |
| [06-roadmap.md](06-roadmap.md) | Lộ trình 12 tuần theo đầu ra và điều kiện hoàn thành |
| [07-backlog.md](07-backlog.md) | Danh sách việc làm có thứ tự ưu tiên |
| [08-reading-and-decisions.md](08-reading-and-decisions.md) | Tài liệu nghiên cứu và nhật ký quyết định |

## Vị trí bộ tài liệu

Bộ này được tạo ở `D:\project\cultural-museum\project-blueprint`, là workspace đang cho phép ghi. Dự án bạn đang chạy nằm ở `D:\project\museum-platform`.

Khi muốn đặt chung với dự án chạy, copy thư mục `project-blueprint` vào `D:\project\museum-platform\docs`. Đây chỉ là tài liệu: chưa di chuyển mã, đổi database hoặc triển khai tính năng.

## Bước đầu tiên

Làm các mục P0 trong backlog: chọn một bộ sưu tập nhỏ, xác nhận nguồn được phép dùng, lập 10 bản ghi có nguồn và 10 câu hỏi để kiểm tra liệu dữ liệu có đủ quan hệ cho graph QA hay không.

Ước lượng 12 tuần giả định làm một mình khoảng 8–12 giờ/tuần. Đây là lịch xây MVP và thí nghiệm ban đầu, không phải cam kết có paper được chấp nhận.
