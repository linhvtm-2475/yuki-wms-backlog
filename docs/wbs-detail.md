# WBS chi tiết (epic → issue → sub-issue theo sprint)

Nguồn: GitHub Project https://github.com/users/linhvtm-2475/projects/1. SWP do `/tkm:sun-estimate` chấm và Linh kiểm mẫu; giờ = SWP × 1,85. Bảng đầy đủ từng sub-issue ở `reports/wbs-detail.xlsx`; dưới đây là epic → issue.

## EP-00 Nền tảng: Azure, CI/CD, khung app, xác thực và cơ chế dùng chung — 292 SWP / 542 h

| Issue | Sprint | Role | SWP | Giờ | Độ tin | Trạng thái |
|---|---|---|---:|---:|---|---|
| [EP00-I01](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/2) Viết ADR kiến trúc đích Azure thay ADR-002 và ADR-012 | S0 | SA | 13 | 24 | placeholder | Todo |
| [EP00-I02](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/7) Dựng IaC môi trường dev và test trên Azure | S0 | Infra | 16 | 30 | firm | Todo |
| [EP00-I03](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/12) Dựng pipeline CI/CD cho repo code | S0 | Infra | 13 | 24 | firm | Todo |
| [EP00-I04](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/16) Dựng môi trường UAT và cổng duyệt release | S5 | Infra | 7 | 13 | firm | Todo |
| [EP00-I05](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/19) Dựng môi trường prod và DR Japan West | S6 | Infra | 14 | 26 | firm | Todo |
| [EP00-I06](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/23) Che dữ liệu khi chép sang môi trường dưới | S5 | Infra | 5 | 10 | provisional | Todo |
| [EP00-I07](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/24) Dựng khung modular monolith theo 9 module | S0 | BE | 13 | 24 | firm | Todo |
| [EP00-I08](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/28) Định nghĩa cổng adapter Auth, Storage, Mail, Map, Queue | S1 | BE | 7 | 13 | firm | Done |
| [EP00-I09](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/31) Dựng nền schema DB và quy ước dữ liệu | S1 | BE | 11 | 20 | firm | In Progress |
| [EP00-I10](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/35) Chuyển bảng mã sang giá trị ASCII và tách nhãn JA | S5 | BE | 13 | 24 | placeholder | Todo |
| [EP00-I11](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/40) Đăng nhập Entra ID có chọn 職務 trước và kiểm 職務 được gán | S1 | BE | 16 | 30 | provisional | In Progress |
| [EP00-I12](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/45) Lưu phiên một 職務 phía server | S1 | BE | 9 | 16 | firm | In Progress |
| [EP00-I13](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/49) Bắt MFA theo 職務 được gán | S1 | BE | 9 | 16 | firm | Done |
| [EP00-I14](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/53) Kiểm quyền theo 職務 ở lớp API theo ma trận | S1 | BE | 14 | 26 | firm | Done |
| [EP00-I15](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/57) Dựng cơ chế duyệt hai người dùng chung | S1 | BE | 6 | 11 | firm | Done |
| [EP00-I16](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/60) Cài thứ tự khóa chung theo ADR-003 | S1 | BE | 14 | 26 | firm | In Progress |
| [EP00-I17](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/64) Dựng sổ idempotency dùng chung cho thao tác ghi | S1 | BE | 16 | 30 | firm | In Progress |
| [EP00-I18](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/68) Dựng khung bảng quy tắc có version | S1 | BE | 9 | 16 | firm | Done |
| [EP00-I19](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/72) Dựng temperature_policy_version và đánh giá nhiệt theo versi | S1 | BE | 9 | 16 | firm | Done |
| [EP00-I20](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/76) Dựng duty_rule_version nạp qua release | S1 | BE | 9 | 16 | firm | Done |
| [EP00-I21](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/80) Version hóa quy tắc 1/3・1/2 theo 顧客×SKU | S1 | BE | 7 | 13 | firm | Done |
| [EP00-I22](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/83) Dựng tham số cấu hình có version (config_parameter) | S1 | BE | 7 | 13 | firm | Done |
| [EP00-I23](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/86) Dựng catalog mã thông điệp từ error-codes 1.6.0 | S1 | BE | 7 | 13 | firm | Done |
| [EP00-I24](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/90) Dựng audit_log chỉ thêm | S1 | BE | 11 | 20 | firm | Done |
| [EP00-I25](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/94) Dựng thư viện gói xuất có manifest SHA-256 | S2 | BE | 6 | 11 | firm | Todo |
| [EP00-I26](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/97) Phân vùng tháng cho bảng lớn | S1 | BE | 11 | 20 | firm | In Progress |
| [EP00-I27](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/101) Dựng khung chạy batch trên Functions | S1 | BE | 12 | 22 | firm | Todo |
| [EP00-I28](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/105) Lưu tệp đính kèm trên Blob và container WORM | S2 | BE | 8 | 15 | firm | Todo |

## EP-10 NFR, セキュリティ và 可観測性 — 193 SWP / 358 h

| Issue | Sprint | Role | SWP | Giờ | Độ tin | Trạng thái |
|---|---|---|---:|---:|---|---|
| [EP10-I01](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/109) Dựng màn COM-04 lỗi chung | S1 | FE | 9 | 16 | provisional | In Progress |
| [EP10-I02](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/113) Dựng màn COM-02 menu theo 職務 | S5 | FE | 15 | 28 | provisional | Todo |
| [EP10-I03](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/118) Dựng COM-03 khóa phiên theo lớp thiết bị | S5 | FE | 15 | 28 | provisional | Todo |
| [EP10-I04](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/123) Xác định lớp thiết bị ở server và chỉ cho duyệt trên PC | HARD | BE | 12 | 22 | provisional | Todo |
| [EP10-I05](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/127) Mã hóa dữ liệu khi truyền, khi lưu và trong tệp | HARD | Infra | 12 | 22 | placeholder | Todo |
| [EP10-I06](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/131) Quản lý bí mật bằng Key Vault và managed identity | S0 | Infra | 8 | 15 | provisional | Todo |
| [EP10-I07](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/132) Dựng quan sát: log có cấu trúc, trace, metric, alert | S2 | Infra | 12 | 22 | provisional | In Progress |
| [EP10-I08](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/136) Cảnh báo batch không chạy hoặc chạy quá giờ | ST | Infra | 5 | 10 | provisional | Todo |
| [EP10-I09](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/137) Soạn runbook sự cố P0 | S6 | Infra | 7 | 13 | provisional | Todo |
| [EP10-I10](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/140) Dựng bộ dữ liệu giả cỡ thật để đo hiệu năng | S4 | QA | 6 | 11 | provisional | Todo |
| [EP10-I11](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/141) Đo truy vết 3 năm ≤ 60 giây và quyết A-3 | S5 | BE | 9 | 16 | provisional | Todo |
| [EP10-I12](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/144) Load test p95 đọc ≤ 2 giây, ghi ≤ 3 giây với 80 phiên | HARD | QA | 13 | 24 | provisional | Todo |
| [EP10-I13](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/148) Cấu hình backup và PITR cho PostgreSQL và Blob | S6 | Infra | 5 | 10 | provisional | Todo |
| [EP10-I14](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/149) Diễn tập restore và chuyển vùng DR, đo RTO 4 giờ | HARD | Infra | 12 | 22 | provisional | Todo |
| [EP10-I15](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/153) Cấu hình HA đạt 99,5% trong giờ phục vụ | S6 | Infra | 5 | 10 | provisional | Todo |
| [EP10-I16](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/154) Kiểm hành vi mất mạng ở màn kho và màn PC | ST | QA | 8 | 15 | provisional | Todo |
| [EP10-I17](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/155) Dựng hiển thị JST và định dạng Nhật dùng chung | S5 | FE | 5 | 10 | provisional | Todo |
| [EP10-I18](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/156) Đưa kiểm WCAG 2.2 AA tự động vào CI | S5 | QA | 4 | 8 | provisional | Todo |
| [EP10-I22](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/157) Kiểm tay WCAG 2.2 AA toàn bộ màn | HARD | QA | 10 | 18 | provisional | Todo |
| [EP10-I19](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/158) Kiểm ma trận quyền toàn hệ thống | HARD | QA | 12 | 22 | provisional | Todo |
| [EP10-I20](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/159) Lập gói bằng chứng bảo mật: threat model, SBOM, quét lỗ hổng | HARD | SA | 6 | 11 | provisional | Todo |
| [EP10-I21](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/160) Tổng hợp bằng chứng NFR cho nghiệm thu | ST | PM | 3 | 6 | provisional | Todo |

