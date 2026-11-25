# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Lương Thị Hồng Hạnh (`hatrang200715`) · Người gắn nhãn 2: Mai Xuân Khang (gắn trong 8 phút, không trao đổi) — **chưa gắn xong**

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | ... | ... | ... |
| 2 | Hệ thống | ... | ... | ... |
| 3 | Ngữ cảnh | ... | ... | ... |
| 4 | Giới hạn hệ thống | ... | ... | ... |
| 5 | Ngầm | ... | ... | ... |
| 6 | Do người dùng | ... | ... | ... |
| 7 | Hệ thống | ... | ... | ... |
| 8 | Hệ thống | ... | ... | ... |
| 9 | Do người dùng | ... | ... | ... |
| 10 | Ngữ cảnh | ... | ... | ... |
| 11 | Giới hạn hệ thống | ... | ... | ... |
| 12 | Ngầm | ... | ... | ... |
| 13 | Giới hạn hệ thống | ... | ... | ... |
| 14 | Do người dùng | ... | ... | ... |
| 15 | Hệ thống | ... | ... | ... |
| 16 | Ngữ cảnh | ... | ... | ... |
| 17 | Ngầm | ... | ... | ... |
| 18 | Ngữ cảnh | ... | ... | ... |
| 19 | Giới hạn hệ thống | ... | ... | ... |
| 20 | Hệ thống | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...% *(điền sau khi so với bộ của người gắn nhãn 2; đạt nếu ≥ 80% tức ≥ 16/20)*

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- *(điền sau khi so nhãn — chỉ liệt kê các ca người 1 và người 2 gắn khác nhau)*

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

*Bản nháp do Hạnh soạn dựa trên bộ nhãn người 1, chờ nhóm duyệt.*

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` đếm theo ngày, cảnh báo khi mã khách nhập không tra được quá 2% số yêu cầu/ngày | Nhận diện mã đơn sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn khách kèm ảnh chụp màn hình | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" nhưng không có bản ghi `refund_ledger_write` với ket_qua = ok cùng trace_id; ngưỡng 0 ca | Chỉ báo "đã hoàn" khi sổ cái trả ok; lỗi 503 sau 3 lần thử thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ mở lại mà kiểm tra thấy số tiền đúng (event `ticket_reopened`, reason = số tiền), theo tuần | Mẫu tin nhắn luôn ghi cách tính kèm số: "Đã hoàn 15.000 đ = 30.000 đ phí giao × 50%" | Trưởng nhóm CSKH |
| 4 | Giới hạn | Event `handoff_to_staff` với reason = thieu_du_lieu, đếm theo loại yêu cầu, xem theo tuần | Giữ cách chuyển kèm tóm tắt cho nhân viên; chặng hãng nước ngoài đưa ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần đối chiếu bảng giá hiện hành; ngưỡng 1% số đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới, ghi phiên bản bảng giá vào trace | Kế toán trưởng |
