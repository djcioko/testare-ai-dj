import streamlit as st
import random
import time
from PIL import Image

# 1. Configurare & Design Dark (Tonomat Edition)
st.set_page_config(page_title="HERCULE AI - DJ TOTAL", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    iframe { border-radius: 20px; border: 4px solid #1ed760; background-color: black; box-shadow: 0px 0px 25px #1ed760; }
    </style>
    """, unsafe_allow_html=True)

# Memorie sesiune pentru piesa curentă
if "yt_id" not in st.session_state:
    st.session_state.yt_id = "v2H4l9RpkwM"
if "nume_piesa" not in st.session_state:
    st.session_state.nume_piesa = "Sistem pregătit. Fă o poză!"

st.title("🎰 HERCULE AI: Tonomat Complet cu Auto-Play")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 Senzor Vizual")
    foto = st.camera_input("Fă o poză pentru predicție")
    upload = st.file_uploader("Sau încarcă o poză", type=['jpg', 'png', 'jpeg'])
    
    sursa = foto if foto else upload

    if sursa:
        # Reparație eroare imagine (RGB)
        img = Image.open(sursa).convert('RGB') 
        st.image(img, width=300)
        
        with st.spinner('🎲 Ruleta se învârte prin toată lista ta...'):
            img_small = img.resize((1, 1))
            r, g, b = img_small.getpixel((0, 0))
            lumina = (r + g + b) / 3
            
            # --- TOATĂ LISTA TA ORGANIZATĂ PE CATEGORII ---
            
            piese_vesele = [
                {"nume": "Pharrell Williams - Happy", "id": "ZbZSe6N_BXs"},
                {"nume": "Bruno Mars - Marry You", "id": "OMr9zCvtOfY"},
                {"nume": "Village People - Y.M.C.A.", "id": "VC_9v-Yv6zI"},
                {"nume": "Taylor Swift - Shake It Off", "id": "nfWlot6h_JM"},
                {"nume": "Justin Timberlake - Can't Stop The Feeling", "id": "ru0K8uYEZWw"},
                {"nume": "Shakira - Waka Waka", "id": "pRpeEdMmmQg"},
                {"nume": "Michel Telo - Ai se eu te pego", "id": "hcm55lU9knw"},
                {"nume": "Andra - Iubirea Schimba Tot", "id": "W-tP-Y6t1yU"},
                {"nume": "Voltaj - 20 de ani", "id": "mU57v_9u_vY"},
                {"nume": "O-Zone - Dragostea Din Tei", "id": "j_9v_UvF6zI"}
            ]

            piese_energetice = [
                {"nume": "AC/DC - Thunderstruck", "id": "v2AC41dglnM"},
                {"nume": "AC/DC - Highway to Hell", "id": "l482T0yNkeo"},
                {"nume": "Bon Jovi - It's My Life", "id": "vx2u5uUu3DE"},
                {"nume": "Enrique Iglesias - Bailando", "id": "b8I-7Wk_Vbc"},
                {"nume": "Don Omar - Danza Kuduro", "id": "7zp1TbLFPp8"},
                {"nume": "Zdob si Zdup - Moldoveni s-au nascut", "id": "S1XUOnE66f4"},
                {"nume": "Phoenix - Andrii Popa", "id": "vSInN5_Xv1s"},
                {"nume": "Shakira - Hips Don't Lie", "id": "DUT5rEU6pqM"}
            ]

            piese_retro = [
                {"nume": "Dan Spataru - Drumurile noastre", "id": "H7I4m8G5zE8"},
                {"nume": "Mirabela Dauer - Ioane, Ioane", "id": "Yv5yW6uM7-c"},
                {"nume": "Ducu Bertzi - M-am indragostit numai de ea", "id": "S-O6v-YhG0I"},
                {"nume": "Ray Charles - Hit The Road Jack", "id": "Q8Tiz6HL7NI"},
                {"nume": "Boney M - Rasputin", "id": "kv---S6Udfg"}
            ]

            piese_elegante = [
                {"nume": "Frank Sinatra - My Way", "id": "qQzdAsjWGPg"},
                {"nume": "Whitney Houston - I Will Always Love You", "id": "3JWTaaS7LdU"},
                {"nume": "John Legend - All Of Me", "id": "450p7goxZqg"},
                {"nume": "Holograf - Sa nu-mi iei niciodata dragostea", "id": "H8-v_uY8v_A"},
                {"nume": "Leonard Cohen - Dance Me To The End Of Love", "id": "NGorjBVag0I"}
            ]

            piese_street = [
                {"nume": "B.U.G. Mafia - Sa Cante Trompetele", "id": "mE1_v_UvF6U"},
                {"nume": "The Weeknd - Blinding Lights", "id": "4NRXx6U8ABQ"},
                {"nume": "Eminem - Lose Yourself", "id": "_Yhyp-_hKXY"},
                {"nume": "Metallica - Nothing Else Matters", "id": "tAGnKpE4NCI"},
                {"nume": "Travis Scott - Goosebumps", "id": "Dst9gZkq1a8"}
            ]

            # Selecție bazată pe culori
            if lumina > 180:
                lista_finala = piese_vesele
            elif r > g and r > b:
                lista_finala = piese_energetice
            elif g > r:
                lista_finala = piese_retro
            elif b > r:
                lista_finala = piese_elegante
            else:
                lista_finala = piese_street

            # Mixare și alegere
            random.shuffle(lista_finala)
            piesa_aleasa = random.choice(lista_finala)
            
            time.sleep(1) 
            st.session_state.yt_id = piesa_aleasa['id']
            st.session_state.nume_piesa = piesa_aleasa['nume']

with col2:
    st.subheader("📺 YouTube Auto-Play")
    
    # REPARAȚIA PENTRU AUTO-PLAY
    # Folosim mute=1 și un key random pentru a forța playerul să plece imediat
    yt_url = f"https://www.youtube.com/embed/{st.session_state.yt_id}?autoplay=1&mute=1&enablejsapi=1"
    
    st.markdown(
        f'<iframe key="{st.session_state.yt_id}_{random.randint(0,1000)}" '
        f'width="100%" height="400" src="{yt_url}" frameborder="0" '
        f'allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>', 
        unsafe_allow_html=True
    )
    
    st.success(f"🎵 AI-ul redă acum: {st.session_state.nume_piesa}")
    st.info("Apasă pe 'Unmute' în player pentru sunet.")
