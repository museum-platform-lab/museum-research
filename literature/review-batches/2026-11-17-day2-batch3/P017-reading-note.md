# P017 — Evidence Sufficiency Benchmark (ESB)

Nguồn chính: https://www.techscience.com/cmc/v89n1/68467/html ; DOI10.32604/cmc.2026.086343. Main-text review; chưa independent extraction. Dữ liệu dưới đây là tác giả báo cáo, không tái lập.

## 1. Đơn vị dữ liệu và điều kiện

§4.2:200 seed QA (100 SQuAD+100 HotpotQA). Mỗi seed có5 evidence conditions, thành1000 question-condition instances;3 prompt strategies thành3000 prompt-level instances/model. §5.2 thêm1200 L5 randomized-order calls/model;7 models →29400 calls, phép đếm này khớp số tác giả báo cáo.3000 prompt instances không phải3000 câu hỏi độc lập; uncertainty estimation nên xét clustering theo seed khi reusing conditions/prompts.

§3.1 và§4: L1 full support, L2 partial support, L3 irrelevant, L4 no context, L5 conflicting. Bài quy định L1/L2 answerable, L3/L4/L5 phải abstain. Điều này là expected-policy của benchmark, không phải chân lý cho mọi museum query. “Partial” có thể là relevance giảm nhưng vẫn đủ fact, hoặc thiếu một phần đáp án; hai trường hợp cần gold rationale riêng. Nguồn mâu thuẫn có thể phản ánh phiên bản, thời điểm, giả thuyết học thuật hoặc authority khác nhau; assistant bảo tàng có thể cần qualified answer/clarify thay vì blanket refusal. Nếu mở action taxonomy phải định nghĩa gold trước khi chạy.

§4.4: L3/L4 không chứa gold answer string, L5 chứa thông tin liên quan mâu thuẫn với gold. Kiểm string absence không tự chứng minh không thể suy luận đáp án; cần xem perturbation artifact và semantic support. Tables1/2 là ảnh không tải được nên chưa xác minh hết thao tác tạo từng level/prompt từ các ô bảng.

## 2. Metric definitions cần phân biệt

§3.2: over-answer rate tính trên insufficient levels L3–L5; accuracy tính trên answerable L1–L2. Đây là các mẫu số khác nhau; không lấy accuracy làm overall source-faithfulness. §5.2 có Invalid(empty/malformed) nhưng §3 mô tả binary answer/abstain, nên khi tái lập phải kiểm invalid được đưa vào mẫu số thế nào.

§3.1.2 Eq1: B-ECE=sum_l (n_l/N)*|observed_abstain_l-ideal_abstain_l|, ideal bằng0 ở L1/L2 và1 ở L3/L4/L5. Với classification nhị phân và cùng mẫu số, biểu thức này chính là tỷ lệ hành vi trái policy: abstain ở answer-expected hoặc answer ở abstain-expected. Đây là suy ra toán học từ định nghĩa, không phải số empirically reproduced. Không có confidence probabilities/bins nên không đồng nhất với probability ECE, reliability diagram hoặc calibration of p(correct).

§5.2: correctness dùng case-insensitive gold-string match; L5 còn flag known-wrong answer của conflict passage. Điều này có thể bỏ paraphrase/partial answer hoặc tính đúng khi output đồng thời chứa đáp án và claim sai. Muốn claim-level support/citation precision phải có metric khác; ESB policy correctness không tự cung cấp nó.

## 3. Kết quả và giới hạn xác minh

§6.1–6.2 báo cáo L5 over-answer khoảng65–91%; dùng để hiểu failure mode, chưa dùng làm con số baseline của dự án vì chưa có same data/prompt/model run. §7.7/§8: tác giả kiểm200 stratified samples(40/level), agreement89% tổng và75% L5; là internal consistency check, không phải external annotator IAA. Không coi89% là độ chính xác gold labels độc lập hoặc Cohen kappa.

Có chỗ cần làm rõ trước trích số: §6.2 ghi GPT-5.5 wrong-answer39.2%, §7.2 ghi46.3%; đoạn sau chưa chỉ rõ aggregation/condition khác. §6.1 và§7.1 cũng dùng khoảng L5 abstention khác nhau; §7.6 mô tả L4 có irrelevant context trong khi định nghĩa L4 no context. Đây là ambiguity/reporting check cần đối chiếu bảng/code, không chứng minh fabrication hoặc tự chọn số có lợi.

§5.4 có2000 bootstrap resamples và proportion tests, nhưng main text chưa nêu rõ bootstrap theo seed hay condition/prompt row. Các observations cùng seed không độc lập hoàn toàn; đây là câu hỏi reproducibility cần kiểm code, không kết luận tests chắc chắn sai.

## 4. Data/code availability

Availability statement vẫn nói sẽ public upon acceptance; trong trang/source links và2 exact-title/DOI resource searches chưa tìm được download dataset/code verified. Không suy dataset không tồn tại. Toàn bộ6 table images CDN vàpublisher PDF route trả403 ở lượt này; HTML main text đọc được. Raw logs giữ outcome thật. Chưa liên hệ tác giả hoặc gửi request thay user.

## 5. Tác động tới hai paper

Paper1 không thể dựa chỉ trên “5 mức bằng chứng” hoặc “đánh giá abstention thay vì accuracy”. Cần đối chiếu ESB cùng ALCE/RAGTruth/RAG-RewardBench/ViCH-QA và các paper gần khác, rồi xác định task/evidence/annotation/analysis khác biệt có ích. Có thể nghiên cứu museum evidence provenance, alternative valid evidence sets, qualified answers to scholarly disagreement, và Vietnam-specific grounding; đây mới là hypotheses chưa novelty confirmed.

Paper2: §7.9 ESB đã đề xuất pairwise contradiction verifier như future work. Làm đúng ý tưởng tương lai của bài không tự chứng minh method novel; cần xem conflict methods khác. KG tiếp tục mở nếu chứng minh structured provenance/relation evidence xử lý lỗi text baseline; không suy ESB dùng generalQA là KG domain trống.
