import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# 1. KONFIGURASI BAHASA (LANGUAGE DICTIONARY)
# ==========================================
LANG = {
    "ID": {
        "page_title": "Kalkulator Proyeksi Outsourcing",
        "sb_title": "Parameter Proyeksi",
        "sb_basic": "1. Data Dasar",
        "lbl_manpower": "Jumlah Manpower (Orang)",
        "sb_loc": "2. Lokasi & Upah",
        "lbl_method": "Metode Input:",
        "opt_db": "Pilih Database",
        "opt_manual": "Input Manual",
        "lbl_prov": "Pilih Provinsi:",
        "lbl_detail_wage": "Detail Upah:",
        "opt_use_ump": "Gunakan UMP Provinsi",
        "opt_use_city": "Pilih Kota/Kabupaten",
        "lbl_city": "Pilih Kota/Kab:",
        "lbl_input_nominal": "Input Nominal (Rp)",
        "sb_bpjs": "3. Konfigurasi BPJS",
        "lbl_bpjs_tk": "BPJS Ketenagakerjaan",
        "exp_bpjs_tk": "Rincian Tarif BPJS TK",
        "lbl_jkk": "Tarif JKK (%)",
        "lbl_jht": "Ikut Jaminan Hari Tua (3.7%)",
        "lbl_jp": "Ikut Jaminan Pensiun (2%)",
        "lbl_bpjs_kes": "BPJS Kesehatan (4%)",
        "sb_benefit": "4. Cadangan Benefit",
        "lbl_thr": "Cadangan THR (1 bln gaji)",
        "lbl_komp": "Kompensasi PKWT (1 bln gaji)",
        "sb_comm": "5. Komersial",
        "lbl_fee": "Management Fee (%)",
        "lbl_ppn": "PPN (%)",
        "warn_data": "Data Belum Lengkap: Masukkan Jumlah Manpower dan pilih Provinsi/Kota di sidebar.",
        "status": "Status",
        "area": "Area",
        "card_inv": "Total Tagihan (Invoice)",
        "card_hpp": "Total Biaya (HPP)",
        "card_profit": "Gross Profit (Fee)",
        "card_margin": "Profit Margin",
        "sub_month": "Per Bulan",
        "sub_cost": "Beban Langsung",
        "sub_net": "Pendapatan Bersih",
        "tab_table": "Rincian & Tabel",
        "tab_chart": "Analisa Grafik",
        "h_unit": "1. Rincian Perhitungan Per Kepala (Unit Cost)",
        "h_total": "2. Total Estimasi Tagihan (Semua Manpower)",
        "info_total": "Perkalian rincian di atas dengan",
        "people": "Orang",
        # Table Items
        "item_salary": "Gaji Pokok (UMK/UMP)",
        "item_tk": "BPJS Ketenagakerjaan",
        "item_kes": "BPJS Kesehatan (4%)",
        "item_thr": "Cadangan THR (Prorata)",
        "item_komp": "Cadangan Kompensasi PKWT",
        "item_subtotal": "SUBTOTAL HPP (COGS)",
        "item_fee": "Management Fee",
        "item_ppn": "PPN",
        "item_total": "TOTAL INVOICE (Per Orang)",
        "col_component": "Komponen Biaya",
        "col_nominal": "Nominal (Rp)",
        "col_total_nominal": "Total Nominal",
        "chart_title_pie": "Komposisi Harga Satuan",
        "chart_title_bar": "Profitabilitas Project",
        "chart_cost": "Total Biaya",
        "chart_profit": "Keuntungan",
        "not_active": "Tidak Aktif"
    },
    "EN": {
        "page_title": "Outsourcing Projection Calculator",
        "sb_title": "Projection Parameters",
        "sb_basic": "1. Basic Data",
        "lbl_manpower": "Manpower Quantity (Pax)",
        "sb_loc": "2. Location & Wage",
        "lbl_method": "Input Method:",
        "opt_db": "Select Database",
        "opt_manual": "Manual Input",
        "lbl_prov": "Select Province:",
        "lbl_detail_wage": "Wage Detail:",
        "opt_use_ump": "Use Provincial Min. Wage (UMP)",
        "opt_use_city": "Select City/Regency",
        "lbl_city": "Select City:",
        "lbl_input_nominal": "Input Amount (IDR)",
        "sb_bpjs": "3. BPJS Configuration",
        "lbl_bpjs_tk": "BPJS Employment (Ketenagakerjaan)",
        "exp_bpjs_tk": "BPJS TK Rate Details",
        "lbl_jkk": "JKK Rate (%)",
        "lbl_jht": "Include Old Age Security (JHT 3.7%)",
        "lbl_jp": "Include Pension Security (JP 2%)",
        "lbl_bpjs_kes": "BPJS Healthcare (Kesehatan 4%)",
        "sb_benefit": "4. Benefit Provisions",
        "lbl_thr": "THR Provision (1 month salary)",
        "lbl_komp": "Severance/PKWT Comp. (1 month salary)",
        "sb_comm": "5. Commercial",
        "lbl_fee": "Management Fee (%)",
        "lbl_ppn": "VAT / PPN (%)",
        "warn_data": "Incomplete Data: Please input Manpower Quantity and select Province/City in the sidebar.",
        "status": "Status",
        "area": "Area",
        "card_inv": "Total Invoice",
        "card_hpp": "Total Cost (COGS)",
        "card_profit": "Gross Profit (Fee)",
        "card_margin": "Profit Margin",
        "sub_month": "Per Month",
        "sub_cost": "Direct Expense",
        "sub_net": "Net Income",
        "tab_table": "Details & Tables",
        "tab_chart": "Chart Analysis",
        "h_unit": "1. Cost Calculation Per Head (Unit Cost)",
        "h_total": "2. Total Estimated Invoice (All Manpower)",
        "info_total": "Multiplication of details above by",
        "people": "Pax",
        # Table Items
        "item_salary": "Basic Salary (UMK/UMP)",
        "item_tk": "BPJS Employment",
        "item_kes": "BPJS Healthcare (4%)",
        "item_thr": "THR Provision (Prorate)",
        "item_komp": "PKWT Compensation Reserve",
        "item_subtotal": "SUBTOTAL COGS",
        "item_fee": "Management Fee",
        "item_ppn": "VAT (PPN)",
        "item_total": "TOTAL INVOICE (Per Head)",
        "col_component": "Cost Component",
        "col_nominal": "Amount (IDR)",
        "col_total_nominal": "Total Amount",
        "chart_title_pie": "Unit Price Composition",
        "chart_title_bar": "Project Profitability",
        "chart_cost": "Total Cost",
        "chart_profit": "Gross Profit",
        "not_active": "Inactive"
    }
}

