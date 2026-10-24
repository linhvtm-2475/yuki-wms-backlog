# AI-report — LAB-5 (break task, SWP, Project, sprint giả lập)

Ghi lại cách làm việc với AI (Claude Code + skill Takumi) cho LAB-5: dùng công cụ nào, AI sai ở đâu, phát hiện và sửa thế nào, và cách ghi SWP đã chốt vào Project.

## 1. Công cụ và skill theo bước

| Bước | Công cụ / skill | Ghi chú |
|---|---|---|
| Chọn skill | `/tkm:help` | Chọn `/tkm:sun-estimate` cho SWP. Loại `/tkm:estimate`, vì skill đó ước man-day theo spec chứ không chấm issue |
| Rủi ro trước khi chấm | `/tkm:brainstorm` | Chọn cách "phân tầng độ tin": nhãn `estimate:firm/provisional/placeholder` |
| Break backlog | 4 sub-agent song song (nhóm A–D) + quy ước chung `docs/breakdown-conventions.md` | Mỗi agent ghi đúng 1 file JSON |
| Gộp, kiểm | `scripts/merge-and-validate-backlog.py` | Kiểm ID trùng, mục Định nghĩa xong, role / sprint, phụ thuộc, luật public (`@`, chuỗi tiếng Nhật dài, mẫu khóa) |
| Đăng GitHub | `gh` CLI + GraphQL qua `scripts/publish-backlog-to-github.py` | Chạy lại được nhiều lần (lưu `backlog/github-map.json`); có thử lại khi bị giới hạn tốc độ hoặc rớt mạng |
| Chấm SWP | `/tkm:sun-estimate` (+ `/tkm:confidence`, 1 lần `/tkm:ask-expert`) | 611 work item, 5 worker song song, 5 issue mẫu do Linh kiểm |
| Ghi SWP, giờ | `scripts/write-swp-hours-to-project.py` | Xem mục 3 |
| Cân sprint | `scripts/rebalance-sprints-by-capacity.py` | Dời 37 issue; không dời issue `domain:*`, chuỗi D-A, và issue có phụ thuộc |
| Sprint giả lập | `scripts/apply-sprint-simulation.py` | Status, đóng issue, comment lý do trễ |
| Báo cáo | `scripts/build-sprint-progress-report.py`, `scripts/build-wbs-outputs.py` | Số đọc từ Project / backlog, không nhập tay |

## 2. AI sai ở đâu và phát hiện thế nào

| # | AI sai / thiếu | Phát hiện bằng | Sửa |
|---|---|---|---|
| 1 | Worker `sun-estimate-worker` được thiết kế không có tool, nên không đọc được batch. Cả 5 worker trả lỗi | Báo cáo của chính worker (worker không bịa điểm) | Chuyển sang sub-agent `general-purpose`, prompt chỉ cho đọc 3 file và ghi 1 file. Sai lệch so với contract được ghi ở caveat của báo cáo HTML |
| 2 | Mức chấm lệch giữa các batch: "Viết DD" 3 SWP (batch 001) và 5 SWP (batch 003/004); "Review" 1–3 SWP | Thống kê SWP theo loại việc sau khi gộp | Hiệu chỉnh của skill chỉ lan sang issue có đúng cùng nhóm phân loại, nên không tự sửa đồng loạt. Ghi vào giới hạn; chấm lại sau khi có velocity thật |
| 3 | 4 nhóm break làm trùng phần dùng chung: đánh giá dải nhiệt (EP00-I19 ↔ EP01-I05), ルール版 (EP00-I20 ↔ EP04-I04) | Grep chéo tiêu đề theo từ khóa khi gộp | Ghi ranh giới và phụ thuộc vào `backlog/merge-overrides.json` |
| 4 | Sub-issue xếp sprint muộn hơn issue cha (EP03-I26) | Cảnh báo của script gộp | Dời issue cha sang S4 |
| 5 | Script đăng dừng: issue đã nằm sẵn trong Project (GitHub tự thêm khi liên kết sub-issue) | Lỗi `Content already exists` | Lấy ID item cũ bằng GraphQL thay vì báo lỗi |
| 6 | Sprint quá tải tới 173% (QA viết TC cho mọi issue) | Tính tải theo SWP × giờ so với FTE plan | Linh chọn hướng kết hợp: +1 QA, +1 BE, dời 37 issue. S6 vẫn 135%, ghi là rủi ro |
| 7 | Số giờ SWP (551 MD) trông "rẻ" hơn bidding (789 MD) | So theo epic | Ghi rõ hai con số không cùng gốc (`docs/hours-convention.md` §3); không dùng để báo khách |
| 8 | Issue-register bị trùng mã ISS-36 với phiên khác | Kiểm trùng ID sau khi ghi | Đổi sang mã trống kế tiếp |

## 3. Cách ghi SWP đã chốt vào trường point của Project

1. `/tkm:sun-estimate` chỉ đọc và chỉ xuất `reports/swp-estimate-261024.html`. Payload đã hiệu chỉnh (`backlog/swp-calibrated-payload.json`) là nguồn duy nhất.
2. Linh kiểm 5 issue mẫu, hai vòng mỗi issue (mức khó → số SWP). #142 được sửa từ 3 lên 6 SWP, chỉ áp riêng issue này, có lý do kèm trích dẫn từ `/tkm:ask-expert`.
3. AI agent (Claude Code) chạy `scripts/write-swp-hours-to-project.py`:
   - Mục lá: `finalSWP` lấy từ payload.
   - Issue có sub-issue và epic: **tổng SWP của con**, không tra lại ma trận.
   - `Hours = SWP × 76/41 ≈ 1,85`, làm tròn 0,5 h.
   - Ghi bằng `gh project item-edit --field-id <SWP|Hours> --number …`. Script lưu lại tiến độ (`backlog/swp-hours-pushed.json`), nên chạy lại không ghi đè lung tung.
4. Kiểm sau khi ghi: đọc lại bằng `gh project item-list`, tổng SWP lá phải bằng 2.378 như trong báo cáo HTML.

## 4. Quy giờ
Cách làm và lý do ở `docs/hours-convention.md`: hệ số lấy từ 5 issue mẫu (76 h / 41 SWP), contingency theo độ tin tính riêng, có so với LAB-1.

## 5. Giới hạn
- Sprint S1 là **giả lập** (`backlog/sprint-s1-simulation.json`). Burndown thực tế là chuỗi số trong kịch bản; không có lịch sử thật trên GitHub.
- Hệ số giờ lấy từ 5 mẫu, nên sai số lớn. Sau sprint thật phải thay bằng velocity.
