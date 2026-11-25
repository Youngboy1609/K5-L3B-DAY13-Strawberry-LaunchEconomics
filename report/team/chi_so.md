# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | Tỉ lệ đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu có `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0` chia tổng số yêu cầu | **82,83%** (994/1.200) |
| Dùng | Tỉ lệ sửa hoặc bỏ gợi ý | Trong các yêu cầu có `duoc_xem_lai = 1`, lấy số quyết định `sua` hoặc `bo` chia tổng số yêu cầu được xem lại | **27,12%** ((41 sửa + 7 bỏ)/177) |
| An toàn | Tỉ lệ mở lại trong 7 ngày | Số yêu cầu có `mo_lai_trong_7_ngay = 1` chia tổng số yêu cầu | **4,25%** (51/1.200) |
| Dùng (đề xuất) | Tỉ lệ nhân viên chủ động mở trợ lý | Số yêu cầu thuộc nhánh can thiệp có ít nhất một lượt mở trợ lý do nhân viên thực hiện chia tổng số yêu cầu thuộc nhánh can thiệp | Đo trong pilot |
| An toàn (đề xuất) | Tỉ lệ hoàn sai số tiền qua kiểm tra mẫu | Số yêu cầu đã kiểm tra có số tiền thực hoàn khác số tiền đúng theo chính sách chia tổng số yêu cầu được kiểm tra | Đo trong pilot |

Ba kết quả trên được tính theo cột trong CSV và mô tả đợt chạy thử giả lập. Ước lượng tác động cần so sánh hai nhánh trong pilot. [Dữ liệu yêu cầu](../../src/logix_requests.csv)

## Danh sách event

Mỗi event có `trace_id` để truy vết, `request_id` để nối các thao tác theo yêu cầu và `occurred_at` để gom số theo tuần. Các chỉ số theo nhánh lấy nhánh được gán cho yêu cầu tại thời điểm vào pilot.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `pilot_request_enrolled` | Dịch vụ phân nhóm | `trace_id`, `request_id`, `arm`, `depot`, `staff_id`, `loai`, `created_at`, `assigned_at` | Khi yêu cầu đủ điều kiện và đã được gán nhánh |
| `staff_assistant_opened` | Giao diện CSKH | `trace_id`, `request_id`, `staff_id`, `opened_at` | Khi nhân viên chủ động mở trợ lý |
| `agent_run_completed` | Agent | `trace_id`, `request_id`, `run_id`, `attempt`, `status`, `tokens_in`, `tokens_out`, `tool_calls` | Khi mỗi lượt chạy kết thúc, kể cả lượt lỗi |
| `staff_review_decision` | Giao diện CSKH | `trace_id`, `request_id`, `staff_id`, `decision` (`giu`/`sua`/`bo`), `review_minutes`, `decided_at` | Khi nhân viên xác nhận quyết định xem lại |
| `staff_rework_completed` | Giao diện CSKH | `trace_id`, `request_id`, `staff_id`, `reason`, `rework_minutes` | Khi nhân viên hoàn thành việc sửa một kết quả sai |
| `ticket_closed` | Hệ thống vé hỗ trợ | `trace_id`, `request_id`, `closed_at` | Khi yêu cầu được đóng |
| `ticket_reopened` | Hệ thống vé hỗ trợ | `trace_id`, `request_id`, `reopened_at`, `reason` | Khi yêu cầu được mở lại |
| `refund_amount_audited` | Bộ phận kiểm soát | `trace_id`, `request_id`, `actual_amount_vnd`, `expected_amount_vnd`, `audited_at` | Khi hoàn tất kiểm tra một yêu cầu trong mẫu tuần |
| `input_validation_failed` | Giao diện hoàn phí | `trace_id`, `request_id`, `input_type`, `reason` | Khi đầu vào thiếu hoặc không tra được mã vận đơn |
| `handoff_to_staff` | Trợ lý | `trace_id`, `request_id`, `reason`, `loai` | Khi một yêu cầu được chuyển cho nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | `trace_id`, `request_id`, `refund_intent_id`, `idempotency_key`, `ledger_transaction_id`, `status`, `actual_amount_vnd` | Khi ghi sổ thành công hoặc thất bại |
| `refund_status_notified` | Dịch vụ thông báo | `trace_id`, `request_id`, `refund_intent_id`, `notification_status` | Khi thông báo trạng thái hoàn phí cho khách |

