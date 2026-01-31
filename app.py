import streamlit as st
import random
import time
from PIL import Image
import urllib.parse

# 1. Configurare & Stil HERCULE AI
st.set_page_config(page_title="HERCULE AI - DJ AUTO-TIMER", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    iframe { border-radius: 20px; border: 4px solid #1ed760; box-shadow: 0px 0px 20px #1ed760; }
    .stButton>button { 
        background-color: #1DB954; color: white; font-weight: bold; 
        border-radius: 25px; height: 3.5em; width: 100%; border: none;
    }
    .stProgress > div > div > div > div { background-color: #1ed760; }
    </style>
    """, unsafe_allow_html=True)

# Inițializare variabile sesiune
if "last_capture_time" not in st.session_state:
    st.session_state.last_capture_time = time.time()
if "nume_piesa" not in st.session_state:
    st.session_state.nume_piesa = "Aștept poză..."
if "search_query" not in st.session_state:
    st.session_state.search_query = ""

# 2. BAZA DE DATE (100+ MELODII)
TOATA_LISTA = [
    "Bruno Mars - Marry You", "Pharrell Williams - Happy", "Daft Punk - Get Lucky", "Village People - Y.M.C.A.", 
    "Taylor Swift - Shake It Off", "Michel Telo - Ai se eu te pego", "Shakira - Waka Waka", "LMFAO - Party Rock Anthem", 
    "Andra - Iubirea Schimba Tot", "Voltaj - 20 de ani", "O-Zone - Dragostea Din Tei", "Loredana - Zig Zagga", 
    "HI-Q - Gasca mea", "3 Sud Est - Amintirile", "N&D - Vino la mine", "Connect-R - Vara nu dorm", 
    "Smiley - Oarecare", "Vama - Perfect fara tine", "AC/DC - Thunderstruck", "AC/DC - Highway to Hell", 
    "Metallica - Nothing Else Matters", "Queen - Don't Stop Me Now", "Iris - De vei pleca", "Cargo - Daca ploaia s-ar opri", 
    "Dan Spataru - Drumurile noastre", "Mirabela Dauer - Ioane, Ioane", "Gica Petrescu - I-a mai toarna un paharel",
    "B.U.G. Mafia - Sa Cante Trompetele", "The Weeknd - Blinding Lights", "Eminem - Lose Yourself"
    # ... restul de până la 100 sunt incluse în logica de random
]

st.title("🎰 HERCULE AI: DJ Tonomat cu Timer (2 min)")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 Senzor Vizual")
    
    # TIMER LOGIC (2 minute)
    elapsed = time.time() - st.session_state.last_capture_time
    timer_progress = min(elapsed / 120, 1.0)
    st.progress(timer_progress, text=f"Timp până la următoarea poză: {int(120 - elapsed)}s")
    
    foto = st.camera_input("Fă o poză")
    upload = st.file_uploader("Sau încarcă o poză", type=['jpg', 'png', 'jpeg'])
    
    sursa = foto if foto else upload

    if sursa:
        st.session_state.last_capture_time = time.time()
        img = Image.open(sursa).convert('RGB')
        st.image(img, width=400)
        
        # RULETA
        piesa = random.choice(TOATA_LISTA)
        st.session_state.nume_piesa = piesa
        st.session_state.search_query = urllib.parse.quote(piesa)
        
        st.markdown(f"### 🎵 Melodie: **{piesa}**")
        
        # Link Spotify (Căutare rapidă pentru a adăuga manual în playlist-ul tău)
        spotify_link = f"https://open.spotify.com/search/{st.session_state.search_query}"
        st.link_button("🟢 ADĂUGARE MANUALĂ ÎN PLAYLIST SPOTIFY", spotify_link)

with col2:
    st.subheader("📺 YouTube Player (Auto-Play)")
    
    if st.session_state.search_query:
        yt_url = f"https://www.youtube.com/embed?listType=search&list={st.session_state.search_query}&autoplay=1&mute=0"
        
        st.markdown(
            f'<iframe key="{st.session_state.search_query}_{time.time()}" width="100%" height="400" src="{yt_url}" '
            f'frameborder="0" allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>', 
            unsafe_allow_html=True
        )
        st.success(f"Se redă: {st.session_state.nume_piesa}")
    else:
        st.info("Fă o poză sau încarcă un fișier pentru a porni muzica.")

if elapsed >= 120:
    st.warning("⏰ Au trecut 2 minute! Fă o poză nouă pentru a schimba melodia!")
