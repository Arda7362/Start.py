
#!/data/data/com.termux/files/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import webbrowser

# Renk kodları
class Renk:
    YESIL = '\033[92m'
    KIRMIZI = '\033[91m'
    MAVI = '\033[94m'
    SARI = '\033[93m'
    MOR = '\033[95m'
    CYAN = '\033[96m'
    BEYAZ = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def temizle():
    os.system('clear')

def banner():
    print(f"""
{Renk.KIRMIZI}{Renk.BOLD}╔══════════════════════════════════════════════════════════╗
{Renk.SARI}{Renk.BOLD}║              NOVA TOOLS - SIRALI MENÜ v8.0               ║
{Renk.YESIL}{Renk.BOLD}║              30+ GÜNCEL VE ÇALIŞAN ARAÇ                  ║
{Renk.MAVI}{Renk.BOLD}╚══════════════════════════════════════════════════════════╝{Renk.RESET}
    """)

def menu():
    print(f"""
{Renk.CYAN}{Renk.BOLD}==================== KAMERA & ANDROİD ===================={Renk.RESET}
{Renk.MOR}[01]{Renk.YESIL} 📸 Camera Hack - CAM-DUMPER
{Renk.MOR}[02]{Renk.YESIL} 🤖 Android RAT - AhMyth
{Renk.MOR}[03]{Renk.YESIL} 📱 Android Payload - Paybag

{Renk.CYAN}{Renk.BOLD}==================== MESAJLAŞMA UYGULAMALARI ===================={Renk.RESET}
{Renk.MOR}[04]{Renk.YESIL} 💬 WhatsApp Bot - LumaBot
{Renk.MOR}[05]{Renk.YESIL} ✈️ Telegram Bot - python-telegram-bot
{Renk.MOR}[06]{Renk.YESIL} 💬 Discord Spam Bot - discord-mass-dm-tool
{Renk.MOR}[07]{Renk.YESIL} 🐦 Twitter API - node-twitter-api-v2

{Renk.CYAN}{Renk.BOLD}==================== SOSYAL MEDYA ARAÇLARI ===================={Renk.RESET}
{Renk.MOR}[08]{Renk.YESIL} 🔍 Instagram OSINT - OSINT-INSTAGRAM
{Renk.MOR}[09]{Renk.YESIL} 🔄 Instagram Bot - InstaBot
{Renk.MOR}[10]{Renk.YESIL} 🎵 TikTok Video İndirici - yt-dlp

{Renk.CYAN}{Renk.BOLD}==================== OYUN HİLELERİ ===================={Renk.RESET}
{Renk.MOR}[11]{Renk.YESIL} 🗺️ PUBG API - api-assets
{Renk.MOR}[12]{Renk.YESIL} 🎮 Oyun Hileleri - GameGuardian

{Renk.CYAN}{Renk.BOLD}==================== AĞ & GÜVENLİK ===================={Renk.RESET}
{Renk.MOR}[13]{Renk.YESIL} 🌊 DDoS Aracı - xaledoser
{Renk.MOR}[14]{Renk.YESIL} 🌐 IP Sorgulama - ip-api
{Renk.MOR}[15]{Renk.YESIL} 📶 WiFi Test - Wifite2
{Renk.MOR}[16]{Renk.YESIL} 🔍 Port Tarama - Nmap
{Renk.MOR}[17]{Renk.YESIL} 📡 Bluetooth Tarama - btlescan
{Renk.MOR}[18]{Renk.YESIL} 📶 Ağ Analiz - Wireshark

{Renk.CYAN}{Renk.BOLD}==================== OSINT & ARAŞTIRMA ===================={Renk.RESET}
{Renk.MOR}[19]{Renk.YESIL} 🕵️ OSINT Aracı - Sherlock
{Renk.MOR}[20]{Renk.YESIL} 📍 Konum Takip - Seeker
{Renk.MOR}[21]{Renk.YESIL} 📊 Sosyal Medya Analiz - Social Analyzer

{Renk.CYAN}{Renk.BOLD}==================== BOMBER ARAÇLARI ===================={Renk.RESET}
{Renk.MOR}[22]{Renk.YESIL} 📧 Mail Bomber - Email-Bomber (Go)
{Renk.MOR}[23]{Renk.YESIL} 💬 SMS Bomber - Enough-Reborn

{Renk.CYAN}{Renk.BOLD}==================== ŞİFRE & METADATA ===================={Renk.RESET}
{Renk.MOR}[24]{Renk.YESIL} 🔐 Şifre Oluşturucu - password-generator
{Renk.MOR}[25]{Renk.YESIL} 🔐 Şifre Kırma - John The Ripper
{Renk.MOR}[26]{Renk.YESIL} 📁 Metadata Temizleme - metadata-cleaner

{Renk.CYAN}{Renk.BOLD}==================== PROXY & PENTEST ===================={Renk.RESET}
{Renk.MOR}[27]{Renk.YESIL} 🌐 Proxy Bulucu - Proxy-Finder
{Renk.MOR}[28]{Renk.YESIL} 🛡️ Pentest Framework - PTF
{Renk.MOR}[29]{Renk.YESIL} 🎣 Phishing Aracı - Zphisher
{Renk.MOR}[30]{Renk.YESIL} 🎤 Ses Kayıt - sox

{Renk.KIRMIZI}[00]{Renk.KIRMIZI} 🚪 Çıkış{Renk.RESET}
    """)

