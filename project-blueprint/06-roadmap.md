# Lộ trình 12 tuần

Ước lượng cho một người làm 8–12 giờ/tuần; điều chỉnh theo thời gian chú giải và chất lượng nguồn. Hoàn thành theo đầu ra, không chạy theo mốc nếu dữ liệu chưa đạt.

| Tuần | Công việc | Đầu ra và điều kiện hoàn thành |
|---|---|---|
| 1 | Chốt phạm vi, quyền dùng, đọc related work | 10 hồ sơ có nguồn, 10 câu hỏi; biết điểm phương pháp cần khảo sát |
| 2 | Schema và quy tắc chú giải | 30–50 hồ sơ, graph nhỏ có evidence; mỗi quan hệ có passage |
| 3 | Đưa corpus vào database mới | Search/detail đọc corpus mới, không lẫn dữ liệu cũ |
| 4 | Baseline vector RAG và log | Trả lời có citation; chạy lại một batch câu hỏi được |
| 5 | Entity linking và graph retrieval | Chuỗi quan hệ tái hiện được; lỗi liên kết được ghi |
| 6 | Xếp hạng chứng cứ và từ chối | Threshold chỉnh trên dev, so pilot với baseline |
| 7 | Hiển thị nguồn và đường graph | Người dùng kiểm tra được evidence của từng claim |
| 8 | Làm sạch benchmark, freeze protocol | 60–100 câu pilot có nhãn; split và rubric được khóa |
| 9 | Baseline và ablation | Kết quả cùng điều kiện, không dùng test để sửa |
| 10 | Review người, phân tích lỗi và bất định | Bảng kết quả có khoảng tin cậy, ví dụ thành công/thất bại |
| 11 | Quyết định mở rộng nghiên cứu | Có/không có tín hiệu; lập kế hoạch corpus/nhãn bổ sung |
| 12 | Demo và báo cáo kỹ thuật | README chạy được, demo, report, outline paper nếu đủ căn cứ |

## Các điểm quyết định

Cuối tuần 2: nếu corpus thiếu quan hệ, thu hẹp câu hỏi hoặc đổi bộ sưu tập. Cuối tuần 6: nếu baseline đã trả lời đủ bằng một passage, bổ sung câu hỏi nhiều bước hợp lệ; không tạo câu khó giả để ưu ái graph.

Cuối tuần 10: nếu phương pháp không cải thiện, phân tích nguyên nhân và báo kết quả trung thực. Có thể hoàn thành pet project tốt dù chưa có đóng góp phù hợp cho full paper.

## Chuyển đổi an toàn

Trước đổi mã: sao lưu phiên bản chạy và database, ghi nơi nào là bản đang dùng. Tạo database riêng cho pet project. Đổi schema/API bằng từng bước nhỏ; giữ một demo cũ để đối chiếu khi cần. Chỉ tạo repository mới sau khi làm rõ quyền sử dụng mã/dữ liệu.
