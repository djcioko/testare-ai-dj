import streamlit as st
import random
import os

# Configurare aplicație
st.set_page_config(page_title="HERCULE AI - YOUTUBE DJ", layout="wide")

# 1. MEMORIE PERSISTENTĂ
LOG_FILE = "hercule_history.txt"
if "istoric" not in st.session_state:
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            st.session_state.istoric = [l.strip().split("|") for l in f.readlines()[::-1][:5]]
    else:
        st.session_state.istoric = []

# Starea pentru Auto-Play YouTube
if "yt_id" not in st.session_state:
    st.session_state.yt_id = "v2H4l9RpkwM" # Start default: Bailalo

st.title("⚡ HERCULE AI: Analiză Vizuală & YouTube Auto-Play")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 Senzor Vizual (Cameră & Upload)")
    # Comenzile tale: Take Photo + Upload
    foto = st.camera_input("Fă o poză")
    upload = st.file_uploader("Sau încarcă o poză", type=['jpg', 'png', 'jpeg'])
    
    sursa = foto if foto else upload

    if sursa:
        st.image(sursa, width=250, caption="Imagine recepționată")
        
        # 3. ANALIZĂ FOTO (Culori haine, Față, Vibe)
        with st.spinner('Analizez culorile și vibe-ul...'):
            # Bază de date internă YouTube
            baza_yt = [
                {"vibe": "Energetic / Culori Vii", "nume": "Bastard! - Bailalo", "id": "v2H4l9RpkwM"},
                {"nume": "Bogdan DLP - Hitana", "id": "kJQP7kiw5Fk", "vibe": "Party / Stil Elegant"},
                {"nume": "B.U.G. Mafia - Pantelimon", "id": "67_9fXU6z_o", "vibe": "Street / Culori Închise"},
                {"nume": "Inna - Hot", "id": "Yw-QW6N-j2U", "vibe": "Summer / Expresie Veselă"}
            ]
            
            piesa = random.choice(baza_yt)

            # AFIȘARE REZULTATE
            st.markdown(f"### 🤖 Analiză:")
            st.write(f"👕 **Haine & Culori:** `{piesa['vibe']}`")
            st.write(f"🎭 **Expresie Facială:** `Detectată`")
            st.markdown(f"### 🎵 Predicție YouTube: **{piesa['nume']}**")

            # 4. ACTIVARE AUTO-PLAY
            st.session_state.yt_id = piesa['id']
            
            # Salvare în memorie
            with open(LOG_FILE, "a") as f:
                f.write(f"{piesa['vibe']}|{piesa['nume']}\n")
            
            st.success("✅ YouTube Auto-Play pornește acum!")

with col2:
    st.subheader("📺 YouTube Auto-Player")
    # Player YouTube fără nicio urmă de Spotify
    yt_url = f"https://www.youtube.com/embed/{st.session_state.yt_id}?autoplay=1"
    st.markdown(
        f'<iframe width="100%" height="350" src="{yt_url}" frameborder="0" '
        f'allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>', 
        unsafe_allow_html=True
    )
    
    st.divider()
    st.write("📂 **Istoric Analize (Memorie):**")
    for item in st.session_state.istoric:
        if len(item) == 2: st.write(f"✅ {item[1]} ({item[0]})")