def git_clone(url, folder=None):
    if not folder:
        folder = url.split('/')[-1].replace('.git', '')
    if os.path.exists(folder):
        os.system(f"cd {folder} && git pull")
    else:
        os.system(f"git clone {url}")

def link_ac(url):
    webbrowser.open(url)

# ========== KAMERA & ANDROİD ==========

def camera_hack():
    temizle()
    banner()
    print(f"{Renk.YESIL}[01] CAM-DUMPER Kuruluyor...{Renk.RESET}")
    os.system("pkg install -y git php wget curl jq")
    git_clone("https://github.com/LiNuX-Mallu/CAM-DUMPER.git")
    print(f"\n{Renk.YESIL}Kullanım:{Renk.RESET}")
    print("cd CAM-DUMPER")
    print("chmod +x camdumper.sh")
    print("./camdumper.sh")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def android_rat():
    temizle()
    banner()
    print(f"{Renk.YESIL}[02] AhMyth Android RAT{Renk.RESET}")
    link_ac("https://github.com/AhMyth/AhMyth-Android-RAT/releases")
    print(f"\n{Renk.YESIL}Yapılacaklar:{Renk.RESET}")
    print("1. Linkten AhMyth'i indir")
    print("2. Bilgisayarına kur")
    print("3. Kullanmaya başla")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def paybag_payload():
    temizle()
    banner()
    print(f"{Renk.YESIL}[03] Paybag Payload Oluşturucu{Renk.RESET}")
    os.system("pkg install -y python")
    git_clone("https://github.com/Deadpool2000/Paybag.git")
    print(f"\n{Renk.YESIL}Kurulum:{Renk.RESET}")
    print("cd Paybag")
    print("pip install -r requirements.txt")
    print("python paybag.py")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

# ========== MESAJLAŞMA ==========

def whatsapp_bot():
    temizle()
    banner()
    print(f"{Renk.YESIL}[04] LumaBot Kuruluyor...{Renk.RESET}")
    os.system("pkg install -y nodejs")
    git_clone("https://github.com/murillous/LumaBot.git")
    print(f"\n{Renk.YESIL}Kurulum:{Renk.RESET}")
    print("cd LumaBot")
    print("npm install")
    print("\nÇalıştırma:")
    print("npm start        # Production")
    print("npm run dev      # Development")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def telegram_bot():
    temizle()
    banner()
    print(f"{Renk.YESIL}[05] python-telegram-bot Kuruluyor...{Renk.RESET}")
    os.system("pkg install -y python")
    git_clone("https://github.com/python-telegram-bot/python-telegram-bot.git")
    print(f"\n{Renk.YESIL}Kurulum:{Renk.RESET}")
    print("cd python-telegram-bot")
    print("pip install build")
    print("python -m build")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def discord_spam_bot():
    temizle()
    banner()
    print(f"{Renk.YESIL}[06] Discord Mass DM Tool Kuruluyor...{Renk.RESET}")
    os.system("pkg install -y nodejs")
    git_clone("https://github.com/tahagorme/discord-mass-dm-tool.git")
    print(f"\n{Renk.YESIL}Kurulum:{Renk.RESET}")
    print("cd discord-mass-dm-tool")
    print("npm install")
    print("node dm.js")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def twitter_api():
    temizle()
    banner()
    print(f"{Renk.YESIL}[07] node-twitter-api-v2{Renk.RESET}")
    os.system("pkg install -y nodejs")
    git_clone("https://github.com/plhery/node-twitter-api-v2.git")
    print(f"\n{Renk.YESIL}Node.js Twitter API v2 kütüphanesi kuruldu{Renk.RESET}")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

