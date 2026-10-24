# Yuki Cold Chain WMS — Backlog phát triển (bài thực hành LAB-5)

Backlog cho hệ thống quản lý kho lạnh 3 dải nhiệt của một công ty logistics **hư cấu**. Backlog được break từ detail design và basic design của bài thực hành.

- **Board:** GitHub Project gắn với repo này. Có các trường Status, Iteration (sprint 2 tuần), Role, SWP, Hours.
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
| `docs/wbs-master-schedule.md` | WBS master schedule: milestone theo tháng (bổ sung sau khi chấm SWP) |
| `docs/wbs-detail.md` | WBS chi tiết theo sprint (bổ sung sau khi chấm SWP) |
| `docs/hours-convention.md` | Cách quy SWP ra giờ và lý do (bổ sung sau khi chấm SWP) |
| `reports/` | Báo cáo SWP và báo cáo tiến độ sprint giả lập |

## Lưu ý
- Dữ liệu và khách hàng đều là **giả lập** cho mục đích học tập.
- Repo chỉ chứa issue và markdown do người làm bài tự viết. Không chép tài liệu đề, không có dữ liệu thật hay dữ liệu cá nhân, không có khóa bí mật.
- Hệ đích giả định là Azure (App Service modular monolith, PostgreSQL). Lịch giả định từ 2026-11 đến Go-Live 2027-06.
