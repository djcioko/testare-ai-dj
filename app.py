import streamlit as st
import random
import time
from PIL import Image

# 1. Configurare & Design Tonomat
st.set_page_config(page_title="HERCULE AI - TONOMAT TOTAL", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    iframe { border-radius: 20px; border: 4px solid #1ed760; background-color: black; box-shadow: 0px 0px 20px #1ed760; }
    </style>
    """, unsafe_allow_html=True)

if "yt_id" not in st.session_state:
    st.session_state.yt_id = "v2H4l9RpkwM"
if "nume_piesa" not in st.session_state:
    st.session_state.nume_piesa = "Sistem pregătit. Fă o poză!"

st.title("🎰 HERCULE AI: Tonomatul cu Toată Lista")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 Senzor Vizual")
    foto = st.camera_input("Fă o poză pentru predicție")
    upload = st.file_uploader("Sau încarcă o poză", type=['jpg', 'png', 'jpeg'])
    
    sursa = foto if foto else upload

    if sursa:
        img = Image.open(sursa).convert('RGB') 
        st.image(img, width=300)
        
        with st.spinner('🎲 Ruleta se învârte prin sute de piese...'):
            img_small = img.resize((1, 1))
            r, g, b = img_small.getpixel((0, 0))
            lumina = (r + g + b) / 3
            
            # --- TOATĂ LISTA TA ORGANIZATĂ PE CATEGORII ---
            
            # 1. CATEGORIA VESELĂ (Pop, Dance, Karaoke, Luminos)
            piese_vesele = [
                {"nume": "Pharrell Williams - Happy", "id": "ZbZSe6N_BXs"},
                {"nume": "Bruno Mars - Marry You", "id": "OMr9zCvtOfY"},
                {"nume": "Village People - Y.M.C.A.", "id": "VC_9v-Yv6zI"},
                {"nume": "Taylor Swift - Shake It Off", "id": "nfWlot6h_JM"},
                {"nume": "Justin Timberlake - Can't Stop The Feeling", "id": "ru0K8uYEZWw"},
                {"nume": "Shakira - Waka Waka", "id": "pRpeEdMmmQg"},
                {"nume": "Michel Telo - Ai se eu te pego", "id": "hcm55lU9knw"},
                {"nume": "LMFAO - Party Rock Anthem", "id": "KQ6zr6kCPj8"},
                {"nume": "Las Ketchup - Asereje", "id": "V0P_a99Uf6A"},
                {"nume": "Andra - Iubirea Schimba Tot", "id": "W-tP-Y6t1yU"},
                {"nume": "Voltaj - 20 de ani", "id": "mU57v_9u_vY"},
                {"nume": "HI-Q - Gasca mea", "id": "p0y_v-tXyvY"},
                {"nume": "Loredana - Zig Zagga", "id": "Yn6iUf-pXyU"},
                {"nume": "O-Zone - Dragostea Din Tei", "id": "j_9v_UvF6zI"},
                {"nume": "Gente de Zona - La Gozadera", "id": "t_9v_UvF6zI"},
                {"nume": "King Africa - La Bomba", "id": "vSInN5_Xv1s"},
                {"nume": "Hermes House Band - Country Roads", "id": "vSInN5_Xv1s"}
            ]

            # 2. CATEGORIA ENERGETICĂ (Rock, Latino, Roșu/Portocaliu)
            piese_energetice = [
                {"nume": "AC/DC - Thunderstruck", "id": "v2AC41dglnM"},
                {"nume": "AC/DC - Highway to Hell", "id": "l482T0yNkeo"},
                {"nume": "Bon Jovi - It's My Life", "id": "vx2u5uUu3DE"},
                {"nume": "Queen - Don't Stop Me Now", "id": "HgzGwKwLmgM"},
                {"nume": "Enrique Iglesias - Bailando", "id": "b8I-7Wk_Vbc"},
                {"nume": "Don Omar - Danza Kuduro", "id": "7zp1TbLFPp8"},
                {"nume": "Zdob si Zdup - Moldoveni s-au nascut", "id": "S1XUOnE66f4"},
                {"nume": "Phoenix - Andrii Popa", "id": "vSInN5_Xv1s"},
                {"nume": "Damian & Brothers - In statie la Lizeanu", "id": "vSInN5_Xv1s"},
                {"nume": "Shakira - Hips Don't Lie", "id": "DUT5rEU6pqM"},
                {"nume": "Pitbull - Timber", "id": "hHUbLv4ThOo"},
                {"nume": "Metallica - Enter Sandman", "id": "CD-E-mdf6uA"}
            ]

            # 3. CATEGORIA RETRO / FOLCLOR (Verde, Relaxat, Clasice)
            piese_retro = [
                {"nume": "Dan Spataru - Drumurile noastre", "id": "H7I4m8G5zE8"},
                {"nume": "Mirabela Dauer - Ioane, Ioane", "id": "Yv5yW6uM7-c"},
                {"nume": "Ducu Bertzi - M-am indragostit numai de ea", "id": "S-O6v-YhG0I"},
                {"nume": "Gica Petrescu - I-a mai toarna un paharel", "id": "vSInN5_Xv1s"},
                {"nume": "Benone Sinulescu - Dulce-i vinul", "id": "vSInN5_Xv1s"},
                {"nume": "Beatles - Twist And Shout", "id": "b-vaYIRjLRI"},
                {"nume": "Ray Charles - Hit The Road Jack", "id": "Q8Tiz6HL7NI"},
                {"nume": "Abba - Dancing Queen", "id": "xFrGuiiL7KI"},
                {"nume": "Boney M - Rasputin", "id": "kv---S6Udfg"}
            ]

            # 4. CATEGORIA ELEGANTĂ / BLUES (Albastru, Nostalgic)
            piese_elegante = [
                {"nume": "Frank Sinatra - My Way", "id": "qQzdAsjWGPg"},
                {"nume": "Frank Sinatra - New York, New York", "id": "leohcvho96k"},
                {"nume": "Whitney Houston - I Will Always Love You", "id": "3JWTaaS7LdU"},
                {"nume": "John Legend - All Of Me", "id": "450p7goxZqg"},
                {"nume": "Leonard Cohen - Dance Me To The End Of Love", "id": "NGorjBVag0I"},
                {"nume": "Holograf - Sa nu-mi iei niciodata dragostea", "id": "H8-v_uY8v_A"},
                {"nume": "Angela Similea - Sa mori de dragoste ranita", "id": "7F_9-Vv8v-c"},
                {"nume": "Mihaela Runceanu - De-ar fi sa vii", "id": "vSInN5_Xv1s"}
            ]

            # 5. CATEGORIA STREET / HARD (Negru, Închis, Intens)
            piese_street = [
                {"nume": "B.U.G. Mafia - Sa Cante Trompetele", "id": "mE1_v_UvF6U"},
                {"nume": "The Weeknd - Blinding Lights", "id": "4NRXx6U8ABQ"},
                {"nume": "Eminem - Lose Yourself", "id": "_Yhyp-_hKXY"},
                {"nume": "House Of Pain - Jump Around", "id": "X_J8v_9Uv-I"},
                {"nume": "Travis Scott - Goosebumps", "id": "Dst9gZkq1a8"},
                {"nume": "50 Cent - In Da Club", "id": "5qm8PH4xAss"},
                {"nume": "Avicii - Wake Me Up", "id": "IcrbM1l_BoI"}
            ]

            # LOGICĂ RULETĂ PE CULORI
            if lumina > 180:
                vibe = "PARTY LUMINOS"
                lista_finala = piese_vesele
            elif r > g and r > b:
                vibe = "ENERGIC ROȘU"
                lista_finala = piese_energetice
            elif g > r:
                vibe = "FOLK/RETRO VERDE"
                lista_finala = piese_retro
            elif b > r:
                vibe = "ELEGANT ALBASTRU"
                lista_finala = piese_elegante
            else:
                vibe = "STREET DARK"
                lista_finala = piese_street

            # RULETA: Amestecăm și alegem
            random.shuffle(lista_finala)
            piesa_aleasa = random.choice(lista_finala)
            
            time.sleep(1) # Efect de tonomat
            st.markdown(f"### 🎰 Vibe: `{vibe}`")
            st.markdown(f"### 🎵 Tonomatul a extras: **{piesa_aleasa['nume']}**")
            
            st.session_state.yt_id = piesa_aleasa['id']
            st.session_state.nume_piesa = piesa_aleasa['nume']

with col2:
    st.subheader("📺 YouTube Player (Auto-Play)")
    yt_url = f"https://www.youtube.com/embed/{st.session_state.yt_id}?autoplay=1&mute=0"
    
    st.markdown(
        f'<iframe key="{st.session_state.yt_id}" width="100%" height="400" src="{yt_url}" '
        f'frameborder="0" allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>', 
        unsafe_allow_html=True
    )
    st.success(f"Acum cântă: {st.session_state.nume_piesa}")
