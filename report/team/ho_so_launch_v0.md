# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm: Strawberry · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | `4.472 đ` toàn mẫu (gấp `16,3 lần` hóa đơn `274,7 đ`). Trong phạm vi `noi_dia` + `hang_nang`, chi phí là `3.414 đ`, hoặc `4.599 đ` gồm cố định ở `45.000` yêu cầu/tháng toàn hệ thống. | Giả lập | Kỹ sư trưởng agent |
| 2 · Ba yếu tố nhạy nhất | 1. Làm lại (`+51,8%` / `-25,9%`) · 2. Xem lại (`+40,7%` / `-20,3%`) · 3. Lương nhân viên (`+23,1%`). Gấp đôi hoặc giảm nửa giá token làm chi phí đổi lần lượt `+5,6%` và `-2,8%`. | Giả lập | Kỹ sư trưởng agent |
| 3 · So với nhân viên tự làm | Chi phí cả hệ thống là `5.865 đ/yêu cầu` (`0,49×` mức `12.000 đ`); giới hạn 2 lượt chạy tối ưu chi phí cả hệ thống (`6.901.220 đ/1.200 yêu cầu`) | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính: `82,83%` (994/1.200 đóng ≤24h & không mở lại 7 ngày); Dùng: `27,12%` sửa/bỏ gợi ý; An toàn: `4,25%` mở lại 7 ngày (`3,97%` trong pilot) | Xong, có bằng chứng | Kỹ sư trưởng dữ liệu |
| 5 · Bảng lỗi và cách khắc phục | Gắn nhãn 20 ca lỗi (PAIR), đồng thuận `95,0%`; khắc phục đủ 5 loại lỗi, mỗi ca có event đo lường và vai trò phụ trách cụ thể | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 6 · Pilot plan | Phân nhóm theo nhân viên, 20 người/nhánh. MDE `0,06` cần `859` yêu cầu hiệu dụng/nhánh, thu ít nhất `5.980` yêu cầu/nhánh với `299` yêu cầu/người. Rollout 10% → 25% → 50%, có 3 luật dừng. | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi tăng CPS lên `6.787 đ` (`+51,8%`); xem lại 100% tốn `11.743–12.415 đ` (`0,98–1,03×`); giảm khối lượng làm cố định tăng lên `2.370 đ/việc` | Giả lập | Giám đốc tài chính |

**Bốn điều kiện tiên quyết:**
1. **Kiểm tra kỹ thuật và sổ cái:** Sửa khoá chống trùng (idempotency key) và hoàn tất đối soát tự động dịch vụ sổ cái với cổng thanh toán (ca 7, 20) trước ngày triển khai pilot (Kỹ sư trưởng agent phụ trách, kiểm tra trước 2026-12-01).
2. **Xác nhận cỡ mẫu:** Giám đốc vận hành chấp nhận MDE 6 điểm phần trăm (power khoảng 0,64 nếu mức chênh thật là 5 điểm) và xác nhận đủ lưu lượng để thu 5.980 yêu cầu mỗi nhánh ở bước 50%, còn đủ thời gian theo dõi mở lại trước ngày quyết định (kiểm tra trước 2026-12-05).
3. **Kích hoạt hạ tầng đo lường:** Triển khai đầy đủ 8 event có `trace_id` trong hệ thống; thay thế các biến thời lượng giả lập (`phut_xem_lai_simulated`, `phut_lam_lai_simulated`) bằng thời gian đo thực tế ngay sau tuần rollout 1 (Kỹ sư trưởng dữ liệu phụ trách, kiểm tra trước 2026-12-15).
4. **Kế hoạch giảm xem lại theo bậc:** Thiết lập lộ trình giảm dần tỷ lệ xem lại từ 100% xuống dưới 30% khi tỷ lệ sửa/bỏ của nhân viên ổn định dưới 15%, tránh rủi ro chi phí xem lại 100% làm mất lợi thế kinh tế (Trưởng nhóm CSKH phụ trách, kiểm tra trước 2026-12-20).

**Đề xuất:** Go có điều kiện
