import streamlit as st
import time

st.title("Visualisasi Searching Algorithm")

# Input data
angka = st.text_input(
    "Masukkan angka dipisahkan koma",
    "7,2,9,4,6,3,10,8"
)

# Konversi ke list integer
try:
    data = [int(x) for x in angka.split(",")]
except:
    st.error("Input harus berupa angka")
    st.stop()

# Input key
key = st.number_input("Masukkan angka yang dicari", step=1)

# Pilih algoritma
pilihan = st.selectbox(
    "Pilih Algoritma",
    ["Linear Search", "Binary Search"]
)

# Tombol mulai
if st.button("Mulai Searching"):

    st.write("Data:", data)

    # LINEAR SEARCH
    if pilihan == "Linear Search":

        ditemukan = False

        for i in range(len(data)):
            st.write(f"Memeriksa index {i} = {data[i]}")
            time.sleep(1)

            if data[i] == key:
                st.success(f"Data ditemukan pada index {i}")
                ditemukan = True
                break

        if not ditemukan:
            st.error("Data tidak ditemukan")

    # BINARY SEARCH
    else:

        data.sort()
        st.write("Data setelah sorting:", data)

        awal = 0
        akhir = len(data) - 1
        ditemukan = False

        while awal <= akhir:

            tengah = (awal + akhir) // 2

            st.write(
                f"Awal={awal}, Tengah={tengah}, Akhir={akhir}"
            )

            st.write(f"Nilai tengah = {data[tengah]}")
            time.sleep(1)

            if data[tengah] == key:
                st.success(
                    f"Data ditemukan pada index {tengah}"
                )
                ditemukan = True
                break

            elif key < data[tengah]:
                akhir = tengah - 1

            else:
                awal = tengah + 1

        if not ditemukan:
            st.error("Data tidak ditemukan")