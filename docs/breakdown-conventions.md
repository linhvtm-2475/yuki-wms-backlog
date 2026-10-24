# Quy ước break backlog (LAB-5) — dùng chung cho mọi người break

## 1. Nguồn break (theo thứ tự ưu tiên)
1. **Detail design LAB-4 đã nộp** (`yuki-wms-prototype/docs/lab4/`):
   - `03-detail-design/SCR-01, 05, 06, 07, 08, 09_DETAIL.md`
   - `02-architecture.md`, `04-adr/*`, `05-database/*`, `PREMISE.md`
   - `README.md`: bảng gap và thứ tự đợt 0–3
2. **Basic design đã duyệt** (`yuki-cold-chain-wms-2360-management/`):
   - `specs/**` (spec màn và 帳票, `_common/`, DB), `business-flows/**`
   - Dùng cho 12 màn chưa có DD và cho batch, IF, NFR.
3. **Quyết định giai đoạn phát triển:** `process-trail/plans/plan-261024-dev-phase-wbs.md` (APV-021).
   - D-1: hệ đích là Azure (App Service modular monolith, PostgreSQL Flexible, Entra ID, Service Bus/Functions, Blob WORM, Key Vault, Maps, DR Japan West).
   - D-3: **không dùng lại prototype**, viết mới.
4. **Estimate LAB-1** (`inputs/customer/breakdown/breakdown-v2.json`): chỉ dùng để ghi mã story bidding `S{n}.{m}` cho truy vết. Không chép MD vào issue.
5. **Việc đang hoãn** (`process-trail/issue-register.md` ISS-35): H-5, H-6, H-7 chưa chốt. Issue chạm vào các mục này gắn nhãn `blocked:ISS-35`.

## 2. Biến đổi so với LAB-4 (bắt buộc khai, không âm thầm đổi)
- Task **"sửa gap prototype"** của LAB-4 (L5-DB-xx, T07-xx, T08-xx, OUT-*, REC-*, TMP-*, SEC-*) → đổi thành task **xây mới** trên Azure. Giữ mã LAB-4 trong mục `Nguồn` để truy vết.
- ADR-002 (logic trong Postgres RPC + RLS chỉ đọc) và ADR-012 (Vercel/Supabase): **không dùng làm tiền đề**. Logic nghiệp vụ nằm ở App Service (modular monolith). PostgreSQL vẫn giữ ràng buộc, khóa và transaction. Chỗ nào DD dựa vào RPC / RLS / Supabase Auth / PostgREST thì ghi vào danh sách `differences` kèm cách hiểu mới.
- ADR-001, ADR-003…ADR-011 là quyết định nghiệp vụ / kỹ thuật độc lập nền tảng → giữ nguyên.
- Mỗi khác biệt ghi một dòng: `{lab4_ref, thay đổi, lý do (D-1/D-3/APV…), ảnh hưởng backlog}`.

## 3. Cấu trúc và kích cỡ
- **Epic** = nhóm theo Epic bidding:
  - `EP-00` Nền tảng (Azure, CI/CD, khung app, auth, thứ tự khóa, idempotency, bảng quy tắc có version, catalog mã thông điệp, audit)
  - `EP-01`…`EP-14` khớp E1…E14
  - `EP-15` Quản lý / BrSE
- **Issue** = một kết quả kiểm được: một chức năng, một quy tắc, một API hoặc một màn.
  - Làm xong trong **≤ 1 sprint bởi 1 người**, khoảng ≤ 5 ngày công.
  - Lớn hơn thì tách theo SPIDR.
- **Sub-issue** = một việc của một vai: DD / TC / DB / BE / FE / IaC / review.
  - **≤ 2 ngày công.**
  - Chỉ bắt buộc cho issue có DD (6 màn + kiến trúc / ADR / DB). Issue không có DD thì có thể không có sub-issue, nhưng phải có 1 sub-issue "Viết DD" khi issue đó là màn hoặc luồng.