# ========== SOSYAL MEDYA ==========

def instagram_osint():
    temizle()
    banner()
    print(f"{Renk.YESIL}[08] OSINT-INSTAGRAM Kuruluyor...{Renk.RESET}")
    os.system("pkg install -y python")
    git_clone("https://github.com/isdteam/OSINT-INSTAGRAM.git")
    os.system("cd OSINT-INSTAGRAM && pip install -r requirements.txt")
    print(f"\n{Renk.YESIL}Kullanım:{Renk.RESET}")
    print("cd OSINT-INSTAGRAM")
    print("python main.py --username KULLANICI_ADI")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def instabot():
    temizle()
    banner()
    print(f"{Renk.YESIL}[09] InstaBot Kuruluyor...{Renk.RESET}")
    os.system("pkg install -y python")
    git_clone("https://github.com/rohanarun/instabot.git")
    os.system("cd instabot && python setup.py install")
    print(f"\n{Renk.YESIL}InstaBot kuruldu!{Renk.RESET}")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def tiktok_indir():
    temizle()
    banner()
    print(f"{Renk.YESIL}[10] yt-dlp Kuruluyor...{Renk.RESET}")
    os.system("pkg install -y python ffmpeg")
    os.system("pip install yt-dlp")
    print(f"\n{Renk.YESIL}Kullanım:{Renk.RESET}")
    print("yt-dlp TIKTOK_VIDEO_URL")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

# ========== OYUN ==========

def pubg_api():
    temizle()
    banner()
    print(f"{Renk.YESIL}[11] PUBG API Assets{Renk.RESET}")
    git_clone("https://github.com/pubg/api-assets.git")
    print(f"\n{Renk.YESIL}PUBG API assets dosyaları indirildi{Renk.RESET}")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def oyun_hile():
    temizle()
    banner()
    print(f"{Renk.YESIL}[12] GameGuardian{Renk.RESET}")
    link_ac("https://gameguardian.net/forum/files/file/2-gameguardian/")
    print(f"\n{Renk.YESIL}Her Oyunda Hile Yapma Uygulaması{Renk.RESET}")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

# ========== AĞ & GÜVENLİK ==========

