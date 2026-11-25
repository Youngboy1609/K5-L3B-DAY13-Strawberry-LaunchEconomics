# Báo cáo cá nhân · Lương Thị Hồng Hạnh

## 1. Thông tin thành viên

- **Họ tên:** Lương Thị Hồng Hạnh
- **MSSV:** `2A202603748`
- **Email:** [26ai.hanhlth@vinuni.edu.vn](mailto:26ai.hanhlth@vinuni.edu.vn)
- **GitHub:** `hatrang200715`
- **Vai trong nhóm:** Người gắn nhãn 1, tổng hợp nhiệm vụ C, phụ trách kế hoạch pilot (nhiệm vụ D).

## 2. Phần việc phụ trách

- **CP3 — Gắn nhãn và tổng hợp C.** Gắn nhãn độc lập 20 ca lỗi (không trao đổi với người gắn nhãn 2 trước khi so), sau đó điền bộ nhãn người 1 và soạn bản nháp bảng khắc phục 5 ca vào `report/team/bang_loi.md`.
- **CP4–CP5 — Kế hoạch pilot.** Nhận kết quả D1 (năm câu cỡ mẫu) và tỉ lệ mở lại từ Phạm Đăng Quang, chốt `report/team/pilot_plan.yaml`: chọn cách chia theo nhân viên 20 + 20, chấp nhận mức chênh 6 điểm, viết 3 luật dừng đủ 4 vế, và kiểm tra file đọc được bằng `yaml.safe_load`. Gửi kế hoạch cho Mai Xuân Khang để tổng hợp hồ sơ.

## 3. Đóng góp cụ thể

- **Bộ nhãn người 1 (20/20 ca):** gắn theo nguyên nhân gốc, không theo chỗ cần sửa, sau khi đối chiếu từng ca với năm loại Google PAIR và các câu hỏi nhận diện. Bộ nhãn ghi trong bảng "Nhãn người 1" của `bang_loi.md`.
- **`bang_loi.md`:** điền khung bảng so 20 ca, chỗ tỉ lệ đồng thuận và mục quy tắc phân biệt (chờ bộ nhãn người 2 để hoàn thành phần so). Soạn bản nháp bảng khắc phục 5 ca — mỗi loại một ca (9, 7, 18, 4, 17) — mỗi dòng có cách phát hiện đo được (event + ngưỡng + tần suất) và một vai trò phụ trách cụ thể, không ghi "cả đội".
- **`pilot_plan.yaml`:** chốt trên số D1 của Quang:
  + Đối chiếu 4 phương án: chia theo yêu cầu (1.251/nhóm, tràn tác động), theo nhân viên m=75 (cần 84 người > 40), 6 depot (trần 300, chỉ 6 cụm — loại), và 20 nhân viên/nhóm (trần 1.000 < 1.251).
  + Chọn chia theo nhân viên 20 + 20 với mức chênh mục tiêu +6 điểm: n hiệu dụng 859/nhóm, Design Effect 6,96, mỗi người ~299 yêu cầu; ghi rõ bất lợi power chỉ còn 0,64 nếu chênh thật 5 điểm và cần Giám đốc vận hành ký chấp nhận.
  + Đặt ngưỡng an toàn dựa trên tỉ lệ mở lại trong mẫu giả lập: 4,25% toàn mẫu (51/1.200), 3,97% trong phạm vi pilot — chọn chênh ≥ +2 điểm so với đối chứng hoặc trần tuyệt đối 6%, thay vì ngưỡng 3% tuyệt đối (sẽ làm pilot dừng ngay tuần đầu).
  + 3 luật dừng đều đủ 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ, người bấm cờ là một vai trò cụ thể.

## 4. Bằng chứng

- **Bộ nhãn người 1 và bản nháp khắc phục:** [bang_loi.md](bang_loi.md), commit `dc30952` ("gan nhan nhiem vu C") trên nhánh `feature/bang-loi-1` — commit trước khi so nhãn với người 2.
- **Kế hoạch pilot:** [pilot_plan.yaml](pilot_plan.yaml), commit `f53bebd` trên nhánh `feature/pilot_plan`, đã push lên origin, author commit là `hatrang200715`.
- **Kiểm tra máy:** chạy `yaml.safe_load` thành công; kiểm tự động xác nhận: không còn dấu `?`, 3 luật dừng đủ 4 vế NẾU–TRONG–THÌ–KHÔNG THÌ, không có thuật ngữ bị cấm theo RULES.md.
- **Đối chiếu số:** mọi số pilot (1.251, 3.103, 1.000, 300, 859, DE 2,48/6,96, power 0,64, 4,25%/3,97%) lấy từ output của `src/lab13.py` (do Phạm Đăng Quang viết) chứ không tính từ nguồn khác.

## 5. Công cụ AI đã dùng

- **Công cụ:** trợ lý AI Mistral Vibe (dùng trên máy cá nhân).
- **Dùng vào việc gì:** điền kết quả so nhãn vào `bang_loi.md` theo bộ nhãn mình đã gắn tay; soạn nháp bảng khắc phục để nhóm duyệt; chốt nội dung `pilot_plan.yaml` theo số D1 bàn giao; viết script kiểm tra tự động (YAML đọc được, không còn `?`, luật dừng đủ 4 vế, không có từ cấm); hỗ trợ thao tác git (amend, force-push có kiểm soát khi đã xin phép).
- **Tự kiểm tra kết quả ra sao:**
  + Bộ nhãn 20 ca là mình gắn độc lập bằng tay, **không dùng AI gắn nhãn** (theo RULES.md), và không xem nhãn của người gắn nhãn 2 trước khi so.
  + Số trong `pilot_plan.yaml` tự đối chiếu trực tiếp với output mà `python lab13.py` in ra, không dùng số AI tự sinh.
  + Chạy lại script `yaml.safe_load` sau khi chốt để xác nhận file hợp lệ; đọc lại 3 luật dừng cho đủ 4 vế trước khi nộp.

## 6. Tự đánh giá

- Hoàn thành bộ nhãn người 1 đúng giờ, đúng quy trình độc lập; `pilot_plan.yaml` đã chốt và kiểm tra kỹ thuật đạt.
- Tại thời điểm nộp bộ nhãn người 1, bảng so nhãn còn chờ cột người 2. Bản tích hợp của nhóm đã giữ hai cột gốc, ghi mức đồng thuận **20/20** và rà soát năm biện pháp. [Bảng lỗi](bang_loi.md)
- Bài học: đặt ngưỡng an toàn phải soi dữ liệu chạy thử trước — ngưỡng 3% tuyệt đối tưởng chừng chặt mà sẽ dừng pilot ngay ở 3,97% trong mẫu phạm vi pilot.
