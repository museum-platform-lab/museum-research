# Day 3, đợt 4 · ContextCite và FACTUM

Ngày 18/11/2026. Đọc các phần phương pháp, đánh giá, kết quả và hạn chế liên quan của hai bài. Cả hai đã được đối chiếu theo tiêu đề và định danh trong catalog 101. Chúng được theo dõi riêng bằng hai ID từ lượt lần theo tài liệu tham khảo. Quyết định nhận chính thức và kiểm chéo Week 6 còn mở.

## ContextCite (L20261118-01)

**Phương pháp.** Giữ cố định câu trả lời đã sinh. Bỏ các tổ hợp câu nguồn khác nhau, tính lại xác suất của đầu ra và dùng hồi quy thưa để ước lượng đóng góp của từng câu nguồn. Phép đo đánh giá ảnh hưởng trong các điều kiện can thiệp cụ thể. Một câu nguồn có thể hỗ trợ về mặt nội dung dù việc bỏ câu ấy ít làm thay đổi xác suất đầu ra. (§§2–3)

**Kết quả.** Bản NeurIPS 2024 so sánh với bỏ từng nguồn, attention, gradient và độ tương đồng ngữ nghĩa trên TyDi QA, HotpotQA và CNN/DailyMail. Figure 4 đánh giá độ giảm log-xác suất khi bỏ các nguồn xếp hạng cao và mức khớp của mô hình xấp xỉ trên các tổ hợp giữ lại. Cấu hình 32 lần can thiệp đạt kết quả mạnh trong các so sánh tác giả báo cáo. Với top-1, bỏ từng nguồn là chuẩn tối ưu theo định nghĩa của phép đo. (§4, Fig. 4, Appendix A.5)

**Giới hạn.** Nguồn trùng lặp có thể làm hỏng giả định tuyến tính. Bỏ một câu có thể đổi nghĩa câu tiếp theo qua đại từ. Ảnh hưởng đi qua các câu sinh trước cũng có thể bị bỏ sót. Tác giả ước tính chi phí quy nguồn khoảng 32 lần chi phí sinh câu trả lời trong cấu hình này. Phần TyDi QA được lọc lấy ví dụ tiếng Anh. (Appendices A.4–A.5, C.4)

Nguồn đọc: [PDF chính thức, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/file/adbea136219b64db96a9941e4249a857-Paper-Conference.pdf). SHA-256: b67c84f1324443ccc645a9c31587510bd7614e83db821f45e1fc8d3fe24d405e.

## FACTUM (L20261118-02)

**Phương pháp.** Dùng bốn nhóm tín hiệu tính toán bên trong mô hình để phân loại một chỉ số citation theo việc tài liệu được trích có hỗ trợ câu hay không. Thử nghiệm trên báo cáo tiếng Anh từ TREC NeuCLIR 2024, với tối đa 15 tài liệu đầu vào đã dịch sang tiếng Anh và một citation mỗi câu theo thiết lập của bài. Dữ liệu gồm 301 citation token cho mô hình 3B và 572 cho mô hình 8B. Các fold được chia theo báo cáo. (§§3–4)

**Kết quả.** Trên Llama-3.1-8B với logistic regression, FACTUM đạt AUC 0,737, precision 0,334 và recall 0,688 cho lớp citation thiếu hỗ trợ. Cấu hình đối chứng ReDeEP mà tác giả tái triển khai đạt lần lượt 0,536, 0,201 và 0,529. Hai người kiểm 100 phán đoán lấy mẫu, với κ trung bình 0,71 giữa người chấm và 0,68 giữa bộ chấm tự động với nhãn người. (§4.3 và §5.1, Table 1)

**Giới hạn.** Precision 0,334 tương ứng với nhiều cảnh báo nhầm trong cấu hình trên. Nhãn chính dựa trên LLM chấm và được kiểm bằng mẫu nhỏ. Thiết lập dùng hai mô hình Llama, một bộ báo cáo và định dạng một nguồn mỗi câu. Kết quả hỗ trợ một phép phát hiện citation thiếu căn cứ trong thiết lập này. Độ tin cậy đối với claim cần nhiều nguồn và khả năng chuyển sang tiếng Việt vẫn cần kiểm.

Các số liệu trích từ [arXiv v4](https://arxiv.org/pdf/2601.05866v4). [Springer xác nhận bản ECIR 2026, tr. 272–288](https://link.springer.com/chapter/10.1007/978-3-032-21289-4_18). Tính tương đương toàn văn giữa hai bản còn chưa xác minh. SHA-256 của bản đọc: d89b763877f8ad59da29e960aaaa74a58374b293e5516026109c0ac53406561b.

## Đối chiếu với đề tài

| Câu hỏi đánh giá | Nghiên cứu gần nhất | Điều cần giữ rõ trong review |
|---|---|---|
| Bỏ nguồn nào khiến xác suất sinh một câu giảm? | ContextCite, MIRAGE và P044 | Can thiệp ngữ cảnh, tín hiệu nội bộ và phép thử chèn tài liệu có phạm vi suy luận khác nhau. |
| Nguồn trích có hỗ trợ câu không? | FACTUM, ALCE và ReClaim | FACTUM học dự đoán nhãn hỗ trợ từ tín hiệu nội bộ. ALCE đo hỗ trợ của cả nhóm nguồn được trích cho câu. |
| Mô hình có phát dấu citation không? | P022 | Tín hiệu chi phối việc phát dấu citation và tín hiệu tạo nội dung câu trả lời cần được kiểm riêng. |

Cả quy nguồn bằng phép bỏ bớt context và phát hiện citation thiếu hỗ trợ bằng tín hiệu nội bộ đã có tiền lệ. Với dữ liệu bảo tàng, câu hỏi còn mở là giá trị đánh giá của nhãn bằng chứng ở cấp từng ý, đặc biệt khi nhiều nguồn phải ghép lại, thiếu căn cứ hoặc bất đồng. Hai bài này cung cấp đối chiếu phương pháp. Việc xác định tính mới của dữ liệu vẫn phụ thuộc vào kiểm nhãn của các bộ gần nhất, bao gồm ViCH-QA.

Hai đầu mối đã chuyển sang trạng thái đọc toàn văn có trọng điểm. Tổng số bài có trong chuỗi đối chiếu chuẩn hóa là 16, gồm 14 bài trong v1 và hai đầu mối của đợt này. Danh sách nhận chính thức Week 6 vẫn chờ quyết định vòng toàn văn và kiểm chéo.
