from unittest import case

import streamlit as st

import streamlit as st

st.set_page_config(
    page_title="Matematika Geometri",
    page_icon="🏆"
)

with st.sidebar:
    col1, col2, col3 = st.columns([1,2,1])

    col2.image("geometri.png")

    st.title("Bangun Datar")

    pilihan = st.selectbox(
        "Pilihan Bangun Datar",
        ["Persegi", "Persegi Panjang", "Lingkaran", "Segitiga", "Trapesium"]
    )

    st.caption("Dibuat dengan :fire: oleh **Safira Nur Azzahra**")

match pilihan:

    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung `luas` dan `keliling` persegi")

        sisi = st.number_input("Masukkan Sisi", min_value=0.0)

        if st.button("Hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi

            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)
            st.balloons()

    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung `luas` dan `keliling` persegi panjang")

        panjang = st.number_input("Masukkan Panjang", min_value=0.0)
        lebar = st.number_input("Masukkan Lebar", min_value=0.0)

        if st.button("Hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)

            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)
            st.balloons()

    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung `luas` dan `keliling` lingkaran")

        jari_jari = st.number_input("Masukkan Jari-jari", min_value=0.0)

        if st.button("Hitung", type="primary"):
            luas = 3.14 * jari_jari ** 2
            keliling = 2 * 3.14 * jari_jari

            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)
            st.balloons()

    case "Segitiga":
        st.title("Segitiga")
        st.markdown("Menghitung `luas` dan `keliling` segitiga")

        alas = st.number_input("Masukkan Alas", min_value=0.0)
        tinggi = st.number_input("Masukkan Tinggi", min_value=0.0)

        sisi1 = st.number_input("Masukkan Sisi 1", min_value=0.0)
        sisi2 = st.number_input("Masukkan Sisi 2", min_value=0.0)
        sisi3 = st.number_input("Masukkan Sisi 3", min_value=0.0)

        if st.button("Hitung", type="primary"):
            luas = 0.5 * alas * tinggi
            keliling = sisi1 + sisi2 + sisi3

            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=f"{luas:.2f}", border=True)
            with col2:
                st.metric("Keliling", value=f"{keliling:.2f}", border=True)

            st.snow()

    case "Trapesium":
        st.title("Trapesium")
        st.markdown("Menghitung `luas` dan `keliling` trapesium")

        sisi_sejajar1 = st.number_input("Masukkan Sisi Sejajar 1", min_value=0.0)
        sisi_sejajar2 = st.number_input("Masukkan Sisi Sejajar 2", min_value=0.0)
        tinggi = st.number_input("Masukkan Tinggi", min_value=0.0)

        sisi_miring1 = st.number_input("Masukkan Sisi Miring 1", min_value=0.0)
        sisi_miring2 = st.number_input("Masukkan Sisi Miring 2", min_value=0.0)

        if st.button("Hitung", type="primary"):
            luas = 0.5 * (sisi_sejajar1 + sisi_sejajar2) * tinggi
            keliling = sisi_sejajar1 + sisi_sejajar2 + sisi_miring1 + sisi_miring2

            col1, col2 = st.columns([2, 2])
            with col1:
                st.metric("Luas", value=f"{luas:.2f}", border=True)
            with col2:
                st.metric("Keliling", value=f"{keliling:.2f}", border=True)

            st.snow()

    case _:
        st.error("Terjadi kesalahan")
