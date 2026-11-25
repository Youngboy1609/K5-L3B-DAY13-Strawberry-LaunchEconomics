# Báo cáo cá nhân · Phạm Đăng Quang

## 1. Thông tin thành viên

- **Họ tên:** Phạm Đăng Quang
- **MSSV:** `2A202603760`
- **Email:** [26ai.quangpd@vinuni.edu.vn](mailto:26ai.quangpd@vinuni.edu.vn)
- **Vai trong nhóm:** Kiểm số, tiếp quản code sau giờ giải lao (CP4: D1, CP5: E1).

## 2. Phần việc phụ trách

- **Trước giờ giải lao (A–B).** Đối chiếu tay các phép thử A1, kiểm tra số liệu chi phí A2–A4 và độ nhạy B1–B4. Điền bảng chi phí và soát nhãn `simulated`.
- **Sau giờ giải lao (D1 và E1).** Tiếp quản `src/lab13.py` từ Hồ Trọng Nghĩa, bổ sung phép tính cho 5 câu D1 và ba chỉ số mô tả E1. Kết quả D1 và tỷ lệ mở lại là số liệu bàn giao cho kế hoạch pilot theo phân công.

## 3. Đóng góp cụ thể

- **Kiểm số độc lập nhiệm vụ A và B:**
  + Xác nhận ba phép thử A1 đạt chuẩn: số lần chạy kỳ vọng k=2 là `1,20`, k=None là `1,25`, hệ số chi phí k=3 là `1,25`.
  + Đối chiếu trace: hóa đơn token + tool là `274,7 đ/yêu cầu`, CPS toàn mẫu là `4.472 đ` (gấp `16,3 lần`, `simulated`). Giờ nhân viên (làm lại `2.264.000 đ` chiếm `51,8%`, xem lại `1.780.000 đ` chiếm `40,7%`) chiếm `92,5%` tổng chi phí.
  + Phân tích loại yêu cầu: xác nhận `quoc_te` không đáng làm (`22.515 đ = 1,88×`, thành công `27,3%`, tỷ lệ ok giảm mạnh theo lần chạy: `30,0%` -> `11,4%` -> `2,2%`). Phân tích chi phí cố định 40 triệu/tháng: ở 45.000 yc/tháng là `1.185 đ/việc` (CPS tổng `4.599 đ = 0,38×`), ở 22.500 yc/tháng là `2.370 đ/việc` (`5.784 đ = 0,48×`).
  + Bảng độ nhạy: kiểm tra tính chất đối xứng giảm một nửa = 1/2 tăng gấp đôi; xác nhận giới hạn 2 lượt chạy tối ưu chi phí cả hệ thống (`6.901.220 đ`, rẻ hơn giới hạn 1 lượt `7.449.781 đ` do đẩy 85 việc sang nhân viên với giá 12.000 đ).
  + Kịch bản B4: ngưỡng hòa vốn xem lại là `5,12 phút/ca` với giả định 9 phút làm lại và `4,80 phút/ca` với trung bình dữ liệu đã làm tròn 15,3 phút làm lại (`simulated`).
- **Phát triển và hoàn thiện code D1 và E1 trong `src/lab13.py`:**
  + Lập trình hàm `co_mau_hai_ti_le` theo phân phối chuẩn hai phía: ra cỡ mẫu yêu cầu mỗi nhóm là `1.251` (statsmodels cho `1.250`).
  + Tính hệ số thiết kế cụm nhân viên với m=75: `DE = 2,48`, cỡ mẫu `3.103/nhóm`, tương đương 42 nhân viên/nhóm (vượt quá 40 nhân viên công ty có).
  + Xác định trần cỡ mẫu tối đa cho 20 nhân viên/nhóm (`c/ICC = 1.000 < 1.251`) và 6 depot/nhóm (`300 < 1.251`).
  + Với mục tiêu chênh 6 điểm phần trăm, cần `859` yêu cầu hiệu dụng mỗi nhánh. Tại `299` yêu cầu/người và 20 người/nhánh, thu `5.980` yêu cầu/nhánh, tương đương `859,20` hiệu dụng với `DE = 6,96`. Power ước tính `0,64` nếu mức chênh thật là 5 điểm.
  + Hàm `in_nhiem_vu_e1` tính ba chỉ số mô tả trên dữ liệu giả lập. Chỉ số chính là `82,83%` (994/1.200), tỉ lệ sửa hoặc bỏ gợi ý là `27,12%` (48/177), và tỉ lệ mở lại 7 ngày là `4,25%` toàn mẫu (3,97% trong phạm vi pilot).

## 4. Bằng chứng

- **Mã nguồn:** Các hàm và đoạn in kết quả D1, E1 trong `src/lab13.py`. Lệnh chạy kiểm thử: `python lab13.py` in đầy đủ các kết quả A1, A2, A3, A4, B1, B2, B3, B4, D1, E1 không có cảnh báo hay ngoại lệ.
- **Bảng chi phí.** Kết quả A1–A4 và B1–B4 có trong [bang_chi_phi.md](bang_chi_phi.md).
- **Nhánh Git.** Phần việc nằm trên `DangQuang`, nối tiếp commit bàn giao `9bb9dc0` của Nghĩa.

## 5. Công cụ AI đã dùng

- **Công cụ.** Gemini / Antigravity hỗ trợ kiểm tra công thức cỡ mẫu hiệu dụng.
- **Cách tự kiểm tra kết quả:**
  + Đối chiếu D1.e bằng phép tính `20m >= 859 × (0,98 + 0,02m)`, suy ra `2,82m >= 841,82` và `m >= 298,52`. Với số nguyên tối thiểu `m = 299`, `5.980 ÷ 6,96 ≈ 859,20`.
  + Tự viết script kiểm tra tính toán độc lập bằng thư viện `statistics` và `statsmodels`.
- **Rà soát bổ sung bằng Codex:** Chạy lại `python lab13.py` và đối chiếu độc lập từ CSV, bao gồm tổng chi phí B4, cỡ mẫu hiệu dụng D1 và tử số, mẫu số của ba chỉ số E1.

## 6. Tự đánh giá

- A1 đạt đủ ba phép thử. Có thể chạy lại mã để đối chiếu kết quả A–B, năm câu D1 và ba chỉ số E1 với hai CSV gốc.
