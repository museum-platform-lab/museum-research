# Dictionary và cách dùng template

CSV UTF-8; header là schema, chưa có dòng dữ liệu. Không được hiểu template rỗng là báo cáo kết quả. record_id giữ nguyên qua 01→02→03. occurrence_id giữ mọi raw hit; work_id nhóm phiên bản; discovery_id liên kết danh mục scoping. DOI có thể trống có reason; abstract thiếu không tự loại.

01_all_records.csv có các cột giảng viên yêu cầu: record_id,database,source,title,year,doi,abstract,authors,venue,url,query,retrieved_date,seed; bổ sung query_run_id,work_id,discovery_id,stream,source_occurrence_ids,version_status,metadata_notes. Đây là view sau dedup; occurrences.csv giữ trước dedup. source formal chỉ search/snowball-back/snowball-fwd, không gán cho AI suggestion.

02_after_screening_v1.csv giữ metadata gốc và thêm hướng, v1_decision (INCLUDE/EXCLUDE/UNSURE), v1_reason, evidence, reviewer/date, ai_suggestion, human_validation. Nếu paper thuộc cả hai hướng, dùng 2 dòng decision gắn cùng record_id, không tạo 2 works; khi đếm PRISMA hợp nhất lấy unique record_id theo quy tắc union có ít nhất một hướng tiếp tục.

03_fulltext_decisions.csv giữ metadata và quyết định vòng 1, thêm v2_decision,v2_reason,near_rq,evidence/fulltext/version/access fields. Giữ cả V2 excluded để đếm flow; xuất view 03_final_included.csv bằng filter v2_decision=INCLUDE (cùng snapshot, không dùng view chỉ included để tính excluded). near_rq là tập P I C O có căn cứ, không phải điểm chất lượng. 03 theo hướng, final union dedup work_id và công bố overlap.

Evidence table dùng 10 nhóm ở protocol; dòng có thể lặp work_id nếu nhiều evaluation setting, phải có evidence_id khác nhau; không tính dòng evidence thành số paper. Results/metrics/units giữ nguyên nghĩa và source locator. Code phải ghi reported URL, license/access khi biết; không có code không đồng nghĩa low quality mặc định.

query-runs.csv: mỗi native query/run một dòng; counts nguồn báo và exported khác nhau. search-log/amendments giữ lịch sử thay đổi. crosscheck.csv dùng cell-level hoặc decision-level, check_type phân biệt V1 và EXTRACTION; checked_value và original_value chỉ so sau independent review.

novelty-matrix.csv dành cho ứng viên gần RQ, kể cả preprint-only; formal_eligibility riêng khỏi contribution_overlap. Một dòng không phải xác nhận gap. readiness.json có null cho ngày/owner chưa biết, không tự gán tên hoặc sự phê duyệt.
