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
            background: rgba(0, 0, 0, 0.75);
            z-index: 0;
            pointer-events: none;
        
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
.stat-label { font-size: 0.72rem; color: #9880b8; text-transform: uppercase; letter-spacing: 0.1em; }
.unvan-box {
    background: rgba(180,130,255,0.1);
    border: 1px solid rgba(180,130,255,0.3);
    border-radius: 12px;
    padding: 2rem;
    text-align: center;
    color: #ddc8ff;
}
</style>
""", unsafe_allow_html=True)

# ── Sabitler ───────────────────────────────────────────────────────────────────

OKULLAR = {
    "🔥 Ateş":  {"hp": 18, "atk": 5, "mp": 10, "aciklama": "Güçlü saldırı, düşük savunma"},
    "🌑 Gölge": {"hp": 25, "atk": 4, "mp": 10, "aciklama": "Hile büyüleri, ekstra HP"},
    "💧 Su":    {"hp": 22, "atk": 3, "mp": 14, "aciklama": "Yüksek savunma, şifa büyüsü"},
}

BUYULAR = {
    "🔥 Ateş":  ["Alev Topu", "Yangın Duvarı", "Kızıl Fırtına"],
    "🌑 Gölge": ["Gölge Darbesi", "Karanlık Perde", "Ruh Emme"],
    "💧 Su":    ["Buz Kılıcı", "Şifa Dalgası", "Fırtına Tuzağı"],
}

HIKAYE = [
    {
        "metin": (
            "Akademinin büyük holüne adım atıyorsun. Taş duvarlar kadim büyü sembolleriyle kaplı. "
            "Bir öğrenci sana yaklaşıyor — **Selene**. Gözleri soğuk ama meraklı bakıyor.\n\n"
            "*\"Yeni misin? Bence buraya ait değilsin,\"* diyor alaycı bir tebessümle."
        ),
        "secimler": [
            {"metin": "\"Bunu sen mi karar vereceksin?\" diye karşılık ver", "sonuc": "güçlü",   "itibar": 2},
            {"metin": "Sessizce gülümse ve geç",                             "sonuc": "gizemli", "itibar": 1},
            {"metin": "\"Belki de haklısın,\" diye kabullen",                "sonuc": "zayıf",   "itibar": 0},
        ],
    },
    {
        "metin": (
            "Büyü sınıfında **Profesör Morrigan** ders veriyor. "
            "Tahtaya yasaklı bir büyü formülü çiziyor — kasıtlı mı, yanlışlıkla mı bilmiyorsun.\n\n"
            "*\"Sen... bunu daha önce gördün mü?\"* diye soruyor, gözleri sana kilitleniyor."
        ),
        "secimler": [
            {"metin": "\"Evet, ailemde bu büyü kullanılırdı\"",          "sonuc": "dürüst",   "itibar": 2},
            {"metin": "\"Hayır, hiç görmedim\" diye yalan söyle",        "sonuc": "temkinli", "itibar": 1},
            {"metin": "\"Ne büyüsü bu, tehlikeli değil mi?\" diye sor",  "sonuc": "meraklı",  "itibar": 3},
        ],
    },
    {
        "metin": (
            "Gece yarısı yasak kütüphanenin kapısının açık olduğunu fark ediyorsun. "
            "İçeriden soluk bir ışık sızıyor. **Selene** orada — yasak bir kitap okuyor.\n\n"
            "*Seni fark etti. İkisi de donup kaldınız.*"
        ),
        "secimler": [
            {"metin": "Düelloya davet et — bu sırrı öğrenmek istiyorsun",          "sonuc": "duello",   "itibar": 0},
            {"metin": "\"Bu sırrın sahibi ben de olabilirim\" de, işbirliği öner",  "sonuc": "müttefik", "itibar": 2},
            {"metin": "Sessizce geri çekil, görmezden gel",                         "sonuc": "kaçış",    "itibar": -1},
        ],
    },
]

SONUC_MESAJLARI = {
    "güçlü":    "Selene seni farklı gözlerle değerlendirdi. Saygı kazandın.",
    "gizemli":  "Sırrını korudun. Selene merak etti.",
    "zayıf":    "Selene güldü. Ama sen bunun geçici olduğunu biliyorsun.",
    "dürüst":   "Morrigan kaşlarını çattı. Aileni araştıracak gibi görünüyor.",
    "temkinli": "Profesör seni daha dikkatlice izlemeye başladı.",
    "meraklı":  "Morrigan gülümsedi — ilk kez. 'Doğru soru,' dedi.",
    "müttefik": "Selene duraksadı. Sonra gülümsedi: 'Belki de fena değilsin.'",
    "kaçış":    "Geri çekildin. Ama o sahneyi aklından çıkaramıyorsun.",
}

# ── Session state ──────────────────────────────────────────────────────────────

DEFAULTS = {
    "ekran": "giris",
    "isim": "",
    "okul": "",
    "hp": 0, "max_hp": 0, "mp": 0, "atk": 0, "itibar": 0,
    "bolum": 0,
    "log": "",
    "duello_sonrasi": 0,
    "dusman_hp": 18,
    "dusman_max_hp": 18,
    "oyuncu_duello_hp": 0,
}

for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

s = st.session_state

# ── Yardımcılar ────────────────────────────────────────────────────────────────

def hp_bar(cur, mx, renk="#9966ff"):
    pct = max(0, int(cur / mx * 100)) if mx else 0
    st.markdown(
        f'<div style="background:rgba(255,255,255,0.1);border-radius:4px;height:8px;margin-top:4px;">'
        f'<div style="width:{pct}%;background:{renk};height:8px;border-radius:4px;"></div></div>',
        unsafe_allow_html=True,
    )

def stat_satiri():
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="stat-card"><div class="stat-label">HP</div>'
                    f'<div class="stat-val">{s["hp"]}/{s["max_hp"]}</div></div>', unsafe_allow_html=True)
        hp_bar(s["hp"], s["max_hp"])
    with c2:
        st.markdown(f'<div class="stat-card"><div class="stat-label">Büyü Puanı</div>'
                    f'<div class="stat-val">{s["mp"]}</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="stat-card"><div class="stat-label">İtibar</div>'
                    f'<div class="stat-val">{s["itibar"]}</div></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

def yeniden_baslat():
    for k in list(st.session_state.keys()):
        del st.session_state[k]
    for k, v in DEFAULTS.items():
        st.session_state[k] = v

# ── GİRİŞ ──────────────────────────────────────────────────────────────────────

if s["ekran"] == "giris":
    st.markdown("<h1 style='text-align:center;color:#ddc8ff;'>✨ Vesper Academy</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#9880b8;font-style:italic;'>Büyücü Kız Akademisi — Seçim Tabanlı RPG</p>", unsafe_allow_html=True)
    st.markdown('<div class="story-box">Yıllardır gizli tutulan bir mektup sana ulaştı. '
                '"Seçildin." yazıyor yalnızca. Sabah sisi henüz dağılmamışken '
                'Vesper Akademisi\'nin demir kapıları önünde duruyorsun...</div>', unsafe_allow_html=True)

    isim = st.text_input("Karakterinin adı", max_chars=20, placeholder="Adını gir...")
    okul_sec = st.radio(
        "Büyü okulunu seç:",
        list(OKULLAR.keys()),
        format_func=lambda x: f"{x}  —  {OKULLAR[x]['aciklama']}",
    )

    if st.button("🚪 Akademiye gir", use_container_width=True):
        if not isim.strip():
            st.warning("Lütfen bir isim gir!")
        else:
            o = OKULLAR[okul_sec]
            s["isim"]   = isim.strip()
            s["okul"]   = okul_sec
            s["hp"]     = o["hp"]
            s["max_hp"] = o["hp"]
            s["mp"]     = o["mp"]
            s["atk"]    = o["atk"]
            s["bolum"]  = 0
            s["ekran"]  = "oyun"
            st.rerun()

# ── OYUN ───────────────────────────────────────────────────────────────────────

elif s["ekran"] == "oyun":
    if s["bolum"] >= len(HIKAYE):
        s["ekran"] = "bitis"
        st.rerun()

    st.markdown(f"<h2 style='color:#ddc8ff;'>🌙 {s['isim']} "
                f"<span style='font-size:1rem;color:#9880b8;'>{s['okul']}</span></h2>",
                unsafe_allow_html=True)
    stat_satiri()

    bolum = HIKAYE[s["bolum"]]
    st.markdown(f'<div class="story-box">{bolum["metin"]}</div>', unsafe_allow_html=True)
    st.markdown(f"**Bölüm {s['bolum'] + 1} / {len(HIKAYE)}**")
    st.divider()

    for i, secim in enumerate(bolum["secimler"]):
        if st.button(secim["metin"], key=f"sec_{s['bolum']}_{i}", use_container_width=True):
            s["itibar"] += secim["itibar"]
            if secim["sonuc"] == "duello":
                s["duello_sonrasi"]    = s["bolum"] + 1
                s["dusman_hp"]         = 18
                s["dusman_max_hp"]     = 18
                s["oyuncu_duello_hp"]  = s["hp"]
                s["log"]               = "Selene sihir çubuğunu kaldırdı. Düello başlıyor!"
                s["ekran"]             = "duello"
            else:
                s["log"]   = SONUC_MESAJLARI[secim["sonuc"]]
                s["bolum"] += 1
                s["ekran"] = "sonuc"
            st.rerun()

# ── SONUÇ ARA EKRANI ───────────────────────────────────────────────────────────

elif s["ekran"] == "sonuc":
    st.markdown(f"<h2 style='color:#ddc8ff;'>🌙 {s['isim']}</h2>", unsafe_allow_html=True)
    stat_satiri()
    st.markdown(f'<div class="story-box">✨ {s["log"]}</div>', unsafe_allow_html=True)

    etiket = "🏁 Sonucu gör" if s["bolum"] >= len(HIKAYE) else f"➡️ Bölüm {s['bolum'] + 1}'e geç"
    if st.button(etiket, use_container_width=True):
        s["ekran"] = "bitis" if s["bolum"] >= len(HIKAYE) else "oyun"
        st.rerun()

# ── DÜELLO ─────────────────────────────────────────────────────────────────────

elif s["ekran"] == "duello":
    st.markdown("<h2 style='color:#ddc8ff;'>⚔️ Düello — Selene ile Yüzleşme</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="stat-card"><div class="stat-label">{s["isim"]}</div>'
                    f'<div class="stat-val">{s["oyuncu_duello_hp"]}/{s["max_hp"]}</div></div>',
                    unsafe_allow_html=True)
        hp_bar(s["oyuncu_duello_hp"], s["max_hp"], "#9966ff")
    with col2:
        st.markdown(f'<div class="stat-card"><div class="stat-label">Selene</div>'
                    f'<div class="stat-val">{s["dusman_hp"]}/{s["dusman_max_hp"]}</div></div>',
                    unsafe_allow_html=True)
        hp_bar(s["dusman_hp"], s["dusman_max_hp"], "#cc4444")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<div class="story-box">{s["log"]}</div>', unsafe_allow_html=True)

    buyular = BUYULAR[s["okul"]]
    EYLEMLER = [
        {"isim": buyular[0], "hasar": (6, 9), "isabet": 0.70,
         "etiket": f"{buyular[0]} — Güçlü saldırı (%70 isabet)"},
        {"isim": buyular[1], "hasar": (3, 5), "isabet": 0.90,
         "etiket": f"{buyular[1]} — Orta saldırı (%90 isabet)"},
        {"isim": buyular[2], "hasar": (1, 3), "isabet": 1.00,
         "etiket": f"{buyular[2]} — Hafif saldırı (%100 isabet)"},
    ]
    if s["okul"] == "💧 Su":
        EYLEMLER.append({
            "isim": "Şifa Büyüsü", "hasar": (0, 0), "isabet": 1.0,
            "etiket": "Şifa Büyüsü — 5 HP kazan (Su okulu özel)", "sifa": True,
        })

    if s["dusman_hp"] > 0 and s["oyuncu_duello_hp"] > 0:
        for i, e in enumerate(EYLEMLER):
            if st.button(e["etiket"], key=f"d_{i}", use_container_width=True):
                log = ""

                # Oyuncu hamlesi
                if e.get("sifa"):
                    iyilesen = min(5, s["max_hp"] - s["oyuncu_duello_hp"])
                    s["oyuncu_duello_hp"] += iyilesen
                    log += f"💧 Şifa büyüsü! +{iyilesen} HP kazandın.\n"
                else:
                    if random.random() < e["isabet"]:
                        hasar = random.randint(*e["hasar"])
                        s["dusman_hp"] = max(0, s["dusman_hp"] - hasar)
                        log += f"✨ {e['isim']} isabet etti! Selene {hasar} hasar aldı.\n"
                    else:
                        log += f"💨 {e['isim']} ıskaladı!\n"

                # Zafer kontrolü
                if s["dusman_hp"] <= 0:
                    s["itibar"] += 3
                    s["hp"]    = s["oyuncu_duello_hp"]
                    s["log"]   = log + "\n🏆 Selene yenildi! İtibarın arttı."
                    s["bolum"] = s["duello_sonrasi"]
                    s["ekran"] = "sonuc"
                    st.rerun()

                # Düşman hamlesi
                dusman_hasar = random.randint(2, 4)
                s["oyuncu_duello_hp"] = max(0, s["oyuncu_duello_hp"] - dusman_hasar)
                log += f"🌑 Selene karşı saldırdı! {dusman_hasar} hasar aldın."

                # Yenilgi kontrolü
                if s["oyuncu_duello_hp"] <= 0:
                    s["hp"]    = 1
                    s["log"]   = log + "\n\n💀 Yenildin... Ama bu savaş bitmedi."
                    s["bolum"] = s["duello_sonrasi"]
                    s["ekran"] = "sonuc"
                    st.rerun()

                s["log"] = log
                st.rerun()

# ── BİTİŞ ──────────────────────────────────────────────────────────────────────

elif s["ekran"] == "bitis":
    itibar = s["itibar"]
    if itibar >= 8:
        unvan = "🌟 Akademi Efsanesi"
        mesaj = "Tüm akademi senin adını fısıldıyor. Efsane başladı."
    elif itibar >= 4:
        unvan = "✨ Umut Vaat Eden Cadı"
        mesaj = "Öğretmenler seni yakından izliyor. Gelecek parlak görünüyor."
    else:
        unvan = "🌙 Sessiz Gözlemci"
        mesaj = "Henüz kimse seni tam tanımıyor. Ama sen her şeyi görüyorsun."

    st.markdown("<h1 style='text-align:center;color:#ddc8ff;'>Yılın Sonu</h1>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="unvan-box">
        <div style="font-size:2rem;margin-bottom:0.5rem;">{unvan}</div>
        <div style="font-size:1rem;color:#c8b0e8;font-style:italic;margin-bottom:1.5rem;">"{mesaj}"</div>
        <div style="font-size:0.9rem;color:#9880b8;">
            {s['isim']} &nbsp;·&nbsp; {s['okul']} &nbsp;·&nbsp;
            İtibar: {itibar} puan &nbsp;·&nbsp; HP: {s['hp']}/{s['max_hp']}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Yeniden başla", use_container_width=True):
        yeniden_baslat()
        st.rerun()