## EP-08 マスタ: vòng đời master, 契約, 温度ポリシー, lưu giữ và purge — 193 SWP / 358 h

| Issue | Sprint | Role | SWP | Giờ | Độ tin | Trạng thái |
|---|---|---|---:|---:|---|---|
| [EP08-I01](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/162) Dựng khung vòng đời master dùng chung | S1 | BE | 11 | 20 | provisional | In Progress |
| [EP08-I02](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/166) Dựng 14-01 SKUマスタ | S1 | FE | 13 | 24 | provisional | In Progress |
| [EP08-I03](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/171) Bắt buộc 期限種別 trên SKU và không suy mặc định | S1 | BE | 5 | 10 | provisional | Done |
| [EP08-I04](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/172) Quản lý traceability_lane và regulated_identifier | S1 | BE | 5 | 10 | provisional | Done |
| [EP08-I05](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/173) Dựng 14-02 顧客-SKU契約 và 顧客ヘッダ | S2 | FE | 13 | 24 | provisional | In Progress |
| [EP08-I06](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/178) Xử lý delivery_window_rule 未確定 | S2 | BE | 5 | 10 | provisional | Todo |
| [EP08-I07](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/179) Dựng 14-03 仕入先 / 位置 / デバイス / 車両 | S2 | FE | 18 | 34 | provisional | In Progress |
| [EP08-I08](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/184) Dựng 14-03 温度ポリシー版 | S1 | FE | 14 | 26 | provisional | In Progress |
| [EP08-I09](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/189) Dựng 14-04 承認キュー | S2 | FE | 14 | 26 | provisional | In Progress |
| [EP08-I10](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/194) Xử lý 依頼 閉鎖・再開 vị trí và IF設定 trong 14-04 | ST | BE | 11 | 20 | provisional | Todo |
| [EP08-I11](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/198) Duyệt reversal dòng giao đã nhận (M.5) | S3 | BE | 12 | 22 | provisional | Todo |
| [EP08-I12](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/202) Hiển thị lịch sử version và reversal chỉ đọc (M.4) | HARD | FE | 3 | 6 | provisional | Todo |
| [EP08-I13](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/203) Dựng 14-06 保持ポリシー | S4 | FE | 13 | 24 | provisional | Todo |
| [EP08-I14](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/208) Áp hạn lưu nhóm luật định 労働関係記録 và 米 賞味 > 3 năm | S4 | BE | 6 | 11 | provisional | Todo |
| [EP08-I15](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/209) Đặt và gỡ Legal hold theo ca hoặc lô | S4 | BE | 14 | 26 | provisional | Todo |
| [EP08-I16](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/214) Chạy B-08 lập danh sách purge hằng tháng và duyệt | S5 | BE | 14 | 26 | provisional | Todo |
| [EP08-I17](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/219) Chạy B-09 purge sau archive và so manifest | S5 | BE | 9 | 16 | provisional | Todo |
| [EP08-I18](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/222) Kiểm phân quyền SCR-14 theo 職務 | ST | QA | 8 | 15 | provisional | Todo |
| [EP08-I19](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/223) Nạp dữ liệu master mẫu cho dev và test | S5 | BE | 5 | 10 | provisional | Todo |

## EP-09 外部IF: ERP, logger, bản đồ, IdP, mail, archive — 130 SWP / 241 h

| Issue | Sprint | Role | SWP | Giờ | Độ tin | Trạng thái |
|---|---|---|---:|---:|---|---|
| [EP09-I01](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/225) Dựng điểm nhận tệp SFTP managed cho ERP | S1 | Infra | 6 | 11 | provisional | In Progress |
| [EP09-I02](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/228) Chạy B-01 nhập 入荷予定 từ ERP | S2 | BE | 11 | 20 | placeholder | In Progress |
| [EP09-I03](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/232) Chạy B-02 nhập 受注 hai tệp delta 10:30 và 13:30 | S2 | BE | 11 | 20 | placeholder | In Progress |
| [EP09-I04](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/236) Chạy B-03 xuất 入出庫・在庫結果 sang ERP lúc 23:30 | ST | BE | 12 | 22 | placeholder | Todo |
| [EP09-I05](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/240) Dựng 14-05 外部IF連携状態 | S3 | FE | 14 | 26 | provisional | Todo |
| [EP09-I06](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/245) Dựng cổng nhận tệp datalogger (IF-LOG-01) | ST | BE | 6 | 11 | placeholder | Todo |
| [EP09-I07](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/248) Dựng adapter bản đồ IF-MAP-01 | ST | BE | 8 | 15 | placeholder | Todo |
| [EP09-I08](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/252) Kết nối Entra ID (IF-IDP-01) | S1 | BE | 13 | 24 | provisional | In Progress |
| [EP09-I09](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/257) Dựng hàng đợi mail và worker gửi lại (IF-MAIL-01) | S2 | BE | 11 | 20 | placeholder | In Progress |
| [EP09-I10](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/261) Dựng bộ phân giải người nhận và mẫu thông báo N-01〜N-16 | ST | BE | 8 | 15 | provisional | Todo |
| [EP09-I11](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/262) Dựng gửi lại mail failed từ 14-05 (F-21) | ST | BE | 5 | 10 | provisional | Todo |
| [EP09-I12](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/263) Xuất archive RPT-14 (IF-ARCH-01) | S4 | BE | 9 | 16 | provisional | Todo |
| [EP09-I13](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/267) Kiểm thử tích hợp IF với mock và hệ thật | ST | QA | 16 | 30 | placeholder | Todo |

