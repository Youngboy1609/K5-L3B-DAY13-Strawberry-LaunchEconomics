# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1 là Lương Thị Hồng Hạnh. Người gắn nhãn 2 là Mai Xuân Khang. Hai cột dưới đây giữ nguyên nội dung trong hai PR của từng người. [Bộ nhãn Hạnh](https://github.com/Youngboy1609/K5-L3B-DAY13-Strawberry-LaunchEconomics/blob/dc30952b6374686873afbd145a266eb45a54ee93/report/team/bang_loi.md#L5-L30) · [Bộ nhãn Khang](https://github.com/Youngboy1609/K5-L3B-DAY13-Strawberry-LaunchEconomics/blob/95191faf081187423c48a6dd6b34f1457537ce97/report/team/bang_loi.md#L5-L30)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** **20/20 = 100%**, vượt ngưỡng 16/20. Cả hai bộ khớp 20/20 nhãn tham khảo. Việc gắn độc lập trước khi đối chiếu cần hai người gắn nhãn xác nhận. [Nhãn tham khảo](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md#nhãn-tham-khảo-cho-20-ca)

## Quy tắc phân biệt cho các ca không trùng

Hai bộ trùng ở cả 20 ca. Cột thống nhất chép lại nhãn chung của từng ca.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Năm ca đại diện cho năm loại lỗi. Các dấu hiệu phát hiện dùng event đề xuất cho pilot. [Đặc tả event](chi_so.md#danh-sách-event)

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` đếm theo ngày, cảnh báo khi mã khách nhập không tra được quá 2% số yêu cầu/ngày | Nhận diện mã đơn sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn khách kèm ảnh chụp màn hình | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ. Cảnh báo nếu có ít nhất một `refund_status_notified` báo đã hoàn mà thiếu `refund_ledger_write` trạng thái `ok` cùng `refund_intent_id` | Chỉ báo đã hoàn sau khi sổ cái xác nhận. Khi lỗi 503 sau ba lượt, báo đang xử lý và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ mở lại mà kiểm tra thấy số tiền đúng (event `ticket_reopened`, reason = số tiền), theo tuần | Mẫu tin nhắn luôn ghi cách tính kèm số: "Đã hoàn 15.000 đ = 30.000 đ phí giao × 50%" | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với reason = thieu_du_lieu, đếm theo loại yêu cầu, xem theo tuần | Giữ cách chuyển kèm tóm tắt cho nhân viên; chặng hãng nước ngoài đưa ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần đối chiếu bảng giá hiện hành; ngưỡng 1% số đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới, ghi phiên bản bảng giá vào trace | Kế toán trưởng |
