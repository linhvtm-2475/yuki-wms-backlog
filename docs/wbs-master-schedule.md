# WBS master schedule (milestone theo tháng)

Giờ = SWP × 1,85 (`docs/hours-convention.md`), chưa gồm contingency và phần ngoài backlog. Ô = giờ việc rơi vào tháng đó (chia theo số ngày của sprint).

## Giai đoạn và mốc

| Mã | Hạng mục | Sprint | Mốc / gate |
|---|---|---|---|
| 1.0 | Đóng gap 基本設計 (DR cuối, Step 4/5, ADR Azure, re-estimate) | P10 | G-BD 2026-11-27 |
| 2.0 | Sprint 0 (repo, CI/CD, IaC, master schedule, backlog, pilot) | S0 | G0 2026-12-04 |
| 3.0–4.0 | 詳細設計 lăn + Implement S1–S6 | S1, S2, S3, S4, S5, S6 |  |
| 5.0a | Hardening (hiệu năng, bảo mật, R-06) | HARD | G4 2027-03-19 |
| 5.0b | System test (IT / ST) | ST | G5 kỹ thuật 2027-04-02 |
| 6.0 | 移行 (rehearsal 1 ở S6, rehearsal 2 tuần 04-19) | S4, S5, S6, UAT | Quyết định nạp lần cuối |
| 7.0 | UAT + đào tạo 7 vai trò | UAT | G5 nghiệp vụ 2027-05-14 |
| 8.0 | Release + cutover (đóng băng master T-5, đơn T-8h) | CUT | G6 2027-05-31 · Go-Live 2027-06-01 |
| 9.0 | Chạy song song + hypercare 4 tuần | HYP | Kết thúc hypercare 2027-06-28 |
| 10.0 | Quản lý / BrSE (xuyên suốt) | toàn kỳ | Báo cáo tuần, steering tháng |

## Giờ theo epic × tháng

| Epic | 2026-10 | 2026-11 | 2026-12 | 2027-01 | 2027-02 | 2027-03 | 2027-04 | 2027-05 | 2027-06 | Tổng |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| EP-00 Nền tảng: Azure, CI/CD, khung app, xác t |  | 21 | 435 | 12 | 46 | 26 |  |  |  | 540 |
| EP-10 NFR, セキュリティ và 可観測性 |  | 3 | 43 | 13 | 95 | 196 | 9 |  |  | 359 |
| EP-08 マスタ: vòng đời master, 契約, 温度ポリシー, lưu gi |  | 2 | 148 | 93 | 74 | 31 | 10 |  |  | 358 |
| EP-09 外部IF: ERP, logger, bản đồ, IdP, mail, ar |  | 2 | 76 | 56 | 6 | 73 | 29 |  |  | 242 |
| EP-01 入荷・検査・保管 — nhập hàng, kiểm, tạo lô |  |  | 131 | 91 |  | 34 | 14 |  |  | 270 |
| EP-02 在庫・ロット・三温度帯 — tồn kho, lô, vị trí theo d |  |  | 21 | 116 | 20 | 36 | 12 |  |  | 205 |
| EP-05 温度監視・逸脱・HACCP — giám sát nhiệt, ca 逸脱, h |  |  |  | 113 | 205 | 22 |  |  |  | 340 |
| EP-03 有効期限管理・出荷・ピッキング・POD (E3) |  |  | 43 | 369 | 61 | 65 | 26 |  |  | 564 |
| EP-04 ルート計画・拘束時間 (E4) |  |  | 61 | 106 | 159 | 35 | 14 |  |  | 375 |
| EP-06 トレーサビリティ・回収 — truy vết lô và recall |  |  |  |  | 66 | 187 |  |  |  | 253 |
| EP-07 報告・KPI — 12 báo cáo vận hành và audit ex |  |  |  |  | 48 | 205 |  |  |  | 253 |
| EP-11 法令再検証 — xác minh lại nguồn pháp lý (OPS- | 10 | 43 |  |  |  |  | 3 | 2 |  | 58 |
| EP-12 データ移行 — migration 6 nguồn có lineage và  |  |  |  | 38 | 91 | 50 | 11 | 7 |  | 197 |
| EP-13 カットオーバー・UAT・教育・ハイパーケア |  |  |  |  |  | 12 | 50 | 80 | 26 | 168 |
| EP-14 QA自動化 — bộ R-06, E2E và hồi quy |  |  |  | 26 | 22 | 56 | 5 | 3 |  | 112 |
| EP-15 Quản lý dự án / BrSE | 8 | 35 |  | 6 | 8 | 37 | 14 | 6 | 8 | 122 |
| **Tổng** | **18** | **106** | **958** | **1039** | **901** | **1065** | **197** | **98** | **34** | **4416** |
