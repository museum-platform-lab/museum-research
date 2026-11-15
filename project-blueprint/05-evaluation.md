# Kế hoạch đánh giá

## Baseline

| Mã | Hệ thống | Mục đích |
|---|---|---|
| B0 | LLM không retrieval | Đo mức phụ thuộc tri thức có sẵn; không so citation |
| B1 | Vector RAG | Baseline chính |
| B2 | Hybrid từ khóa + vector | Kiểm tra lợi ích graph ngoài retrieval mạnh hơn |
| B3 | Graph retrieval theo đường ngắn, không xếp hạng chứng cứ | Tách lợi ích cấu trúc khỏi ranking |
| P | Vector + graph + chọn chứng cứ + từ chối | Phương pháp ứng viên |

Cùng corpus, generator, prompt sinh, giới hạn token và chính sách chi phí. Tách experiment kiểm soát bằng graph chú giải thủ công khỏi experiment end-to-end có graph tự trích xuất.

## Chỉ số

- Độ đúng của claim: kiểm tra theo nhãn chuẩn và nguồn.
- Citation precision: claim có citation được passage đó hỗ trợ hay không.
- Citation completeness: claim cần chứng cứ được gắn nguồn đủ hay không.
- Evidence recall: tìm được bao nhiêu passage chuẩn; chấp nhận chứng cứ thay thế sau thẩm định.
- Đường graph: cạnh tồn tại, có nguồn, và liên quan tới câu hỏi; đường hợp lệ chưa bảo đảm câu trả lời đúng.
- Từ chối: precision/recall trên câu không trả lời được, cùng độ bao phủ câu trả lời.
- Chi phí: latency, token và chi phí API; ghi môi trường chạy.

Chấm tự động chỉ hỗ trợ sàng lọc. Đánh giá người trên mẫu phân tầng, ẩn tên hệ thống; không dùng duy nhất một LLM judge để kết luận chất lượng.

## Split và kiểm soát rò rỉ

Protocol A: QA trên corpus cố định; chia câu hỏi theo nhóm thực thể/nguồn để giảm câu gần trùng. Protocol B: giữ riêng bộ sưu tập để đo khả năng chuyển phương pháp.

Với retrieval QA, hệ thống được index corpus của bộ sưu tập test lúc suy luận, nhưng không được dùng câu hỏi/đáp án test để chỉnh ranking, prompt hoặc ngưỡng. Đây là đánh giá chuyển bộ sưu tập; không mặc định giống LODO huấn luyện mô hình dự báo. Nếu fine-tune, tài liệu và nhãn test cũng phải tách khỏi dữ liệu fine-tune.

Chỉ chạy leave-one-collection-out khi có ít nhất ba nhóm đủ lớn và thực sự khác nhau. Một corpus nhỏ chỉ cho phép pilot, chưa đủ chứng minh tổng quát hóa.

## Thí nghiệm cần làm

Ablation: bỏ graph, bỏ evidence ranking, bỏ abstention. Thử độ nhạy với số hop và token budget. Phân tích lỗi entity linking, thiếu cạnh, nguồn mâu thuẫn, retrieval hụt và generator thêm claim.

Freeze test trước chạy cuối. Chạy paired comparison trên cùng câu hỏi, báo bootstrap confidence interval, nhóm theo collection khi phù hợp. Báo seed/lần lặp và thay đổi phiên bản model API.

Run record tối thiểu: run_id, commit, dataset_version, split, model_version, prompt_version, seed, context_budget, retrieved_passage_ids, paths, answer, citations, latency, token_usage, scores. Không ghi credentials.
