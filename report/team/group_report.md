# Báo cáo nhóm Strawberry · Lab 13

## 1. Thông tin nhóm

- **Nhóm Strawberry, lớp L3B.**
- **Nhóm trưởng** là Hồ Trọng Nghĩa. Nhóm có bốn thành viên, gồm Nghĩa, Mai Xuân Khang, Lương Thị Hồng Hạnh và Phạm Đăng Quang. [Danh sách và phân công](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Nhóm xây dựng hồ sơ Gate 2a để quyết định có nên thử nghiệm trợ lý hoàn phí LogiX-VN trong một pilot có đối chứng hay không. Đánh giá dựa trên chi phí cả hệ thống, mức độ sử dụng, lỗi và khả năng đo tác động. Dữ liệu giả lập đã được đối chiếu gồm **1.200 yêu cầu và 1.624 lượt chạy** từ 6 depot, với 20 mã nhân viên trong mẫu. [Dữ liệu yêu cầu](../../src/logix_requests.csv) · [Dữ liệu lượt chạy](../../src/logix_runs.csv)

## 3. Giải pháp

| Nhiệm vụ | Cách thực hiện và bằng chứng |
| --- | --- |
| A · Mô hình chi phí | Qua ba phép thử A1 rồi cộng chi phí của mọi lượt chạy và thời gian nhân viên. Tính chi phí trên mỗi việc thành công theo từng loại yêu cầu và xét chi phí cố định trong phạm vi pilot. [Mã tính](../../src/lab13.py) · [Bảng chi phí](bang_chi_phi.md) |
| B · Độ nhạy | Thay đổi từng yếu tố, xếp hạng ba yếu tố ảnh hưởng nhất, so giới hạn 1–3 lượt chạy và đo tác động của việc xem lại 100%. Dùng chi phí cả hệ thống để so với mức 12.000 đ cho một yêu cầu do nhân viên tự xử lý. [Bảng chi phí](bang_chi_phi.md) |
| C · Bảng lỗi | Đối chiếu hai bộ nhãn do thành viên nộp riêng, giữ nguyên các cột gốc và ghi cách phát hiện, khắc phục, người phụ trách cho một ca ở mỗi loại lỗi. [Bảng lỗi](bang_loi.md) |
| D · Thiết kế pilot | Tính cỡ mẫu hiệu dụng cho ba đơn vị phân nhóm. Chọn cách chia dựa trên cỡ mẫu và nguy cơ ảnh hưởng giữa các nhánh, rồi xác định ngưỡng chi phí, an toàn và mức sử dụng để dừng pilot. [Kế hoạch pilot](pilot_plan.yaml) |
| E · Chỉ số và hồ sơ | Tính ba chỉ số trên dữ liệu chạy thử, đề xuất thêm chỉ số sử dụng và an toàn, đặc tả event có `trace_id`, đưa rủi ro từ bảng độ nhạy vào hồ sơ một trang. [Chỉ số và rủi ro](chi_so.md) · [Hồ sơ launch v0](ho_so_launch_v0.md) |

## 4. Kết quả

- **A · Chi phí.** Ba phép thử A1 đạt **1,20 · 1,25 · 1,25**. Agent xử lý thành công 978/1.200 yêu cầu với chi phí **4.472 đ/việc thành công**. Chi phí cả hệ thống là **5.865 đ/yêu cầu**, sau khi cộng phần nhân viên xử lý các ca agent không hoàn thành (`simulated`). [Mã tính A1–A4](../../src/lab13.py)
- **B · Độ nhạy.** Giới hạn **2 lượt** cho tổng chi phí hệ thống thấp nhất, **6.901.220 đ** cho 1.200 yêu cầu. Khi xem lại toàn bộ ca có lượt `ok` trong phạm vi nội địa và hàng nặng, chi phí đạt **11.743–12.415 đ/việc thành công**, tùy thời lượng làm lại (`simulated`). [Mã tính B1–B4](../../src/lab13.py)
- **C.** Hai bộ nhãn nộp ở PR #3 và #4 trùng **20/20 ca (100%)**. Bảng có năm biện pháp khắc phục. Hạnh và Khang cần xác nhận quy trình gắn độc lập. [Bảng lỗi](bang_loi.md)
- **D.** Kế hoạch chia **20 nhân viên mỗi nhánh**. Với MDE 6 điểm, thu **5.980 yêu cầu mỗi nhánh** (859 hiệu dụng) và chờ đủ bảy ngày theo dõi sau đóng. Power khoảng 64% nếu chênh thực là 5 điểm. [Kế hoạch pilot](pilot_plan.yaml)
- **E.** Ba chỉ số mô tả lần lượt là đóng đúng hạn và không mở lại **82,83%**, sửa hoặc bỏ gợi ý **27,12%**, mở lại **4,25%**. Đặc tả có 12 event. Hồ sơ đề xuất **No-go** vì xem lại toàn bộ làm chi phí cả hệ thống lên **12.850–13.559 đ/yêu cầu** gồm thủ công và cố định, trên định mức 12.000 đ (`simulated`). [Đặc tả chỉ số](chi_so.md) · [Hồ sơ launch](ho_so_launch_v0.md)

Phiếu Strawberry chấm đội trình đang chờ hồ sơ đã xác minh. Điểm Strawberry nhận từ hội đồng chờ ghi nhận của buổi duyệt chéo. [Phiếu chấm](phieu_cham.md)

## 5. Khó khăn và cách xử lý

Tối ưu riêng chi phí agent có thể dịch việc sang nhân viên. Giới hạn 1 lượt có chi phí mỗi việc thành công thấp nhất, **4.111 đ** (`simulated`), đồng thời có thêm **85 yêu cầu không thành công** so với giới hạn 2 lượt. Phương án pilot cần theo dõi cả hai khoản chi phí và nêu rõ đánh đổi về cỡ mẫu hiệu dụng khi chọn đơn vị phân nhóm. [Kịch bản B3](../../src/lab13.py)

## 6. Tổng hợp đóng góp

Nghĩa triển khai code A–B, đặc tả chỉ số và tổng hợp báo cáo. Quang kiểm số A–B, hoàn thiện code D1 và E1. Hạnh nộp bộ nhãn người 1, đề xuất năm biện pháp và soạn kế hoạch pilot. Khang nộp bộ nhãn người 2, phân tích chi phí cả hệ thống và tổng hợp hồ sơ launch cùng phiếu chấm. [Chi tiết và bằng chứng](../../TEAM.md)

## 7. Hạn chế và hướng cải thiện

Dữ liệu chạy thử là giả lập và thiếu nhóm đối chứng, nên các chỉ số hiện có chỉ mô tả mẫu. Trong pilot, nhóm dự kiến đo lại thời gian xem xét và làm lại bằng event thực tế, theo dõi nguy cơ nhân viên chia sẻ gợi ý giữa các nhánh và báo cáo kết quả theo phạm vi yêu cầu đã chọn.

## 8. Tài liệu tham khảo

- [Đề Lab 13 và 20 ca lỗi](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx)
- [Dữ liệu, giả định và công thức của lab](../../docs/du_lieu_va_cong_thuc.md)
- [Checkpoint và tiêu chí chấm](../../CHECKPOINTS.md) · [Rubric](../../RUBRIC.md)
