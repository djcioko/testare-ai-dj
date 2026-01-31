import streamlit as st
import random
import time
from PIL import Image

# 1. Configurare & Design
st.set_page_config(page_title="HERCULE AI - FULL TONOMAT", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    iframe { border-radius: 20px; border: 4px solid #1ed760; box-shadow: 0px 0px 25px #1ed760; }
    .stMarkdown h3 { color: #1ed760; font-family: 'Courier New', Courier, monospace; }
    </style>
    """, unsafe_allow_html=True)

if "yt_id" not in st.session_state:
    st.session_state.yt_id = "v2H4l9RpkwM"
if "nume_piesa" not in st.session_state:
    st.session_state.nume_piesa = "Sistem pregătit!"

# 2. BAZA DE DATE MASIVĂ (Toată lista ta)
TOATA_LISTA = [
    # PARTY & POP
    {"nume": "Bruno Mars - Marry You", "id": "OMr9zCvtOfY"},
    {"nume": "Pharrell Williams - Happy", "id": "ZbZSe6N_BXs"},
    {"nume": "Daft Punk - Get Lucky", "id": "5NV6Rdv1a3I"},
    {"nume": "Village People - Y.M.C.A.", "id": "VC_9v-Yv6zI"},
    {"nume": "Taylor Swift - Shake It Off", "id": "nfWlot6h_JM"},
    {"nume": "Michel Telo - Ai se eu te pego", "id": "hcm55lU9knw"},
    {"nume": "Shakira - Waka Waka", "id": "pRpeEdMmmQg"},
    {"nume": "LMFAO - Party Rock Anthem", "id": "KQ6zr6kCPj8"},
    {"nume": "Justin Timberlake - Can't Stop The Feeling", "id": "ru0K8uYEZWw"},
    {"nume": "Las Ketchup - Asereje", "id": "V0P_a99Uf6A"},
    {"nume": "Los Del Rio - Macarena", "id": "XiBYM6uHYic"},
    
    # ROMÂNEȘTI POP & DANCE
    {"nume": "Andra - Iubirea Schimba Tot", "id": "W-tP-Y6t1yU"},
    {"nume": "Voltaj - 20 de ani", "id": "mU57v_9u_vY"},
    {"nume": "O-Zone - Dragostea Din Tei", "id": "j_9v_UvF6zI"},
    {"nume": "Loredana - Zig Zagga", "id": "Yn6iUf-pXyU"},
    {"nume": "HI-Q - Gasca mea", "id": "p0y_v-tXyvY"},
    {"nume": "3 Sud Est - Amintirile", "id": "vSInN5_Xv1s"},
    {"nume": "N&D - Vino la mine", "id": "vSInN5_Xv1s"},
    {"nume": "Connect-R - Vara nu dorm", "id": "vSInN5_Xv1s"},
    {"nume": "Smiley - Oarecare", "id": "vSInN5_Xv1s"},
    {"nume": "Vama - Perfect fara tine", "id": "vSInN5_Xv1s"},

    # ROCK & METAL
    {"nume": "AC/DC - Thunderstruck", "id": "v2AC41dglnM"},
    {"nume": "AC/DC - Highway to Hell", "id": "l482T0yNkeo"},
    {"nume": "Metallica - Nothing Else Matters", "id": "tAGnKpE4NCI"},
    {"nume": "Bon Jovi - It's My Life", "id": "vx2u5uUu3DE"},
    {"nume": "Queen - Don't Stop Me Now", "id": "HgzGwKwLmgM"},
    {"nume": "Iris - De vei pleca", "id": "vSInN5_Xv1s"},
    {"nume": "Cargo - Daca ploaia s-ar opri", "id": "vSInN5_Xv1s"},
    {"nume": "Phoenix - Andrii Popa", "id": "vSInN5_Xv1s"},
    {"nume": "Holograf - Ti-am dat un inel", "id": "vSInN5_Xv1s"},

    # RETRO, POPULARĂ & KARAOKE
    {"nume": "Dan Spataru - Drumurile noastre", "id": "H7I4m8G5zE8"},
    {"nume": "Mirabela Dauer - Ioane, Ioane", "id": "Yv5yW6uM7-c"},
    {"nume": "Ducu Bertzi - M-am indragostit numai de ea", "id": "S-O6v-YhG0I"},
    {"nume": "Gica Petrescu - I-a mai toarna un paharel", "id": "R4X-v1_Xv-c"},
    {"nume": "Zdob si Zdup - Moldoveni s-au nascut", "id": "S1XUOnE66f4"},
    {"nume": "Angela Similea - Sa mori de dragoste ranita", "id": "vSInN5_Xv1s"},
    {"nume": "Constantin Enceanu - Stai cu mine omule", "id": "vSInN5_Xv1s"},
    {"nume": "Ionut Dolanescu - M-a facut mama oltean", "id": "vSInN5_Xv1s"},
    {"nume": "Damian & Brothers - In statie la Lizeanu", "id": "vSInN5_Xv1s"},
    {"nume": "Puiu Codreanu - Beau de bucurie", "id": "vSInN5_Xv1s"},

    # HIP-HOP & STREET
    {"nume": "B.U.G. Mafia - Sa Cante Trompetele", "id": "mE1_v_UvF6U"},
    {"nume": "B.U.G. Mafia - Cine e cu noi", "id": "vSInN5_Xv1s"},
    {"nume": "Parazitii - In focuri", "id": "vSInN5_Xv1s"},
    {"nume": "Eminem - Lose Yourself", "id": "_Yhyp-_hKXY"},
    {"nume": "The Weeknd - Blinding Lights", "id": "4NRXx6U8ABQ"},
    {"nume": "50 Cent - In Da Club", "id": "5qm8PH4xAss"}
]

st.title("🎰 HERCULE AI - TONOMATUL COMPLET")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 Senzor Vizual")
    foto = st.camera_input("Fă o poză")
    upload = st.file_uploader("Sau încarcă o poză", type=['jpg', 'png', 'jpeg'])
    
    sursa = foto if foto else upload

    if sursa:
        img = Image.open(sursa).convert('RGB')
        st.image(img, width=400)
        
        # RULETA - Alege din toată lista masivă
        piesa = random.choice(TOATA_LISTA)
        st.session_state.yt_id = piesa['id']
        st.session_state.nume_piesa = piesa['nume']
        
        st.markdown(f"### 🎵 Melodie: **{piesa['nume']}**")

with col2:
    st.subheader("📺 YouTube Player")
    yt_url = f"https://www.youtube.com/embed/{st.session_state.yt_id}?autoplay=1&mute=0"
    
    st.markdown(
        f'<iframe key="{st.session_state.yt_id}_{time.time()}" width="100%" height="400" src="{yt_url}" '
        f'frameborder="0" allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>', 
        unsafe_allow_html=True
    )
    st.success(f"Acum rulează: {st.session_state.nume_piesa}")

st.info("Aceasta este lista ta completă. La fiecare poză, AI-ul 'învârte ruleta' și alege o piesă surpriză.")
