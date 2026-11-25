# Báo cáo cá nhân · Phạm Đăng Quang

## 1. Thông tin thành viên

- **Họ tên:** Phạm Đăng Quang
- **MSSV:** `2A202603760`
- **Email:** [26ai.quangpd@vinuni.edu.vn](mailto:26ai.quangpd@vinuni.edu.vn)
- **Vai trong nhóm:** Kiểm số, tiếp quản code sau giờ giải lao (CP4: D1, CP5: E1).

## 2. Phần việc phụ trách

- **Trước giờ giải lao (A–B):** Tính tay đối chiếu các phép thử A1, kiểm tra số liệu mô hình chi phí A2, A3, A4 và bảng độ nhạy B1–B4; soát các con số và nhãn `simulated`, hoàn thiện nội dung `report/team/bang_chi_phi.md`.
- **Sau giờ giải lao (D–E):** Tiếp quản `src/lab13.py` từ Hồ Trọng Nghĩa; bổ sung và chạy mã nguồn tính toán cỡ mẫu D1 (`co_mau_hai_ti_le`, `NormalIndPower`), kiểm tra 5 câu D1 và ba chỉ số mô tả E1; chuyển giao kết quả cho Hồng Hạnh hoàn thiện `pilot_plan.yaml` và Khang tổng hợp hồ sơ launch v0.

## 3. Đóng góp cụ thể

- **Kiểm số độc lập nhiệm vụ A và B:**
  + Xác nhận ba phép thử A1 đạt chuẩn: số lần chạy kỳ vọng k=2 là `1,20`, k=None là `1,25`, hệ số chi phí k=3 là `1,25`.
  + Đối chiếu trace: hóa đơn token + tool là `274,7 đ/yêu cầu`, CPS toàn mẫu là `4.472 đ` (gấp `16,3 lần`, `simulated`). Giờ nhân viên (làm lại `2.264.000 đ` chiếm `51,8%`, xem lại `1.780.000 đ` chiếm `40,7%`) chiếm `92,5%` tổng chi phí.
  + Phân tích loại yêu cầu: xác nhận `quoc_te` không đáng làm (`22.515 đ = 1,88×`, thành công `27,3%`, tỷ lệ ok giảm mạnh theo lần chạy: `30,0%` -> `11,4%` -> `2,2%`). Phân tích chi phí cố định 40 triệu/tháng: ở 45.000 yc/tháng là `1.185 đ/việc` (CPS tổng `4.599 đ = 0,38×`), ở 22.500 yc/tháng là `2.370 đ/việc` (`5.784 đ = 0,48×`).
  + Bảng độ nhạy: kiểm tra tính chất đối xứng giảm một nửa = 1/2 tăng gấp đôi; xác nhận giới hạn 2 lượt chạy tối ưu chi phí cả hệ thống (`6.901.220 đ`, rẻ hơn giới hạn 1 lượt `7.449.781 đ` do đẩy 85 việc sang nhân viên với giá 12.000 đ).
  + Kịch bản B4: tính toán ngưỡng hòa vốn thời gian xem lại là `≤ 5,12 phút/ca` (với 9 phút làm lại) và `≤ 4,80 phút/ca` (với 15,3 phút làm lại thực tế).
- **Phát triển và hoàn thiện code D1 và E1 trong `src/lab13.py`:**
  + Lập trình hàm `co_mau_hai_ti_le` theo phân phối chuẩn hai phía: ra cỡ mẫu yêu cầu mỗi nhóm là `1.251` (statsmodels cho `1.250`).
  + Tính hệ số thiết kế cụm nhân viên với m=75: `DE = 2,48`, cỡ mẫu `3.103/nhóm`, tương đương 42 nhân viên/nhóm (vượt quá 40 nhân viên công ty có).
  + Xác định trần cỡ mẫu tối đa cho 20 nhân viên/nhóm (`c/ICC = 1.000 < 1.251`) và 6 depot/nhóm (`300 < 1.251`).
  + Giải phương trình tìm cỡ mẫu tối thiểu cho mức chênh 6 điểm phần trăm (`n=859`): `m >= 299 yêu cầu/nhân viên` (`DE = 6,96`), đánh đổi statistical power giảm xuống `0,64` nếu mức chênh thật chỉ đạt 5 điểm.
  + Viết hàm `in_nhiem_vu_e1` trích xuất 3 chỉ số thực tế: chỉ số chính `82,83%` (994/1.200), tỷ lệ bỏ qua gợi ý `27,12%` (48/177), và tỷ lệ mở lại 7 ngày `4,25%` toàn mẫu (3,97% phạm vi pilot).
- **Hoàn thiện các hồ sơ liên quan:**
  + Điền và soát số toàn bộ `report/team/bang_chi_phi.md`.
  + Phối hợp cùng Hạnh kiểm tra các thông số cỡ mẫu và luật dừng trong `report/team/pilot_plan.yaml`.
  + Đóng góp số liệu và tham gia thảo luận phản biện nội dung trong `report/team/ho_so_launch_v0.md` và `report/team/phieu_cham.md`.

## 4. Bằng chứng

- **Mã nguồn:** Các hàm và đoạn in kết quả D1, E1 trong `src/lab13.py`. Lệnh chạy kiểm thử: `python lab13.py` in đầy đủ các kết quả A1, A2, A3, A4, B1, B2, B3, B4, D1, E1 không có cảnh báo hay ngoại lệ.
- **Tài liệu nộp:**
  + File `report/team/bang_chi_phi.md` với đầy đủ số liệu và nhãn `simulated`.
  + Phần chú thích D1 và các thông số cỡ mẫu trong `report/team/pilot_plan.yaml`.
  + Mục 1, 2, 3, 4 trong `report/team/ho_so_launch_v0.md`.
- **Commit Git:** Các commit thuộc nhánh cá nhân `feature/quang-lab13-d1-e1` và merge vào bài nộp chung của nhóm.

## 5. Công cụ AI đã dùng

- **Công cụ:** Gemini / Antigravity hỗ trợ kiểm tra công thức giải tích cỡ mẫu hiệu dụng, rà soát tính hợp lệ của file YAML và đối chiếu các trường trong phiếu chấm.
- **Cách tự kiểm tra kết quả:**
  + Tự giải phương trình bậc nhất cho câu D1.e trên giấy nháp: `20m >= 859 * (0,98 + 0,02m) => 19,5718m >= 841,82 => m >= 298,5 => m = 299`.
  + Tự viết script kiểm tra tính toán độc lập bằng thư viện `statistics` và `statsmodels`.
  + Dùng lệnh `yaml.safe_load` kiểm tra cú pháp file cấu hình `pilot_plan.yaml`.

## 6. Tự đánh giá

- Hoàn thành đầy đủ, chính xác và đúng thời hạn toàn bộ phần việc được giao theo phân công của nhóm trong `TEAM.md`.
- Tất cả các số liệu tính toán đều ăn khớp 100% với tài liệu hướng dẫn và dữ liệu gốc `logix_requests.csv`, `logix_runs.csv`.
- Phối hợp nhịp nhàng với các thành viên khác trong nhóm để tạo nên bộ hồ sơ Gate 2a chất lượng cao.