# ==========================================
# DATABASE UMK 2025 (TERBARU)
# ==========================================
DATA_UMK = {
    "Jawa Barat": {
        "Kota Bekasi": 5690752, "Kab. Karawang": 5599593, "Kab. Bekasi": 5558515,
        "Kota Depok": 5195721, "Kota Bogor": 5126897, "Kab. Bogor": 4877211,
        "Kota Bandung": 4482914, "Kota Cimahi": 3863692, "Kab. Bandung": 3757284,
        "Kab. Bandung Barat": 3736741, "Kab. Sumedang": 3732088, "Kab. Sukabumi": 3604482,
        "Kab. Subang": 3508626, "Kab. Cianjur": 3104583, "Kab. Purwakarta": 4792252,
    },
    "Banten": {
        "Kota Cilegon": 5128084, "Kota Tangerang": 5069389, "Kota Tangerang Selatan": 4974052,
        "Kab. Tangerang": 4900778, "Kab. Serang": 4857032,
    },
    "DKI Jakarta": {"DKI Jakarta (Semua Wilayah)": 5396761},
    "Jawa Tengah": {
        "Kota Semarang": 3454767, "Kab. Demak": 2940616, "Kab. Kendal": 2783320,
        "Kab. Kudus": 2680436, "Kota Surakarta (Solo)": 2416489, "Kab. Batang": 2534352,
    },
    "Jawa Timur": {
        "Kota Surabaya": 5033475, "Kab. Gresik": 4944633, "Kab. Sidoarjo": 4940940,
        "Kab. Pasuruan": 4937247, "Kab. Mojokerto": 4926228, "Kab. Malang": 3587053,
    },
    "Kepulauan Riau": {"Kota Batam": 4990238, "Kab. Bintan": 4208451, "Kab. Karimun": 3956750},
    "Riau": {"Kota Dumai": 4118944, "Kab. Bengkalis": 3933615, "Kota Pekanbaru": 3675916},
    "Sumatera Utara": {"Kota Medan": 4014022, "Kab. Deli Serdang": 3732866},
    "Sulawesi Selatan": {"Kota Makassar": 3879971},
    "Kalimantan Timur": {"Kota Balikpapan": 3701518, "Kota Samarinda": 3724397},
    "Papua": {"Kota Jayapura": 4285847, "Kab. Mimika": 4898750}
}

