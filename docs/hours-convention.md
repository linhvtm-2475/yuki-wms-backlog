# Quy ước quy SWP ra giờ (LAB-5)

## 1. Cách chọn và lý do
- **Cách làm:** quy ước có hiệu chỉnh. Lấy 5 issue mẫu mà `/tkm:sun-estimate` đã chọn. Linh vừa kiểm SWP của chúng, vừa ước giờ trực tiếp từ nội dung issue (2026-10-24). Hệ số chung = tổng giờ / tổng SWP. Mọi issue khác: **Hours = SWP × hệ số**, làm tròn 0,5 h.
- **Lý do:**
  - Lặp lại được và giải thích được: một con số, nguồn rõ ràng.
  - Các issue mẫu trải từ thấp nhất tới cao nhất của backlog, gồm cả issue có độ tin thấp nhất.
  - Ước giờ trực tiếp cho cả 611 mục thì tốn công, và dễ lệch giữa các mục cùng loại.
- **Không làm:** không dùng giờ thực tế của dự án cũ, vì chưa có dữ liệu cho đội và stack này.

| Issue mẫu | SWP (Linh đã kiểm) | Giờ Linh ước | Giờ / SWP |
|---|---:|---:|---:|
| #6 Review chéo ADR + APV | 1 | 2 | 2,00 |
| #629 TC biên R-HR-10 | 3 | 6 | 2,00 |
| #142 Tối ưu chỉ mục truy vết (sửa từ 3 lên 6, sau tra cứu chuyên gia) | 6 | 12 | 2,00 |
| #767 Nạp lần cuối lên prod + đối soát | 15 | 24 | 1,60 |
| #267 Kiểm thử tích hợp 6 IF | 16 | 32 | 2,00 |
| **Hệ số** | **41** | **76** | **1,85** |

## 2. Contingency theo độ tin (không ghi vào trường Hours)
Trường **Hours** trên Project chỉ là giờ làm trực tiếp. Contingency tính riêng theo nhãn `estimate:*` (brainstorm-261024):

| Nhãn | Ý nghĩa | Tỷ lệ |
|---|---|---|
| `firm` | Có DD | 10% |
| `provisional` | Chỉ có basic design | 25% |
| `placeholder` | Chờ quyết định / chờ khách | 50% |

## 3. So với estimate LAB-1 (bidding)

| Epic | SWP | Giờ | MD | MD + contingency | Bidding MD | Δ (MD + cont − bidding) |
|---|---:|---:|---:|---:|---:|---:|
| EP-00 Nền tảng: Azure, CI/CD, khung app, xác thự | 292 | 541 | 67.6 | 77.5 | — | mới |
| EP-10 NFR, セキュリティ và 可観測性 | 193 | 359 | 44.9 | 56.8 | 75 | -18 |
| EP-08 マスタ: vòng đời master, 契約, 温度ポリシー, lưu giữ  | 193 | 358 | 44.8 | 56.0 | 55 | +1 |
| EP-09 外部IF: ERP, logger, bản đồ, IdP, mail, arch | 130 | 240 | 30.1 | 41.9 | 37 | +5 |
| EP-01 入荷・検査・保管 — nhập hàng, kiểm, tạo lô | 146 | 270 | 33.8 | 37.4 | 44 | -7 |
| EP-02 在庫・ロット・三温度帯 — tồn kho, lô, vị trí theo dải | 111 | 206 | 25.7 | 32.1 | 56 | -24 |
| EP-05 温度監視・逸脱・HACCP — giám sát nhiệt, ca 逸脱, hồ  | 184 | 340 | 42.5 | 50.4 | 63 | -13 |
| EP-03 有効期限管理・出荷・ピッキング・POD (E3) | 305 | 564 | 70.6 | 81.8 | 101 | -19 |
| EP-04 ルート計画・拘束時間 (E4) | 203 | 374 | 46.8 | 52.2 | 56 | -4 |
| EP-06 トレーサビリティ・回収 — truy vết lô và recall | 135 | 254 | 31.7 | 41.1 | 44 | -3 |
| EP-07 報告・KPI — 12 báo cáo vận hành và audit expo | 135 | 252 | 31.6 | 39.5 | 21 | +18 |
| EP-11 法令再検証 — xác minh lại nguồn pháp lý (OPS-LA | 31 | 58 | 7.2 | 9.1 | 4 | +5 |
| EP-12 データ移行 — migration 6 nguồn có lineage và đố | 106 | 197 | 24.6 | 32.2 | 71 | -39 |
| EP-13 カットオーバー・UAT・教育・ハイパーケア | 90 | 168 | 21.1 | 26.6 | 48 | -21 |
| EP-14 QA自動化 — bộ R-06, E2E và hồi quy | 60 | 112 | 13.9 | 17.9 | 24 | -6 |
| EP-15 Quản lý dự án / BrSE | 64 | 119 | 14.9 | 18.8 | 90 | -71 |
| **Tổng** | **2378** | **4414** | **551.7** | **671.3** | **789** | **-118** |

### Đọc bảng
- **Hai con số không cùng gốc.**
  - MD bidding gồm cả họp, review chung, điều phối, sửa bug, và hỗ trợ UAT / hypercare theo người.
  - SWP × giờ chỉ là thời gian làm từng task trong backlog.
  - Phần **ngoài backlog** (năng lực sửa bug khi ST / UAT, trực hypercare, nhân sự bổ sung) tính ở plan §9.3 và ở quyết định cân sprint: +1 QA từ S1, +1 BE từ S3. Xem `docs/sprint-capacity.md`.
- **EP-00 nền tảng** là phần mới so với bidding: Azure, IaC, CI/CD, auth, thứ tự khóa, idempotency, bảng quy tắc có version.
- **Thấp hơn bidding nhiều ở EP-12, EP-13, EP-15.** Trong bidding, các epic này chủ yếu là năng lực theo thời gian (rehearsal, UAT, quản lý). Backlog chỉ chứa phần việc đếm được thành task.
- **Không dùng bảng này để báo khách.** Con số chính thức ra ở bước 1.10 (plan, D-5), sau khi cộng phần ngoài backlog và chấm lại các mục `placeholder` theo bảng kích hoạt.

## 4. Giới hạn
- Hệ số lấy từ 5 mẫu, nên sai số lớn. Sau sprint S1 thật, thay bằng giờ thực tế trên SWP.
- 51 mục độ tin thấp (BrSE / PM có discipline `Unknown`). Giờ của chúng kém chắc chắn hơn.
