# Tài liệu đọc và quyết định

## Tài liệu khởi đầu

Đây là danh sách đọc ban đầu đã kiểm tra nguồn ngày 02/10/2026, không phải literature review đầy đủ.

| Công trình | Đọc để làm gì |
|---|---|
| [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130) | Hiểu graph RAG cho tổng hợp thông tin; đối chiếu loại câu hỏi với bài toán của dự án |
| [RAGAS: Automated Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2309.15217) | Tham khảo đánh giá retrieval và generation |
| [ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems](https://arxiv.org/abs/2311.09476) | Tham khảo đánh giá tự động và cách kiểm chứng bằng nhãn người |

Sau đó tìm thêm nghiên cứu graph retrieval cho multi-hop QA, provenance, abstention và digital humanities. Chỉ chốt novelty sau khi so sánh những công trình gần nhất và phiên bản hiện hành.

## Mẫu ghi một paper

- Tên, link, phiên bản và ngày đọc:
- Câu hỏi và dataset:
- Thuật toán, baseline, ngân sách context:
- Đánh giá và điểm hạn chế:
- Phần có thể tái lập:
- Điểm giống/khác với Art Evidence Graph:
- Hệ quả đối với thiết kế thí nghiệm:

## Quyết định ban đầu

| ID | Quyết định đề xuất | Lý do | Khi nào xem lại |
|---|---|---|---|
| D01 | Văn bản và metadata trước, ảnh tùy chọn | Người dùng đã tạm bỏ việc lưu ảnh | Khi có corpus ảnh hợp lệ và câu hỏi đa phương thức |
| D02 | Chọn chứng cứ bằng graph là hướng chính | Phù hợp kinh nghiệm KG | Sau related work và pilot |
| D03 | PostgreSQL lưu graph nhỏ | Tái sử dụng hạ tầng | Khi truy vấn/hiệu năng cần hệ khác |
| D04 | Không mặc định dữ liệu cũ được phép dùng | Người dùng đã rời dự án trước | Khi xác nhận quyền và nguồn |
| D05 | Benchmark pilot trước mở rộng | Giảm công chú giải trước khi thấy tín hiệu | Cuối tuần 10 |

## Nhật ký tiếp theo

Mỗi quyết định ghi: ngày, vấn đề, lựa chọn, bằng chứng, tác động, điều kiện xem lại. Mỗi phiên bản thí nghiệm ghi những thay đổi khác với run trước. Không xóa kết quả âm để chỉ giữ run tốt nhất.