## EP-01 入荷・検査・保管 — nhập hàng, kiểm, tạo lô — 146 SWP / 270 h

| Issue | Sprint | Role | SWP | Giờ | Độ tin | Trạng thái |
|---|---|---|---:|---:|---|---|
| [EP01-I01](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/269) Rà lại DD SCR-01 入荷検品 theo kiến trúc Azure | S1 | SA | 17 | 32 | firm | In Progress |
| [EP01-I02](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/275) Tạo schema REC cho 入荷予定, dòng kiểm và 判定 | S2 | BE | 6 | 11 | firm | Todo |
| [EP01-I03](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/278) Đăng ký 入荷予定 và xem danh sách 予定 | S2 | BE | 10 | 18 | firm | Todo |
| [EP01-I04](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/282) Lưu nháp 検査入力 với kiểm đủ trường P0 | S2 | BE | 14 | 26 | firm | Todo |
| [EP01-I05](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/287) Kiểm dải nhiệt lúc nhập theo 版 ngưỡng hiệu lực và 一時温度帯 | S2 | BE | 12 | 22 | firm | Todo |
| [EP01-I06](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/292) Phân biệt 消費期限 và 賞味期限 khi nhập hạn | S2 | BE | 8 | 15 | firm | Todo |
| [EP01-I07](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/296) Kiểm truy xuất bắt buộc 米 / 牛 lúc nhập | S2 | BE | 9 | 16 | firm | Todo |
| [EP01-I08](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/300) Xác nhận 判定 idempotent theo request_id | S2 | BE | 15 | 28 | firm | Todo |
| [EP01-I09](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/304) Tạo lô bất biến, cách ly lúc nhập và ca 逸脱 nhập hàng | S2 | BE | 14 | 26 | firm | Todo |
| [EP01-I10](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/309) 分散承認 khi tổng lệch 報告数, maker ≠ checker trên PC | S2 | BE | 15 | 28 | firm | Todo |
| [EP01-I11](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/314) Nhập 返品 theo dòng giao vào 隔離 | ST | BE | 9 | 16 | firm | Todo |
| [EP01-I12](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/318) Xuất RPT-16 受入票 PDF | ST | BE | 7 | 13 | firm | Todo |
| [EP01-I13](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/321) Chạy kiểm thử SCR-01 trên môi trường test | ST | QA | 10 | 18 | firm | Todo |

## EP-02 在庫・ロット・三温度帯 — tồn kho, lô, vị trí theo dải nhiệt — 111 SWP / 206 h