def ddos_xaledoser():
    temizle()
    banner()
    print(f"{Renk.YESIL}[13] xaledoser DDoS Aracı{Renk.RESET}")
    print(f"{Renk.CYAN}Açıklama:{Renk.RESET} DDoS saldırıları, bir hostun hizmetlerini geçici olarak aksatır.")
    os.system("pkg install -y python")
    git_clone("https://github.com/thexale/xaledoser.git")
    print(f"\n{Renk.YESIL}Kullanım:{Renk.RESET}")
    print("cd xaledoser")
    print("chmod +x xdoser.py")
    print("./xdoser.py -s HEDEF_IP")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def ip_sorgu():
    temizle()
    banner()
    print(f"{Renk.YESIL}[14] IP Sorgulama Aracı{Renk.RESET}")
    os.system("pkg install -y curl jq")

    with open("ip_sorgula.sh", "w") as f:
        f.write("""#!/bin/bash
read -p "IP adresi: " ip
curl -s "http://ip-api.com/json/$ip?fields=country,regionName,city,isp,org,lat,lon" | jq '.'
""")
    os.system("chmod +x ip_sorgula.sh")
    print(f"\n{Renk.YESIL}Kullanım: ./ip_sorgula.sh{Renk.RESET}")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def wifite2():
    temizle()
    banner()
    print(f"{Renk.YESIL}[15] Wifite2 Kuruluyor...{Renk.RESET}")
    os.system("pkg install -y python aircrack-ng")
    git_clone("https://github.com/derv82/wifite2")
    print(f"\n{Renk.YESIL}Kullanım: cd wifite2 && python wifite.py{Renk.RESET}")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def nmap_kur():
    temizle()
    banner()
    print(f"{Renk.YESIL}[16] Nmap Kuruluyor...{Renk.RESET}")
    os.system("pkg install -y nmap")
    print(f"\n{Renk.YESIL}Kullanım: nmap -sV HEDEF.COM{Renk.RESET}")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def bluetooth_scan():
    temizle()
    banner()
    print(f"{Renk.YESIL}[17] btlescan Kuruluyor...{Renk.RESET}")
    os.system("pkg install -y git bluez")
    os.system("git clone https://github.com/ztroop/btlescan.git")
    print(f"\n{Renk.YESIL}Kullanım: cd btlescan && ./btlescan{Renk.RESET}")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def wireshark_kur():
    temizle()
    banner()
    print(f"{Renk.YESIL}[18] Wireshark Kurulumu{Renk.RESET}")
    print(f"""
{Renk.YESIL}Ubuntu/Debian:{Renk.RESET}
sudo add-apt-repository ppa:wireshark-dev/stable
sudo apt-get update
sudo apt-get install wireshark

{Renk.YESIL}Termux:{Renk.RESET}
pkg install wireshark
    """)
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

# ========== OSINT ==========

def sherlock():
    temizle()
    banner()
    print(f"{Renk.YESIL}[19] Sherlock Kuruluyor...{Renk.RESET}")
    os.system("pkg install -y python")
    git_clone("https://github.com/sherlock-project/sherlock.git")
    os.system("cd sherlock && pip install -r requirements.txt")
    print(f"\n{Renk.YESIL}Kullanım: cd sherlock && python sherlock KULLANICI{Renk.RESET}")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def seeker():
    temizle()
    banner()
    print(f"{Renk.YESIL}[20] Seeker Kuruluyor...{Renk.RESET}")
    os.system("pkg install -y git php wget curl")
    git_clone("https://github.com/thewhiteh4t/seeker")
    print(f"\n{Renk.YESIL}Kurulum: cd seeker && chmod +x install.sh && ./install.sh{Renk.RESET}")
    print(f"Çalıştır: ./seeker.py{Renk.RESET}")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def social_analyzer():
    temizle()
    banner()
    print(f"{Renk.YESIL}[21] Social Analyzer Kuruluyor...{Renk.RESET}")
    os.system("pkg install -y nodejs")
    git_clone("https://github.com/qeeqbox/social-analyzer")
    print(f"\n{Renk.YESIL}Kurulum: cd social-analyzer && npm install{Renk.RESET}")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

# ========== BOMBER ==========

def email_bomber():
    temizle()
    banner()
    print(f"{Renk.YESIL}[22] Email-Bomber Kuruluyor (Go)...{Renk.RESET}")
    os.system("pkg install -y golang")
    git_clone("https://github.com/esfelorm/Email-Bomber.git")
    print(f"\n{Renk.YESIL}Kullanım:{Renk.RESET}")
    print("cd Email-Bomber")
    print("go run bomb.go")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def sms_bomber():
    temizle()
    banner()
    print(f"{Renk.YESIL}[23] Enough-Reborn SMS Bomber Kuruluyor...{Renk.RESET}")
    os.system("pkg install -y python")
    git_clone("https://github.com/tingirifistik/Enough-Reborn.git")
    os.system("cd Enough-Reborn && pip install -r requirements.txt")
    print(f"\n{Renk.YESIL}Kullanım: cd Enough-Reborn && python enough.py{Renk.RESET}")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

# ========== ŞİFRE & METADATA ==========