**Event dùng để tính từng chỉ số**

- **Chính.** Lấy `created_at` từ `pilot_request_enrolled`, thời điểm đóng đầu tiên từ `ticket_closed` và lọc `ticket_reopened` trong 7 ngày sau khi đóng. Chỉ chốt báo cáo khi đã đủ cửa sổ quan sát của các yêu cầu được đưa vào mẫu số.
- **Sửa hoặc bỏ gợi ý.** Dùng quyết định cuối cùng của mỗi `request_id` từ `staff_review_decision`.
- **Mở lại.** Nối `pilot_request_enrolled`, `ticket_closed` và `ticket_reopened`. Đếm mỗi yêu cầu mở lại ở cửa sổ 7 ngày một lần.
- **Chủ động mở trợ lý.** Nối `pilot_request_enrolled` ở nhánh can thiệp với `staff_assistant_opened`, đếm mỗi yêu cầu tối đa một lần.
- **Hoàn sai số tiền.** Dùng `refund_amount_audited` để đối chiếu số tiền thực hoàn và số tiền đúng trong mẫu đã kiểm tra.
- **Hoàn trùng.** Cảnh báo khi một `refund_intent_id` có hai `ledger_transaction_id` khác nhau cùng ghi thành công. Mã ý định hoàn phí dùng chung cho các lượt thử và yêu cầu gửi lại của cùng một khoản hoàn. [Luật dừng an toàn](pilot_plan.yaml)

## E2 · Rủi ro kinh tế

Mức tác động lấy từ đầu ra A4, B1 và B4. Ngưỡng theo dõi và hành động dưới đây là đề xuất để nhóm chốt trước pilot. [Mã tính](../../src/lab13.py) · [Bảng chi phí](bang_chi_phi.md)

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng | Gấp đôi tiền làm lại làm chi phí tăng **51,8%**, lên **6.787 đ/việc thành công** (`simulated`, B1). | Số yêu cầu có `staff_rework_completed` vượt 7% yêu cầu trong phạm vi trong một tuần. Mẫu chạy thử có 48/982 ca, tức 4,9%. | Rà tối đa 20 trace làm lại, xác định loại yêu cầu gây tăng và đề xuất thu hẹp phạm vi nếu lỗi tập trung. | PM trợ lý hoàn phí |
| Xem lại toàn bộ kéo dài | Với 5 phút xem lại mỗi ca có lượt `ok`, chi phí là **11.743 đ/việc thành công** nếu làm lại 9 phút/ca và **12.415 đ** nếu làm lại 15,3 phút/ca (`simulated`, B4). | Cuối tuần vẫn xem lại toàn bộ yêu cầu có lượt `ok` và thời gian xem lại trung bình vượt 4,8 phút/ca, tính từ `staff_review_decision` và `agent_run_completed`. | Rút ngắn thao tác xem lại, chỉ giảm tỉ lệ xem lại theo bậc khi đạt ngưỡng an toàn đã chốt. | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự báo | Khi tổng khối lượng giảm từ 45.000 xuống 22.500 yêu cầu/tháng, chi phí cố định phân bổ tăng từ **1.185 lên 2.370 đ/việc thành công** (`simulated`, A4). | Yêu cầu vào pilot trong tuần thấp hơn 50% kế hoạch, theo `pilot_request_enrolled`. | Tính lại chi phí ở khối lượng quan sát được trước quyết định mở rộng. | PM trợ lý hoàn phí |
