import streamlit as st
import random
import base64

st.set_page_config(page_title="Vesper Academy", page_icon="🌙", layout="centered")

def set_background(image_file):
    try:
        with open(image_file, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{data}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        .stApp::before {{
            content: "";
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.65);
            z-index: 0;
            pointer-events: none;
        }}
        </style>
        """, unsafe_allow_html=True)
    except FileNotFoundError:
        pass

set_background("foto.png")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap');

html, body, [class*="css"] { font-family: 'Crimson Text', serif; }
h1, h2, h3 { font-family: 'Cinzel', serif !important; }

.story-box {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(180,150,255,0.2);
    border-radius: 12px;
    padding: 1.5rem 2rem;
    font-size: 1.1rem;
    line-height: 1.9;
    color: #e8e0f0;
    margin-bottom: 1.5rem;
    font-style: italic;
}

.stat-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(180,150,255,0.15);
    border-radius: 10px;
    padding: 0.75rem 1rem;
    text-align: center;
}

.stat-val { font-size: 1.5rem; font-weight: 600; color: #ddc8ff; }
.stat-label { font-size: 0.72rem; color: #9880b8; }

.unvan-box {
    background: rgba(180,130,255,0.1);
    border: 1px solid rgba(180,130,255,0.3);
    border-radius: 12px;
    padding: 2rem;
    text-align: center;
    color: #ddc8ff;
}

.logo-img img {
    filter: drop-shadow(0 0 15px rgba(180,130,255,0.6));
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

OKULLAR = {
    "🔥 Ateş":  {"hp": 18, "atk": 5, "mp": 10, "aciklama": "Güçlü saldırı"},
    "🌑 Gölge": {"hp": 25, "atk": 4, "mp": 10, "aciklama": "Ekstra HP"},
    "💧 Su":    {"hp": 22, "atk": 3, "mp": 14, "aciklama": "Şifa büyüsü"},
}

BUYULAR = {
    "🔥 Ateş":  ["Alev Topu", "Yangın Duvarı", "Kızıl Fırtına"],
    "🌑 Gölge": ["Gölge Darbesi", "Karanlık Perde", "Ruh Emme"],
    "💧 Su":    ["Buz Kılıcı", "Şifa Dalgası", "Fırtına Tuzağı"],
}

HIKAYE = [
    {
        "metin": "Akademiye girdin. Selene seni süzüyor.",
        "secimler": [
            {"metin": "Karşılık ver", "sonuc": "güçlü", "itibar": 2},
            {"metin": "Sessiz kal", "sonuc": "gizemli", "itibar": 1},
        ],
    }
]

SONUC_MESAJLARI = {
    "güçlü": "Saygı kazandın.",
    "gizemli": "Merak uyandırdın.",
}

DEFAULTS = {
    "ekran": "giris",
    "isim": "",
    "okul": "",
    "hp": 0, "max_hp": 0, "mp": 0, "atk": 0, "itibar": 0,
    "bolum": 0,
    "log": "",
}

for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

s = st.session_state

def yeniden_baslat():
    st.session_state.clear()
    st.rerun()

# Giriş
if s["ekran"] == "giris":
    st.title("✨ Vesper Academy")
    isim = st.text_input("İsim")
    okul = st.radio("Okul seç", list(OKULLAR.keys()))

    if st.button("Başla"):
        s["isim"] = isim
        s["okul"] = okul
        s["hp"] = OKULLAR[okul]["hp"]
        s["max_hp"] = s["hp"]
        s["ekran"] = "oyun"
        st.rerun()

# Oyun
elif s["ekran"] == "oyun":
    bolum = HIKAYE[s["bolum"]]
    st.write(bolum["metin"])

    for secim in bolum["secimler"]:
        if st.button(secim["metin"]):
            s["itibar"] += secim["itibar"]
            s["log"] = SONUC_MESAJLARI[secim["sonuc"]]
            s["ekran"] = "bitis"
            st.rerun()

# Bitiş
elif s["ekran"] == "bitis":
    st.markdown("<h1 style='text-align:center;color:#ddc8ff;'>Yılın Sonu</h1>", unsafe_allow_html=True)

    # LOGO
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown('<div class="logo-img">', unsafe_allow_html=True)
        st.image("okullogo.png", width=200)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="unvan-box">
        <h2>{s['isim']}</h2>
        <p>İtibar: {s['itibar']}</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Yeniden başla"):
        yeniden_baslat()
