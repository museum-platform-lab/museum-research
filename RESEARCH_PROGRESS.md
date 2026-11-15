# Museum Platform — Historical Record Verification Ledger

Bảng theo dõi tiến độ thẩm định và xác minh chuyên sâu từng bản ghi di sản lịch sử (Historical Deep Verification Ledger).

---

## 1. Summary Statistics

- **Tổng số bản ghi trong danh sách mục tiêu:** 5 ID đầu tiên (`1`, `3`, `4`, `5`, `6`)
- **Số bản ghi đã hoàn tất hồ sơ nghiên cứu & hiệu chỉnh chuyên sâu (Audit Complete):** 1 (Record ID: 1)
- **Số bản ghi đang tiến hành:** 0
- **Số bản ghi đang chờ trong hàng đợi (Queued):** 4 (`3`, `4`, `5`, `6`)
- **Tỷ lệ hoàn thành đợt hiện tại:** 20%
- **Trạng thái thẩm định kỹ thuật:** `RESEARCH_COMPLETE` | `QUALITY_GATE_PASSED`
- **Trạng thái phê duyệt tổng thể:** `PENDING_HUMAN_REVIEW` *(Đã qua mô phỏng thẩm định đa chiều 4 góc nhìn chuyên gia; sẵn sàng chờ Hội đồng Giám tuyển và Chuyên gia Di sản thẩm định độc lập; tuyệt đối không tự động đóng dấu phê duyệt).*

---

## 2. Verification Records Ledger

| Record ID | Tên hiện vật (Dataset) | Tên thực thể chuẩn hóa | Loại thực thể | Trạng thái thẩm định | Thống kê Claims Chi tiết (v2.2) | Hồ sơ chi tiết | Cập nhật lần cuối |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: | :---: |
| **1** | Ngọc Lũ I | **Trống đồng Ngọc Lũ I** (Số ĐK: `LSb. 5722`) | `ARTIFACT` | `QUALITY_GATE_PASSED`<br>*(Pending Human Review)* | **18 Đầu việc Danh mục cha (C01–C18):**<br>• **8** Verified<br>• **4** Partially Verified<br>• **2** Institutional Narrative<br>• **1** Conflicting Evidence<br>• **2** Refuted<br>• **1** Data Quality Issue<br>---<br>**23 Mệnh đề Nguyên tử (Atomic Claims):**<br>• **10** Verified<br>• **4** Partially Verified<br>• **3** Institutional Narrative<br>• **1** Conflicting Evidence<br>• **3** Refuted / Corrupted Scrape<br>• **2** Data Quality Issue | [1.md](records/1.md) | 09/11/2026 (v2.2) |
| **3** | Thạp đồng Đào Thịnh | *Đang chờ nghiên cứu* | `ARTIFACT` | `QUEUED` | - | - | - |
| **4** | Đường Kách mệnh | *Đang chờ nghiên cứu* | `HISTORICAL_DOCUMENT` | `QUEUED` | - | - | - |
| **5** | Nhật ký trong tù | *Đang chờ nghiên cứu* | `HISTORICAL_DOCUMENT` | `QUEUED` | - | - | - |
| **6** | Lời kêu gọi toàn quốc kháng chiến | *Đang chờ nghiên cứu* | `HISTORICAL_DOCUMENT` | `QUEUED` | - | - | - |

---

## 3. Nhật ký kiểm tra & Hiệu chỉnh chuyên sâu theo đợt

