import streamlit as st


st.set_page_config(page_title="CV Digital Mahasiswa", page_icon="🎓", layout="centered")


st.sidebar.title("⚙️ Pengaturan Profil")
st.sidebar.write("Masukkan data diri Anda di bawah ini:")


nama = st.sidebar.text_input("Nama Lengkap")
nim = st.sidebar.text_input("NIM")
jurusan = st.sidebar.selectbox("Jurusan",["informatika","pendidikan_bahasa_jawa","matematika"])
deskripsi = st.sidebar.text_area("Deskripsi Singkat (Bio)")
Organisasi = st.sidebar.text_area("Organisasi")
sertif = ""
if st.sidebar.checkbox("Punya pengalaman magang atau setifikasi?"):
    sertif= st.sidebar.text_area("Deskripsikan pengalaman magang atau sertifikasi Anda:")
foto_profil = st.sidebar.file_uploader("Unggah Foto Profil (Opsional)", type=['jpg', 'png', 'jpeg'])
Nama_Email = st.sidebar.text_input("Nama Email (Opsional)")


st.title("📄 Curriculum Vitae Digital")
st.markdown("---") 


kolom_kiri, kolom_kanan = st.columns([2, 1])

with kolom_kiri:
    st.header(nama)
    if jurusan == "pendidikan_bahasa_jawa":
        st.subheader(f"Pendidikan Bahasa Jawa | NIM: {nim}")
    else:
        st.subheader(f"{jurusan} | NIM: {nim}")
    st.subheader(f"Pengalaman Organisasi:")
    for item in Organisasi.split('\n'):
        if item.strip():
            st.markdown(f"- {item.strip()}")
    if sertif:
        st.subheader("Pengalaman Magang/Sertifikasi")
        for item in sertif.split('\n'):
            if item.strip():
                st.markdown(f"- {item.strip()}")
    st.write(deskripsi)


    
with kolom_kanan:
    if foto_profil is not None:
        st.image(foto_profil, width=200, caption="Foto Profil")
    else:
        st.info("Belum ada foto yang diunggah.")


st.markdown("### 🛠️ Keahlian Teknis")

st.sidebar.markdown("---")
st.sidebar.subheader("Atur Kemahiran Skill")
if jurusan == "informatika": 
    skill_python = st.sidebar.slider("Python", 0, 100)
    skill_web = st.sidebar.slider("Web Development", 0, 100)
    skill_db = st.sidebar.slider("Database", 0, 100)

elif jurusan == "pendidikan_bahasa_jawa":
    skill_Aksara =  st.sidebar.slider("Aksara", 0, 100)
    skill_Bahasa = st.sidebar.slider("Bahasa", 0, 100)
    skill_Mengajar = st.sidebar.slider("Mengajar", 0, 100)

else:
    skill_pembuktian =  st.sidebar.slider("pembuktian sistematis", 0, 100)
    skill_pemodelan = st.sidebar.slider("Pemodelan", 0, 100)
    skill_gagasan = st.sidebar.slider("Presentasi dan Komunikasi gagasan", 0, 100)

if jurusan == "informatika": 
    st.write("**Python**")
    st.progress(skill_python)

    st.write("**Web Development (HTML/CSS)**")
    st.progress(skill_web)

    st.write("**Database (SQL)**")
    st.progress(skill_db)


elif jurusan == "pendidikan_bahasa_jawa":
    st.write("**Aksara**")
    st.progress(skill_Aksara)

    st.write("**Bahasa**")
    st.progress(skill_Bahasa)

    st.write("**Mengajar**")
    st.progress(skill_Mengajar)

else:
    st.write("**Pembuktian Sistematis**")
    st.progress(skill_pembuktian)

    st.write("**Pemodelan**")
    st.progress(skill_pemodelan)

    st.write("**Presentasi dan Komunikasi Gagasan**")
    st.progress(skill_gagasan)


st.markdown("### @ Hubungi Saya")
with st.expander("Klik untuk melihat detail kontak"):
    email_user = Nama_Email.lower().replace(' ', '')
    st.write(f"📧 **Email:** {email_user}@mahasiswa.univ.ac.id")
    st.write(f"🔗 **LinkedIn:** linkedin.com/in/{email_user}")
    st.write(f"💻 **GitHub:** github.com/{email_user}")

text_sertif = ""
if sertif:
    text_sertif = f"Pengalaman Magang/Sertifikasi:\n{sertif}\n"

data_cv = f"""
Nama: {nama}
NIM: {nim}
Jurusan: {jurusan}
Deskripsi Singkat: 
{deskripsi}
Pengalaman Organisasi:
{Organisasi}
{text_sertif}
"""

st.download_button(
    label="📥 Unduh CV (.txt)",
    data = data_cv,
    file_name=f"CV_{nama.replace(' ', '_')}.txt",
    mime="text/plain"
)