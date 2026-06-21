import streamlit as st
import time

# Konfigurasi Halaman
st.set_page_config(page_title="Visualisasi Circular Queue", layout="centered")
st.title("🔄 Visualisasi Antrian Pasien (Circular Queue)")
st.caption("Struktur Data - Informatika | Berbasis Streamlit")

# 1. Inisialisasi Ukuran Maksimal dan State Queue
MAX_SIZE = 6  # Ukuran tetap untuk demonstrasi circular queue

if "queue" not in st.session_state:
    st.session_state.queue = [None] * MAX_SIZE
    st.session_state.front = -1
    st.session_state.rear = -1
    st.session_state.log = []

# Fungsi Helper Circular Queue
def is_full():
    return (st.session_state.rear + 1) % MAX_SIZE == st.session_state.front

def is_empty():
    return st.session_state.front == -1

def enqueue(patient_name):
    if is_full():
        st.error("❌ Antrian Penuh! Tidak dapat menambahkan pasien baru.")
        return False
    
    if is_empty():
        st.session_state.front = 0
        st.session_state.rear = 0
    else:
        st.session_state.rear = (st.session_state.rear + 1) % MAX_SIZE
        
    st.session_state.queue[st.session_state.rear] = patient_name
    st.session_state.log.insert(0, f"📥 Pasien '{patient_name}' datang & masuk antrian.")
    return True

def dequeue():
    if is_empty():
        st.sidebar.error("❌ Antrian Kosong! Tidak ada pasien yang bisa dilayani.")
        return None
    
    served_patient = st.session_state.queue[st.session_state.front]
    st.session_state.queue[st.session_state.front] = None  # Reset slot menjadi kosong
    
    if st.session_state.front == st.session_state.rear:
        # Jika hanya ada satu elemen, reset queue ke kondisi kosong
        st.session_state.front = -1
        st.session_state.rear = -1
    else:
        st.session_state.front = (st.session_state.front + 1) % MAX_SIZE
        
    st.session_state.log.insert(0, f"✅ Pasien '{served_patient}' telah dilayani.")
    return served_patient

# ==========================================
# SIDEBAR: Kontrol Antrian (Enqueue & Dequeue)
# ==========================================
st.sidebar.header("🕹️ Panel Kontrol Antrian")

# Input Pasien Baru (Enqueue)
with st.sidebar.form(key="enqueue_form", clear_on_submit=True):
    new_patient = st.text_input("Nama Pasien:")
    submit_btn = st.form_submit_button("Pasien Datang (Enqueue)")
    
    if submit_btn and new_patient.strip():
        enqueue(new_patient.strip())

st.sidebar.markdown("---")

# Layani Pasien (Dequeue)
if st.sidebar.button("Layani Pasien (Dequeue)", type="primary"):
    dequeue()

# Reset Sistem
if st.sidebar.button("Reset Sistem Antrian"):
    st.session_state.queue = [None] * MAX_SIZE
    st.session_state.front = -1
    st.session_state.rear = -1
    st.session_state.log = ["🔄 Sistem antrian direset."]

# ==========================================
# HALAMAN UTAMA: Visualisasi Grid Melingkar
# ==========================================
st.write("### 📊 Status Slot Memori Antrian")
st.write("Circular queue memanfaatkan array statis dengan indeks melingkar (*wrap-around*).")

# Menampilkan representasi visual slot
cols = st.columns(MAX_SIZE)
for i in range(MAX_SIZE):
    with cols[i]:
        val = st.session_state.queue[i]
        
        # Penanda Posisi Front dan Rear
        label = f"**Indeks {i}**"
        if i == st.session_state.front and i == st.session_state.rear:
            label += " <br>⚠️ **[FRONT & REAR]**"
        elif i == st.session_state.front:
            label += " <br>🔵 **[FRONT]**"
        elif i == st.session_state.rear:
            label += " <br>🟢 **[REAR]**"
            
        # Tampilan Box Card
        if val is not None:
            st.markdown(
                f"<div style='border:2px solid #3182ce; padding:15px; border-radius:8px; text-align:center; background-color:#ebf8ff; min-height:100px;'>"
                f"{label}<br><br><span style='color:#2b6cb0; font-weight:bold;'>👤 {val}</span>"
                f"</div>", 
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div style='border:2px dashed #cbd5e0; padding:15px; border-radius:8px; text-align:center; color:#a0aec0; min-height:100px;'> "
                f"{label}<br><br><i>Kosong</i>"
                f"</div>", 
                unsafe_allow_html=True
            )

st.write("---")

# Informasi Log dan Detail Pointer
col_left, col_right = st.columns([1, 2])

with col_left:
    st.write("### 📌 Status Indeks Pointer")
    st.metric(label="FRONT (Kepala Antrian)", value=st.session_state.front)
    st.metric(label="REAR (Ekor Antrian)", value=st.session_state.rear)

with col_right:
    st.write("### 🕒 Log Aktivitas Terbaru")
    if st.session_state.log:
        for item in st.session_state.log[:5]:  # Tampilkan 5 aktivitas terakhir
            st.write(item)
    else:
        st.write("Belum ada aktivitas.")