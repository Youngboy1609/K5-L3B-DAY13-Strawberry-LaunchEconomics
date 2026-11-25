# Báo cáo cá nhân · Lương Thị Hồng Hạnh

## 1. Thông tin thành viên

- **Họ tên:** Lương Thị Hồng Hạnh
- **MSSV:** `2A202603748`
- **Email:** [26ai.hanhlth@vinuni.edu.vn](mailto:26ai.hanhlth@vinuni.edu.vn)
- **Vai trong nhóm:** Gắn nhãn 1, phụ trách tổng hợp bảng lỗi (C) và kế hoạch pilot (D).

## 2. Phần việc phụ trách

- **Nhiệm vụ C (Bảng lỗi và khắc phục):** Đóng vai người gắn nhãn 1, thực hiện phân loại độc lập 20 ca lỗi theo Google PAIR trong 8 phút; tổng hợp hai bộ nhãn, tính tỷ lệ đồng thuận, ghi nhận quy tắc phân biệt và hoàn thiện bảng khắc phục 5 ca đại diện cho 5 loại lỗi vào `report/team/bang_loi.md`.
- **Nhiệm vụ D (Kế hoạch pilot):** Tiếp nhận kết quả tính toán D1 từ Quang để hoàn thiện cấu trúc `report/team/pilot_plan.yaml`, trả lời 5 câu hỏi D2 về tính tách biệt tác động, xây dựng 3 luật dừng an toàn - chi phí - sử dụng theo mẫu chuẩn NẾU-TRONG-THÌ-KHÔNG THÌ.

## 3. Đóng góp cụ thể

- **Gắn nhãn độc lập và hoàn thiện bảng lỗi (`bang_loi.md`):**
  + Gắn nhãn độc lập 20 ca lỗi, đạt đồng thuận 19/20 (95%) với Khang.
  + Viết phần quy tắc phân biệt cho ca 6 (Do người dùng do khách chọn sai danh mục) và các ca dễ gây nhầm lẫn khác.
  + Xây dựng bảng khắc phục cho 5 ca (ca 9: Người dùng, ca 7: Hệ thống, ca 18: Ngữ cảnh, ca 4: Giới hạn hệ thống, ca 17: Ngầm); mỗi ca đều có cơ chế phát hiện đo được bằng event, ngưỡng kích hoạt, tần suất và vai trò phụ trách cụ thể (PM, Kỹ sư trưởng agent, Trưởng nhóm CSKH, Kế toán trưởng).
- **Xây dựng kế hoạch pilot chuẩn xác (`pilot_plan.yaml`):**
  + Tích hợp đầy đủ các thông số cỡ mẫu D1 vào phần chú thích và các trường dữ liệu YAML: MDE = 0,06, n = 859 yêu cầu/nhóm, m ≥ 299 yêu cầu/nhân viên, design effect = 6,96, clusters_per_arm = 20.
  + Trình bày 5 câu trả lời D2 khẳng định tính tách biệt tác động: có đối chứng song song 20 nhân viên, phân nhóm ngẫu nhiên theo seed phân tầng depot, log tương tác chống tràn tác động, chỉ số và luật dừng công bố trước, đủ 20 cụm mỗi nhóm.
  + Thiết lập 3 luật dừng hoàn chỉnh theo đúng cấu trúc 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ:
    1. An toàn: Mở lại 7 ngày cao hơn đối chứng ≥ 2 điểm hoặc vượt 6%, hoặc có ≥ 1 ca hoàn trùng trong 3 ngày -> Giám đốc vận hành tắt trợ lý trong 30 phút -> Không được sang bước rollout tiếp theo.
    2. Chi phí: Chi phí mỗi việc thành công > 8.000 đ trong 2 tuần liên tiếp -> PM thu hẹp về noi_dia và giới hạn 2 lần chạy -> Không được mở hang_nang.
    3. Mức sử dụng: Tỉ lệ bỏ qua gợi ý > 40% trong 1 tuần -> Trưởng nhóm CSKH phỏng vấn 5 nhân viên -> Không được chuyển bước rollout.
  + Kiểm tra file YAML hợp lệ, đọc được qua `yaml.safe_load` và sạch hoàn toàn dấu `?`.

## 4. Bằng chứng

- File `report/team/bang_loi.md` hoàn chỉnh với hai bộ nhãn và bảng khắc phục 5 ca.
- File `report/team/pilot_plan.yaml` hợp lệ, đầy đủ thông số và không còn ký tự placeholder `?`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity / Gemini hỗ trợ kiểm tra ngữ pháp tiếng Việt, định dạng YAML chuẩn và đối chiếu bảng mã lỗi PAIR.
- **Tự kiểm tra:** Tự gắn nhãn trước khi tham khảo đáp án; dùng lệnh `python -c "import yaml; yaml.safe_load(open('report/team/pilot_plan.yaml'))"` để kiểm tra cú pháp và dùng lệnh tìm kiếm xác nhận không còn ký tự `?` trong file.

## 6. Tự đánh giá

- Hoàn thành xuất sắc và đúng hạn các nhiệm vụ C và D.
- Kế hoạch pilot thiết kế khoa học, giải quyết trọn vẹn yêu cầu kiểm soát tác động và các luật dừng chặt chẽ.
