import streamlit as st
import time

# Judul
st.title("Visualisasi Searching & Hashing")

menu = st.sidebar.selectbox(
    "Pilih Menu",
    ["Linear Search", "Binary Search", "Hashing"]
)

# =========================
# LINEAR SEARCH
# =========================
if menu == "Linear Search":

    st.header("Linear Search")

    data_input = st.text_input(
        "Masukkan data dipisahkan koma",
        "7,2,9,4,6,3,10,8"
    )

    key = st.number_input(
        "Masukkan angka yang dicari",
        step=1
    )

    if st.button("Mulai Linear Search"):

        data = [int(x) for x in data_input.split(",")]

        ditemukan = False

        st.write("Data:", data)

        for i in range(len(data)):

            st.write(f"Memeriksa index {i} = {data[i]}")
            time.sleep(1)

            if data[i] == key:
                st.success(
                    f"Data ditemukan di index {i}"
                )
                ditemukan = True
                break

        if not ditemukan:
            st.error("Data tidak ditemukan")


# =========================
# BINARY SEARCH
# =========================
elif menu == "Binary Search":

    st.header("Binary Search")

    data_input = st.text_input(
        "Masukkan data dipisahkan koma",
        "7,2,9,4,6,3,10,8"
    )

    key = st.number_input(
        "Masukkan angka yang dicari",
        step=1,
        key="binary"
    )

    if st.button("Mulai Binary Search"):

        data = [int(x) for x in data_input.split(",")]

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

            st.write(
                f"Nilai tengah = {data[tengah]}"
            )

            time.sleep(1)

            if data[tengah] == key:

                st.success(
                    f"Data ditemukan di index {tengah}"
                )

                ditemukan = True
                break

            elif key < data[tengah]:

                akhir = tengah - 1

            else:

                awal = tengah + 1

        if not ditemukan:
            st.error("Data tidak ditemukan")


# =========================
# HASHING
# =========================
else:

    st.header("Implementasi Hashing")

    data_input = st.text_input(
        "Masukkan data hashing dipisahkan koma",
        "14,5,9,1,24,34"
    )

    ukuran = st.number_input(
        "Ukuran Hash Table",
        min_value=5,
        value=10
    )

    if st.button("Proses Hashing"):

        data = [int(x) for x in data_input.split(",")]

        # Membuat tabel hash
        tabel = [None] * ukuran

        st.write("## Proses Hashing")

        for angka in data:

            index = angka % ukuran

            st.write(
                f"{angka} % {ukuran} = {index}"
            )

            # Linear Probing
            while tabel[index] is not None:

                st.warning(
                    f"Collision di index {index}"
                )

                index = (index + 1) % ukuran

            tabel[index] = angka

            st.success(
                f"{angka} disimpan di index {index}"
            )

            time.sleep(1)

        st.write("## Hasil Hash Table")

        for i in range(len(tabel)):
            st.write(f"Index {i} => {tabel[i]}")