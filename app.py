from numpy import double
import streamlit as st
from core import Blockchain

st.set_page_config(page_title="Blockchain Eksplorer", page_icon="🎓", layout="wide")

st.title("💻 Eksplorer Blockchain")

# Inisialisasi Blockchain di Session State
if "blockchain" not in st.session_state:
    st.session_state["blockchain"] = Blockchain()

# Form Input di Sidebar
st.sidebar.header("➕ Tambah Data")
jumlah_panen = double(0)  
petani = st.sidebar.text_input("Nama Petani =")
jumlah_panen = st.sidebar.number_input("Jumlah Panen (kg) =", min_value=0.0, step=0.1, format="%.2f")
lokasi = st.sidebar.text_input("Lokasi Panen =")

if st.sidebar.button("Tambahkan Data"):
    if petani and lokasi:
        data = f"Petani: {petani}, Jumlah Panen: {jumlah_panen} kg, Lokasi: {lokasi}"
        st.session_state.blockchain.add_block(data)
        st.success("Data berhasil ditambahkan ke blockchain!")
    else:
        st.error("Harap isi semua field sebelum menambahkan data.")

# Tampilan Riwayat Blockchain (Selalu muncul di halaman utama)
st.subheader("📜 Riwayat Blockchain")

is_chain_valid = st.session_state.blockchain.is_chain_valid()
if is_chain_valid:
    st.success("✅ Blockchain valid") 
else:
    st.error("❌ Blockchain tidak valid")

for block in st.session_state.blockchain.chain[1:]:
    with st.expander(f"Data {block.index} | Hash: {block.hash[:15]}..."):
        col1, col2 = st.columns(2)

        with col1:
            st.write("**Data Payload:**")
            st.info(block.data)
            st.write(f"**Waktu:** {block.timestamp_readable}")

        with col2:
            st.write("**Kriptografi:**")
            st.write("**Hash saat ini:**")
            st.code(block.hash, language="python")
            st.write("**Hash sebelumnya (pointer):**")
            st.code(block.previous_hash, language="python")
