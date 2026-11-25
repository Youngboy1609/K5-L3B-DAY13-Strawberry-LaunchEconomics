# Báo cáo cá nhân — Mai Xuân Khang-2A202603722

## 1. Thông tin thành viên

- Họ tên: Mai Xuân Khang
- MSSV: `2A202603722`
- Email: [26ai.khangmx@vinuni.edu.vn](mailto:26ai.khangmx@vinuni.edu.vn)
- Vai trong nhóm: Gắn nhãn 2 kiêm giữ hồ sơ.

## 2. Phần việc phụ trách

Gắn nhãn người 2 cho 20 ca CP3, tổng hợp hồ sơ launch v0 và chuẩn bị phiếu Strawberry chấm nhóm được giao.

## 3. Đóng góp cụ thể

### Bộ nhãn ban đầu CP3



| Ca | Nhãn ban đầu | Căn cứ |
| --: | --- | --- |
| 1 | Do người dùng | Khách nhập thiếu hai chữ số tài khoản, dẫn đến lỗi trả về từ ngân hàng. |
| 2 | Hệ thống | Trợ lý tra giá hàng thường cho kiện 28 kg thuộc hàng nặng, hoàn thiếu 45.000 đ. |
| 3 | Ngữ cảnh | Hệ thống hoàn vào ví đúng thiết kế, còn khách chờ tiền vào tài khoản ngân hàng. |
| 4 | Giới hạn hệ thống | LogiX thiếu dữ liệu chặng hãng nước ngoài, nên trợ lý thông báo và chuyển nhân viên. |
| 5 | Ngầm | 14 đơn được hoàn theo giá trước giảm và chỉ bị phát hiện khi kiểm tra mẫu cuối tuần. |
| 6 | Do người dùng | Khách chọn luồng giao trễ cho kiện bị vỡ, khiến trợ lý xét sai nhóm yêu cầu. |
| 7 | Hệ thống | Sổ cái trả 503 sau ba lần thử nhưng trợ lý vẫn báo đã hoàn thành công. |
| 8 | Hệ thống | Trợ lý viện dẫn điều 7.2 không tồn tại trong chính sách hiện hành dù tính đúng tiền. |
| 9 | Do người dùng | Khách nhập mã đơn của sàn vào ô cần mã vận đơn. |
| 10 | Ngữ cảnh | Từ chối do bão đúng điều khoản, còn khách dựa vào cam kết 24 giờ trên ứng dụng. |
| 11 | Giới hạn hệ thống | Trợ lý không hỗ trợ đầu vào âm thanh nên yêu cầu khách gửi văn bản. |
| 12 | Ngầm | Tool thiếu trường làm tăng số lần gọi và chi phí token D05 gấp ba trong ba tuần mà không ai phát hiện. |
| 13 | Giới hạn hệ thống | Bảo hiểm của đối tác nằm ngoài phạm vi hỗ trợ, dù trợ lý diễn đạt giới hạn không rõ. |
| 14 | Do người dùng | Khách bấm xác nhận đã nhận tiền khi chưa nhận nên yêu cầu bị đóng. |
| 15 | Hệ thống | Trợ lý tính 100% cho đơn trễ 26 giờ thay vì 50% và nhân viên đã phát hiện khi xem lại. |
| 16 | Ngữ cảnh | Quy tắc báo ngay khi xong gửi Zalo lúc 2:14 sáng, trái kỳ vọng giờ nhận tin của khách. |
| 17 | Ngầm | Bộ nhớ đệm dùng bảng giá cũ làm lệch tiền 212 đơn trong chín ngày mà không có yêu cầu mở lại. |
| 18 | Ngữ cảnh | Trợ lý hoàn đúng 15.000 đ nhưng thiếu diễn giải 50% của 30.000 đ, khiến khách hiểu là hoàn thiếu. |
| 19 | Giới hạn hệ thống | Dữ liệu chỉ có 12 tháng, nên yêu cầu cho đơn 14 tháng phải chuyển nhân viên. |
| 20 | Hệ thống | Lệnh thứ hai thiếu khóa chống trùng, khiến một đơn bị hoàn tiền hai lần. |

### Đối chiếu sau khi lưu bộ nhãn