def sifre_olustur():
    temizle()
    banner()
    print(f"{Renk.YESIL}[24] password-generator Kuruluyor...{Renk.RESET}")
    os.system("pkg install -y nodejs")
    git_clone("https://github.com/sebastienrousseau/password-generator.git")
    print(f"\n{Renk.YESIL}Kurulum:{Renk.RESET}")
    print("cd password-generator")
    print("npm install")
    print("npm run build")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def john_ripper():
    temizle()
    banner()
    print(f"{Renk.YESIL}[25] John The Ripper{Renk.RESET}")
    git_clone("https://github.com/openwall/john.git")
    print(f"\n{Renk.YESIL}Derleme:{Renk.RESET}")
    print("cd john/src")
    print("./configure && make")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def metadata_cleaner():
    temizle()
    banner()
    print(f"{Renk.YESIL}[26] metadata-cleaner Kuruluyor...{Renk.RESET}")
    os.system("pkg install -y python")
    git_clone("https://github.com/sandy-sp/metadata-cleaner.git")
    print(f"\n{Renk.YESIL}Kurulum:{Renk.RESET}")
    print("cd metadata-cleaner")
    print("pip install poetry")
    print("poetry install")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

# ========== PROXY & PENTEST ==========

def proxy_bul():
    temizle()
    banner()
    print(f"{Renk.YESIL}[27] Proxy-Finder Kuruluyor...{Renk.RESET}")
    git_clone("https://github.com/SonzaiEkkusu/Proxy-Finder.git")
    print(f"\n{Renk.YESIL}Proxy bulucu kuruldu{Renk.RESET}")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def pentest():
    temizle()
    banner()
    print(f"{Renk.YESIL}[28] Pentest Framework{Renk.RESET}")
    git_clone("https://github.com/trustedsec/ptf")
    print(f"\n{Renk.YESIL}Kullanım: cd ptf && ./ptf{Renk.RESET}")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def zphisher():
    temizle()
    banner()
    print(f"{Renk.YESIL}[29] Zphisher Kuruluyor...{Renk.RESET}")
    os.system("pkg install -y git php wget curl")
    git_clone("https://github.com/htr-tech/zphisher")
    print(f"\n{Renk.YESIL}Kullanım: cd zphisher && bash zphisher.sh{Renk.RESET}")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def ses_kayit():
    temizle()
    banner()
    print(f"{Renk.YESIL}[30] Ses Kayıt Aracı (sox){Renk.RESET}")
    os.system("pkg install -y sox")
    print(f"\n{Renk.YESIL}Kayıt: sox -d kayit.wav{Renk.RESET}")
    print(f"Oynat: play kayit.wav{Renk.RESET}")
    input(f"\n{Renk.SARI}Devam için ENTER...{Renk.RESET}")

def main():
    while True:
        temizle()
        banner()
        menu()

        secim = input(f"{Renk.SARI}Seçiminiz (00-30): {Renk.RESET}")

        if secim == "00" or secim == "0":
            print(f"{Renk.YESIL}NOVA TOOLS'dan çıkılıyor... Görüşmek üzere!{Renk.RESET}")
            break
        elif secim == "01": camera_hack()
        elif secim == "02": android_rat()
        elif secim == "03": paybag_payload()
        elif secim == "04": whatsapp_bot()
        elif secim == "05": telegram_bot()
        elif secim == "06": discord_spam_bot()
        elif secim == "07": twitter_api()
        elif secim == "08": instagram_osint()
        elif secim == "09": instabot()
        elif secim == "10": tiktok_indir()
        elif secim == "11": pubg_api()
        elif secim == "12": oyun_hile()
        elif secim == "13": ddos_xaledoser()
        elif secim == "14": ip_sorgu()
        elif secim == "15": wifite2()
        elif secim == "16": nmap_kur()
        elif secim == "17": bluetooth_scan()
        elif secim == "18": wireshark_kur()
        elif secim == "19": sherlock()
        elif secim == "20": seeker()
        elif secim == "21": social_analyzer()
        elif secim == "22": email_bomber()
        elif secim == "23": sms_bomber()
        elif secim == "24": sifre_olustur()
        elif secim == "25": john_ripper()
        elif secim == "26": metadata_cleaner()
        elif secim == "27": proxy_bul()
        elif secim == "28": pentest()
        elif secim == "29": zphisher()
        elif secim == "30": ses_kayit()
        else:
            print(f"{Renk.KIRMIZI}Geçersiz seçim! Lütfen 00-30 arası bir sayı girin.{Renk.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
