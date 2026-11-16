# Hướng dẫn screening và extraction v0.1

1. Pilot trên discovery ghi PILOT_SCOPING và discovery_id; không cấp source=search cho một lead chỉ vì có DOI. Chưa khóa protocol thì kết quả là nhãn thử, không formal included.
2. Formal ingestion: giữ raw export và occurrence_id. Cấp record_id ổn định, database/source/query/retrieved_date, map query run và raw row. Dedup theo protocol, giữ duplicate_of; file 01 là view canonical sau dedup, bảng occurrences vẫn đủ để đếm trước dedup.
3. V1 theo từng hướng: đọc title+abstract, xác định stream. INCLUDE hoặc UNSURE chuyển V2. Thiếu abstract phải tìm lại/ghi thiếu, không loại chỉ vì thiếu. Không suy metric/results từ title. Mỗi nhãn có reason, evidence URL/locator, reviewer và ngày.
4. V2 đọc full-text đúng version. Xác minh published, pages, thực nghiệm/Table-Figure và task. Giữ PDF/local ID hoặc URL hợp pháp, nhật ký access. Không chắc tương đương phiên bản: UNSURE + version_link pending. Chưa full-text chưa được extraction Results.
5. Extraction pilot 2–3 bài độc lập bởi hai người; sửa dictionary có log. Số đo ghi value, unit, setting và locator. Phân biệt author-reported limitation với reviewer-inferred limitation. N/A nghĩa không có trong nguồn; NOT_CHECKED nghĩa chưa đọc. Không điền 0 cho missing. Comparator NONE_REPORTED khác comparator chưa kiểm.
6. Người kiểm chéo xem nguồn gốc; không xem nhãn đầu trong V1. Giữ cả hai nhãn/ô, agreement và adjudication. Tác giả extractor không tự đóng vai reviewer2. AI suggestions giữ field riêng, không gắn tên người dùng như đã duyệt.

## Kiểm các khái niệm quan trọng

- Relevant retrieved passage: liên quan câu hỏi; chưa bảo đảm đủ trả lời.
- Claim support: đoạn nguồn entail claim; khác answer accuracy và causal faithfulness.
- Citation correctness: nguồn được dẫn hỗ trợ claim; citation recall/coverage: claim cần nguồn có được dẫn đủ hay không. Ghi định nghĩa metric nguyên bản.
- Sufficiency: tập bằng chứng có đủ cho yêu cầu; contradiction có thể đòi trả lời có điều kiện thay vì từ chối toàn bộ.
- Abstention: báo cả lỗi trả lời và lỗi từ chối, accuracy–coverage/risk–coverage khi nguồn có; không chỉ refusal rate.
- VQA/benchmark văn hóa không có citation labels: có thể làm nền domain, không kết luận đã đo grounded support.

## Ví dụ provenance, không phải record thật

Occurrence O-EXAMPLE → record R-EXAMPLE → work W-EXAMPLE; source=search cần query_run_id và raw row. source=snowball-back/fwd cần seed DOI/work ID và dịch vụ/ngày. Nếu chỉ có discovery Pxxx/Nxxx thì role=SCOPING, chưa có formal record. Mỗi decision có hướng P1/P2; total union không cộng hai tập trùng nhau.

## Tiêu chí hoàn tất một đợt lọc

Mọi record trong phạm vi đợt có trạng thái, UNSURE được giữ để giải quyết; lý do loại có mã; không có INCLUDE formal thiếu full-text evidence; kiểm chéo nêu rõ đã làm/chưa làm. Chỉ lập flow từ CSV có dữ liệu thực. Template trống không chứng minh 0 exclusions/0 disagreements.
