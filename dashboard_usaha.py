import streamlit as st
import pandas as pd
import re
import altair as alt

# Konfigurasi halaman
st.set_page_config(page_title="DISPARTA - Pemetaan Usaha", layout="wide", page_icon="🏝️")

# Branding logo (opsional, ganti dengan logo instansi jika ada)
st.image("data:image/png;base64,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", width=250)

# CSS Kustom
st.markdown("""
    <style>
    body {
        background-color: #f0fdf4;
    }
    .main { background-color: #f9fff9; }
    h1, h2, h3, h4 {
        color: #00695c;
    }
    .stSelectbox label, .stFileUploader label {
        font-weight: 400;
        color: #004d40;
    }
    .stCheckbox > div {
        font-weight: 300;
    }
    .block-container {
        padding-top: 4rem;
    }
    </style>
""", unsafe_allow_html=True)

# Judul dan header
st.title("🌴 DISPARTA (Rekap Usaha)")
st.caption("Dinas Pariwisata Kabupaten - Visualisasi & Pemetaan Usaha Masyarakat")

# Sidebar input
with st.sidebar:
    st.header("📂 Input Dataset")
    uploaded_file = st.file_uploader("Unggah CSV Data Usaha :", type=["csv"])

# Fungsi ekstrak kecamatan
def ekstrak_kecamatan(alamat):
    if isinstance(alamat, str):
        match = re.search(r'\bKec(?:amatan)?\.?\s+([A-Za-z\s]+?)(?:,|$)', alamat, re.IGNORECASE)
        if match:
            return match.group(1).strip().upper()
    return "TIDAK DIKETAHUI"

if uploaded_file is not None:
    try:
        df_raw = pd.read_csv(uploaded_file, skiprows=3)
        df = df_raw.iloc[2:].reset_index(drop=True)

        # Rename kolom
        df = df.rename(columns={
            df.columns[0]: "NAMA USAHA",
            df.columns[1]: "ALAMAT",
            df.columns[2]: "KONTAK",
            df.columns[4]: "TENAGA KERJA LAKI",
            df.columns[5]: "TENAGA KERJA PEREMPUAN",
            df.columns[6]: "TENAGA KERJA TOTAL",
            df.columns[15]: "SUBSEKTOR",
            df.columns[16]: "JENIS USAHA"
        })

        # Tambah kolom kecamatan
        df["KECAMATAN"] = df["ALAMAT"].apply(ekstrak_kecamatan)

        # Sidebar filter
        kecamatan_terdaftar = sorted(df["KECAMATAN"].dropna().unique())
        selected_kecamatan = st.sidebar.selectbox("🏘️ Pilih Kecamatan", kecamatan_terdaftar)

        # Filter data
        filtered_df = df[df["KECAMATAN"] == selected_kecamatan]

        # Ringkasan data
        with st.expander("📌 Ringkasan Umum", expanded=True):
            total_usaha = len(df)
            total_tenaga_kerja = pd.to_numeric(df["TENAGA KERJA TOTAL"], errors="coerce").sum()
            st.metric("Total Usaha Terdata", f"{total_usaha:,}")
            st.metric("Total Tenaga Kerja", f"{int(total_tenaga_kerja):,} orang")

        # Tabel usaha per kecamatan
        st.subheader(f"📍 Usaha Terdata di Kecamatan **{selected_kecamatan}**")
        if not filtered_df.empty:
            st.dataframe(
                filtered_df[["NAMA USAHA", "ALAMAT", "TENAGA KERJA TOTAL", "SUBSEKTOR", "JENIS USAHA", "KONTAK"]],
                use_container_width=True
            )
        else:
            st.warning("⚠️ Tidak ada data ditemukan untuk kecamatan ini.")

        # Grafik jumlah usaha per kecamatan
        if st.checkbox("📊 Grafik Jumlah Usaha per Kecamatan"):
            usaha_count = df["KECAMATAN"].value_counts().reset_index()
            usaha_count.columns = ["KECAMATAN", "JUMLAH"]

            chart = alt.Chart(usaha_count).mark_bar(color="#00796B").encode(
                x=alt.X("JUMLAH:Q", title="Jumlah Usaha"),
                y=alt.Y("KECAMATAN:N", sort='-x', title="Kecamatan"),
                tooltip=["KECAMATAN", "JUMLAH"]
            ).properties(
                width=800,
                height=400,
                title="📊 Jumlah Usaha Tervalidasi per Kecamatan"
            )
            st.altair_chart(chart, use_container_width=True)

    except Exception as e:
        st.error(f"❌ Gagal memproses file: {e}")
else:
    st.info("⬅️ Silakan unggah file CSV terlebih dahulu melalui sidebar.")
