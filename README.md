# Yuki Cold Chain WMS — Backlog phát triển (bài thực hành LAB-5)

Backlog cho hệ thống quản lý kho lạnh 3 dải nhiệt của một công ty logistics **hư cấu**. Backlog được break từ detail design và basic design của bài thực hành.

## Repo liên quan

| Repo | Vai trò |
|---|---|
| [`AIDD-lab1-Linh`](https://github.com/linhvtm-2475/AIDD-lab1-Linh) (management) | 基本設計 đã duyệt — nguồn sự thật nghiệp vụ/DB/API |
| `yuki-wms-backlog` (repo này) | Epic/Story/Sub-task/Bug/CR — theo dõi tiến độ |
| [`yuki-wms-app`](https://github.com/linhvtm-2475/yuki-wms-app) | Code thật (Azure, Sprint 0 trở đi) — cùng link vào **GitHub Project #1** với repo này |

- **Board:** GitHub Project #1, gắn với cả repo này lẫn `yuki-wms-app`. Có các trường Status, Iteration (sprint 2 tuần), Role, SWP, Hours, Actual Hours, Loại task, Loại bug, Nguyên nhân gốc, Mức độ.
- **Cấu trúc:**
  - **Epic** (16): `EP-00` nền tảng, `EP-01`…`EP-14` theo nhóm chức năng, `EP-15` quản lý.
  - **Issue** (306): một kết quả kiểm được, ≤ 1 sprint cho 1 người.
  - **Sub-issue** (483): một việc của một vai, ≤ 2 ngày công.
- **Ràng buộc nghiệp vụ đặc thù** được tách thành issue riêng, gắn nhãn `domain:*`:
  - giới hạn giờ lái xe tải từ 2024 (`domain:duty-hours-2024`)
  - cấm giao lô có hạn cũ hơn lô đã giao cho cùng khách (`domain:date-reversal`)
  - hai loại hạn dùng (`domain:expiry-type`)
  - quy tắc hạn giao theo tập quán (`domain:delivery-window`)
  - truy xuất bắt buộc cho gạo / thịt bò (`domain:traceability-rice-beef`)
  - ngưỡng 3 dải nhiệt có version (`domain:temp-band`)
  - HACCP (`domain:haccp`)

## Tài liệu trong repo
| File | Nội dung |
|---|---|
| [docs/breakdown-conventions.md](docs/breakdown-conventions.md) | Quy ước break: kích cỡ issue, Định nghĩa xong, nhãn, sprint |
| [docs/differences-vs-lab4.md](docs/differences-vs-lab4.md) | Mọi chỗ backlog break khác detail design LAB-4 đã nộp, kèm lý do |
| [docs/spec-gaps.md](docs/spec-gaps.md) | Chỗ hở / mâu thuẫn của spec phát hiện khi break |
| [docs/wbs-master-schedule.md](docs/wbs-master-schedule.md) · [xlsx](reports/wbs-master-schedule.xlsx) | WBS master schedule: giai đoạn / gate và giờ epic × tháng (10/2026 → 06/2027) |
| [docs/wbs-detail.md](docs/wbs-detail.md) · [xlsx](reports/wbs-detail.xlsx) | WBS chi tiết: epic → issue → sub-issue, sprint, role, SWP, giờ, độ tin, trạng thái |
| [docs/hours-convention.md](docs/hours-convention.md) | Cách quy SWP ra giờ (1,85 h/SWP), contingency, so với estimate LAB-1 |
| [docs/sprint-capacity.md](docs/sprint-capacity.md) | Năng lực và tải từng sprint sau khi cân |
| [reports/swp-estimate-261024.html](reports/swp-estimate-261024.html) | Báo cáo SWP của `/tkm:sun-estimate` (tải về để mở) |
| [reports/progress-report-sprint-S1.md](reports/progress-report-sprint-S1.md) | Báo cáo tiến độ sprint S1 (giả lập) lấy từ Project |
| [AI-report.md](AI-report.md) | Cách làm với AI, chỗ AI sai, cách ghi SWP vào Project |

## Lưu ý
- Dữ liệu và khách hàng đều là **giả lập** cho mục đích học tập.
- Repo chỉ chứa issue và markdown do người làm bài tự viết. Không chép tài liệu đề, không có dữ liệu thật hay dữ liệu cá nhân, không có khóa bí mật.
- Hệ đích giả định là Azure (App Service modular monolith, PostgreSQL). Lịch giả định từ 2026-11 đến Go-Live 2027-06.
