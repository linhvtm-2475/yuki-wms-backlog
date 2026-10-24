# Năng lực và tải sprint (sau khi cân, 2026-10-24)

Năng lực = (FTE plan §9.2 + bổ sung) × ngày làm việc × 8 h × 75%. Bổ sung theo quyết định Linh: +1 QA từ S1, +1 BE từ S3. Tải = giờ SWP của mục lá + contingency theo độ tin (firm 10% · provisional 25% · placeholder 50%).

| Sprint | Năng lực (h) | Tải sau cân (h) | Mức dùng |
|---|---:|---:|---:|
| P10 | 483 | 119 | 25% |
| S0 | 237 | 141 | 59% |
| S1 | 534 | 613 | 115% |
| S2 | 587 | 638 | 109% |
| S3 | 624 | 621 | 100% |
| S4 | 684 | 667 | 98% |
| S5 | 684 | 680 | 99% |
| S6 | 624 | 844 | 135% |
| HARD | 264 | 262 | 99% |
| ST | 528 | 527 | 100% |
| UAT | 855 | 149 | 17% |
| CUT | 297 | 65 | 22% |
| HYP | 294 | 44 | 15% |

Đã dời 37 issue (kèm sub-issue):

| Issue | Từ | Sang | Giờ + contingency |
|---|---|---|---:|
| EP10-I17 Dựng hiển thị JST và định dạng Nhật dùng chung | S1 | S5 | 12 |
| EP10-I18 Đưa kiểm WCAG 2.2 AA tự động vào CI | S1 | S5 | 9 |
| EP08-I19 Nạp dữ liệu master mẫu cho dev và test | S1 | S5 | 12 |
| EP00-I10 Chuyển bảng mã sang giá trị ASCII và tách nhãn JA | S1 | S5 | 36 |
| EP05-I02 Chốt câu hỏi khách về logger CSV và mức HACCP | S1 | S5 | 11 |
| EP15-I03 Báo cáo tuần và RAID S1–S2 | S2 | S5 | 9 |
| EP10-I02 Dựng màn COM-02 menu theo 職務 | S2 | S5 | 35 |
| EP10-I03 Dựng COM-03 khóa phiên theo lớp thiết bị | S2 | S5 | 35 |
| EP10-I05 Mã hóa dữ liệu khi truyền, khi lưu và trong tệp | S2 | HARD | 33 |
| EP10-I04 Xác định lớp thiết bị ở server và chỉ cho duyệt trên PC | S2 | HARD | 28 |
| EP08-I12 Hiển thị lịch sử version và reversal chỉ đọc (M.4) | S2 | HARD | 7 |
| EP02-I16 Chốt câu hỏi mở tồn kho / kiểm kê với PO | S2 | HARD | 9 |
| EP09-I07 Dựng adapter bản đồ IF-MAP-01 | S2 | ST | 22 |
| EP15-I10 Theo dõi câu hỏi chặn trước S4 (dữ liệu 移行, layout IF, pháp lý) | S3 | HARD | 8 |
| EP10-I08 Cảnh báo batch không chạy hoặc chạy quá giờ | S3 | ST | 12 |
| EP08-I10 Xử lý 依頼 閉鎖・再開 vị trí và IF設定 trong 14-04 | S3 | ST | 26 |
| EP08-I18 Kiểm phân quyền SCR-14 theo 職務 | S3 | ST | 19 |
| EP02-I04 Đề xuất vị trí lưu kho hợp lệ (FEFO, cùng SKU khác hạn) | S3 | ST | 7 |
| EP02-I06 Giữ dung lượng / 閉鎖 vị trí và gửi 閉鎖・再開依頼 | S3 | ST | 7 |
| EP03-I17 Màn SCR-05 ロット引当結果確認 (xem kết quả, đánh giá lô, F-4 / F-5) | S3 | ST | 25 |
| EP04-I21 Màn SCR-07 View 1 ルート作成 và View 3 公開・版履歴 | S3 | ST | 23 |
| EP01-I13 Chạy kiểm thử SCR-01 trên môi trường test | S3 | ST | 20 |
| EP09-I10 Dựng bộ phân giải người nhận và mẫu thông báo N-01〜N-16 | S3 | ST | 19 |
| EP03-I16 受注取消 trước picking (F-5) và job phục hồi dòng kẹt 処理中 | S3 | ST | 18 |
| EP04-I09 Sửa nháp, 版 n+1, đơn sau 14:00 và chặn bỏ stop đã giao | S3 | ST | 18 |
| EP09-I06 Dựng cổng nhận tệp datalogger (IF-LOG-01) | S3 | ST | 16 |
| EP01-I12 Xuất RPT-16 受入票 PDF | S3 | ST | 14 |
| EP04-I02 Chỉnh DD SCR-08 phần lịch trình, シール確認, 出発 / 帰着, 例外事象 | S3 | ST | 13 |
| EP09-I11 Dựng gửi lại mail failed từ 14-05 (F-21) | S3 | ST | 12 |
| EP03-I07 Màn SCR-04 View 2: duyệt dòng từ 2 tệp ERP delta | S3 | ST | 12 |
| EP15-I04 Báo cáo tuần và RAID S3–S4 (bắt đầu 移行) | S4 | ST | 9 |
| EP02-I17 Chạy kiểm thử SCR-02 / 03 / 16 trên môi trường test | S4 | ST | 23 |
| EP02-I14 Điều chỉnh chênh lệch kiểm kê: lý do, ngưỡng có version, maker–checker | S4 | ST | 14 |
| EP09-I04 Chạy B-03 xuất 入出庫・在庫結果 sang ERP lúc 23:30 | S4 | ST | 33 |
| EP03-I33 Màn SCR-08 POD登録 và vùng đồng bộ (375 px) | S4 | ST | 25 |
| EP03-I26 Màn SCR-06 ba view (ハンディ View 1〜2, tablet View 3) | S4 | ST | 23 |
| EP01-I11 Nhập 返品 theo dòng giao vào 隔離 | S4 | ST | 18 |
