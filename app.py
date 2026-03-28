import random
import time

# ─────────────────────────────────────────
#  VESPER ACADEMY — Büyücü Kız Akademisi RPG
# ─────────────────────────────────────────

BUYULAR = {
    "Ateş":  ["Alev Topu", "Yangın Duvarı", "Kızıl Fırtına"],
    "Gölge": ["Gölge Darbesi", "Karanlık Perde", "Ruh Emme"],
    "Su":    ["Buz Kılıcı", "Şifa Dalgası", "Fırtına Tuzağı"],
}

HIKAYE = [
    {
        "metin": (
            "Akademinin büyük holüne adım atıyorsun. Taş duvarlar kadim büyü sembolleriyle kaplı.\n"
            "Bir öğrenci sana yaklaşıyor — Selene. Gözleri soğuk ama meraklı.\n"
            "\n\"Yeni misin? Bence buraya ait değilsin,\" diyor alaycı bir tebessümle."
        ),
        "secimler": [
            {"metin": "\"Bunu sen mi karar vereceksin?\" diye karşılık ver",  "sonuc": "güçlü",   "itibar": 2},
            {"metin": "Sessizce gülümse ve geç",                              "sonuc": "gizemli", "itibar": 1},
            {"metin": "\"Belki de haklısın,\" diye kabullen",                 "sonuc": "zayıf",   "itibar": 0},
        ],
    },
    {
        "metin": (
            "Büyü sınıfında Profesör Morrigan ders veriyor.\n"
            "Tahtaya yasaklı bir büyü formülü çiziyor — kasıtlı mı, yanlışlıkla mı bilmiyorsun.\n"
            "\nSonra sana bakıyor: \"Sen... bunu daha önce gördün mü?\""
        ),
        "secimler": [
            {"metin": "\"Evet, ailemde bu büyü kullanılırdı\"",              "sonuc": "dürüst",   "itibar": 2},
            {"metin": "\"Hayır, hiç görmedim\" diye yalan söyle",            "sonuc": "temkinli", "itibar": 1},
            {"metin": "\"Ne büyüsü bu, tehlikeli değil mi?\" diye sor",      "sonuc": "meraklı",  "itibar": 3},
        ],
    },
    {
        "metin": (
            "Gece yarısı yasak kütüphanenin kapısının açık olduğunu fark ediyorsun.\n"
            "İçeriden bir ışık sızıyor. Selene orada — yasak bir kitap okuyor.\n"
            "\nSeni fark etti. İkisi de donup kaldınız."
        ),
        "secimler": [
            {"metin": "Düelloya davet et — bu sırrı öğrenmek istiyorsun",   "sonuc": "duello",    "itibar": 0},
            {"metin": "\"Bu sırrın sahibi ben de olabilirim\" de, işbirliği öner", "sonuc": "müttefik", "itibar": 2},
            {"metin": "Sessizce geri çekil, görmezden gel",                 "sonuc": "kaçış",     "itibar": -1},
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


# ─── Yardımcı fonksiyonlar ───────────────

def baslik(metin: str) -> None:
    print("\n" + "═" * 50)
    print(f"  {metin}")
    print("═" * 50)

def ayrac() -> None:
    print("─" * 50)

def durakla(sn: float = 0.8) -> None:
    time.sleep(sn)

def secim_al(min_val: int, max_val: int) -> int:
    while True:
        try:
            val = int(input(f"  Seçiminiz [{min_val}-{max_val}]: "))
            if min_val <= val <= max_val:
                return val
            print(f"  Lütfen {min_val} ile {max_val} arasında bir sayı gir.")
        except ValueError:
            print("  Geçersiz giriş, tekrar dene.")


# ─── Karakter oluşturma ──────────────────

def karakter_olustur() -> dict:
    baslik("VESPER ACADEMY — Kayıt")
    print("\n  Yüzyıllık Vesper Akademisi seni bekliyor.")
    print("  Sihrin, seçimlerinin ve cesaretinin hikayesi başlıyor...\n")

    isim = input("  Karakterinin adı: ").strip()
    while not isim:
        isim = input("  Lütfen bir isim gir: ").strip()

    ayrac()
    print("\n  Büyü okulunu seç:\n")
    print("  1) 🔥 Ateş   — Güçlü saldırı, düşük savunma (ATK +2)")
    print("  2) 🌑 Gölge  — Hile büyüleri, ekstra HP  (+5 HP)")
    print("  3) 💧 Su     — Yüksek savunma, şifa büyüsü aktif\n")

    okul_sec = secim_al(1, 3)
    okullar = {1: "Ateş", 2: "Gölge", 3: "Su"}
    okul = okullar[okul_sec]

    hp, atk, mp = 20, 3, 10
    if okul == "Ateş":
        atk = 5
        hp  = 18
    elif okul == "Gölge":
        hp  = 25
        atk = 4
    elif okul == "Su":
        hp  = 22
        mp  = 14

    karakter = {
        "isim":   isim,
        "okul":   okul,
        "hp":     hp,
        "max_hp": hp,
        "mp":     mp,
        "atk":    atk,
        "itibar": 0,
    }

    print(f"\n  ✨ Hoş geldin, {isim}! Okul: {okul}")
    print(f"     HP: {hp}  |  Güç: {atk}  |  Büyü Puanı: {mp}")
    durakla()
    return karakter


# ─── Düello sistemi ──────────────────────

def duello(karakter: dict) -> bool:
    """
    Oyuncu ile Selene arasındaki büyü düellosu.
    Kazanırsa True, kaybederse False döner.
    """
    baslik("⚔  DÜELLO — Selene ile Yüzleşme")

    dusman_hp     = 18
    dusman_max_hp = 18
    oyuncu_hp     = karakter["hp"]
    buyular       = BUYULAR[karakter["okul"]]

    EYLEMLER = [
        {"isim": buyular[0], "hasar": (6, 9), "isabet": 0.70, "aciklama": "Güçlü saldırı, %70 isabet"},
        {"isim": buyular[1], "hasar": (3, 5), "isabet": 0.90, "aciklama": "Orta saldırı,  %90 isabet"},
        {"isim": buyular[2], "hasar": (1, 3), "isabet": 1.00, "aciklama": "Hafif saldırı, %100 isabet"},
    ]
    if karakter["okul"] == "Su":
        EYLEMLER.append({
            "isim": "Şifa Büyüsü", "hasar": (0, 0),
            "isabet": 1.00, "aciklama": "5 HP kazan (Su okulu özel)",
            "sifa": True,
        })

    tur = 0
    while oyuncu_hp > 0 and dusman_hp > 0:
        tur += 1
        ayrac()
        print(f"\n  TUR {tur}")
        print(f"  {karakter['isim']:20s}  HP: {oyuncu_hp}/{karakter['max_hp']}")
        print(f"  {'Selene':20s}  HP: {dusman_hp}/{dusman_max_hp}\n")

        for i, e in enumerate(EYLEMLER, 1):
            print(f"  {i}) {e['isim']:20s} — {e['aciklama']}")
        print()

        sec = secim_al(1, len(EYLEMLER))
        eylem = EYLEMLER[sec - 1]
        durakla()

        # Oyuncu hamlesi
        if eylem.get("sifa"):
            iyilesen = min(5, karakter["max_hp"] - oyuncu_hp)
            oyuncu_hp += iyilesen
            print(f"\n  💧 Şifa büyüsü kullandın! +{iyilesen} HP → {oyuncu_hp} HP")
        else:
            if random.random() < eylem["isabet"]:
                hasar = random.randint(*eylem["hasar"])
                dusman_hp = max(0, dusman_hp - hasar)
                print(f"\n  ✨ {eylem['isim']} isabet etti! Selene {hasar} hasar aldı.")
            else:
                print(f"\n  💨 {eylem['isim']} ıskaladı!")

        if dusman_hp <= 0:
            break

        # Düşman hamlesi
        dusman_hasar = random.randint(2, 4)
        oyuncu_hp = max(0, oyuncu_hp - dusman_hasar)
        print(f"  🌑 Selene karşı saldırdı! {dusman_hasar} hasar aldın → {oyuncu_hp} HP")
        durakla()

    ayrac()
    if dusman_hp <= 0:
        print("\n  🏆 Selene yenildi! Akademideki itibarın arttı.")
        karakter["hp"]     = oyuncu_hp
        karakter["itibar"] += 3
        return True
    else:
        print("\n  💀 Yenildin... Ama bu seferin bitti, savaş bitmedi.")
        karakter["hp"] = 1
        return False


# ─── Hikaye bölümleri ────────────────────

def bolum_oyna(karakter: dict, idx: int) -> None:
    bolum = HIKAYE[idx]
    baslik(f"BÖLÜM {idx + 1}")
    print()
    print(bolum["metin"])
    print()
    ayrac()

    for i, s in enumerate(bolum["secimler"], 1):
        print(f"  {i}) {s['metin']}")
    print()

    sec = secim_al(1, len(bolum["secimler"])) - 1
    secim = bolum["secimler"][sec]
    karakter["itibar"] += secim["itibar"]

    durakla()

    if secim["sonuc"] == "duello":
        duello(karakter)
    else:
        print(f"\n  → {SONUC_MESAJLARI[secim['sonuc']]}")
        print(f"  İtibar: {karakter['itibar']} puan")

    durakla(1.2)


# ─── Bitiş ekranı ────────────────────────

def bitis_ekrani(karakter: dict) -> None:
    baslik("YILIN SONU — Vesper Academy")

    itibar = karakter["itibar"]
    if itibar >= 8:
        unvan = "Akademi Efsanesi"
        mesaj = "Tüm akademi senin adını fısıldıyor. Efsane başladı."
    elif itibar >= 4:
        unvan = "Umut Vaat Eden Cadı"
        mesaj = "Öğretmenler seni yakından izliyor. Gelecek parlak görünüyor."
    else:
        unvan = "Sessiz Gözlemci"
        mesaj = "Henüz kimse seni tam olarak tanımıyor. Ama sen her şeyi görüyorsun."

    print(f"\n  🎓 {karakter['isim']} — {unvan}")
    print(f"\n  \"{mesaj}\"\n")
    print(f"  Okul   : {karakter['okul']}")
    print(f"  İtibar : {itibar} puan")
    print(f"  HP     : {karakter['hp']}/{karakter['max_hp']}")
    ayrac()
    print("\n  Vesper Academy — İlk Yıl Tamamlandı.\n")


# ─── Ana oyun döngüsü ────────────────────

def main() -> None:
    print("\n" + "═" * 50)
    print("      ✨  VESPER ACADEMY  ✨")
    print("     Büyücü Kız Akademisi RPG")
    print("═" * 50)

    while True:
        karakter = karakter_olustur()

        for i in range(len(HIKAYE)):
            bolum_oyna(karakter, i)

        bitis_ekrani(karakter)

        print("  Tekrar oynamak ister misin? (e/h): ", end="")
        cevap = input().strip().lower()
        if cevap != "e":
            print("\n  Elveda, genç cadı. Yolun açık olsun. 🌙\n")
            break


if __name__ == "__main__":
    main()
