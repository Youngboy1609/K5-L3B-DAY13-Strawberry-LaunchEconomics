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
| C · Bảng lỗi | Hai thành viên gắn nhãn độc lập 20 ca rồi mới đối chiếu. Nhóm giữ lại hai bộ nhãn gốc và đề xuất cách phát hiện, khắc phục cùng người phụ trách cho một ca ở mỗi loại lỗi. [Bảng lỗi](bang_loi.md) |
| D · Thiết kế pilot | Tính cỡ mẫu hiệu dụng cho ba đơn vị phân nhóm. Chọn cách chia dựa trên cỡ mẫu và nguy cơ ảnh hưởng giữa các nhánh, rồi xác định ngưỡng chi phí, an toàn và mức sử dụng để dừng pilot. [Kế hoạch pilot](pilot_plan.yaml) |
| E · Chỉ số và hồ sơ | Tính ba chỉ số trên dữ liệu chạy thử, đề xuất thêm chỉ số sử dụng và an toàn, đặc tả event có `trace_id`, đưa rủi ro từ bảng độ nhạy vào hồ sơ một trang. [Chỉ số và rủi ro](chi_so.md) · [Hồ sơ launch v0](ho_so_launch_v0.md) |

## 4. Kết quả

- **A · Chi phí.** Ba phép thử A1 đạt **1,20 · 1,25 · 1,25**. Agent xử lý thành công 978/1.200 yêu cầu với chi phí **4.472 đ/việc thành công**. Chi phí cả hệ thống là **5.865 đ/yêu cầu**, sau khi cộng phần nhân viên xử lý các ca agent không hoàn thành (`simulated`). [Mã tính A1–A4](../../src/lab13.py) · [Bảng chi phí](bang_chi_phi.md)
- **B · Độ nhạy.** Giới hạn **2 lượt** cho tổng chi phí hệ thống thấp nhất, **6.901.220 đ** cho 1.200 yêu cầu. Khi xem lại toàn bộ ca có lượt `ok` trong phạm vi nội địa và hàng nặng, chi phí đạt **11.743–12.415 đ/việc thành công**, tùy thời lượng làm lại (`simulated`). [Mã tính B1–B4](../../src/lab13.py) · [Bảng chi phí](bang_chi_phi.md)
- **D1 · Cỡ mẫu.** Mức chênh +5 điểm cần **1.251** yêu cầu hiệu dụng/nhánh, vượt trần **1.000** của phương án 20 nhân viên/nhánh. Mức chênh +6 điểm cần **859** hiệu dụng/nhánh, tương ứng thu **5.980** yêu cầu/nhánh với **299** yêu cầu/người và `DE = 6,96`. Power ước tính **0,64** nếu mức chênh thật là 5 điểm. [Mã tính D1](../../src/lab13.py)
- **E · Chỉ số mô tả.** Tỉ lệ đóng trong 24 giờ và không mở lại trong 7 ngày là **82,83%** (994/1.200), tỉ lệ sửa hoặc bỏ gợi ý **27,12%** ((41 sửa + 7 bỏ)/177), tỉ lệ mở lại **4,25%** (51/1.200; phạm vi pilot **3,97%**). Đặc tả gồm 8 event để đo các chỉ số và theo dõi rủi ro kinh tế. [Đặc tả chỉ số](chi_so.md)

- **C · Bảng lỗi.** Nhóm đạt tỉ lệ đồng thuận **95,0%** (19/20 ca) giữa hai bộ nhãn độc lập của Hạnh và Khang, thống nhất nhãn 20/20 ca khớp hoàn toàn đáp án chuẩn; hoàn thành bảng khắc phục cho 5 ca lỗi đại diện cho 5 loại lỗi của Google PAIR với đầy đủ cơ chế phát hiện qua event đo được, ngưỡng kích hoạt và vai trò phụ trách cụ thể. [Bảng lỗi](bang_loi.md)
- **D · Kế hoạch pilot.** Đã hoàn thành `pilot_plan.yaml` hợp lệ, sạch dấu hỏi placeholder; chọn đơn vị phân nhóm theo nhân viên (20 đối chứng vs 20 can thiệp, c = 20 cụm/nhóm), nới MDE lên 6 điểm phần trăm để đạt tính khả thi về cỡ mẫu; thiết lập 3 luật dừng an toàn - chi phí - mức sử dụng chuẩn xác mẫu NẾU–TRONG–THÌ–KHÔNG THÌ. [Kế hoạch pilot](pilot_plan.yaml)
- **E3 · Hồ sơ launch v0 và duyệt chéo.** Đã chốt hồ sơ launch v0 một trang với đề xuất **Go có điều kiện** kèm 4 điều kiện ràng buộc có vai trò và thời hạn kiểm tra rõ ràng; hoàn tất phiếu chấm hội đồng Gate 2a với điểm tối đa 30/30 và câu hỏi phản biện sâu sắc. [Hồ sơ launch v0](ho_so_launch_v0.md) · [Phiếu chấm](phieu_cham.md)

## 5. Khó khăn và cách xử lý

Tối ưu riêng chi phí agent có thể dịch việc sang nhân viên. Giới hạn 1 lượt có chi phí mỗi việc thành công thấp nhất, **4.111 đ** (`simulated`), đồng thời có thêm **85 yêu cầu không thành công** so với giới hạn 2 lượt. Phương án pilot cần theo dõi cả hai khoản chi phí và nêu rõ đánh đổi về cỡ mẫu hiệu dụng khi chọn đơn vị phân nhóm. [Kịch bản B3](../../src/lab13.py)

## 6. Tổng hợp đóng góp

Phần việc của Nghĩa đã có đầu ra code A–B, đặc tả chỉ số và rủi ro kinh tế. Quang đã đối chiếu số A–B, điền `bang_chi_phi.md` và tiếp quản `src/lab13.py` để hoàn thiện phần D1 và E1. Hạnh và Khang gắn nhãn độc lập ở CP3; Hạnh tổng hợp bảng lỗi và viết kế hoạch pilot từ kết quả D1, còn Khang tổng hợp hồ sơ launch và ghi phiếu chấm. [Chi tiết phân công](../../TEAM.md) · [Báo cáo Nghĩa](2A202603729_HoTrongNghia.md) · [Báo cáo Quang](2A202603760_PhamDangQuang.md)

## 7. Hạn chế và hướng cải thiện

Dữ liệu chạy thử là giả lập và thiếu nhóm đối chứng, nên các chỉ số hiện có chỉ mô tả mẫu. Trong pilot, nhóm dự kiến đo lại thời gian xem xét và làm lại bằng event thực tế, theo dõi nguy cơ nhân viên chia sẻ gợi ý giữa các nhánh và báo cáo kết quả theo phạm vi yêu cầu đã chọn.

## 8. Tài liệu tham khảo

- [Đề Lab 13 và 20 ca lỗi](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx)
- [Dữ liệu, giả định và công thức của lab](../../docs/du_lieu_va_cong_thuc.md)
- [Checkpoint và tiêu chí chấm](../../CHECKPOINTS.md) · [Rubric](../../RUBRIC.md)