DATA_UMP = {
    "DKI Jakarta": 5396761, "Jawa Barat": 2191232, "Jawa Tengah": 2169348, "Jawa Timur": 2305984,
    "Banten": 2905119, "DIY Yogyakarta": 2264080, "Bali": 2996560, "Sumatera Utara": 2992559,
    "Riau": 3508775, "Kepulauan Riau": 3623653, "Kalimantan Timur": 3579313,
    "Sulawesi Selatan": 3657527, "Papua": 4285847
}

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Finfleet Calculator",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FINFLEET THEME CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #F1F6F9; font-family: 'Segoe UI', sans-serif; }
    section[data-testid="stSidebar"] { background-color: #0A2647; }
    section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3, 
    section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] label, 
    section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] div[data-testid="stWidgetLabel"] p,
    section[data-testid="stSidebar"] div[role="radiogroup"] label p { color: #ffffff !important; }
    section[data-testid="stSidebar"] input, section[data-testid="stSidebar"] select, 
    section[data-testid="stSidebar"] div[data-baseweb="select"] span { color: #333333 !important; font-weight: bold; }
    .metric-card { background-color: white; border: 1px solid #e0e0e0; border-radius: 10px; padding: 15px; text-align: center; height: 100%; display: flex; flex-direction: column; justify-content: center; }
    .metric-label { font-size: 0.9em; color: #666; margin-bottom: 5px; font-weight: 600; }
    .metric-value { font-size: 1.6em; font-weight: 700; color: #0A2647; word-wrap: break-word; }
    .metric-sub { font-size: 0.8em; margin-top: 5px; padding: 2px 8px; border-radius: 10px; display: inline-block; }
    .sub-success { background-color: #dcfce7; color: #166534; }
    .sub-info { background-color: #dbeafe; color: #1e40af; }
    .sub-warning { background-color: #fef9c3; color: #854d0e; }
    thead tr th:first-child { display:none } tbody th { display:none }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR & LANGUAGE SELECTION ---
with st.sidebar:
    # 1. Pilih Bahasa
    lang_code = st.selectbox("🌐 Language / Bahasa", ["Indonesia", "English"])
    L_CODE = "ID" if lang_code == "Indonesia" else "EN"
    txt = LANG[L_CODE] # Shortcut untuk akses teks

    try:
        st.image("logo.png", width=180)
    except:
        st.markdown("## FINFLEET")
        
    st.markdown("---")
    st.markdown(f"### ⚙️ {txt['sb_title']}")
    
    # 2. Data Dasar
    st.markdown(f"#### {txt['sb_basic']}")
    jumlah_karyawan = st.number_input(txt['lbl_manpower'], min_value=0, value=0)

    # 3. Lokasi & Upah
    st.markdown(f"#### {txt['sb_loc']}")
    mode_input = st.radio(txt['lbl_method'], [txt['opt_db'], txt['opt_manual']], horizontal=True)
    
    ump_val = 0
    selected_area_name = ""
    
    if mode_input == txt['opt_db']:
        provinsi_list = sorted(list(DATA_UMP.keys()))
        selected_prov = st.selectbox(txt['lbl_prov'], provinsi_list)
        
        has_cities = selected_prov in DATA_UMK
        opsi_upah = [txt['opt_use_ump']]
        if has_cities:
            opsi_upah.append(txt['opt_use_city'])
            
        jenis_upah = st.radio(txt['lbl_detail_wage'], opsi_upah)
        
        if jenis_upah == txt['opt_use_ump']:
            ump_val = DATA_UMP[selected_prov]
            selected_area_name = f"UMP {selected_prov}"
            st.info(f"Nominal: **Rp {ump_val:,.0f}**")
        else:
            kota_dict = DATA_UMK[selected_prov]
            kota_list = sorted(list(kota_dict.keys()))
            selected_kota = st.selectbox(txt['lbl_city'], kota_list)
            ump_val = kota_dict[selected_kota]
            selected_area_name = f"UMK {selected_kota}"
            st.info(f"Nominal: **Rp {ump_val:,.0f}**")
            
    else:
        ump_val = st.number_input(txt['lbl_input_nominal'], min_value=0, value=0, step=100000)
        selected_area_name = "Manual Input"

    # 4. BPJS
    st.markdown(f"#### {txt['sb_bpjs']}")
    use_bpjs_tk = st.checkbox(txt['lbl_bpjs_tk'], value=True)
    
    jkk_rate = 0.0024
    tk_components = []
    
    if use_bpjs_tk:
        with st.expander(txt['exp_bpjs_tk'], expanded=True):
            jkk_pct = st.slider(txt['lbl_jkk'], 0.24, 1.74, 0.24, 0.01)
            jkk_rate = jkk_pct / 100
            tk_components.append("JKK")

            jkm_rate = 0.0030
            tk_components.append("JKM")
            
            include_jht = st.checkbox(txt['lbl_jht'], value=True)
            jht_rate = 0.0370 if include_jht else 0
            if include_jht: tk_components.append("JHT")
            
            include_jp = st.checkbox(txt['lbl_jp'], value=True)
            jp_rate = 0.0200 if include_jp else 0
            if include_jp: tk_components.append("JP")
    else:
        jkk_rate = jkm_rate = jht_rate = jp_rate = 0

    use_bpjs_kes = st.checkbox(txt['lbl_bpjs_kes'], value=True)

    # 5. Benefit & Commercial
    st.markdown(f"#### {txt['sb_benefit']}")
    use_thr = st.toggle(txt['lbl_thr'], value=True)
    use_kompensasi = st.toggle(txt['lbl_komp'], value=True)
    
    st.markdown(f"#### {txt['sb_comm']}")
    mgmt_fee_pct = st.number_input(txt['lbl_fee'], min_value=0.0, value=0.0, step=0.5)
    ppn_pct = st.number_input(txt['lbl_ppn'], value=11.0) / 100

# --- LOGIC PERHITUNGAN ---
def hitung_proyeksi():
    biaya_jkk = ump_val * jkk_rate if use_bpjs_tk else 0
    biaya_jkm = ump_val * 0.003 if use_bpjs_tk else 0
    biaya_jht = ump_val * jht_rate if use_bpjs_tk else 0
    biaya_jp = ump_val * jp_rate if use_bpjs_tk else 0 
    total_bpjs_tk = biaya_jkk + biaya_jkm + biaya_jht + biaya_jp
    biaya_kes = ump_val * 0.04 if use_bpjs_kes else 0
    biaya_thr = (ump_val / 12) if use_thr else 0
    biaya_kompensasi = (ump_val / 12) if use_kompensasi else 0

    hpp_per_orang = ump_val + total_bpjs_tk + biaya_kes + biaya_thr + biaya_kompensasi
    nominal_fee = hpp_per_orang * (mgmt_fee_pct / 100)
    subtotal = hpp_per_orang + nominal_fee
    ppn = subtotal * ppn_pct
    total_invoice = subtotal + ppn

    label_tk = txt['item_tk']
    if use_bpjs_tk and tk_components:
        label_tk += f" ({', '.join(tk_components)})"
    elif use_bpjs_tk:
        label_tk += " (0%)"
    else:
        label_tk += f" ({txt['not_active']})"

    return {
        "raw": {
            "gaji": ump_val, "tk": total_bpjs_tk, "kes": biaya_kes, "thr": biaya_thr,
            "komp": biaya_kompensasi, "hpp": hpp_per_orang, "fee": nominal_fee,
            "ppn": ppn, "total": total_invoice, "label_tk": label_tk
        }
    }

res = hitung_proyeksi()
raw = res['raw']

# --- MAIN CONTENT ---
st.title(f"📊 {txt['page_title']}")
lokasi_teks = f"| {txt['area']}: **{selected_area_name}**" if ump_val > 0 and mode_input == txt['opt_db'] else ""
st.markdown(f"**{txt['status']}:** {jumlah_karyawan} Manpower {lokasi_teks} | Fee {mgmt_fee_pct}%")

if ump_val == 0 or jumlah_karyawan == 0:
    st.warning(f"👈 **{txt['warn_data']}**")
else:
    # METRICS
    total_rev_month = raw['total'] * jumlah_karyawan
    total_cost_month = raw['hpp'] * jumlah_karyawan
    total_profit_month = raw['fee'] * jumlah_karyawan
    margin = (raw['fee'] / (raw['hpp'] + raw['fee']) * 100) if raw['total'] > 0 else 0

    col1, col2, col3, col4 = st.columns(4)
    def fmt(val): return f"Rp {val:,.0f}"

    with col1:
        st.markdown(f"""<div class="metric-card"><div class="metric-label">{txt['card_inv']}</div>
        <div class="metric-value" style="color:#2563eb;">{fmt(total_rev_month)}</div>
        <div class="metric-sub sub-info">{txt['sub_month']}</div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div class="metric-card"><div class="metric-label">{txt['card_hpp']}</div>
        <div class="metric-value" style="color:#dc2626;">{fmt(total_cost_month)}</div>
        <div class="metric-sub sub-warning">{txt['sub_cost']}</div></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""<div class="metric-card"><div class="metric-label">{txt['card_profit']}</div>
        <div class="metric-value" style="color:#16a34a;">{fmt(total_profit_month)}</div>
        <div class="metric-sub sub-success">{txt['sub_net']}</div></div>""", unsafe_allow_html=True)
    with col4:
        st.markdown(f"""<div class="metric-card"><div class="metric-label">{txt['card_margin']}</div>
        <div class="metric-value" style="color:#4b5563;">{margin:.2f}%</div>
        <div class="metric-sub sub-info">Fee / (HPP + Fee)</div></div>""", unsafe_allow_html=True)

    st.markdown("---")

    # TABS
    tab_table, tab_chart = st.tabs([f"📋 {txt['tab_table']}", f"📈 {txt['tab_chart']}"])

    with tab_table:
        st.subheader(txt['h_unit'])
        rows = []
        idx = 1
        rows.append([f"{idx}. {txt['item_salary']}", raw['gaji']])
        idx += 1
        
        if use_bpjs_tk:
            rows.append([f"{idx}. {raw['label_tk']}", raw['tk']])
            idx += 1
        if use_bpjs_kes:
            rows.append([f"{idx}. {txt['item_kes']}", raw['kes']])
            idx += 1
        if use_thr:
            rows.append([f"{idx}. {txt['item_thr']}", raw['thr']])
            idx += 1
        if use_kompensasi:
            rows.append([f"{idx}. {txt['item_komp']}", raw['komp']])
            idx += 1
            
        rows.append([txt['item_subtotal'], raw['hpp']])
        rows.append([f"{idx}. {txt['item_fee']} ({mgmt_fee_pct}%)", raw['fee']])
        idx += 1
        rows.append([f"{idx}. {txt['item_ppn']} ({ppn_pct*100:.0f}%)", raw['ppn']])
        rows.append([txt['item_total'], raw['total']])
        
        df_unit = pd.DataFrame(rows, columns=[txt['col_component'], txt['col_nominal']])
        
        def highlight_totals(row):
            text = str(row[txt['col_component']])
            if "SUBTOTAL" in text or "TOTAL" in text:
                return ['background-color: #e0f2fe; color: #0284c7; font-weight: bold'] * len(row)
            return [''] * len(row)

        st.table(df_unit.style.apply(highlight_totals, axis=1).format({txt['col_nominal']: "Rp {:,.0f}"}))

        st.subheader(txt['h_total'])
        st.info(f"{txt['info_total']} **{jumlah_karyawan} {txt['people']}**.")
        
        df_total = df_unit.copy()
        df_total[txt['col_nominal']] = df_total[txt['col_nominal']] * jumlah_karyawan
        df_total.columns = [txt['col_component'], txt['col_total_nominal']]
        
        st.table(df_total.style.apply(highlight_totals, axis=1).format({txt['col_total_nominal']: "Rp {:,.0f}"}))

    with tab_chart:
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            chart_vals = [raw['gaji'], raw['tk'], raw['kes'], raw['thr'], raw['komp'], raw['fee']]
            chart_lbls = [txt['item_salary'], txt['item_tk'], txt['item_kes'], txt['item_thr'], txt['item_komp'], txt['item_fee']]
            clean_vals = [v for v in chart_vals if v > 0]
            clean_lbls = [l for l, v in zip(chart_lbls, chart_vals) if v > 0]

            if clean_vals:
                fig = px.pie(values=clean_vals, names=clean_lbls, hole=0.4, title=txt['chart_title_pie'])
                st.plotly_chart(fig, use_container_width=True)
        
        with col_c2:
            fig_bar = go.Figure(data=[
                go.Bar(name=txt['chart_cost'], x=['Finance'], y=[total_cost_month], marker_color='#dc2626'),
                go.Bar(name=txt['chart_profit'], x=['Finance'], y=[total_profit_month], marker_color='#16a34a')
            ])
            fig_bar.update_layout(barmode='stack', title=txt['chart_title_bar'])
            st.plotly_chart(fig_bar, use_container_width=True)