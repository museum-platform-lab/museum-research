# Kết quả kiểm tài nguyên và tác động tới kế hoạch

## ViCH-QA: tìm được gì?

Candidate gần khớp nhất: https://huggingface.co/datasets/quockhangdev/vietnamese-cultural-rag-benchmark ; revision metadata `08fb0e375220ffbea018a8a1d7b3a8cffa738aca`.

| Config | Hàng khai báo | Trường khai báo |
| --- | ---: | --- |
| qa_pairs | 4719 | question, answer, type, source: list[string] |
| recursive_chunks | 494 | chunk_id, filename, chunk_idx, text |
| contextual_summaries | 159 | filename, contextual_summary |
| knowledge_graphs | 159 | filename, knowledge_graph: string |
| corpus | 174 | filename, content |

Các config chỉ khai báo split tên train; đây là tên split của kho, chưa chứng minh tác giả huấn luyện bằng chúng hoặc có leakage. Chưa thấy top-level metadata cho gold evidence span/claim support/answerability. Trường graph là chuỗi, có thể chứa cấu trúc bên trong chưa đọc được. Không suy từ một tên config rằng paper đã chạy KG hoặc rằng graph có provenance đúng.

Kho khác `quockhangdev/vietnamese-cultural-qa-benchmark` (revision `be7f079cf7a39d4fa5541becdf8a50f9886d3991`) khai báo 5400 QA và360 conversations, cũng gated. Không dùng kho đó thay thế dataset4719 một cách im lặng. Chưa có license metadata rõ cho hai kho; license của article không tự áp cho dataset.

Raw README và dataset-server của hai kho trả401; public registry metadata đọc được. Để kiểm thực tế, người dùng cần đăng nhập HF và xin quyền ở trang dataset, rồi cung cấp file được phép sử dụng qua cơ chế phù hợp. Không gửi password/token qua chat. Agent chưa gửi yêu cầu hoặc liên hệ tác giả. Không xem việc chưa truy cập được là chứng minh dataset không tồn tại hoặc paper sai.

Các việc còn thiếu trước tái lập: xác nhận đây là release dùng trong paper; giải thích174 corpus rows vs159 documents; kiểm values source và join filenames; kiểm4719 uniqueQA, duplicates, question-type counts, source cardinalities và4940 citations; kiểm gold paragraphs/claims, absent/conflicting evidence labels, annotator metadata; kiểm license và split/calibration. Các kiểm này đều BLOCKED_BY_DATA_ACCESS, chưa được ghi thành pass/fail trên data.

Trong bounded exact-title/code search và trang publisher đã kiểm, chưa tìm được repo chính thức chạy SACR. Điều này không chứng minh không có code ở nơi khác. SACR hiện chỉ là candidate baseline hoặc faithful reimplementation có ghi rõ prompts/chunking/summary budget/deviations, không gọi là đã reproduce.

## Nearest work: phần nào đã có?

