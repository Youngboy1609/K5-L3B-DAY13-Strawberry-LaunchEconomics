# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Strawberry (L3B)
- Nhóm được chấm: Nhóm 05 (L3B)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất Go có điều kiện nêu rõ con số bất lợi của việc xem lại 100% (`11.743–12.415 đ = 0,98–1,03×`), độ nhạy làm lại (`+51,8%`), và suy giảm statistical power xuống 0,64 khi nới MDE lên 6 điểm; đi kèm 4 điều kiện ràng buộc có vai trò và ngày kiểm tra cụ thể. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Ghi rõ nhãn `simulated` ở toàn bộ các con số liên quan đến thời gian xem lại, làm lại và chi phí suy diễn; phạm vi pilot thu hẹp về `noi_dia` + `hang_nang` có lý do bằng số rõ ràng: loại `quoc_te` vì tốn `22.515 đ` (`1,88×`, thành công chỉ 27,3%) và `doi_tac` (`10.215 đ = 0,85×`). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Thiết kế đối chứng song song 20 nhân viên/nhóm (đạt chuẩn 20 cụm), phân tầng ngẫu nhiên, MDE = 0,06 với m ≥ 299 yêu cầu/nhân viên; 3 luật dừng chuẩn xác cấu trúc NẾU-TRONG-THÌ-KHÔNG THÌ, có ngưỡng dừng an toàn (chênh ≥ 2% hoặc trần 6%), thời hạn và người có thẩm quyền dừng (Giám đốc vận hành). |
| **Tổng** | | | | **30 / 30** | Hồ sơ đạt chất lượng xuất sắc, luận điểm bảo vệ chặt chẽ và nhất quán bằng số liệu thực chứng. |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ launch v0 của nhóm đánh giá rất thực tế về mặt kinh tế học. Nhóm không vội vã đưa ra đề xuất Go toàn diện mà thẳng thắn chỉ ra rằng ở giai đoạn đầu nếu buộc phải xem lại 100%, chi phí trợ lý hầu như không tiết kiệm so với nhân viên tự làm (0,98× đến 1,03× định mức 12.000 đ). Thiết kế pilot phân nhóm theo nhân viên 20 vs 20 giải quyết được bài toán 20 cụm, có tính toán đánh đổi power cụ thể.

**Một câu hỏi cho đội trình:** Nếu trong 2 tuần đầu tiên của pilot, tỷ lệ xem lại vẫn bắt buộc duy trì ở mức 100% để đảm bảo an toàn nghiệp vụ, nhóm sẽ quản trị chi phí như thế nào để tổng chi phí không vượt quá định mức 12.000 đ/yêu cầu của nhân viên tự làm?

**Câu trả lời của đội trình (ghi lại tại buổi):** Trong 2 tuần đầu với rollout 10% và 25%, khối lượng yêu cầu qua trợ lý còn thấp nên mục tiêu trọng tâm là kiểm định an toàn và đo lường thời gian xem lại thực tế. Đội ngũ đã tính toán thời gian xem lại hoà vốn là ≤ 4,80–5,12 phút/ca. Đội trình áp dụng giao diện xem lại tinh gọn (bôi đậm thông tin cần đối chiếu) để hạ thời gian xem lại thực tế xuống dưới 3 phút/ca; đồng thời thiết lập luật dừng chi phí nếu chi phí mỗi việc vượt 8.000 đ liên tiếp 2 tuần thì lập tức thu hẹp phạm vi về chỉ riêng nội địa.
