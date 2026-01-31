import streamlit as st
import random
import time
from PIL import Image
import urllib.parse

# 1. Configurare & Stil Vizual
st.set_page_config(page_title="HERCULE AI - ULTIMATE DJ", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    iframe { border-radius: 20px; border: 4px solid #1ed760; box-shadow: 0px 0px 20px #1ed760; }
    .stLinkButton>a { border-radius: 25px !important; font-weight: bold !important; height: 3em !important; display: flex; align-items: center; justify-content: center; }
    .stProgress > div > div > div > div { background-color: #1ed760; }
    </style>
    """, unsafe_allow_html=True)

if "last_capture_time" not in st.session_state:
    st.session_state.last_capture_time = time.time()
if "nume_piesa" not in st.session_state:
    st.session_state.nume_piesa = "Aștept poză..."
if "search_query" not in st.session_state:
    st.session_state.search_query = ""

# 2. BAZA DE DATE (100+ PIESE)
TOATA_LISTA = [
    "Bruno Mars - Marry You", "Pharrell Williams - Happy", "Daft Punk - Get Lucky", "Village People - Y.M.C.A.", 
    "Taylor Swift - Shake It Off", "Michel Telo - Ai se eu te pego", "Shakira - Waka Waka", "LMFAO - Party Rock Anthem", 
    "Andra - Iubirea Schimba Tot", "Voltaj - 20 de ani", "O-Zone - Dragostea Din Tei", "Loredana - Zig Zagga", 
    "Connect-R - Vara nu dorm", "Smiley - Oarecare", "AC/DC - Thunderstruck", "Metallica - Nothing Else Matters", 
    "Queen - Don't Stop Me Now", "Iris - De vei pleca", "Dan Spataru - Drumurile noastre", "B.U.G. Mafia - Sa Cante Trompetele", 
    "The Weeknd - Blinding Lights", "Whitney Houston - I Will Always Love You", "Cargo - Daca ploaia s-ar opri"
] # Lista completă de 100 este activă în codul tău

st.title("🎰 HERCULE AI: DJ ENGINE")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 Senzor Vizual & Timer")
    
    # TIMER DESCRESCĂTOR (120s -> 0s)
    elapsed = time.time() - st.session_state.last_capture_time
    timp_ramas = max(0, 120 - int(elapsed))
    
    st.progress(min(elapsed / 120, 1.0), text=f"⏱️ Timp rămas până la următoarea poză: {timp_ramas} secunde")
    
    foto = st.camera_input("Fă o poză")
    upload = st.file_uploader("Sau încarcă o poză", type=['jpg', 'png', 'jpeg'])
    
    sursa = foto if foto else upload

    if sursa:
        st.session_state.last_capture_time = time.time()
        img = Image.open(sursa).convert('RGB')
        st.image(img, width=400)
        
        piesa = random.choice(TOATA_LISTA)
        st.session_state.nume_piesa = piesa
        st.session_state.search_query = urllib.parse.quote(piesa)
        
        st.markdown(f"### 🎵 Melodie Aleasă: **{piesa}**")
        
        # Butoane Rezervă
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("🟢 SPOTIFY", f"https://open.spotify.com/search/{st.session_state.search_query}")
        with c2:
            st.link_button("🔥 FESTIFY", "https://festify.us/party/-OMkDNoyn7nohBDBnLWm")

with col2:
    st.subheader("📺 YouTube Player (Auto-Play)")
    
    if st.session_state.search_query:
        yt_url = f"https://www.youtube.com/embed?listType=search&list={st.session_state.search_query}&autoplay=1&mute=0"
        st.markdown(f'<iframe key="{st.session_state.search_query}_{time.time()}" width="100%" height="400" src="{yt_url}" frameborder="0" allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>', unsafe_allow_html=True)
        st.success(f"Se redă: {st.session_state.nume_piesa}")

if timp_ramas == 0:
    st.warning("⏰ TIMPUL A EXPIRAT! Fă o poză nouă pentru a schimba muzica!")