- **Sufficient Context**: paper ICLR2025 §6 kết hợp sufficient-context signal với P(True)/P(Correct) bằng logistic regression, threshold để điều chỉnh accuracy–coverage. Tính P(True) trong paper có nhiều lần lấy mẫu; không mặc định một confidence prompt tái lập đúng phương pháp. Repo đã kiểm có README/prompts và ảnh, chưa thấy runnable selective-generation code trong inventory. Nguồn: https://github.com/hljoren/sufficientcontext và https://proceedings.iclr.cc/paper_files/paper/2025/file/33dffa2e3d2ab74a783d1a8c292f66d9-Paper-Conference.pdf .
- **ReClaim**: paper NAACL2025 §3.2–3.5 có NLI-filtered training, reference–claim interleaving và constrained decoding để reference lấy từ câu nguồn. Code train/inference/evaluation có trong https://github.com/pdxthree/ReClaim . Training/data link ngoài repo chưa tải ở đợt này. Sentence citations/evidence-first đơn thuần không mới; prompting approximation phải ghi khác trained ReClaim.
- **RAGChecker**: paper §3 và computation.py đã có claim-level entailment, retrieval claim recall/context precision và response faithfulness. Input schema dùng query/gt_answer/response/retrieved_context[].text. Faithfulness kiểm support từ retrieved context, chưa tự chứng minh mỗi citation đã chọn đúng hoặc source causally used. Hallucination trong code khác toàn bộ unfaithfulness: code phân biệt unsupported-but-GT-supported self_knowledge. Nguồn: https://github.com/amazon-science/RAGChecker . Code mở không đồng nghĩa inference không có chi phí; backend cần cấu hình, chưa chạy.
- **DeclineCraft**: code hiện có ABSTAIN/DENY/ANSWER, CAR strict/lenient, AAR, accuracy và leakage audit. README data URL vẫn là TODO-namespace/DeclineCraft; chưa có download xác minh. README cũng mô tả thay đổi corpus/construction so với paper v13, nên phải pin version và không coi code hiện tại là paper dataset identical. Nguồn: https://github.com/Thakur-Atharva/declinecraft-benchmark .
- **NoMIRACL**: registry gated=false, card và file inventory truy cập được, licenseApache2 khai báo. Relevant/non-relevant passage judgments, dev/test và binary assessment có sẵn; chưa tải/chạy whole dataset. Card nói18 languages nhưng list language tag có16, không cóvi trong list đã xem; không mặc định đây là benchmark tiếng Việt. Metric hallucination rate ở đây là false-positive relevance assessment, không phải tỉ lệ unsupported atomic claims. Nguồn: https://huggingface.co/datasets/miracl/nomiracl và https://github.com/project-miracl/nomiracl .

## Đóng góp dự án nên nhắm tới đâu?

**Paper1 còn là ứng viên:** benchmark Museum QA dựa trên bằng chứng, có provenance tới đoạn/câu, gold support cho claims, nhãn đủ/thiếu/mâu thuẫn bằng chứng và đánh giá human-validated. Có thể dùng cả câu hỏi answerable nhưng retrieved context bị thiếu, tách khỏi câu hỏi không thể trả lời trong toàn corpus. Tiếng Việt hoặc đổi sang hiện vật một mình chưa đủ novelty. Chưa xác nhận benchmark kết hợp này chưa tồn tại trong literature.

**Paper2 chưa khóa:** dùng error analysis để chọn method. Sufficiency-only/claim verifier/abstention gate đã có nearest work, nên cần cơ chế/giả thuyết khác và ablation đáng tin. **Knowledge graph vẫn là hướng mở**, cần chứng minh quan hệ/multi-hop/provenance giúp giải quyết một lỗi cụ thể so với text/SACR và existing KG-QA/GraphRAG. Dataset related có KG làm yêu cầu đối chiếu mạnh hơn, không tự triệt tiêu hướng KG.

## Kế hoạch tiếp theo có thể làm ngay

1. Tiếp tục scoping77 mục chưa vào pilot; ưu tiên KG-QA/GraphRAG nếu mục tiêu Paper2 còn giữ KG. Không gọi follow-up này là đã lọc chúng.
2. Chốt draft annotation schema: corpus answerability, retrieved-context sufficiency và claim support là3 nhãn khác nhau; lưu original source và synthetic summary riêng.
3. Chuẩn bị annotation pilot nhỏ trên corpus đã có quyền và source traceable; chưa tạo gold hoặc nhãn người giả. Cần reviewer độc lập trước quality/IAA claims.
4. Sau access/version checks, thử viability của baseline B0/B1 rồi mới cân nhắc B2/B3/B5. Calibration và finaltest tách biệt. Không chạy API trả phí hoặc dựng đồ thị lớn trong đợt này.

Các nguồn miễn phí/code mở đủ để tiếp tục review; không cần mua quota Elicit. ViCH candidate vẫn cần tác giả duyệt quyền; raw-row audit chưa thể hoàn tất khi chưa có data.
