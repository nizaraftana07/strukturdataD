import streamlit as st
import re

# Konfigurasi Halaman Streamlit
st.set_page_config(page_title="Tugas Mandiri Struktur Data", page_icon="📚", layout="wide")

# Sidebar untuk Navigasi Menu Tugas
st.sidebar.title("Menu Tugas")
pilihan_tugas = st.sidebar.radio("Pilih Tugas:", ["1. Visualisasi Operasi Set", "2. Word Count Komentar"])

st.sidebar.markdown("---")
st.sidebar.info("Silakan pilih menu di atas untuk melihat visualisasi masing-masing tugas.")

# ==============================================================================
# TUGAS 1: VISUALISASI OPERASI SET
# ==============================================================================
if pilihan_tugas == "1. Visualisasi Operasi Set":
    st.title("🔢 Visualisasi Operasi Set")
    st.write("Aplikasi untuk menghitung operasi set: Union, Intersection, Difference, dan Symmetric Difference.")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        input_a = st.text_input("Masukkan elemen Set A (pisahkan dengan koma):", "1, 2, 3, 4, 5")
        # Mengubah input teks menjadi python set (menghapus spasi kosong)
        set_a = set(val.strip() for val in input_a.split(",") if val.strip())
        st.write("**Set A:**", set_a)

    with col2:
        input_b = st.text_input("Masukkan elemen Set B (pisahkan dengan koma):", "4, 5, 6, 7, 8")
        set_b = set(val.strip() for val in input_b.split(",") if val.strip())
        st.write("**Set B:**", set_b)
        
    st.markdown("### Hasil Operasi Set:")
    
    # Melakukan perhitungan operasi set
    union_res = set_a.union(set_b)
    intersect_res = set_a.intersection(set_b)
    diff_a_b = set_a.difference(set_b)
    diff_b_a = set_b.difference(set_a)
    sym_diff_res = set_a.symmetric_difference(set_b)
    
    # Menampilkan hasil dalam layout kolom/card yang rapi
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.metric(label="Union (A ∪ B)", value=len(union_res))
        st.code(f"{union_res}")
        
    with c2:
        st.metric(label="Intersection (A ∩ B)", value=len(intersect_res))
        st.code(f"{intersect_res}")
        
    with c3:
        st.metric(label="Difference (A - B)", value=len(diff_a_b))
        st.code(f"{diff_a_b}")
        
    with c4:
        st.metric(label="Symmetric Diff (A Δ B)", value=len(sym_diff_res))
        st.code(f"{sym_diff_res}")

# ==============================================================================
# TUGAS 2: WORD COUNT KOMENTAR SOSIAL MEDIA
# ==============================================================================
elif pilihan_tugas == "2. Word Count Komentar":
    st.title("📊 'Word Count' Komentar Sosial Media")
    st.write("Menghitung frekuensi kata dari teks komentar menggunakan struktur data Dictionary (Key: Kata, Value: Frekuensi).")
    st.markdown("---")
    
    # Input area untuk contoh komentar
    default_text = (
        "Belajar struktur data di kampus seru sekali! "
        "Struktur data membantu kita memahami pemrograman lebih dalam. Seru banget!"
    )
    user_comment = st.text_area("Masukkan teks komentar sosial media:", default_text, height=150)
    
    # Checkbox opsi pembersihan kata
    ignore_case = st.checkbox("Abaikan Huruf Kapital (Case Insensitive)", value=True)
    remove_punctuation = st.checkbox("Hapus Tanda Baca", value=True)
    
    if st.button("Hitung Frekuensi Kata", use_container_width=True):
        # Proses pembersihan teks
        processed_text = user_comment
        if ignore_case:
            processed_text = processed_text.lower()
        if remove_punctuation:
            processed_text = re.sub(r'[^\w\s]', '', processed_text)
            
        # Memisahkan kalimat menjadi list kata
        words_list = processed_text.split()
        
        # Menggunakan Dictionary untuk menghitung frekuensi kata
        word_counts = {}
        for word in words_list:
            if word: # Memastikan kata tidak kosong
                word_counts[word] = word_counts.get(word, 0) + 1
                
        # Menampilkan hasil implementasi Dictionary
        if word_counts:
            st.success("Berhasil menghitung frekuensi kata!")
            
            # Membuat layout tabel untuk representasi Key-Value
            st.markdown("### Struktur Data Dictionary (Hasil)")
            
            # Mengurutkan dictionary berdasarkan frekuensi tertinggi
            sorted_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))
            
            # Tampilkan dalam format tabel Streamlit
            st.table([{"Kata (Key)": k, "Frekuensi (Value)": v} for k, v in sorted_counts.items()])
        else:
            st.warning("Teks kosong atau tidak mengandung kata yang valid.")