- Với khóa tham khảo, bộ nhãn trên khớp **20/20** theo cả [hướng dẫn chi tiết](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md#nhãn-tham-khảo-cho-20-ca) và [slide chữa, trang 71](../../docs/Ngay13_Slide_Launch_Economics.pdf#page=71). Slide chấp nhận *Hệ thống* cho ca 6 nếu yêu cầu trợ lý đối chiếu mục với mô tả, hoặc ca 13 nếu tập trung vào việc trợ lý báo giới hạn không rõ. Ca 18 thuộc *Ngữ cảnh* vì số tiền đúng. Điểm đối chiếu 20/20 dùng các nhãn chính trong khóa.
- Với nguồn ghi tên Hạnh, cột người 1 trong [bảng của nhánh DangQuang](https://github.com/Youngboy1609/K5-L3B-DAY13-Strawberry-LaunchEconomics/blob/124349cc7371f57120cd4565ecf855cb67fd15ed/report/team/bang_loi.md) có đủ 20 ca và trùng **20/20** , không có ca lệch. Bản trên nhánh tích hợp hiện vẫn trống cột người 1. Chưa có bản gốc do Hạnh cung cấp trực tiếp để xác nhận đồng thuận giữa hai người gắn nhãn theo quy trình CP3.
- Cột đề tên Khang trong cùng nguồn trùng **19/20** với bộ đã lưu, lệch ở ca 6 (*Hệ thống* trong PR #2, *Do người dùng* trong bộ đã lưu). Đề xuất khi tổng hợp là ghi rõ bộ nhãn nào được so, lấy thao tác chọn sai mục làm nguyên nhân chính của ca 6 và dùng bước đối chiếu mô tả làm biện pháp khắc phục. Chưa có xác nhận thống nhất của hai người.

### Hồ sơ và phiếu duyệt chéo

- [Hồ sơ launch v0](ho_so_launch_v0.md) tổng hợp đủ bảy mục. Đề xuất No-go tại Gate 2a dựa trên phép so chi phí cùng phạm vi khi xem lại toàn bộ và các đầu vào về an toàn, đo lường, thiết kế pilot còn thiếu.
- [Phiếu chấm](phieu_cham.md) giữ thang 0/5/10 và có câu hỏi dự kiến. PR #2 ghi ứng viên Nhóm 05 (L3B). TEAM.md, các trao đổi công khai của repo và hồ sơ công khai tìm được chưa xác nhận repo của đội trình, phân công duyệt chéo hoặc biên bản trả lời.

## 4. Bằng chứng

### Mã nguồn và dữ liệu

Bộ nhãn ban đầu nằm ở commit `3f28fa83cf54451b2160f71d748c2e675945f342`. Nguồn tính là [logix_runs.csv](../../src/logix_runs.csv) và [logix_requests.csv](../../src/logix_requests.csv), với `keep_default_na=False` khi đọc file yêu cầu. Hai CSV có cùng Git blob giữa mốc tích hợp `2e4dfb4` và `DangQuang@124349c`.

Từ `src/`, `python lab13.py` của mốc tích hợp dừng ở A1 với `NotImplementedError` tại `so_lan_chay_ky_vong`. Chạy bản mã xuất riêng từ `feature/nghia-lab13-a-b-metrics@9bb9dc0` và `DangQuang@124349c` với cùng thư mục làm việc và CSV. Cả hai bản in A1 ĐẠT (1,20 · 1,25 · 1,25). Bản Quang in thêm D1 và E1. Các kết quả dưới đây được tính chéo từ CSV. [Mã Nghĩa](https://github.com/Youngboy1609/K5-L3B-DAY13-Strawberry-LaunchEconomics/blob/9bb9dc0c3bd50741ec7043c901009e1e537ebecb/src/lab13.py) · [Mã Quang](https://github.com/Youngboy1609/K5-L3B-DAY13-Strawberry-LaunchEconomics/blob/124349cc7371f57120cd4565ecf855cb67fd15ed/src/lab13.py) · [Bảng chi phí của Quang](https://github.com/Youngboy1609/K5-L3B-DAY13-Strawberry-LaunchEconomics/blob/124349cc7371f57120cd4565ecf855cb67fd15ed/report/team/bang_chi_phi.md)

### A2–A4 · Chi phí và phạm vi

- Cộng đủ 1.624 lượt, gồm 572 lượt lỗi. Tiền token là `(5.771.712 × 26 + 734.774 × 130) / 1.000 = 245.585,132 đ`. Tiền tool là `5.600 × 15 = 84.000 đ`. Trong hai khoản đó, 93.804,488 đ thuộc lượt 2–3. Hóa đơn token và tool chia 1.200 yêu cầu là 274,65 đ/yêu cầu.
- Xem lại `890 × 2.000 = 1.780.000 đ` và làm lại `1.132 × 2.000 = 2.264.000 đ`, đều `simulated`. Tổng `4.373.585,132 / 978 = 4.471,97 đ/việc thành công` (`simulated`), khoảng 16,28 lần hóa đơn/yêu cầu (`simulated`). Theo B3, cộng `(1.200 − 978) × 12.000` rồi chia 1.200, được **5.864,65 đ/yêu cầu** (`simulated`).
- Khi tách loại, lọc lượt chạy theo `request_id` thuộc từng loại. Tử số là tổng tiền token, tool và hai khoản thời lượng của loại đó.

| Loại | Thành công / yêu cầu | Lượt chạy | Tổng trợ lý (đ, simulated) | Đ/việc thành công (simulated) | Cả hệ thống đ/yêu cầu, chưa có cố định (simulated) |
| --- | ---: | ---: | ---: | ---: | ---: |
| `noi_dia` | 783/824 | 916 | 2.110.687,298 | 2.696 | 3.159 |
| `hang_nang` | 117/158 | 232 | 961.825,976 | 8.221 | 9.201 |
| `quoc_te` | 41/150 | 348 | 923.121,766 | 22.515 | 14.874 |
| `doi_tac` | 37/68 | 128 | 377.950,092 | 10.215 | 11.029 |

Tỉ lệ lượt `ok` của `quoc_te` giảm từ 45/150 xuống 12/105 và 2/93 ở lượt 1–3. `doi_tac` còn ít dư địa so với 12.000 đ khi tính hết xử lý thủ công và có điều khoản riêng. Phạm vi xem xét gồm `noi_dia` và `hang_nang` với 900/982 việc thành công.

| A4 · Tổng yêu cầu toàn hệ thống/tháng | Việc thành công trong phạm vi, dự phóng | Cố định đ/việc | Đ/việc gồm cố định (simulated) | Cả hệ thống đ/yêu cầu trong phạm vi gồm cố định (simulated) |
| ---: | ---: | ---: | ---: | ---: |
| 45.000 | 33.750 | 1.185,19 | 4.599 | 5.217 |
| 22.500 | 16.875 | 2.370,37 | 5.784 | 6.303 |

A4 dùng `số việc thành công/tháng = tổng yêu cầu/tháng × 900/1.200` để phân bổ 40 triệu đ vào mẫu số thành công. Ở cột cuối, chi phí cơ sở là `(3.072.513,274 + 82 × 12.000) / 982 = 4.130,87 đ/yêu cầu` (`simulated`), rồi cộng 40 triệu đ chia số yêu cầu **trong phạm vi** (`tổng yêu cầu/tháng × 982/1.200`).

### B1–B4 · Độ nhạy và xử lý thủ công

B1 đổi từng khoản so với A2, giữ nguyên mẫu số 978 trừ hai kịch bản cắt lượt. B2 thay hai khoản cùng lúc. Tất cả kết quả và mức thay đổi trong bảng đều `simulated`.

| Kịch bản | Đ/việc thành công | Thay đổi so với A2 |
| --- | ---: | ---: |
| Token gấp đôi / giảm nửa | 4.723 / 4.346 | +5,6% / −2,8% |
| Xem lại gấp đôi / giảm nửa | 6.292 / 3.562 | +40,7% / −20,3% |
| Làm lại gấp đôi / giảm nửa | 6.787 / 3.315 | +51,8% / −25,9% |
| Lương tăng 25% | 5.506 | +23,1% |
| Tối đa hai lượt | 4.237 | −5,2% |
| Tối đa một lượt | 4.111 | −8,1% |
| Token và xem lại cùng gấp đôi | 6.543 | +46,3% |

Ba yếu tố nhạy nhất theo kịch bản đã tính là làm lại, xem lại và lương. Phép tính chéo kiểm tra cả chín kịch bản B1 trong dung sai 2% trước khi làm tròn và xác nhận mức giảm khi giảm nửa bằng nửa mức tăng khi gấp đôi. Mô hình thay đổi **chi phí** xem lại hoặc làm lại trong từng kịch bản và chưa mô phỏng thay đổi tỷ lệ thành công.

B3 lọc `attempt ≤ k`. Mọi yêu cầu có `so_lan_chay > k` chuyển nhân viên và không tính phút xem lại/làm lại của trợ lý. Chi phí hệ thống bằng tổng trợ lý cộng `12.000 × (1.200 − số thành công)`.

| Lượt tối đa | Thành công | Không thành công | Tổng trợ lý (đ, simulated) | Tổng cả hệ thống (đ, simulated) | Đ/yêu cầu (simulated) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 881 | 319 | 3.621.780,644 | 7.449.780,644 | 6.208 |
| 2 | 966 | 234 | 4.093.220,230 | 6.901.220,230 | 5.751 |
| 3 | 978 | 222 | 4.373.585,132 | 7.037.585,132 | 5.865 |

Hai lượt tối ưu tổng hệ thống theo B3. Một lượt thấp nhất trên mỗi việc thành công nhưng có thêm 85 ca nhân viên phải xử lý so với hai lượt.

B4 xem lại 5 phút cho từng yêu cầu có ít nhất một lượt `ok` (948/982), với 48 ca làm lại, 900 thành công và 224.513,274 đ tiền lượt chạy. Tính tổng bằng `224.513,274 + 948 × 5 × 2.000 + 48 × phút_làm_lại × 2.000`. Cột cuối cộng 82 ca xử lý thủ công và phần phân bổ 40 triệu đ/tháng ở quy mô 45.000 yêu cầu/tháng toàn hệ thống.

| Giả định phút làm lại/ca | Tổng trợ lý (đ, simulated) | Đ/việc thành công (simulated) | Cả hệ thống đ/yêu cầu trước cố định (simulated) | Cả hệ thống đ/yêu cầu có cố định (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 9 phút theo đề | 10.568.513,274 | 11.743 | 11.764 | 12.850 |
| 1.132/74 phút, lấy trên toàn mẫu (simulated) | 11.173.053,815 | 12.415 | 12.380 | 13.466 |
| 780/48 = 16,25 phút trong phạm vi (simulated) | 11.264.513,274 | 12.516 | 12.473 | 13.559 |

Bản code Quang dùng 15,3 phút, nên tổng theo giả định làm tròn là 11.173.313,274 đ (`simulated`). Kết quả 12.415 đ/việc (`simulated`) lệch 1 đ so với hướng dẫn và nằm trong dung sai 2%. Theo cách so cùng mẫu số là yêu cầu, để giữ ở mức 12.000 đ khi đã cộng thủ công và cố định tại quy mô trên, thời gian xem lại trung bình phải ≤ 4,56 phút (làm lại 9 phút) hoặc ≤ 4,24 phút (làm lại theo trung bình toàn mẫu), đều `simulated`. Ngưỡng là `[982 × 12.000 − 82 × 12.000 − chi phí lượt chạy − chi phí làm lại − cố định phân bổ cho mẫu] / (948 × 2.000)`. [Hướng dẫn kiểm số](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md)

### E1 · Chỉ số và dữ liệu cần ghi

| Chỉ số | Phép đếm từ CSV | Kết quả |
| --- | --- | ---: |
| Chính | `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0`, chia tổng yêu cầu | 994/1.200 = 82,83% |
| Dùng | `sua` hoặc `bo`, trong tập `duoc_xem_lai = 1` | (41 + 7)/177 = 27,12% |
| An toàn | `mo_lai_trong_7_ngay = 1`, chia tổng yêu cầu | 51/1.200 = 4,25% |
| An toàn trong phạm vi | Cùng phép đếm trên nội địa và hàng nặng | 39/982 = 3,97% |

Đây là các chỉ số mô tả mẫu giả lập của lab. Chênh lệch so với baseline 70% chưa ước lượng được tác động vì mẫu chưa có đối chứng. Bản đặc tả Nghĩa liệt kê tám event có `trace_id` và ba rủi ro. Cần bằng chứng event đã chạy nối được theo yêu cầu, bổ sung dấu vết xác nhận ghi sổ cho ca 7 và khóa chống trùng cho ca 20. [Đặc tả chỉ số và rủi ro của Nghĩa](https://github.com/Youngboy1609/K5-L3B-DAY13-Strawberry-LaunchEconomics/blob/9bb9dc0c3bd50741ec7043c901009e1e537ebecb/report/team/chi_so.md)

### D1–D3 · Cỡ mẫu và mức sẵn sàng

Công thức hai tỉ lệ dùng baseline 0,70, alpha 0,05 hai phía và power 0,80. Với mức chênh 5 điểm, làm tròn lên cần 1.251 yêu cầu độc lập/nhánh (statsmodels dùng cách xấp xỉ khác cho 1.250). Hệ số thiết kế `DE = 1 + (m − 1) × 0,02`.

- Với 75 yêu cầu/nhân viên, `DE = 2,48` và `ceil(1.251 × 2,48) = 3.103` yêu cầu/nhánh, tương đương 42 nhân viên/nhánh. Nếu chỉ có 20 nhân viên hoặc 6 depot mỗi nhánh, cỡ mẫu hiệu dụng luôn thấp hơn lần lượt 1.000 và 300. Chia theo yêu cầu đạt cỡ mẫu dễ hơn, nhưng cùng nhân viên xử lý cả hai nhánh dễ làm lan tác động.
- Với MDE 6 điểm cần 859 quan sát hiệu dụng/nhánh. Phương án 20 nhân viên × 299 yêu cầu có 5.980 yêu cầu thực/nhánh, `DE = 6,96` và `5.980/6,96 = 859,20` hiệu dụng. `NormalIndPower` tại 859 quan sát hiệu dụng cho power khoảng 0,642 nếu tác động thật chỉ 5 điểm. Cần xác nhận số nhân viên, depot, khối lượng và thời gian theo dõi thêm 7 ngày sau đóng. Mẫu phạm vi hiện có chỉ bao phủ 6 depot và 20 mã nhân viên.
- `yaml.safe_load` đọc được [YAML tại mốc tích hợp](pilot_plan.yaml), nhưng còn 24 dấu hỏi ngoài chú thích và 0/3 luật có nội dung. [Bản DangQuang@124349c](https://github.com/Youngboy1609/K5-L3B-DAY13-Strawberry-LaunchEconomics/blob/124349cc7371f57120cd4565ecf855cb67fd15ed/report/team/pilot_plan.yaml) parse được, sạch placeholder, đề xuất ngẫu nhiên theo nhân viên phân tầng theo depot, đối chứng đồng thời và phân quyền giảm chia sẻ gợi ý. Bản này có ba luật đủ bốn vế về an toàn (chênh mở lại ≥ 2 điểm hoặc vượt 6%, hay có ca hoàn trùng, Giám đốc vận hành tắt trong 30 phút), chi phí (> 8.000 đ/việc thành công trong hai tuần, PM thu hẹp) và sử dụng (> 40% sửa/bỏ trong một tuần, Trưởng nhóm CSKH xử lý). Cần xác nhận các ngưỡng và người có quyền dừng, chốt depot/lịch và làm rõ điều kiện qua từng bước rollout.

### Bàn giao các file có nội dung trùng

[PR #1](https://github.com/Youngboy1609/K5-L3B-DAY13-Strawberry-LaunchEconomics/pull/1) là nguồn A–B và đặc tả E. [PR #2](https://github.com/Youngboy1609/K5-L3B-DAY13-Strawberry-LaunchEconomics/pull/2) có thay đổi cùng đường dẫn ở cả năm file của phần Khang. Hai bản cần được rà khi tích hợp để giữ cột người 1 và phần tổng hợp thuộc phạm vi Hạnh, dùng bộ nhãn có nguồn rõ ràng cho cột người 2 và bỏ các ghi nhận duyệt chéo chưa xác minh.

## 5. Công cụ AI đã dùng

Codex hỗ trợ lập bộ phân tích nhãn, đối chiếu nguồn, tổng hợp hồ sơ  Dùng Git để đối chiếu phiên bản, Python/pandas và Decimal để đếm và tính lại từ CSV, statsmodels để kiểm tra power, PyYAML để đọc kế hoạch và pypdf để đọc slide. Kiểm tra tự động đối chiếu bộ nhãn đã lưu, các phép tính, phạm vi diff và liên kết. Bộ nhãn được phân tích trước khi mở khóa tham khảo.

## 6. Tự đánh giá

Đã lập đủ 20 nhãn, chốt phần phân tích chi phí và chuẩn bị hồ sơ bảy mục. CP3 còn thiếu nguồn trực tiếp để xác nhận hai bộ nhãn độc lập. Phiếu chưa chấm điểm vì thiếu hồ sơ đội trình đã xác minh. Phần tích hợp của nhóm vẫn thiếu đầu ra A1 chạy được, bảng khắc phục đã xác nhận và kế hoạch pilot có thể thực hiện.
