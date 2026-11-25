"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist

import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH = 40_000_000  # đồng/tháng
YEU_CAU_MOI_THANG = 45_000
LOAI_TRONG_PILOT = ('noi_dia', 'hang_nang')


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if p == 0:
        return math.inf if k is None else k
    if k is None:
        return 1 / p
    return ti_le_thanh_cong(p, k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return float(p > 0)
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    xac_suat = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / xac_suat if xac_suat else math.inf


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Tính chi phí từ các lượt chạy và yêu cầu trong phạm vi được truyền vào.

    `tong` gồm từng lượt chạy (kể cả lỗi) và thời gian xem lại, làm lại giả lập.
    `chay_lai` là phần đã nằm trong chi phí token và tool. `tong_he_thong`
    cộng thêm chi phí làm tay cho các yêu cầu agent không hoàn thành.
    `cps` là chi phí mỗi việc thành công, hoặc vô cực nếu không có việc nào thành công.
    """
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    reqs_agent = reqs
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        # Các ca vượt giới hạn chuyển thẳng cho nhân viên, nên không tính phút xem/làm lại của agent.
        reqs_agent = reqs[reqs['so_lan_chay'] <= max_lan_chay]

    tien_token = runs['tokens_in'] * gia_vao / 1000 + runs['tokens_out'] * gia_ra / 1000
    tien_tool = runs['tool_calls'] * gia_tool
    token, tool = tien_token.sum(), tien_tool.sum()
    xem_lai = reqs_agent['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs_agent['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = reqs_agent['ket_qua'].eq('thanh_cong').sum()
    khong_thanh_cong = len(reqs) - thanh_cong
    # Theo B3, cộng định mức làm tay cho từng yêu cầu agent không làm thành công.
    tong_he_thong = tong + khong_thanh_cong * BASELINE
    return dict(
        token=token,
        tool=tool,
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong if thanh_cong else math.inf,
        hoa_don_moi_yc=(token + tool) / len(reqs) if len(reqs) else math.nan,
        so_lan_chay=len(runs),
        khong_thanh_cong=khong_thanh_cong,
        tong_he_thong=tong_he_thong,
    )


def in_nhiem_vu_a(runs, reqs, reqs_pilot, goc):
    print('\nA2 | Chi phí từ trace (đồng)')
    for nhan, khoa in (
        ('Token', 'token'),
        ('Tool', 'tool'),
        ('Trong đó, lượt chạy lại (token + tool)', 'chay_lai'),
        ('Xem lại [simulated]', 'xem_lai'),
        ('Làm lại [simulated]', 'lam_lai'),
        ('Tổng chi phí [simulated]', 'tong'),
        ('Số việc thành công', 'thanh_cong'),
        ('Chi phí mỗi việc thành công [simulated]', 'cps'),
    ):
        print(f'{nhan:<42} {goc[khoa]:>12,.0f}')
    hoa_don = goc['hoa_don_moi_yc']
    he_thong_moi_yc = goc['tong_he_thong'] / len(reqs)
    print(f'Hóa đơn token + tool mỗi yêu cầu: {hoa_don:,.1f} đ')
    print(f"Chi phí mỗi việc thành công gấp {goc['cps'] / hoa_don:.1f} lần hóa đơn [simulated].")
    print(f"Phần chi phí làm lại: {goc['lam_lai'] / goc['tong']:.1%} tổng chi phí [simulated].")
    print(f'Chi phí cả hệ thống: {he_thong_moi_yc:,.0f} đ/yêu cầu, '
          f'{he_thong_moi_yc / BASELINE:.2f}× định mức làm tay [simulated].')

    print('\nA3 | Theo loại: số yêu cầu | thành công | lượt chạy/yêu cầu | đ/việc thành công [simulated] | CPS/định mức')
    for loai, nhom in reqs.groupby('loai', sort=False):
        ket_qua = mo_hinh(runs, nhom)
        print(f"{loai:<12} {len(nhom):>4} | {ket_qua['thanh_cong'] / len(nhom):>6.1%} | "
              f"{ket_qua['so_lan_chay'] / len(nhom):.2f} | {ket_qua['cps']:>6,.0f} | "
              f"{ket_qua['cps'] / BASELINE:.2f}×")
    quoc_te = runs[runs['request_id'].isin(reqs.loc[reqs['loai'].eq('quoc_te'), 'request_id'])]
    ti_le_ok = quoc_te['status'].eq('ok').groupby(quoc_te['attempt']).mean()
    print('Tỉ lệ lượt chạy quốc tế có trạng thái ok: '
          + ', '.join(f'lần {lan}: {ti_le:.1%}' for lan, ti_le in ti_le_ok.items()))

    print('\nA4 | Phân bổ 40 triệu đ/tháng cho phạm vi nội địa + hàng nặng [simulated]')
    pilot = mo_hinh(runs, reqs_pilot)
    thanh_cong_moi_yc = pilot['thanh_cong'] / len(reqs)
    print('Yêu cầu/tháng | Việc thành công/tháng | Cố định/việc | Tổng đ/việc thành công | CPS/định mức')
    for khoi_luong in (YEU_CAU_MOI_THANG, YEU_CAU_MOI_THANG // 2):
        viec_thanh_cong = khoi_luong * thanh_cong_moi_yc
        co_dinh_moi_viec = CHI_PHI_CO_DINH / viec_thanh_cong
        tong_moi_viec = pilot['cps'] + co_dinh_moi_viec
        print(f'{khoi_luong:>13,} | {viec_thanh_cong:>21,.0f} | {co_dinh_moi_viec:>13,.0f} | '
              f'{tong_moi_viec:>23,.0f} | {tong_moi_viec / BASELINE:.2f}×')
    if pilot['cps'] < BASELINE:
        hoa_von = math.ceil(CHI_PHI_CO_DINH / ((BASELINE - pilot['cps']) * thanh_cong_moi_yc))
        print(f'Ngưỡng để CPS gồm cố định không vượt định mức: {hoa_von:,} yêu cầu/tháng.')


def in_nhiem_vu_b(runs, reqs, reqs_pilot, goc):
    gioi_han = {lan: mo_hinh(runs, reqs, max_lan_chay=lan) for lan in (1, 2, 3)}
    kich_ban = {
        'Giá token gấp đôi': mo_hinh(runs, reqs, gia_vao=2 * GIA_VAO, gia_ra=2 * GIA_RA),
        'Giá token giảm một nửa': mo_hinh(runs, reqs, gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2),
        'Xem lại gấp đôi': mo_hinh(runs, reqs, he_so_xem_lai=2),
        'Xem lại giảm một nửa': mo_hinh(runs, reqs, he_so_xem_lai=0.5),
        'Làm lại gấp đôi': mo_hinh(runs, reqs, he_so_lam_lai=2),
        'Làm lại giảm một nửa': mo_hinh(runs, reqs, he_so_lam_lai=0.5),
        'Lương tăng 25%': mo_hinh(runs, reqs, luong_phut=1.25 * LUONG_PHUT),
        'Tối đa 2 lần chạy': gioi_han[2],
        'Chỉ 1 lần chạy': gioi_han[1],
    }
    thay_doi = {}
    print('\nB1 | Độ nhạy: đ/việc thành công và thay đổi so với gốc [simulated]')
    for ten, ket_qua in kich_ban.items():
        cps = ket_qua['cps']
        thay_doi[ten] = cps / goc['cps'] - 1
        print(f'{ten:<26} {cps:>8,.0f} {thay_doi[ten]:>+7.1%}')

    print('\nB2 | Kịch bản cặp và xếp hạng [simulated]')
    cap = mo_hinh(runs, reqs, gia_vao=2 * GIA_VAO, gia_ra=2 * GIA_RA, he_so_xem_lai=2)['cps']
    print(f"Token và xem lại cùng gấp đôi: {cap:,.0f} đ ({cap / goc['cps'] - 1:+.1%}).")
    yeu_to = {
        'Giá token': thay_doi['Giá token gấp đôi'],
        'Xem lại': thay_doi['Xem lại gấp đôi'],
        'Làm lại': thay_doi['Làm lại gấp đôi'],
        'Lương nhân viên': thay_doi['Lương tăng 25%'],
    }
    xep_hang = sorted(yeu_to.items(), key=lambda muc: muc[1], reverse=True)
    print('Ba yếu tố ảnh hưởng nhất: ' + ', '.join(f'{ten} ({muc:+.1%})' for ten, muc in xep_hang[:3]))

    print('\nB3 [simulated] | Giới hạn | Chi phí agent | Yêu cầu không thành công | Chi phí cả hệ thống | CPS')
    for lan, ket_qua in gioi_han.items():
        print(f"{lan:>13} | {ket_qua['tong']:>12,.0f} | {ket_qua['khong_thanh_cong']:>24} | "
              f"{ket_qua['tong_he_thong']:>19,.0f} | {ket_qua['cps']:>5,.0f}")
    re_nhat = min(gioi_han, key=lambda lan: gioi_han[lan]['tong_he_thong'])
    cps_thap_nhat = min(gioi_han, key=lambda lan: gioi_han[lan]['cps'])
    print(f'Tối ưu chi phí cả hệ thống: {re_nhat} lượt. Tối ưu CPS của agent: {cps_thap_nhat} lượt.')

    in_kich_ban_xem_lai_toan_bo(runs, reqs, reqs_pilot)


def in_kich_ban_xem_lai_toan_bo(runs, reqs, reqs_pilot):
    print('\nB4 | Xem lại 100% ca có lượt chạy ok trong phạm vi pilot [simulated]')
    pilot = mo_hinh(runs, reqs_pilot)
    luot_ok = runs['request_id'].isin(reqs_pilot['request_id']) & runs['status'].eq('ok')
    so_ca_ok = runs.loc[luot_ok, 'request_id'].nunique()
    so_ca_lam_lai = reqs_pilot['ket_qua'].eq('lam_lai').sum()
    phut_lam_lai = reqs.loc[reqs['ket_qua'].eq('lam_lai'), 'phut_lam_lai_simulated']
    phut_trung_binh = round(phut_lam_lai.mean(), 1)
    chi_phi_luot_chay = pilot['token'] + pilot['tool']
    tien_moi_phut_xem_lai = so_ca_ok * LUONG_PHUT
    phut_xem_lai = 5
    print(f"{len(reqs_pilot)} yêu cầu, {so_ca_ok} ca có lượt ok, {so_ca_lam_lai} ca làm lại, "
          f"{pilot['thanh_cong']} thành công. Xem lại {phut_xem_lai} phút/ca.")
    for phut in (9, phut_trung_binh):
        tien_lam_lai = so_ca_lam_lai * phut * LUONG_PHUT
        tong = chi_phi_luot_chay + phut_xem_lai * tien_moi_phut_xem_lai + tien_lam_lai
        chi_phi = tong / pilot['thanh_cong']
        hoa_von = (BASELINE * pilot['thanh_cong'] - chi_phi_luot_chay - tien_lam_lai) / tien_moi_phut_xem_lai
        print(f'Làm lại {phut:g} phút/ca: tổng {tong:,.0f} đ, '
              f'{chi_phi:,.0f} đ/việc thành công ({chi_phi / BASELINE:.2f}× định mức), '
              f'ngưỡng xem lại {hoa_von:.2f} phút/ca.')


def co_mau_hai_ti_le(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm theo công thức so sánh hai tỉ lệ độc lập."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    p_bar = (p1 + p2) / 2
    tu = za * math.sqrt(2 * p_bar * (1 - p_bar)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil((tu / (p2 - p1)) ** 2)


def in_nhiem_vu_d(reqs, reqs_pilot):
    """Tính năm câu D1 về cỡ mẫu pilot và tỉ lệ mở lại 7 ngày để chốt luật an toàn."""
    p1, alpha, power, icc = 0.70, 0.05, 0.80, 0.02
    n_5 = co_mau_hai_ti_le(p1, 0.75, alpha=alpha, power=power)
    n_5_sm = math.ceil(NormalIndPower().solve_power(
        effect_size=proportion_effectsize(0.75, p1), alpha=alpha, power=power, alternative='two-sided'
    ))
    so_nv_hien_co = 40
    so_nv_moi_nhanh = so_nv_hien_co // 2
    so_depot_moi_nhanh = 6
    de_75 = 1 + (75 - 1) * icc
    n_nv_75 = math.ceil(n_5 * de_75)
    so_nv_nhom = math.ceil(n_nv_75 / 75)
    tran_nv = so_nv_moi_nhanh / icc
    tran_depot = so_depot_moi_nhanh / icc

    n_6 = co_mau_hai_ti_le(p1, 0.76, alpha=alpha, power=power)
    m_min_6 = math.ceil((1 - icc) * n_6 / (so_nv_moi_nhanh - icc * n_6))
    de_6 = 1 + (m_min_6 - 1) * icc
    n_thu_thap = so_nv_moi_nhanh * m_min_6
    n_hieu_dung = n_thu_thap / de_6
    power_5 = NormalIndPower().solve_power(
        effect_size=proportion_effectsize(0.75, p1), nobs1=n_hieu_dung, alpha=alpha, alternative='two-sided'
    )

    mo_lai_toan_bo = reqs['mo_lai_trong_7_ngay'].mean()
    mo_lai_pilot = reqs_pilot['mo_lai_trong_7_ngay'].mean()

    print('\nD1 | Cỡ mẫu pilot (baseline 0.70, alpha 0.05, power 0.80, ICC 0.02)')
    print(f'a) Theo yêu cầu (+5 điểm): {n_5:,} mỗi nhóm (statsmodels: {n_5_sm:,})')
    print(f'b) Theo nhân viên, m=75: DE={de_75:.2f} -> {n_nv_75:,}/nhóm -> '
          f'{so_nv_nhom} người/nhóm (tổng {2 * so_nv_nhom} > {so_nv_hien_co})')
    print(f'c) {so_nv_moi_nhanh} nhân viên mỗi nhóm: trần c/ICC = {tran_nv:,.0f} < {n_5:,} (không đạt +5 điểm)')
    print(f'd) {so_depot_moi_nhanh} depot mỗi nhóm: trần c/ICC = {tran_depot:,.0f} (< 20 cụm và không đủ mẫu)')
    print(f'e) Mức chênh 6 điểm: cần {n_6:,} hiệu dụng/nhóm. Với {so_nv_moi_nhanh} người/nhóm, '
          f'm >= {m_min_6} yêu cầu/người (DE={de_6:.2f}): thu thập {n_thu_thap:,}/nhóm, '
          f'tương đương {n_hieu_dung:,.2f} hiệu dụng/nhóm.')
    print(f'   Power nếu chênh thật 5 điểm: {power_5:.2f}.')
    print(f"Tỉ lệ mo_lai_trong_7_ngay hiện tại: toàn mẫu {mo_lai_toan_bo:.2%} "
          f"({reqs['mo_lai_trong_7_ngay'].sum()}/{len(reqs)}), "
          f"phạm vi pilot {mo_lai_pilot:.2%} ({reqs_pilot['mo_lai_trong_7_ngay'].sum()}/{len(reqs_pilot)})")


def in_nhiem_vu_e1(reqs, reqs_pilot):
    """Tính thử ba chỉ số mô tả E1 trên 1.200 yêu cầu."""
    chinh_dem = ((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).sum()
    chinh = chinh_dem / len(reqs)
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    sua_dem = (xem['quyet_dinh_xem_lai'] == 'sua').sum()
    bo_dem = (xem['quyet_dinh_xem_lai'] == 'bo').sum()
    bo_qua = (sua_dem + bo_dem) / len(xem)
    an_toan_dem = (reqs['mo_lai_trong_7_ngay'] == 1).sum()
    an_toan = an_toan_dem / len(reqs)
    an_toan_pv = reqs_pilot['mo_lai_trong_7_ngay'].mean()

    print('\nE1 | Ba chỉ số mô tả trên 1.200 yêu cầu (đợt chạy thử không đối chứng)')
    print(f'Chính (đóng <=24h & không mở lại 7 ngày): {chinh:.2%} ({chinh_dem}/{len(reqs):,})')
    print(f'Dùng (sửa/bỏ gợi ý trên ca xem lại):     {bo_qua:.2%} '
          f'(({sua_dem} sửa + {bo_dem} bỏ)/{len(xem)})')
    print(f'An toàn (mở lại trong 7 ngày):            {an_toan:.2%} ({an_toan_dem}/{len(reqs):,}); '
          f'phạm vi pilot: {an_toan_pv:.2%}')


if __name__ == '__main__':
    kiem_tra_dap_an_biet_truoc()
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    reqs_pilot = reqs[reqs['loai'].isin(LOAI_TRONG_PILOT)]
    goc = mo_hinh(runs, reqs)
    in_nhiem_vu_a(runs, reqs, reqs_pilot, goc)
    in_nhiem_vu_b(runs, reqs, reqs_pilot, goc)
    in_nhiem_vu_d(reqs, reqs_pilot)
    in_nhiem_vu_e1(reqs, reqs_pilot)
