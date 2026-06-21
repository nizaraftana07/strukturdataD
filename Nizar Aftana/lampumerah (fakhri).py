import streamlit as st
import time

# 1. Definisi Node untuk Doubly Circular Linked List (sesuai contoh materi)
class Node:
    def __init__(self, warna, durasi):
        self.warna = warna
        self.durasi = durasi
        self.next = None
        self.prev = None

# 2. Inisialisasi Circular Linked List untuk Lampu Lalu Lintas
def inisialisasi_lampu():
    # Membuat node sesuai ketentuan tugas
    merah = Node("Merah", 40)
    hijau = Node("Hijau", 20)
    kuning = Node("Kuning", 5)
    
    # Menghubungkan secara circular (Merah -> Hijau -> Kuning -> Merah)
    merah.next = hijau
    hijau.prev = merah
    
    hijau.next = kuning
    kuning.prev = hijau
    
    kuning.next = merah
    merah.prev = kuning
    
    return merah

# --- Konfigurasi Halaman Streamlit ---
st.set_page_config(page_title="Visualisasi Lampu Merah", page_icon="🚦", layout="centered")

st.title("🚦 Visualisasi Lampu Lalu Lintas")
st.subheader("Struktur Data - Circular Linked List")
st.write("Sesuai instruksi tugas pada gambar `1000291464.jpg`")
st.markdown("---")

# Gunakan session state agar status lampu tetap terjaga saat re-run
if "current_node" not in st.session_state:
    st.session_state.current_node = inisialisasi_lampu()
    st.session_state.running = False

# Tombol Kontrol Simulasi
col1, col2 = st.columns(2)
with col1:
    if st.button("▶️ Mulai Simulasi", use_container_width=True):
        st.session_state.running = True
with col2:
    if st.button("🛑 Berhenti", use_container_width=True):
        st.session_state.running = False

# Placeholder untuk visualisasi dinamis
lampu_placeholder = st.empty()
status_placeholder = st.empty()

# Pengaturan warna CSS untuk tampilan lingkaran lampu
color_map = {
    "Merah": "#FF4B4B",
    "Kuning": "#FFAA00",
    "Hijau": "#00E676"
}

# Loop Simulasi Berjalan
while st.session_state.running:
    node = st.session_state.current_node
    warna = node.warna
    durasi = node.durasi
    hex_color = color_map[warna]
    
    # Hitung mundur durasi lampu
    for detik_tersisa in range(durasi, 0, -1):
        # Hentikan loop seketika jika tombol Berhenti ditekan
        if not st.session_state.running:
            break
            
        # Tampilan Visualisasi Menggunakan HTML/CSS di Streamlit
        lampu_placeholder.markdown(
            f"""
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; 
                        background-color: #262730; padding: 30px; border-radius: 20px; width: 200px; margin: auto; box-shadow: int 0px 0px 10px rgba(0,0,0,0.5);">
                <div style="width: 100px; height: 100px; background-color: {hex_color}; border-radius: 50%; 
                            box-shadow: 0 0 30px {hex_color}; margin-bottom: 20px;"></div>
                <h2 style="color: white; margin: 0;">{warna.upper()}</h2>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        status_placeholder.markdown(
            f"<h3 style='text-align: center;'>Sisa Waktu: <span style='color:{hex_color};'>{detik_tersisa} Detik</span></h3>", 
            unsafe_allow_html=True
        )
        
        time.sleep(1)
    
    # Berpindah ke node berikutnya (Circular Linked List) setelah durasi habis
    st.session_state.current_node = node.next
    
    # Paksa Streamlit untuk mendeteksi perubahan state tombol berhenti secara real-time
    if not st.session_state.running:
        st.rerun()

# Jika dalam kondisi stanby / berhenti
if not st.session_state.running:
    lampu_placeholder.info("Klik 'Mulai Simulasi' untuk menjalankan lampu lalu lintas.")