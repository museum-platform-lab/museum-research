# Dữ liệu và schema

## Chọn corpus

Chọn một bộ sưu tập có mô tả nghệ thuật đủ chi tiết, nguồn kiểm tra được và quyền dùng rõ. Khởi đầu bằng văn bản/metadata. Có quyền truy cập ảnh không đồng nghĩa có quyền phát hành ảnh hoặc corpus.

Không mặc định được mang dữ liệu và mã của dự án trước sang pet project: xác nhận phần do bạn sở hữu, phần có giấy phép và phần cần cho phép. Dữ liệu không được phép dùng có thể thay bằng hồ sơ tự biên soạn từ nguồn hợp lệ.

## Schema tối thiểu

| Bảng | Trường chính |
|---|---|
| artworks | id, title, artist_id, material, date_text, collection_id |
| entities | id, type, canonical_name, aliases |
| relations | id, subject_id, predicate, object_id, review_status |
| sources | id, url, title, publisher, accessed_at, rights_status |
| passages | id, source_id, locator, text, content_hash |
| relation_evidence | relation_id, passage_id, supporting_excerpt |
| questions | id, question, answerable, reference_claims, evidence_ids, group_id, split |

Node: Artwork, Artist, Material, Period, Collection. Cạnh đầu tiên: CREATED_BY, USES_MATERIAL, DATED_TO, IN_COLLECTION. Chỉ thêm motif hoặc influenced_by khi nguồn thực sự nêu quan hệ và có quy tắc chú giải rõ.

Ngày nghệ thuật có thể là khoảng hoặc chưa chắc chắn: lưu văn bản gốc và trường start/end nếu xác định được. Không tự chuyển một mốc không rõ thành năm chính xác.

## Quy trình một bản ghi

1. Ghi nguồn, quyền sử dụng và vị trí đoạn chứng cứ.
2. Trích xuất metadata và alias, giữ giá trị không biết là trống.
3. Tạo quan hệ chỉ khi có chứng cứ trực tiếp.
4. Người chú giải kiểm tra đoạn nguồn và quan hệ.
5. Ghi version để biết corpus nào đã dùng cho mỗi thí nghiệm.

Không dùng kiến thức LLM làm nhãn chuẩn. Nguồn mâu thuẫn cần giữ cả hai phát biểu và đánh dấu chưa giải quyết; không tự chọn theo sự tự tin của mô hình.

## Benchmark

Pilot 60–100 câu hỏi: câu đơn bước, nhiều bước, so sánh và không thể trả lời từ corpus. Nhãn chuẩn ghi các claim cần có cùng passage hỗ trợ, không ép mọi câu trả lời giống một chuỗi chữ.

Từ chối dựa trên thiếu thông tin trong corpus, không dựa trên việc thông tin có tồn tại ngoài đời. Câu hỏi nhiều bước phải cần nhiều quan hệ thật, tránh chỉ thêm một câu dài nhưng một passage đã trả lời đủ.

Nhờ người thứ hai chú giải độc lập một phần mẫu, ghi tỷ lệ nhất trí và giải quyết bất đồng. Nếu chưa có người thứ hai, đánh dấu pilot một người và giới hạn kết luận.
