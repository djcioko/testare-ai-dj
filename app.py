import streamlit as st
import random
import time
from PIL import Image
import urllib.parse

# 1. Configurare & Design Dark
st.set_page_config(page_title="HERCULE AI - TONOMAT TOTAL", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    iframe { border-radius: 20px; border: 4px solid #1ed760; background-color: black; box-shadow: 0px 0px 25px #1ed760; }
    .stButton>button { background-color: #1ed760; color: black; font-weight: bold; border-radius: 15px; height: 3em; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

if "query" not in st.session_state:
    st.session_state.query = ""
if "nume_piesa" not in st.session_state:
    st.session_state.nume_piesa = "Aștept poză..."

# 2. BAZA DE DATE COMPLETĂ (Toate melodiile tale)
LISTA_COMPLETA = [
    "Bruno Mars - Marry You", "Hermes House Band - Live Is Life", "Pharrell Williams - Happy", "Daft Punk - Get Lucky",
    "Chubby Checker - The Twist", "TNN - La Cucamarcha", "Whitney Houston - I Wanna Dance With Somebody",
    "Robin Thicke - Blurred Lines", "Kaoma - Lambada", "Village People - Y.M.C.A.", "T-Rio - Choopeta",
    "Taylor Swift - Shake It Off", "Michel Telo - Ai se eu te pego", "House Of Pain - Jump Around", "Queen - We Are The Champions",
    "Leonard Cohen - Dance Me To The End Of Love", "Black Eyed Peas - I Gotta Feeling", "Michel Telo - Bara bere",
    "Bon Jovi - Livin' On A Prayer", "Enrique Iglesias - Bailando", "Scorpions - Love Of My Life", "John Legend - All Of Me",
    "Beatles - Twist And Shout", "Tony Christie - Amarillo", "Tom Jones - Delilah", "Ed Sheeran - Thinking Out Loud",
    "LMFAO - Party Rock Anthem", "Usher - Yeah!", "Ray Charles - Hit The Road Jack", "Tom Jones - Sex Bomb",
    "Conecte-R - Vara nu dorm", "Shakira - Hips Don't Lie", "Juanes - La Camisa Negra", "Rihanna - We Found Love",
    "AC/DC - You Shook Me All Night Long", "O-Zone - Dragostea Din Tei", "Abba - Dancing Queen", "Pitbull - Timber",
    "Michael Jackson - Billie Jean", "Maroon 5 - Sugar", "Zdob si Zdup - Moldoveni s-au nascut", "Don Omar - Danza Kuduro",
    "Goran Bregovic - Kalasnjikov", "Holograf - Sa nu-mi iei niciodata dragostea", "Vama - Perfect fara tine",
    "Damian & Brothers - In statie la Lizeanu", "Las Ketchup - Asereje", "Depeche Mode - Enjoy the Silence",
    "Metallica - Nothing else matters", "Smiley - Oarecare", "Loredana - Zig Zagga", "Avicii - Wake Me Up!",
    "Goran Bregovic - Mahalageasca", "N&D - Vino la mine", "Phoenix - Andrii Popa", "Holograf - Cat de departe",
    "Dan Spataru - Drumurile noastre", "Iris - De vei pleca", "Laura Stoica - Un actor grabit", "Pepe - 9 vieti",
    "3 Sud Est - Amintirile", "Cargo - Daca ploaia s-ar opri", "Fuego - Ce seara minunata"
]

st.title("🎰 HERCULE AI: Tonomatul cu 200+ Melodii")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 Senzor Vizual")
    foto = st.camera_input("Fă o poză")
    upload = st.file_uploader("Sau încarcă poză", type=['jpg', 'png', 'jpeg'])
    
    sursa = foto if foto else upload

    if sursa:
        img = Image.open(sursa).convert('RGB')
        st.image(img, width=300, caption="Analiză vizuală în curs...")
        
        # RULETĂ: Căutare automată prin text
        piesa_aleasa = random.choice(LISTA_COMPLETA)
        st.session_state.query = urllib.parse.quote(piesa_aleasa)
        st.session_state.nume_piesa = piesa_aleasa
        
        st.markdown(f"### 🤖 AI a ales: **{piesa_aleasa}**")
        
        if st.button("🔊 ACTIVEAZĂ SUNETUL & PLAY"):
            st.success("Muzica pornește cu sonor!")

with col2:
    st.subheader("📺 YouTube (Căutare automată)")
    
    if st.session_state.query:
        # Căutare automată pe YouTube fără MUTE
        yt_url = f"https://www.youtube.com/embed?listType=search&list={st.session_state.query}&autoplay=1&mute=0"
        
        st.markdown(
            f'<iframe key="{time.time()}" width="100%" height="400" src="{yt_url}" '
            f'frameborder="0" allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>', 
            unsafe_allow_html=True
        )
        st.info(f"Se redă: {st.session_state.nume_piesa}")
