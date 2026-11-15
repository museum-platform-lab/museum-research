# Kiến trúc và chuyển đổi mã

## Hiện trạng

Theo quá trình tích hợp: frontend Next.js chạy cổng 3000, backend Spring Boot cổng 8080, PostgreSQL cổng 5432. Route `/api/artifacts` ở Next.js chuyển tiếp tới `/artifact`. Danh sách và chi tiết đã hiển thị dữ liệu backend. Ảnh dùng fallback khi lỗi.

Backend workspace hiện có controller hiện vật, tài khoản và chatbot, cùng pgvector. Frontend đang chỉnh ở `D:\project\museum-platform\frontend`; backend chạy ở `D:\project\museum-platform\backend`. Đối chiếu bản đang chạy trước khi thay đổi vì workspace `cultural-museum` là một bản khác.

## Cấu trúc đề xuất khi triển khai

```text
art-evidence-graph/
├── frontend/              # Next.js: khám phá, hồ sơ, câu trả lời và nguồn
├── backend/               # Spring Boot: API, metadata và kiểm tra nguồn
├── research/
│   ├── retrieval/         # Baseline và thuật toán graph
│   ├── evaluation/        # Scoring, bootstrap và phân tích lỗi
│   └── configs/           # Model, prompt, seed, split, ngân sách
├── data/
│   ├── manifests/         # Danh sách nguồn, quyền dùng, hash phiên bản
│   ├── annotations/       # Nhãn thực thể, quan hệ và chứng cứ
│   └── benchmarks/        # Câu hỏi và split
├── experiments/           # Run metadata và kết quả; không lưu khóa API
└── docs/                  # Bộ project-blueprint này
```

Đây là cấu trúc mục tiêu, chưa tạo hoặc chuyển các thư mục ứng dụng. Thư mục research dùng Python khi cần thư viện thí nghiệm; MVP có thể chạy thuật toán trong cùng backend để giảm công vận hành. Chọn sau pilot.

## Tái sử dụng

| Thành phần | Cách sử dụng |
|---|---|
| ArtifactCard, trang search/detail | Đổi nhãn và hiển thị metadata nghệ thuật |
| API trung gian Next.js | Giữ mô hình gọi backend; thêm API tác phẩm và QA |
| PostgreSQL | Lưu tác phẩm, node, cạnh, nguồn và đoạn chứng cứ |
| pgvector | Baseline truy xuất ngữ nghĩa và candidate retrieval |
| Chatbot hiện có | Tách truy xuất, chọn chứng cứ và sinh câu trả lời để đo riêng |
| Dữ liệu bảo tàng cũ | Chỉ dùng sau khi xác nhận quyền; không tự coi là corpus mới |

Graph MVP lưu trong bảng node/edge của PostgreSQL. Chưa cần thêm Neo4j khi chưa chứng minh nhu cầu truy vấn hoặc hiệu năng.

API đề xuất: `GET /artworks`, `GET /artworks/{id}`, `GET /sources/{id}`, `POST /qa`. Phản hồi QA gồm `answer`, `status`, `citations`, `paths`, `runId`. Mỗi citation trỏ tới passage ID; không chỉ một URL chung.

Trước triển khai công khai: kiểm tra quyền admin ở backend, role khi đăng ký và khóa API/JWT từng được ghi trong source. Các điểm này đã được nhận diện ở phiên bản cũ, cần kiểm tra lại bản chạy. Giữ công cụ thí nghiệm nội bộ cho tới khi hoàn tất.
