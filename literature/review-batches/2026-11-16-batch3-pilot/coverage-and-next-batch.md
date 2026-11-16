# Coverage từ pilot và đợt tiếp

Đây là quan sát trên mẫu có chủ đích 24 mục, không phải bản đồ đầy đủ của 101 mục hoặc xác nhận research gap. Các dòng dưới là câu hỏi cần kiểm ở full-text/dataset, không phải kết luận paper không có đặc tính đó.

| Nhánh | Đã thấy qua title/abstract | Cần kiểm trước quyết định đóng góp |
| --- | --- | --- |
| Vietnamese heritage text QA | P008 Vichat/ViCH-QA; retrieval và generator baselines đã hiện diện | Gold evidence, provenance, unanswerability/conflict, data license/split/leakage, corpus overlap; hiện vật hay di sản phi vật thể khác nhau ra sao |
| Museum QA và retrieval | P001, P004; P090 mới xác minh identity/title | Nguồn dữ liệu, human labels và metric; P090 cần abstract hợp pháp |
| Multimodal/visual heritage | P012 Amarna, P014 VISCOUNTH, P073 VQArt, P081 VaseVQA | Đừng suy visual/cultural accuracy thành citation faithfulness; paragraph link có đủ cho claim support hay không |
| Structured heritage evidence | P083 CIDOC-CRM QA | Gold graph query/path và cách so structured evidence với prose citations |
| Claim/citation evaluation | P018 RAGChecker, P044 attribution faithfulness, P046 ReClaim, P069 ARES; P076 là boundary | Overlap metric/method; judge reliability tiếng Việt, causal use khác support; tránh chỉ đóng gói verifier có sẵn |
| Sufficiency/conflict/abstention | P050, P049, N011; N008 là boundary | Định nghĩa answerability, conflict response, calibration splits, risk–coverage và refusal errors |

## Ưu tiên đọc full-text sau pilot

1. P008 để khóa đối chiếu gần nhất cho Paper1: không tuyên bố benchmark tiếng Việt đầu tiên. Contribution cần khác biệt có bằng chứng ở annotation/evaluation/task, không chỉ thay domain hoặc số lượng QA.
2. P050, P046, P044, P018, P049 cho Paper2 và nền metric Paper1: lập nearest-work matrix từ protocol, không tuyên bố evidence-first/abstention mới chỉ vì chưa đọc đủ.
3. P004, P012, P083 và bản published P069 để kiểm khả năng tận dụng benchmark/metric. P090 ưu tiên tìm abstract/author copy; một lỗi 403 chưa là EC-A.

## Công việc đợt tiếp đề xuất

- Phần A: mở rộng title/abstract scoping cho 77 mục chưa vào pilot, giữ source và AI/human status riêng; không loại vì missing abstract.
- Phần B: giải quyết 6 UNSURE (P002/P010/P016/P090/P076/N008); đọc đoạn liên quan khi được chuyển sang full-text stage, ghi rõ mức evidence. Không lén đổi tiêu chí sau khi nhìn kết quả.
- Phần C: pilot native queries của 3 DB, kiểm seed recall và export; nguồn không hoạt động có amendment/coverage limitation. Chưa phải web-query đợt 2 rộng tùy tiện.
- Trước formal: xác nhận RQ, IC-Y, deadline, người phụ trách và người kiểm chéo. Ghi commit khóa bản sau pilot; discovery/pilot trước khóa không được hồi tố như formal search.

## Lead phát sinh ngoài mẫu

Trong exact-title lookup MuseumQA có lead CArtBench (arXiv 2604.11632) từ kết quả web; chưa mở/đánh giá paper, chưa thêm catalogue hoặc đếm là candidate formal. Nếu theo đuổi cần xác minh metadata và hợp lệ đường ingest. Không tăng 101 từ một web hit chưa kiểm.