- **Không gộp** các hạng mục chịu ràng buộc nghiệp vụ đặc thù vào issue chung. Mỗi ràng buộc là issue riêng, gắn nhãn `domain:*`:
  - `domain:duty-hours-2024` (拘束時間 / 改善基準告示)
  - `domain:date-reversal` (日付逆転禁止 theo lịch sử giao)
  - `domain:expiry-type` (賞味 / 消費)
  - `domain:delivery-window` (1/3・1/2, là tập quán thương mại)
  - `domain:traceability-rice-beef` (米・牛 bắt buộc)
  - `domain:temp-band` (ngưỡng 3 dải có version)
  - `domain:haccp`

## 4. Nội dung mỗi issue / sub-issue (tự viết, KHÔNG chép đoạn RFP hay đề)
- `title`: tiếng Việt, ngắn, động từ + đối tượng. Thuật ngữ nghiệp vụ tiếng Nhật giữ nguyên (日付逆転, 拘束時間…), nhưng **không chép nguyên câu** từ RFP / spec.
- `body` gồm các mục:
  - **Mục tiêu** (1–2 câu)
  - **Phạm vi**: làm gì, không làm gì
  - **Nguồn**: đường dẫn tương đối `DD:SCR-05 §4.2`, `SPEC:SCR-02`, `DB:OUT_DB R4a`, `ADR-003`, `LAB4:OUT-ALLOC-03`, `bidding:S3.2` — chỉ là con trỏ, không chép nội dung
  - **Định nghĩa xong** (checklist 3–6 dòng, kiểm được; với BE/FE có test đi kèm)
  - **Phụ thuộc** (ID issue khác)
  - **Ràng buộc nghiệp vụ** (nếu có)
  - **Spec gap** (ID nếu có)
- `role`: một trong `BE`, `FE`, `QA`, `Infra`, `BrSE`, `PM`, `SA`
- `sprint`: một trong `S0`, `S1`…`S6`, `HARD`, `ST`, `UAT`, `CUT`, `HYP`, theo lịch ở plan §7 và §8. Thứ tự: nền trước, bẫy nghiệp vụ sớm, DD đi trước code 1 sprint.
- `labels`: `type:epic|issue|sub-issue`, `role:*`, `domain:*`, `dd:yes|no`, `blocked:ISS-35`, `spec-gap`
- **Không** ghi SWP / giờ. Phần này chấm sau bằng `/tkm:sun-estimate`.

## 5. Spec gap (chỗ hở / mâu thuẫn phát hiện khi break)
Mỗi gap ghi một dòng: `{id GAP-xx-nn, file:line hai phía, mô tả, mức (high/med/low), đề xuất (sửa DD / CR / hỏi khách / chấp nhận), issue bị ảnh hưởng}`.
- Không lặp lại các finding đã có ở `process-trail/reports/review-261024-step3-dr-final.md` và `gap-261024-wbs-summary.md`. Chỉ trỏ ID của chúng nếu liên quan.

## 6. Định dạng output (JSON, UTF-8)
```json
{"group":"A","epics":[{"id":"EP-03","title":"...","body":"...","labels":[],"issues":[
  {"id":"EP03-I01","title":"...","body":"...","role":"BE","sprint":"S3","labels":[],"depends_on":["EP00-I05"],"bidding_ref":["S3.2"],
   "sub_issues":[{"id":"EP03-I01-S01","title":"...","body":"...","role":"BE","sprint":"S3","labels":[]}]}]}],
 "spec_gaps":[{"id":"GAP-03-01","where":"...","evidence":"...","desc":"...","severity":"med","proposal":"...","issues":["EP03-I01"]}],
 "differences":[{"lab4_ref":"...","change":"...","reason":"...","impact":"..."}]}
```

## 7. Luật repo public
Chỉ chứa issue và markdown tự viết. **Không** có:
- đoạn RFP / đề gốc
- dữ liệu thật, dữ liệu cá nhân (email, tên người thật)
- khóa / bí mật

Tài khoản demo và địa chỉ email (kể cả email demo) cũng không đưa vào.
