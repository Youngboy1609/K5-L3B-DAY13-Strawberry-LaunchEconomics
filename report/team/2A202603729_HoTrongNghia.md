# Báo cáo cá nhân · Hồ Trọng Nghĩa

## 1. Thông tin thành viên

- **Họ tên** Hồ Trọng Nghĩa
- **MSSV** `2A202603729`
- **Email** [26ai.nghiaht@vinuni.edu.vn](mailto:26ai.nghiaht@vinuni.edu.vn)
- **Vai trong nhóm** Nhóm trưởng và người viết code trước giờ giải lao.

## 2. Phần việc phụ trách

Triển khai mô hình chi phí A–B, đặc tả chỉ số, event và rủi ro kinh tế của E và tổng hợp báo cáo nhóm. Bàn giao đầu ra A–B và vị trí nối tiếp D1, E1 cho Phạm Đăng Quang. [Phân công nhóm](../../TEAM.md)

## 3. Đóng góp cụ thể

- Hoàn thiện ba hàm A1 và mô hình chi phí từ trace. Tách chi phí mỗi việc thành công, chi phí hệ thống mỗi yêu cầu và phần cố định theo khối lượng. [Mã tính](../../src/lab13.py)
- Tính chín kịch bản độ nhạy, kịch bản đổi một cặp, ba giới hạn số lượt chạy và kịch bản xem lại 100%. Giới hạn hai lượt cho chi phí hệ thống thấp nhất, **6.901.220 đ/1.200 yêu cầu** (`simulated`). [Mã tính](../../src/lab13.py)
- Viết đặc tả năm chỉ số và tám event, gắn ba rủi ro kinh tế với kết quả A4, B1 và B4. Tổng hợp các kết quả đã kiểm tra vào báo cáo nhóm. [Đặc tả chỉ số](chi_so.md) · [Báo cáo nhóm](group_report.md)

## 4. Bằng chứng

Chạy `python -B lab13.py` trong `src/`. Ba phép thử A1 đạt **1,20 · 1,25 · 1,25** và chương trình in đủ A2–A4, B1–B4. Kiểm tra đối chiếu xác nhận giới hạn hai lượt có tổng chi phí hệ thống thấp nhất, đồng thời ba chỉ số mô tả lần lượt là **994/1.200**, **48/177** và **51/1.200**. [Mã và dữ liệu](../../src/README.md)

## 5. Công cụ AI đã dùng

Codex hỗ trợ triển khai mã và soạn báo cáo. Kết quả được kiểm tra bằng ba phép thử A1 có sẵn, đối chiếu chi phí với hướng dẫn, kiểm tra quan hệ tăng gấp đôi và giảm một nửa ở B1, và đếm trực tiếp trên CSV cho E1 và B4. [Hướng dẫn lab](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md)

## 6. Tự đánh giá

Phần A–B có thể tái lập từ hai CSV và ba phép thử A1. Số đo về thời gian xem lại và làm lại dựa trên giả định `simulated`. Phần E đã xác định event để thu các số đo thực tế trong pilot. Kết luận Gate 2a còn phụ thuộc vào gắn nhãn, kế hoạch đối chứng và duyệt chéo của nhóm.