| Issue | Sprint | Role | SWP | Giờ | Độ tin | Trạng thái |
|---|---|---|---:|---:|---|---|
| [EP02-I01](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/325) Tạo schema INV lõi: lô, phiên bản lô, tồn theo vị trí, sự ki | S2 | BE | 6 | 11 | provisional | Todo |
| [EP02-I02](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/328) Tra cứu tồn / lô đa điều kiện và chi tiết lô (SCR-02 View 1– | S3 | FE | 12 | 22 | provisional | Todo |
| [EP02-I03](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/332) Ghi 移動 bất biến, idempotent, chặn tồn âm | S3 | BE | 6 | 11 | provisional | Todo |
| [EP02-I04](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/335) Đề xuất vị trí lưu kho hợp lệ (FEFO, cùng SKU khác hạn) | ST | BE | 3 | 6 | provisional | Todo |
| [EP02-I05](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/337) Chặn put-away / 移動 sai dải áp dụng, không tạo 逸脱 | S3 | BE | 3 | 6 | provisional | Todo |
| [EP02-I06](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/339) Giữ dung lượng / 閉鎖 vị trí và gửi 閉鎖・再開依頼 | ST | BE | 3 | 6 | provisional | Todo |
| [EP02-I07](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/341) 訂正 lô có phiên bản và duyệt người thứ hai | S4 | BE | 7 | 13 | provisional | Todo |
| [EP02-I08](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/344) 訂正 牛個体識別番号 cho lô lane 牛 | S4 | BE | 3 | 6 | provisional | Todo |
| [EP02-I09](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/346) 訂正 有効期限: duyệt hai người, giải phóng 引当, giữ loại hạn | S4 | BE | 3 | 6 | provisional | Todo |
| [EP02-I10](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/348) Máy trạng thái 隔離: 隔離へ, 記録, リリース (SCR-03) | S3 | BE | 13 | 24 | provisional | Todo |
| [EP02-I11](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/352) 廃棄依頼 và duyệt người thứ hai theo 位置 × ロット | S3 | BE | 5 | 10 | provisional | Todo |
| [EP02-I12](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/355) Dịch vụ cách ly dùng chung: nhiều 起因, giải phóng 引当 theo thứ | S3 | BE | 10 | 18 | provisional | Todo |
| [EP02-I13](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/358) Kiểm kê blind count: tạo task, đếm, nộp (SCR-16) | S4 | BE | 11 | 20 | provisional | Todo |
| [EP02-I14](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/362) Điều chỉnh chênh lệch kiểm kê: lý do, ngưỡng có version, mak | ST | BE | 6 | 11 | provisional | Todo |
| [EP02-I15](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/365) 返品 vào kho qua 隔離 (D-B) phía tồn kho | S4 | BE | 6 | 11 | provisional | Todo |
| [EP02-I16](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/368) Chốt câu hỏi mở tồn kho / kiểm kê với PO | HARD | BrSE | 4 | 8 | provisional | Todo |
| [EP02-I17](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/369) Chạy kiểm thử SCR-02 / 03 / 16 trên môi trường test | ST | QA | 10 | 18 | provisional | Todo |

## EP-05 温度監視・逸脱・HACCP — giám sát nhiệt, ca 逸脱, hồ sơ HACCP — 184 SWP / 341 h

| Issue | Sprint | Role | SWP | Giờ | Độ tin | Trạng thái |
|---|---|---|---:|---:|---|---|
| [EP05-I01](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/371) Rà lại DD SCR-09 温度監視 theo kiến trúc Azure | S3 | SA | 13 | 24 | firm | Todo |
| [EP05-I02](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/376) Chốt câu hỏi khách về logger CSV và mức HACCP | S5 | BrSE | 4 | 8 | placeholder | Todo |
| [EP05-I03](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/377) Tạo schema TMP: tệp nhập, reading, event, alarm, haccp_task | S4 | BE | 8 | 15 | firm | Todo |
| [EP05-I04](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/380) Nhập CSV logger idempotent theo SHA-256 (SCR-09 View 2) | S4 | BE | 20 | 37 | firm | Todo |
| [EP05-I05](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/386) Đánh giá ngưỡng theo 版 và phạm vi zone / lô có ticket | S4 | BE | 6 | 11 | firm | Todo |
| [EP05-I06](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/389) Đợt lệch và alarm theo thời lượng, khoảng trống không cắt đợ | S4 | BE | 12 | 22 | firm | Todo |
| [EP05-I07](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/393) Lô ảnh hưởng của alarm, ca 逸脱 và cách ly theo thứ tự khóa | S4 | BE | 13 | 24 | placeholder | Todo |
| [EP05-I08](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/397) Gửi mail N-01 sau mỗi lần nhập có alarm mới hoặc 未評価 | S4 | BE | 6 | 11 | firm | Todo |
| [EP05-I09](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/400) Ghi review alarm đầu tiên và đánh dấu quá hạn 15 phút | S4 | BE | 11 | 20 | firm | Todo |
| [EP05-I10](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/404) Dashboard giám sát nhiệt độ (SCR-09 View 1) | S4 | FE | 6 | 11 | firm | Todo |
| [EP05-I11](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/407) Cảnh báo 取込遅延 theo logger (B-05, A-8) | S5 | BE | 9 | 16 | firm | Todo |
| [EP05-I12](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/411) Cờ 要確認 chặn 引当 / 出荷確認 khi mất dữ liệu nhiệt | S5 | BE | 6 | 11 | placeholder | Todo |
| [EP05-I13](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/414) Đánh giá tăng dần cho khối lượng 2,5 triệu reading | S5 | BE | 6 | 11 | firm | Todo |
| [EP05-I14](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/417) Xuất RPT-17 温度記録表 | S5 | BE | 7 | 13 | firm | Todo |
| [EP05-I15](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/420) Quản lý ca 逸脱: điều tra, 再測定 品温, chứng cứ, 決定案 (SCR-10) | S5 | BE | 15 | 28 | provisional | Todo |
| [EP05-I16](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/424) Vai trò theo 重大度 và điều kiện đóng ca | S5 | BE | 4 | 8 | provisional | Todo |
| [EP05-I17](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/426) Hàng đợi HACCP欠落 và batch B-07 phát hiện thiếu hồ sơ | S5 | BE | 12 | 22 | provisional | Todo |
| [EP05-I18](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/430) 日次確認 / 月次確認 với maker ≠ checker | S5 | BE | 3 | 6 | provisional | Todo |
| [EP05-I19](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/432) Nhập hồ sơ 衛生 và 来訪者・ドライバー trên tablet chung (SCR-10 View 4) | S5 | FE | 8 | 15 | provisional | Todo |
| [EP05-I20](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/435) Xuất RPT-18 逸脱・隔離記録 cho một ca | S5 | BE | 3 | 6 | provisional | Todo |
| [EP05-I21](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/437) Chạy kiểm thử SCR-09 / SCR-10 trên môi trường test | S6 | QA | 12 | 22 | firm | Todo |

## EP-03 有効期限管理・出荷・ピッキング・POD (E3) — 305 SWP / 566 h

| Issue | Sprint | Role | SWP | Giờ | Độ tin | Trạng thái |
|---|---|---|---:|---:|---|---|
| [EP03-I01](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/441) Chỉnh DD SCR-05 cho hệ đích Azure | S2 | SA | 10 | 18 | firm | Todo |
| [EP03-I02](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/445) Chỉnh DD SCR-06 cho hệ đích Azure | S2 | SA | 10 | 18 | firm | Todo |
| [EP03-I03](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/449) Chỉnh DD SCR-08 phần POD / hàng đợi / đồng bộ | S3 | SA | 10 | 18 | placeholder | Todo |
| [EP03-I04](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/453) Dựng schema OUT_DB cho luồng xuất | S2 | BE | 12 | 22 | firm | In Progress |
| [EP03-I05](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/458) Nhập dòng 受注 tay và kiểm master / trùng tham chiếu | S3 | BE | 5 | 10 | provisional | Todo |
| [EP03-I06](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/460) 受注確定 một dòng / 一括 kèm giờ cắt 16:00 và kích hoạt 引当 | S3 | BE | 5 | 10 | provisional | Todo |
| [EP03-I07](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/462) Màn SCR-04 View 2: duyệt dòng từ 2 tệp ERP delta | ST | FE | 5 | 10 | provisional | Todo |
| [EP03-I08](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/464) Engine 引当 ở server: loại trừ 6 mức, FEFO/FIFO, khóa nguyên t | S3 | BE | 20 | 37 | firm | Todo |
| [EP03-I09](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/470) 日付逆転: so hạn với lần giao 受領済 gần nhất theo cặp khách × SKU | S3 | BE | 9 | 16 | firm | Todo |
| [EP03-I10](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/474) 日付逆転: thêm nguồn (b)(c) đơn khác cùng cặp đang 引当 / 積込 / đan | S4 | BE | 6 | 11 | firm | Todo |
| [EP03-I11](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/477) 消費期限 chặn cứng / 賞味期限 chỉ cảnh báo trong 引当 và lúc 積込・出荷 | S3 | BE | 7 | 13 | placeholder | Todo |
| [EP03-I12](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/481) 配送ウィンドウ 1/3・1/2 theo 要求日 và lưu bằng chứng tính | S3 | BE | 7 | 13 | firm | Todo |
| [EP03-I13](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/485) Chặn lô 牛 確認待ち ở 引当 và lúc 積込・出荷 | S3 | BE | 7 | 13 | firm | Todo |
| [EP03-I14](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/489) 温度帯: loại lô lệch dải ở 引当 và kiểm 3 giá trị ở 積込確認 | S3 | BE | 9 | 16 | firm | Todo |
| [EP03-I15](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/493) 解放 → 再引当: giải phóng khi lô 隔離 / 訂正 / 棚卸し và F-4 | S3 | BE | 13 | 24 | firm | Todo |
| [EP03-I16](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/497) 受注取消 trước picking (F-5) và job phục hồi dòng kẹt 処理中 | ST | BE | 9 | 16 | firm | Todo |
| [EP03-I17](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/501) Màn SCR-05 ロット引当結果確認 (xem kết quả, đánh giá lô, F-4 / F-5) | ST | FE | 12 | 22 | firm | Todo |
| [EP03-I18](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/505) タスク一覧 và quét GS1-128 / JAN / ITF, lần quét đầu → picked | S3 | BE | 10 | 18 | firm | Todo |
| [EP03-I19](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/509) 積込確認 (C-11) theo thứ tự kiểm OUT_DB R7 | S3 | BE | 6 | 11 | firm | Todo |
| [EP03-I20](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/512) 積込完了 (車両) và ghi seal một lần cho xe × chuyến | S3 | BE | 6 | 11 | firm | Todo |
| [EP03-I21](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/515) 出荷前チェック 記録 / 再測定 theo ngưỡng có version và tạo 逸脱 | S3 | BE | 9 | 16 | firm | Todo |
| [EP03-I22](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/519) 貨物温度 NG khi task loaded: bắt 積込取消 rồi mới 解放 (H-7) | S4 | BE | 6 | 11 | placeholder | Todo |
| [EP03-I23](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/522) 出荷確認: trừ tồn đúng một lần (D-A) | S4 | BE | 12 | 22 | firm | Todo |
| [EP03-I24](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/527) 積込取消: dỡ hàng, vô hiệu seal, đưa task khác về 出荷再確認 | S4 | BE | 6 | 11 | firm | Todo |
| [EP03-I25](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/530) Chặn 出発 khi lô đã 出荷確認 bị 隔離 / recall và cho 出荷取消 trước 出発 ( | S4 | BE | 7 | 13 | placeholder | Todo |
| [EP03-I26](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/534) Màn SCR-06 ba view (ハンディ View 1〜2, tablet View 3) | ST | FE | 11 | 20 | firm | Todo |
| [EP03-I27](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/538) Sổ pod_sync_receipt: idempotency bản ghi tài xế, N-13, B-16 | S3 | BE | 10 | 18 | firm | Todo |
| [EP03-I28](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/542) OfflineQueue mã hóa chỉ ở app tài xế (IndexedDB + WebCrypto) | S3 | FE | 12 | 22 | firm | Todo |
| [EP03-I29](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/547) Đồng bộ tự động hàng đợi tài xế, phân loại synced / duplicat | S4 | FE | 10 | 18 | firm | Todo |
| [EP03-I30](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/551) POD theo dòng 受注: pod, pod_line, shipment_line, không trừ tồ | S4 | BE | 10 | 18 | firm | Todo |
| [EP03-I31](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/556) Bằng chứng POD theo hợp đồng 車上渡し / 軒先渡し và snapshot lúc ser | S4 | BE | 6 | 11 | firm | Todo |
| [EP03-I32](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/559) Upload tệp POD idempotent lên Blob với SHA-256 | S4 | BE | 6 | 11 | placeholder | Todo |
| [EP03-I33](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/562) Màn SCR-08 POD登録 và vùng đồng bộ (375 px) | ST | FE | 12 | 22 | firm | Todo |
| [EP03-I34](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/566) POD訂正 bằng 版 mới ở SCR-12 (7 ngày, chỉ thêm bằng chứng) | S4 | BE | 5 | 10 | provisional | Todo |
| [EP03-I35](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/568) Claim gắn dòng giao / lô / bằng chứng, trạng thái tách xử lý | S4 | BE | 5 | 10 | provisional | Todo |

## EP-04 ルート計画・拘束時間 (E4) — 203 SWP / 376 h

| Issue | Sprint | Role | SWP | Giờ | Độ tin | Trạng thái |
|---|---|---|---:|---:|---|---|
| [EP04-I01](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/571) Chỉnh DD SCR-07 cho hệ đích Azure và chốt tham số 【仮定】 | S1 | SA | 10 | 18 | firm | Todo |
| [EP04-I02](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/576) Chỉnh DD SCR-08 phần lịch trình, シール確認, 出発 / 帰着, 例外事象 | ST | SA | 6 | 11 | firm | Todo |
| [EP04-I03](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/579) Dựng schema DSP_DB và CR thêm 帰着予定 | S2 | BE | 10 | 18 | firm | In Progress |
| [EP04-I04](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/584) ルール版 拘束時間 2024 kèm nguồn pháp lý và cờ xác minh | S2 | BE | 12 | 22 | firm | In Progress |
| [EP04-I05](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/589) 公開: server tự tính lại, không tin nháp, chặn ルール版 未検証 ở prod | S2 | BE | 9 | 16 | firm | Todo |
| [EP04-I06](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/594) Khóa tài xế và tính lại lũy kế 拘束時間 trong giao dịch 公開 (H-6) | S2 | BE | 8 | 15 | placeholder | Todo |
| [EP04-I07](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/597) Tạo / tạo lại nháp route từ đơn 引当済 (ルート作成) | S3 | BE | 12 | 22 | firm | Todo |
| [EP04-I08](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/601) 連続運転 ≤ 4 h và tự chèn 休息 30 phút trước khi vượt | S3 | BE | 6 | 11 | firm | Todo |
| [EP04-I09](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/604) Sửa nháp, 版 n+1, đơn sau 14:00 và chặn bỏ stop đã giao | ST | BE | 9 | 16 | firm | Todo |
| [EP04-I10](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/608) Khung engine 拘束時間: dựng timeline, gộp kết quả, 未判定, API チェック | S3 | BE | 9 | 16 | firm | Todo |
| [EP04-I11](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/612) R-HR-01/02: 1日拘束 13 h / tối đa 15 h, cửa sổ 24 h từ 始業 | S5 | BE | 8 | 15 | firm | Todo |
| [EP04-I12](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/616) R-HR-04/05: 拘束 tháng 284 h và năm 3,300 h | S5 | BE | 8 | 15 | firm | Todo |
| [EP04-I13](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/620) R-HR-06: 休息期間 ≥ 9 h (mục tiêu 11 h) | S5 | BE | 8 | 15 | firm | Todo |
| [EP04-I14](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/624) R-HR-07/08: 運転 trung bình 2 ngày 9 h và 2 tuần 44 h | S5 | BE | 8 | 15 | firm | Todo |
| [EP04-I15](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/628) R-HR-10: 時間外 năm ≤ 960 h (bộ đếm riêng với 拘束) | S5 | BE | 8 | 15 | firm | Todo |
| [EP04-I16](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/632) Đầu vào 始業 / 終業 từ 出発 / 帰着 và số dư đầu kỳ cho timeline | S5 | BE | 9 | 16 | firm | Todo |
| [EP04-I17](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/636) Kiểm hợp lý giờ thiết bị (CK-1〜CK-4) cho 出発 / 帰着 / POD / 例外事 | S5 | BE | 6 | 11 | firm | Todo |
| [EP04-I18](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/639) シール番号確認 trên app tài xế (online / offline) và báo lệch | S4 | BE | 9 | 16 | firm | Todo |
| [EP04-I19](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/643) 出発 / 帰着 trên app tài xế, đổi route.status, cổng 出荷確認 | S4 | BE | 9 | 16 | firm | Todo |
| [EP04-I20](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/647) 例外事象 bất biến và 計画超過スロット tách khỏi kết quả tuân thủ | S5 | BE | 11 | 20 | firm | Todo |
| [EP04-I21](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/651) Màn SCR-07 View 1 ルート作成 và View 3 公開・版履歴 | ST | FE | 11 | 20 | firm | Todo |
| [EP04-I22](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/655) Màn SCR-07 View 2 拘束時間チェック | S5 | FE | 7 | 13 | firm | Todo |
| [EP04-I23](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/658) Lịch trình tài xế SCR-08 View 1 (版 mới nhất, 2 chuyến / ngày | S4 | BE | 10 | 18 | firm | Todo |

## EP-06 トレーサビリティ・回収 — truy vết lô và recall — 135 SWP / 250 h

| Issue | Sprint | Role | SWP | Giờ | Độ tin | Trạng thái |
|---|---|---|---:|---:|---|---|
| [EP06-I01](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/663) Dựng màn SCR-11 トレーサビリティ検索 | S6 | FE | 13 | 24 | provisional | Todo |
| [EP06-I02](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/667) Xây API truy vết thượng / hạ nguồn theo lô, 仕入先ロット, SKU, nhà | S6 | BE | 8 | 15 | provisional | Todo |
| [EP06-I03](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/668) Xây lane 牛: tìm theo 牛個体識別番号 và trả đủ giao dịch | S6 | BE | 5 | 10 | provisional | Todo |
| [EP06-I04](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/669) Xây lane 米: hiển thị đủ trường truy xuất BR-TRACE-01 | S6 | BE | 3 | 6 | provisional | Todo |
| [EP06-I05](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/670) Xây lane 社内ロット và hai loại 終端 | S6 | BE | 5 | 10 | provisional | Todo |
| [EP06-I06](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/671) Đạt truy vết lô 3 năm ≤ 60 giây | S6 | BE | 10 | 18 | placeholder | Todo |
| [EP06-I07](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/672) Hiển thị bản ghi truy vết migrate (legacy_trace_record) | S6 | BE | 5 | 10 | provisional | Todo |
| [EP06-I08](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/673) Dựng màn SCR-12 phần recall (View 1 danh sách ca, View 2 ca  | S6 | FE | 13 | 24 | provisional | Todo |
| [EP06-I09](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/677) Mở ca recall và chốt phạm vi (scoped) với 範囲版 1 | S6 | BE | 5 | 10 | provisional | Todo |
| [EP06-I10](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/679) Tự 隔離 lô trong phạm vi và giải phóng 引当 khi scoped | S6 | BE | 10 | 18 | placeholder | Todo |
| [EP06-I11](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/680) Đổi phạm vi recall thành 範囲版 n+1 và bắt buộc 取消通知 | S6 | BE | 10 | 18 | provisional | Todo |
| [EP06-I12](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/681) Xây bảng đối chiếu hai đẳng thức và đóng ca recall | S6 | BE | 5 | 10 | provisional | Todo |
| [EP06-I13](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/683) Xây thông báo recall có phiên bản, duyệt hai người và gửi qu | S6 | BE | 5 | 10 | provisional | Todo |
| [EP06-I14](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/685) Xây tác vụ ca recall và cột 担当 / 期限 | S6 | BE | 4 | 8 | provisional | Todo |
| [EP06-I15](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/686) Xây 取消 và 再開 ca recall | S6 | BE | 5 | 10 | provisional | Todo |
| [EP06-I16](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/688) Xây 保全依頼 từ ca recall theo người gửi (X-8 (a)) | S6 | BE | 5 | 10 | provisional | Todo |
| [EP06-I17](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/690) Xuất RPT-21 リコール追跡票 (PDF) | S6 | BE | 5 | 10 | provisional | Todo |
| [EP06-I18](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/691) Xuất RPT-20 POD・クレーム票 (PDF) | S6 | BE | 5 | 10 | provisional | Todo |
| [EP06-I19](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/692) Kiểm thiết bị PC và MFA cho thao tác duyệt recall ở server | S6 | BE | 6 | 11 | provisional | Todo |
| [EP06-I20](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/693) Kiểm thử luồng truy vết / recall theo ACC-TRC-01 | S6 | QA | 8 | 15 | provisional | Todo |

## EP-07 報告・KPI — 12 báo cáo vận hành và audit export — 135 SWP / 250 h

| Issue | Sprint | Role | SWP | Giờ | Độ tin | Trạng thái |
|---|---|---|---:|---:|---|---|
| [EP07-I01](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/695) Dựng màn SCR-13 運用レポート/KPI | S6 | FE | 12 | 22 | provisional | Todo |
| [EP07-I02](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/699) Xây danh mục báo cáo, 閲覧ロール và 基準日時 | S6 | BE | 5 | 10 | provisional | Todo |
| [EP07-I03](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/700) Xây xuất CSV chung có manifest và nhật ký | S6 | BE | 6 | 11 | provisional | Todo |
| [EP07-I04](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/701) Xây batch B-06 kpi_daily và job dọn export dở | S6 | BE | 5 | 10 | provisional | Todo |
| [EP07-I05](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/703) Xây RPT-02 期限接近 theo hạn giao hợp đồng | S6 | BE | 6 | 11 | provisional | Todo |
| [EP07-I06](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/704) Xây RPT-10 ドライバー遵守 có cột 事象起因 tách riêng | S6 | BE | 6 | 11 | provisional | Todo |
| [EP07-I07](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/705) Xây RPT-04 HACCP欠落 | S6 | BE | 5 | 10 | provisional | Todo |
| [EP07-I08](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/706) Xây RPT-05 温度逸脱 | S6 | BE | 5 | 10 | provisional | Todo |
| [EP07-I09](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/707) Xây RPT-06 アラームSLA (review trong 15 phút) | S6 | BE | 5 | 10 | provisional | Todo |
| [EP07-I10](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/708) Xây RPT-01 期限別在庫 tách 賞味 / 消費 | S6 | BE | 5 | 10 | provisional | Todo |
| [EP07-I11](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/709) Xây RPT-03 隔離 và RPT-07 受入差異 | S6 | BE | 8 | 15 | provisional | Todo |
| [EP07-I12](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/710) Xây RPT-08 配送実績 và RPT-09 POD完全性 | S6 | BE | 8 | 15 | provisional | Todo |
| [EP07-I13](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/711) Xây RPT-11 リコール照合 | S6 | BE | 6 | 11 | provisional | Todo |
| [EP07-I14](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/712) Xây RPT-12 監査変更履歴 (chỉ xem) | S6 | BE | 3 | 6 | provisional | Todo |
| [EP07-I15](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/713) Dựng màn SCR-15 監査ログ検索 | S6 | FE | 11 | 20 | provisional | Todo |
| [EP07-I16](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/717) Xây API tìm và xem nhật ký kiểm toán chỉ đọc | S6 | BE | 5 | 10 | provisional | Todo |
| [EP07-I17](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/718) Xây tạo gói RPT-13 監査エクスポート có manifest SHA-256 | S6 | BE | 5 | 10 | provisional | Todo |
| [EP07-I18](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/720) Xây 再作成して照合 cho gói RPT-13 | S6 | BE | 6 | 11 | provisional | Todo |
| [EP07-I19](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/721) Xây 依頼 Legal hold / アーカイブ từ SCR-15 | S6 | BE | 5 | 10 | provisional | Todo |
| [EP07-I20](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/723) Chạy nền cho CSV lớn và gói RPT-13 | S6 | BE | 10 | 18 | provisional | Todo |
| [EP07-I21](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/724) Kiểm thử báo cáo và audit export | S6 | QA | 8 | 15 | provisional | Todo |

## EP-11 法令再検証 — xác minh lại nguồn pháp lý (OPS-LAW-01) — 31 SWP / 58 h

| Issue | Sprint | Role | SWP | Giờ | Độ tin | Trạng thái |
|---|---|---|---:|---:|---|---|
| [EP11-I01](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/726) Xác minh lại giá trị 改善基準告示 cho ルール版 giờ lái | P10 | BrSE | 5 | 10 | provisional | Todo |
| [EP11-I02](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/727) Chốt 36協定 và ngoại lệ giờ lái áp cho tài xế Yuki | P10 | BrSE | 5 | 10 | provisional | Todo |
| [EP11-I03](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/728) Kiểm lại phạm vi 米トレサ法 / 牛トレサ法 áp cho Yuki | P10 | BrSE | 3 | 6 | provisional | Todo |
| [EP11-I04](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/729) Xác định mức HACCP Yuki áp dụng và 手引書 tham chiếu | P10 | BrSE | 3 | 6 | provisional | Todo |
| [EP11-I05](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/730) Xác minh định nghĩa 賞味期限 / 消費期限 theo quy định ghi nhãn | P10 | BrSE | 3 | 6 | provisional | Todo |
| [EP11-I06](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/731) Xác nhận 1/3・1/2 là tập quán hợp đồng, không phải luật | P10 | BrSE | 1 | 2 | provisional | Todo |
| [EP11-I07](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/732) Xác minh thời hạn lưu hồ sơ và nghĩa vụ dữ liệu (L-1…L-6) | P10 | BrSE | 5 | 10 | provisional | Todo |
| [EP11-I08](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/733) Đóng gói bằng chứng pháp lý cho DR đóng băng thiết kế | P10 | PM | 3 | 6 | provisional | Todo |
| [EP11-I09](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/734) Kiểm lại nguồn pháp lý trước go / no-go | UAT | BrSE | 3 | 6 | provisional | Todo |

## EP-12 データ移行 — migration 6 nguồn có lineage và đối soát — 106 SWP / 196 h

| Issue | Sprint | Role | SWP | Giờ | Độ tin | Trạng thái |
|---|---|---|---:|---:|---|---|
| [EP12-I01](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/736) Thiết kế chi tiết migration: job B-13, lineage, mapping 6 ng | S3 | SA | 10 | 18 | placeholder | Todo |
| [EP12-I02](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/739) Xây khung job migration có lineage một dòng / dòng thô | S4 | BE | 10 | 18 | provisional | Todo |
| [EP12-I03](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/740) Profile dữ liệu nguồn và chạy workshop mapping với データオーナー | S4 | BrSE | 5 | 10 | placeholder | Todo |
| [EP12-I04](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/741) Xây loader MIG.1 master (SKU / 顧客 / 仕入先) | S4 | BE | 5 | 10 | provisional | Todo |
| [EP12-I05](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/742) Xây loader MIG.2 lô và tồn theo zone | S5 | BE | 6 | 11 | provisional | Todo |
| [EP12-I06](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/743) Chuẩn hóa lịch sử xuất 3 năm (ngày nhiều định dạng, hạn trốn | S5 | BE | 6 | 11 | provisional | Todo |
| [EP12-I07](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/744) Nạp lịch sử xuất làm mốc 日付逆転 và ánh xạ mã khách đổi | S5 | BE | 10 | 18 | placeholder | Todo |
| [EP12-I08](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/745) Xây loader MIG.4 dữ liệu nhiệt độ ~2,5 triệu bản ghi | S5 | BE | 9 | 16 | provisional | Todo |
| [EP12-I09](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/746) Xây loader MIG.7 tệp 米原産地 và 牛個体識別番号 | S5 | BE | 3 | 6 | provisional | Todo |
| [EP12-I10](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/747) Xây loader MIG.5 chỉ mục route / POD | S6 | BE | 6 | 11 | provisional | Todo |
| [EP12-I11](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/748) Xuất RPT-15 移行照合レポート từ lineage | S5 | BE | 5 | 10 | provisional | Todo |
| [EP12-I12](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/749) Chạy dry run migration trên môi trường test | S6 | BE | 8 | 15 | provisional | Todo |
| [EP12-I13](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/750) Chạy rehearsal 1 và đối soát | S6 | BE | 10 | 18 | provisional | Todo |
| [EP12-I14](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/751) Lấy chữ ký danh sách ngoại lệ sau rehearsal 1 và sửa dữ liệu | HARD | BrSE | 3 | 6 | provisional | Todo |
| [EP12-I15](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/752) Chạy rehearsal 2 và quyết định nạp lần cuối | UAT | BE | 10 | 18 | provisional | Todo |

## EP-13 カットオーバー・UAT・教育・ハイパーケア — 90 SWP / 167 h

| Issue | Sprint | Role | SWP | Giờ | Độ tin | Trạng thái |
|---|---|---|---:|---:|---|---|
| [EP13-I01](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/754) Lập kế hoạch UAT 6 tuần theo kịch bản R-06 | ST | QA | 4 | 8 | provisional | Todo |
| [EP13-I02](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/755) Chuẩn bị môi trường UAT, tài khoản theo 職務 và dữ liệu mask | ST | Infra | 5 | 10 | provisional | Todo |
| [EP13-I03](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/756) Hỗ trợ UAT đợt 1 (04-05 → 04-16) | UAT | QA | 4 | 8 | provisional | Todo |
| [EP13-I04](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/757) Hỗ trợ UAT đợt 2 (04-19 → 04-30) cùng rehearsal 2 | UAT | QA | 4 | 8 | provisional | Todo |
| [EP13-I05](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/758) Hỗ trợ UAT đợt 3 (05-03 → 05-14) và biên bản G5 nghiệp vụ | UAT | QA | 4 | 8 | provisional | Todo |
| [EP13-I06](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/759) Dựng khung đào tạo: sandbox mask, bài kiểm tra, hồ sơ đào tạ | UAT | BrSE | 4 | 8 | provisional | Todo |
| [EP13-I07](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/760) Soạn tài liệu đào tạo nhóm 倉庫 và 品質 | UAT | BrSE | 4 | 8 | provisional | Todo |
| [EP13-I08](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/761) Soạn tài liệu đào tạo nhóm 配車 và ドライバー | UAT | BrSE | 4 | 8 | provisional | Todo |
| [EP13-I09](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/762) Soạn tài liệu đào tạo nhóm CS / クレーム, 管理者 / サポート, 監査 | UAT | BrSE | 4 | 8 | provisional | Todo |
| [EP13-I10](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/763) Tổ chức đào tạo 7 nhóm và kiểm tra (05-17 → 05-21) | CUT | BrSE | 4 | 8 | provisional | Todo |
| [EP13-I11](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/764) Viết runbook cutover và hàng đợi đơn thủ công khi đóng băng  | UAT | SA | 5 | 10 | provisional | Todo |
| [EP13-I12](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/765) Diễn tập rollback trên UAT | UAT | Infra | 6 | 11 | provisional | Todo |
| [EP13-I13](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/766) Đóng băng master T-5 ngày (05-27) | CUT | PM | 2 | 4 | provisional | Todo |
| [EP13-I14](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/767) Đóng băng đơn T-8 giờ, trích xuất cuối, nạp lần cuối và đối  | CUT | BE | 15 | 28 | provisional | Todo |
| [EP13-I15](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/768) Smoke test E2E sau nạp với 6 owner | CUT | QA | 4 | 8 | provisional | Todo |
| [EP13-I16](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/769) Họp go / no-go và lấy chữ ký 6 owner (ACC-GO-01) | CUT | PM | 3 | 6 | provisional | Todo |
| [EP13-I17](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/770) Giám sát chạy song song 1 tuần (hệ cũ chỉ đọc) | HYP | BrSE | 5 | 10 | provisional | Todo |
| [EP13-I18](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/771) Hypercare tuần 1–2: trực sự cố và báo cáo SLA | HYP | BE | 5 | 10 | provisional | Todo |
| [EP13-I19](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/772) Hypercare tuần 3–4 và bàn giao vận hành (PLAN-B7) | HYP | PM | 4 | 8 | placeholder | Todo |

## EP-14 QA自動化 — bộ R-06, E2E và hồi quy — 60 SWP / 111 h

| Issue | Sprint | Role | SWP | Giờ | Độ tin | Trạng thái |
|---|---|---|---:|---:|---|---|
| [EP14-I01](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/774) Dựng khung test tự động E2E / API trong CI | S3 | QA | 5 | 10 | provisional | Todo |
| [EP14-I02](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/775) Nạp fixture R-06 vào bộ test | S3 | QA | 3 | 6 | placeholder | Todo |
| [EP14-I03](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/776) Tự động hóa ca 温度boundary | S5 | QA | 3 | 6 | provisional | Todo |
| [EP14-I04](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/777) Tự động hóa ca hai loại hạn (賞味 / 消費) | S4 | QA | 3 | 6 | provisional | Todo |
| [EP14-I05](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/778) Tự động hóa ca 日付逆転 (date reversal) | S4 | QA | 3 | 6 | provisional | Todo |
| [EP14-I06](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/779) Tự động hóa ca route infeasible (giờ lái 2024) | S6 | QA | 5 | 10 | placeholder | Todo |
| [EP14-I07](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/780) Tự động hóa ca rice / beef (trường truy xuất có kiểu và tìm  | S6 | QA | 3 | 6 | provisional | Todo |
| [EP14-I08](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/781) Tự động hóa ca POD term (車上渡し / 軒先渡し) | S5 | QA | 3 | 6 | provisional | Todo |
| [EP14-I09](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/782) Tự động hóa ca dirty migration | S6 | QA | 3 | 6 | provisional | Todo |
| [EP14-I10](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/783) Tự động hóa ca FEFO nhiều lô cùng SKU | S4 | QA | 3 | 6 | provisional | Todo |
| [EP14-I11](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/784) Tự động hóa ca cửa sổ giao theo 顧客-SKU | S4 | QA | 3 | 6 | provisional | Todo |
| [EP14-I12](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/785) Tự động hóa ca 牛個体識別番号 sai định dạng | S6 | QA | 3 | 6 | provisional | Todo |
| [EP14-I13](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/786) Tự động hóa E2E luồng kho ACC-FUN-01 | HARD | QA | 8 | 15 | provisional | Todo |
| [EP14-I14](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/787) Chạy hồi quy toàn bộ ở Hardening / ST và lập TR | HARD | QA | 8 | 15 | provisional | Todo |
| [EP14-I15](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/788) Chạy hồi quy cho mỗi bản sửa trong UAT | UAT | QA | 4 | 8 | provisional | Todo |

## EP-15 Quản lý dự án / BrSE — 64 SWP / 118 h

| Issue | Sprint | Role | SWP | Giờ | Độ tin | Trạng thái |
|---|---|---|---:|---:|---|---|
| [EP15-I01](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/790) Dựng khung quản trị: báo cáo tuần, RAID, decision log, CR bo | P10 | PM | 4 | 8 | provisional | Todo |
| [EP15-I02](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/791) Báo cáo tuần và RAID giai đoạn 1.0 – S0 | P10 | PM | 4 | 8 | provisional | Todo |
| [EP15-I03](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/792) Báo cáo tuần và RAID S1–S2 | S5 | PM | 4 | 8 | provisional | Todo |
| [EP15-I04](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/793) Báo cáo tuần và RAID S3–S4 (bắt đầu 移行) | ST | PM | 4 | 8 | provisional | Todo |
| [EP15-I05](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/794) Báo cáo tuần và RAID S5–S6 (rehearsal 1) | S6 | PM | 4 | 8 | provisional | Todo |
| [EP15-I06](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/795) Báo cáo tuần và RAID Hardening – ST (G4, G5 kỹ thuật) | ST | PM | 4 | 8 | provisional | Todo |
| [EP15-I07](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/796) Báo cáo tuần và RAID giai đoạn UAT (G5 nghiệp vụ) | UAT | PM | 4 | 8 | provisional | Todo |
| [EP15-I08](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/797) Báo cáo hằng ngày khi cutover và báo cáo hypercare | HYP | PM | 4 | 8 | provisional | Todo |
| [EP15-I09](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/798) Gửi và theo dõi lô Q&A 69 câu, chốt CR lab4 | P10 | BrSE | 6 | 11 | provisional | Todo |
| [EP15-I10](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/799) Theo dõi câu hỏi chặn trước S4 (dữ liệu 移行, layout IF, pháp  | HARD | BrSE | 3 | 6 | placeholder | Todo |
| [EP15-I11](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/800) Q&A với khách và dịch phản hồi trong UAT | UAT | BrSE | 4 | 8 | provisional | Todo |
| [EP15-I12](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/801) Re-estimate bottom-up bằng SWP và so với bidding | P10 | PM | 6 | 11 | provisional | Todo |
| [EP15-I13](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/802) Cập nhật PREMISE và baseline sau re-estimate và Q&A | P10 | BrSE | 3 | 6 | provisional | Todo |
| [EP15-I14](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/803) Cập nhật PREMISE, RTM và ma trận tuân thủ trước G4 | HARD | BrSE | 4 | 8 | provisional | Todo |
| [EP15-I15](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/804) Tổ chức demo cách tuần và review với khách S1–S3 | S3 | BrSE | 3 | 6 | provisional | Todo |
| [EP15-I16](https://github.com/linhvtm-2475/yuki-wms-backlog/issues/805) Tổ chức demo cách tuần và review với khách S4–S6 | S6 | BrSE | 3 | 6 | provisional | Todo |

