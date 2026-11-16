# IC/EC v0.1 — draft

Các dòng cố định giữ nguyên ý từ RBL-1 tuần 7; các dòng phụ thuộc RQ là đề xuất chưa đăng ký. Nhãn relevance/role khác quyết định formal inclusion.

| Mã | Quy tắc | Cách áp dụng |
| --- | --- | --- |
| IC-L | Paper tiếng Anh | Ngôn ngữ bài, không phải ngôn ngữ dataset |
| IC-T | Đã đăng conference/journal | Kiểm trang proceedings/publisher, năm và bản cụ thể; DOI đơn thuần chưa đủ. Preprint chưa đăng không đạt |
| IC-E | Có ≥1 số kết quả trong Table/Figure | Kiểm full-text, không lấy citation count, số trang hoặc lời quảng cáo làm kết quả |
| EC-D | Trùng paper đã có | Giữ bản ghi gốc và ánh xạ work/version, không xóa nguồn |
| EC-A | Không lấy được full-text sau thử đủ đường hợp pháp | Ghi publisher, repository/author copy, DOI/OA lookup và kết quả; không vượt paywall |
| EC-S | Dưới 4 trang, abstract/poster | Kiểm loại tài liệu và số trang bản thực, chưa biết thì UNSURE |
| EC-N | Không có thực nghiệm, vision/tutorial | Survey thuần mô tả vào BACKGROUND; không tính formal empirical included |
| IC-Y | Đề xuất 2016 đến cutoff formal | Lý do và cách xử lý bài nền trước 2016 trong protocol; cutoff chưa khóa |

## Các stream theo RQ

| Stream | IC-P: task/data | IC-I: kỹ thuật/đối tượng nghiên cứu | EC-O: dễ nhầm nhưng ngoài phạm vi |
| --- | --- | --- | --- |
| S1: domain benchmark, Paper1 | QA trên hồ sơ, tài liệu, hiện vật hoặc hình ảnh có ngữ cảnh di sản/bảo tàng | Dataset/benchmark QA hoặc hệ thống QA có đánh giá | Chỉ phân loại/nhận dạng ảnh không QA; chỉ recommendation/visitor analytics không QA; số hóa/3D reconstruction không QA |
| S2: domain grounded system, Paper1+2 | QA di sản trên nguồn văn bản/tri thức có thể truy vết | Retrieval, grounded generation hoặc KG-QA | Tour chatbot thuần trải nghiệm không đo QA có nguồn; entity extraction đơn lẻ không QA |
| S3: general evidence method, Paper2 và nền metric Paper1 | Document/context-grounded QA hoặc RAG ngoài di sản, có đầu vào nguồn | Attribution/claim verification, sufficiency/conflict, abstention/selective QA hoặc benchmark đo các yếu tố này | General chat safety refusal không liên quan thiếu bằng chứng; fact-checking tin tức độc lập không đặt trong QA có nguồn; general retrieval-only không đánh giá QA/support |

Một record có thể có nhiều stream; chỉ cần đạt ít nhất một stream và tất cả tiêu chí cố định để formal INCLUDE trong hướng tương ứng. S3 không cho phép gom mọi paper về RAG. Code-only/toolbox không có paper phù hợp giữ RESOURCE. Survey/nền tảng không đạt EC-N giữ BACKGROUND. Preprint gần RQ giữ NOVELTY_WATCHLIST dù không đạt IC-T; tìm bản published trước quyết định. Một benchmark VQA có thể formal INCLUDE S1 nhưng ghi ADJACENT_MODALITY, không coi là trực tiếp đánh giá grounded text QA.

Ưu tiên primary_reason nhất quán khi nhiều lý do: duplicate → ngoài task/technique → year/language/type/pages → no empirics/numeric evidence → access (chỉ dùng access khi chưa xác định được lỗi loại khác). Ghi cả secondary_reasons; ở vòng 1 chỉ dùng thông tin có căn cứ, chưa chắc chuyển UNSURE. Mã tiêu chí không đạt ghi FAIL_IC-L/IC-T/IC-E/IC-Y/IC-P/IC-I, mã loại dùng EC-*; mọi mã có citation/notes tương ứng.

Ba ví dụ giả định minh họa quy tắc, không phải quyết định cho paper thật: (a) benchmark pottery VQA có số đánh giá và đã đăng ≥4 trang → có thể S1, đánh dấu khác modality; (b) preprint kiểm chứng citation có empirical results → watchlist, chưa formal INCLUDE theo IC-T; (c) paper phân loại ảnh bảo tàng không QA → EC-O dù đúng domain. Không có quyết định screening nào được tạo trong đợt này.
