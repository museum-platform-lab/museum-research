# Search strings v0.1 — thiết kế khái niệm, chưa chạy formal

OR trong một khối; AND giữa khối. Không trộn domain với technique trong cùng khối. Không ép từ Vietnamese vào tất cả truy vấn. Comparator chưa là khối bắt buộc. Cùng khái niệm giữa CSDL, nhưng mỗi chuỗi native phải được pilot và ghi nguyên văn trong query-runs.csv. Cú pháp bên dưới chưa được xác minh chạy trên IEEE/ACM/OpenAlex/S2, không trình bày như truy vấn đã chạy.

```text
D = (museum OR museums OR "cultural heritage" OR "cultural asset" OR artwork OR artefact OR artifact)
P = ("question answering" OR "visual question answering" OR "document question answering" OR "knowledge grounded dialogue")
I_QA = (benchmark OR dataset OR evaluation OR "retrieval augmented generation" OR "retrieval-augmented generation" OR "knowledge graph")
I_RAG = ("retrieval augmented generation" OR "retrieval-augmented generation" OR "grounded generation" OR "retrieval augmented question answering")
O_SUPPORT = ("claim support" OR "evidence attribution" OR "citation correctness" OR "citation faithfulness" OR "answer attribution" OR "natural language inference" OR "evidence verification")
O_SUFF = ("sufficient context" OR "evidence sufficiency" OR "conflicting evidence" OR "context conflict" OR "contradictory evidence")
O_ABSTAIN = (abstention OR abstain OR "selective prediction" OR "selective question answering" OR "unanswerable questions" OR "answerability detection" OR calibration)
O_METRIC = ("citation precision" OR "citation recall" OR "unsupported claims" OR "attribution evaluation" OR "answer faithfulness")
```

| Query ID | Khối cần triển khai | Mục đích/stream |
| --- | --- | --- |
| Q01 | D AND P AND I_QA | Domain benchmark/system S1/S2 |
| Q02 | D AND P | Kiểm coverage domain, tránh bỏ QA cũ không dùng từ benchmark/RAG; overlap Q01 được dedup |
| Q03 | P AND I_RAG AND O_SUPPORT | Verification/attribution S3 |
| Q04 | P AND I_RAG AND O_SUFF | Sufficiency và conflict S3 |
| Q05 | P AND I_RAG AND O_ABSTAIN | Selective answering S3 |
| Q06 | P AND I_RAG AND O_METRIC | Evaluation/faithfulness S3 |

Không bắt buộc keyword O trong Q02 vì QA di sản có thể dùng thuật ngữ khác; đây là nhánh rộng đã định trước. Q01 dùng D cho population và P/I_QA cho task/intervention. Các khối cần pilot với seed đã xác minh; nếu ALCE hoặc các công trình gần không có thuật ngữ P/I_RAG và bị bỏ sót, ghi amendment hoặc thu qua snowball hợp lệ, không tự coi chúng là hit của Q03.

## Native adaptation checklist

IEEE: kiểm Command Search và trường metadata hỗ trợ, tạo chuỗi có ngoặc và field theo giao diện đang dùng. ACM: chọn Title/Abstract/Keywords trong Advanced Search, lưu từng field expression. OpenAlex: kiểm trạng thái truy cập/API key và cú pháp hiện hành; không mặc định ngoặc/AND/OR của web và API tương đương. S2: nếu không hỗ trợ Boolean đầy đủ, tách các cụm thành truy vấn nhỏ, log mỗi truy vấn và union/dedup, nêu lệch chiến lược; chưa thể là sự thay thế im lặng cho query nguyên khối. ACL Anthology: xác minh search/export trước khi bổ sung.

Nếu quá nhiều: ưu tiên title/abstract, năm, bỏ synonym quá chung trước khi cân nhắc C; nếu quá ít: thử synonym và nới O, giữ task đúng. Mọi đổi sau khóa phải ghi amendment. Khoảng 50 hit trong hướng dẫn là dấu hiệu kiểm độ rộng, không phải quota hoặc quy tắc dừng. Không ghi counts khi chưa chạy.

Pilot readiness cần: native query được lưu, trường/filters chính xác, raw export đọc được, seed check có/không với lý do, quota/truncation và thời gian. Không cần quota Elicit cho quy trình này; web/API miễn phí vẫn phải báo rate limit/quyền truy cập thực tế.
