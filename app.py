import streamlit as st
import random
import time
from PIL import Image
import urllib.parse

# 1. Configurare & Stil
st.set_page_config(page_title="HERCULE AI - 100 PIESE", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    iframe { border-radius: 20px; border: 4px solid #1ed760; box-shadow: 0px 0px 20px #1ed760; }
    .stButton>button { 
        background-color: #1DB954; color: white; font-weight: bold; 
        border-radius: 25px; height: 3em; width: 100%; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

if "search_query" not in st.session_state:
    st.session_state.search_query = ""
if "nume_piesa" not in st.session_state:
    st.session_state.nume_piesa = "Aștept analiză..."

# 2. BAZA DE DATE MASIVĂ (100+ MELODII)
TOATA_LISTA = [
    # POP & DANCE INTERNAȚIONAL
    "Bruno Mars - Marry You", "Pharrell Williams - Happy", "Daft Punk - Get Lucky", "Village People - Y.M.C.A.", 
    "Taylor Swift - Shake It Off", "Michel Telo - Ai se eu te pego", "Shakira - Waka Waka", "LMFAO - Party Rock Anthem", 
    "Justin Timberlake - Can't Stop The Feeling", "Las Ketchup - Asereje", "Los Del Rio - Macarena", "T-Rio - Choopeta",
    "Rihanna - We Found Love", "Maroon 5 - Sugar", "Ed Sheeran - Shape of You", "Katy Perry - Roar", 
    "Black Eyed Peas - I Gotta Feeling", "Enrique Iglesias - Bailando", "Jennifer Lopez - On The Floor", "Avicii - Wake Me Up",

    # ROMÂNEȘTI POP & PARTY
    "Andra - Iubirea Schimba Tot", "Voltaj - 20 de ani", "O-Zone - Dragostea Din Tei", "Loredana - Zig Zagga", 
    "HI-Q - Gasca mea", "3 Sud Est - Amintirile", "N&D - Vino la mine", "Connect-R - Vara nu dorm", 
    "Smiley - Oarecare", "Vama - Perfect fara tine", "Alex Velea - Minim doi", "Delia - Pe aripi de vant",
    "Holograf - Sa nu-mi iei niciodata dragostea", "Directia 5 - O fata ca ea", "A.S.I.A - Luati-ma de aici", 
    "Simplu - Oficial imi merge bine", "Fly Project - Toca Toca", "Edward Maya - Stereo Love",

    # RETRO & FOLCLOR
    "Dan Spataru - Drumurile noastre", "Mirabela Dauer - Ioane, Ioane", "Ducu Bertzi - M-am indragostit numai de ea", 
    "Gica Petrescu - I-a mai toarna un paharel", "Zdob si Zdup - Moldoveni s-au nascut", "Angela Similea - Sa mori de dragoste ranita", 
    "Constantin Enceanu - Stai cu mine omule", "Ionut Dolanescu - M-a facut mama oltean", "Damian & Brothers - In statie la Lizeanu", 
    "Puiu Codreanu - Beau de bucurie", "Fuego - Ce seara minunata", "Benone Sinulescu - Radu mamii", 
    "Goran Bregovic - Kalasnjikov", "Goran Bregovic - Mahalageasca", "Margareta Paslaru - Lasati-ma sa cant",

    # ROCK & METAL
    "AC/DC - Thunderstruck", "AC/DC - Highway to Hell", "AC/DC - Back in Black", "Metallica - Nothing Else Matters", 
    "Metallica - Enter Sandman", "Bon Jovi - It's My Life", "Queen - Don't Stop Me Now", "Queen - We Will Rock You", 
    "Queen - Bohemian Rhapsody", "Iris - De vei pleca", "Iris - Strada ta", "Cargo - Daca ploaia s-ar opri", 
    "Cargo - Aproape de voi", "Phoenix - Andrii Popa", "Phoenix - Mugur de fluier", "Holograf - Ti-am dat un inel",
    "Guns N' Roses - Sweet Child O' Mine", "Deep Purple - Smoke on the Water", "Nirvana - Smells Like Teen Spirit",

    # HIP-HOP & STREET
    "B.U.G. Mafia - Sa Cante Trompetele", "B.U.G. Mafia - Cine e cu noi", "B.U.G. Mafia - Limbaj de cartier", 
    "Parazitii - In focuri", "Parazitii - Arde", "Eminem - Lose Yourself", "Eminem - Without Me", 
    "The Weeknd - Blinding Lights", "50 Cent - In Da Club", "Snoop Dogg - Still D.R.E.", "Dr. Dre - The Next Episode", 
    "Travis Scott - Goosebumps", "Coolio - Gangsta's Paradise",

    # ALTE HITURI & KARAOKE
    "Frank Sinatra - My Way", "Whitney Houston - I Will Always Love You", "John Legend - All Of Me", 
    "Adele - Rolling in the Deep", "Elvis Presley - Suspicious Minds", "Ray Charles - Hit The Road Jack", 
    "Abba - Dancing Queen", "Boney M - Rasputin", "Gloria Gaynor - I Will Survive", "Bee Gees - Stayin' Alive"
]

st.title("🎰 HERCULE AI - TONOMATUL CU 100+ PIESE")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 Senzor Vizual")
    foto = st.camera_input("Fă o poză")
    upload = st.file_uploader("Sau încarcă o poză", type=['jpg', 'png', 'jpeg'])
    
    sursa = foto if foto else upload

    if sursa:
        img = Image.open(sursa).convert('RGB')
        st.image(img, width=400)
        
        # RULETA - Alegem din cele 100+
        piesa = random.choice(TOATA_LISTA)
        st.session_state.nume_piesa = piesa
        st.session_state.search_query = urllib.parse.quote(piesa)
        
        st.markdown(f"### 🎵 Melodie: **{piesa}**")
        
        # Buton Spotify
        spotify_url = f"https://open.spotify.com/search/{st.session_state.search_query}"
        st.link_button("🟢 DESCHIDE ÎN SPOTIFY", spotify_url)

with col2:
    st.subheader("📺 YouTube Player")
    
    if st.session_state.search_query:
        yt_url = f"https://www.youtube.com/embed?listType=search&list={st.session_state.search_query}&autoplay=1&mute=0"
        
        st.markdown(
            f'<iframe key="{st.session_state.search_query}_{time.time()}" width="100%" height="400" src="{yt_url}" '
            f'frameborder="0" allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>', 
            unsafe_allow_html=True
        )
        st.success(f"Se redă: {st.session_state.nume_piesa}")
