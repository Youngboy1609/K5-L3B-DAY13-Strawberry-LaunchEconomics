# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Lương Thị Hồng Hạnh · Người gắn nhãn 2: Mai Xuân Khang (gắn độc lập trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 (Hạnh) | Nhãn người 2 (Khang) | Trùng? | Nhãn thống nhất |
| --: | --- | --- | :---: | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Hệ thống | Không | Do người dùng |
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

**Tỉ lệ đồng thuận:** 19 / 20 = **95,0%** (khớp đáp án chuẩn 20/20 ca sau khi thống nhất).

## Quy tắc phân biệt cho các ca không trùng và các ca dễ lẫn

- **Ca 6 (Do người dùng, không phải Hệ thống):** Khách chọn sai phân loại lý do hủy đơn ngay từ màn hình giao diện; việc trợ lý không tự nhận biết để chuyển hướng là giải pháp khắc phục ở hệ thống, còn nguyên nhân gốc vẫn là do người dùng nhập/chọn sai.
- **Ca 9 (Do người dùng, không phải Hệ thống):** Khách nhập nhầm mã đơn hàng của sàn TMĐT thay vì mã vận đơn LogiX-VN; gốc lỗi là dữ liệu đầu vào của người dùng sai.
- **Ca 8, 15 (Hệ thống, không phải Ngầm):** Lỗi tính toán sai số tiền hoặc trích dẫn chính sách sai đã lộ ra ngay trên màn hình và bị nhân viên/khách phát hiện lập tức, không phải lỗi ẩn.
- **Ca 13 (Giới hạn hệ thống):** Khách khiếu nại bồi thường hàng vỡ vượt trần ngoài phạm vi hoàn phí tiêu chuẩn; đây là giới hạn phạm vi nghiệp vụ được giao.
- **Ca 18 (Ngữ cảnh):** Trợ lý áp dụng đúng chính sách khấu trừ 50%, nhưng khách không hiểu ngữ cảnh dẫn tới bức xúc; cần minh bạch giải thích cách tính.
- **Ca 12 (Ngầm):** Trợ lý gọi lặp tool ngầm gây tăng chi phí gấp 3 lần suốt 3 tuần mà kết quả trả lời vẫn đúng, chỉ bị phát hiện khi chạy đối soát chi phí.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi tỷ lệ vượt quá 2% số yêu cầu/ngày | Tự động nhận diện tiền tố mã sàn TMĐT để đối chiếu sang mã vận đơn nội bộ; nếu không tìm thấy, hiện thông báo hướng dẫn kèm ảnh minh họa vị trí mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ: tin nhắn báo "đã hoàn tiền" nhưng không có bản ghi sổ cái ghi nhận trạng thái `ok` cùng `trace_id`; ngưỡng kích hoạt cảnh báo là 0 ca | Chỉ gửi thông báo "đã hoàn" khi nhận mã xác nhận thành công từ API sổ cái; nếu gặp lỗi mạng 503 sau 3 lần gọi lại thì chuyển trạng thái "đang xử lý" và handoff cho nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ mở lại khiếu nại vì thắc mắc số tiền mà kết quả kiểm tra xác nhận đúng chính sách, theo dõi tổng kết theo tuần | Định dạng lại mẫu thông báo hoàn tiền: luôn hiển thị rõ công thức và các bước tính cụ thể (ví dụ: `Cước gốc 30.000 đ × Khấu trừ thời gian 50% = Thực nhận 15.000 đ`) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với thuộc tính `reason = thieu_du_lieu_ngoai_he_thong`, theo dõi theo từng phân loại yêu cầu | Thiết kế mẫu chuyển tiếp có tóm tắt dữ liệu đã thu thập cho nhân viên; loại bỏ phân loại `quoc_te` ra khỏi phạm vi pilot để tránh lãng phí lượt chạy | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm toán định kỳ chọn mẫu ngẫu nhiên 100 đơn/tuần đối chiếu với bảng giá cước ban hành mới nhất; ngưỡng kích hoạt xử lý khi phát hiện ≥ 1% đơn lệch | Tự động xóa bộ nhớ đệm (cache) bảng giá ngay khi phòng tài chính phát hành phiên bản mới; lưu `version_bang_gia` trực tiếp vào metadata của trace | Kế toán trưởng |