### Đợt 1 — Record ID: 1 (`Ngọc Lũ I`)
- **Phiên bản 1.0 (Khởi tạo ban đầu):** 09/11/2026 — Dựng khung 11 mục, phát hiện số ký hiệu `LSb. 5722` và QĐ 1426/QĐ-TTg.
- **Phiên bản 2.0 (Audit đợt 1):** 09/11/2026 — Thay link nội bộ, lập ma trận claim thô.
- **Phiên bản 2.1 (Hiệu chỉnh theo phản biện ban đầu):** 09/11/2026 — Chuẩn hóa trích dẫn, tách atomic subclaims sơ khởi.
- **Phiên bản 2.2 (Kiểm toán & Hiệu chỉnh toàn diện theo PROMPT v2.2):** 09/11/2026.
  - **Hồ sơ lưu trữ:** [research/records/1.md](records/1.md).
  - **Nội dung hoàn thiện trọng tâm (100% P0, P1, P2):**
    1. **Tách triệt để Danh mục Nguồn (P0-01):** Phân định rạch ròi 8 nguồn kiểm chứng độc lập (SRC-01 đến SRC-08). Tách bài viết BTLSQG năm 2013 (SRC-01) và năm 2023 (SRC-02); định danh chính thức Quyết định số 1674/QĐ-TTg ngày 26/09/2011 thành lập BTLSQG (SRC-05) sửa dứt điểm lỗi nhầm lẫn số văn bản cũ.
    2. **Khắc phục niên đại viện bảo tàng EFEO (P0-02):** Sửa lỗi phi lịch sử về địa điểm lưu giữ 1903. Xác lập đúng dòng lịch sử: Năm 1903 đưa về trụ sở nghiên cứu ban đầu của EFEO tại Hà Nội; tòa nhà Musée Louis Finot (số 1 Tràng Tiền) do KTS. Ernest Hébrard thiết kế và khánh thành năm 1932. Bổ sung thông tin cơ sở 1 Tràng Tiền tạm dừng đón khách từ 15/12/2025 để trùng tu tổng thể.
    3. **Chuẩn hóa Ma trận Claim 18/23 đa chiều (P0-03, P1-10):** Đồng bộ tuyệt đối giữa 18 đầu việc mục cha và 23 atomic claims. Bổ sung 3 cột nhận thức luận: `Observation Status` (100% OBSERVED), `Semantic Validity` (VALID / INVALID / PARTIAL), và `Evidence Status` (7 trạng thái chuẩn hóa).
    4. **Hiệu chỉnh trích dẫn nguyên văn chuẩn xác (P0-04):** Đối soát từng từ ngữ với bản lưu trữ gốc của Quyết định 1426/QĐ-TTg (Mục 1 danh mục), bài viết BTLSQG 2013 và Cục Di sản văn hóa. Các đoạn văn tóm tắt được chuyển sang nhãn `Paraphrase` nghiêm ngặt.
    5. **Định vị chính xác Record 1 trong CSV Production (P1-01):** Khảo sát tệp `scraper/crawled_artifacts_production.csv` (SHA-256: `44416c559675be23fb0fce91e12f1fff542bccac553dc1a26e5875843e466c90`). Record ID 1 nằm tại Logical Record Index #39, trải dài từ Physical lines 418 đến 428.
    6. **Phân tích đối soát crawler.py (P1-02):** Chứng minh logic `Public Date` trong scraper/crawler.py là trích xuất năm công nhận di tích / xếp hạng BVQG bằng biểu thức chính quy (`19\d\d|20\d\d`), bảo vệ tính chuẩn xác của đề xuất điền `2012`.
    7. **Lý giải nguyên nhân dị bản kích thước & bề mặt (P1-03):** Xác định số đo chính thức đường kính chân là 80 cm, lý giải dị bản 81 cm do vành chân loe méo nhẹ hoặc sai số phương pháp đo; phân tích nguyên nhân biến thể màu sắc patin xanh xám vs nâu xám theo môi trường chôn lấp và oxy hóa.
    8. **Phân định rạch ròi 6 chiều thời gian (P1.4):** Làm rõ độ vênh giữa khung "2.500–2.000 BP" trong văn bản công nhận pháp lý và "thế kỷ III–II TCN" trong các công trình khảo cổ học chuyên sâu; phân tách tuyệt đối với các mốc lịch sử cận đại (1893/1894, 1902, 1903, 2012) và thời điểm crawl (2026).
    9. **Bảo tồn toàn diện Schema và dữ liệu Raw (P1-05):** Giữ nguyên vẹn 13 trường raw; giải trình chi tiết từng trường đề xuất; không ghi đè trường `Author` / `Contributor` của hệ thống kỹ thuật mà đề xuất bổ sung `cultural_creator`.
    10. **Xác minh kỹ thuật ảnh & Bản quyền (P1-06):** Kiểm tra 100% kết nối thực tế (HTTP 200) của 5 ảnh Wikimedia Commons và giấy phép CC BY-SA / Public Domain; loại bỏ vĩnh viễn 2 ảnh rác hệ thống (ảnh tượng Áo và icon Wikipedia).
    11. **Chuẩn hóa 14 cạnh Knowledge Graph (P1-07):** Chuyển toàn bộ sang `PENDING_REVIEW` kèm đầy đủ thuộc tính bằng chứng, mã nguồn và trạng thái epistemic.
    12. **Mô phỏng Thẩm định Đa chiều 4 Hội đồng Chuyên gia (P1-09):** Tích hợp phân tích từ 4 góc nhìn: Chuyên gia Khảo cổ học Đông Sơn, Giám tuyển Bảo tàng học, Chuyên gia Pháp lý Di sản, và Kỹ sư Tri thức/KG.

---

<details>
<summary><strong>Nhấn để xem: Lịch sử Lưu trữ Phiên bản cũ (Archive v1.0, v2.0 & v2.1)</strong></summary>

```markdown
# Lịch sử Sổ cái Cũ:
- Phiên bản 1.0 (09/11/2026): Thống kê sơ khởi 9 Đạt / 2 Bác bỏ / 1 Cập nhật (thiếu phân rã).
- Phiên bản 2.0 (09/11/2026): Cập nhật ma trận 18 claims, nhưng chưa phân rã atomic subclaims và chưa phân loại Institutional Narrative.
- Phiên bản 2.1 (09/11/2026): Bổ sung ma trận atomic claims (10/4/3/1/3/2), tách 6 chiều thời gian.
- Bản v2.2 hiện hành (09/11/2026): Chuẩn hóa toàn bộ 12 mục theo PROMPT v2.2, hoàn thành 100% tiêu chí Quality Gate.
```
</details>