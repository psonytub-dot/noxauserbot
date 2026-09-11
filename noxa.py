from pyrogram import Client, filters
import asyncio
import os

# Buraya kendi my.telegram.org bilgilerinizi girin
API_ID = 36417573  # Kendi API ID'niz
API_HASH = "0729c97fd294441920d5e242b58eaed1"

app = Client("noxa_session", api_id=API_ID, api_hash=API_HASH)

# --- KONSOL İÇİN HAVALI AÇILIŞ EKRANI (ASCII ART) ---
# \033[96m : Neon Mavi | \033[92m : Yeşil | \033[0m : Rengi Sıfırla
NOXA_BANNER = """\033[96m
 _   _  ___  __  __  _    
| \\ | |/ _ \\ \\ \\/ / / \\   
|  \\| | | | | >  < / _ \\  
| |\\  | |_| |/ . \\/ ___ \\ 
|_| \\_|\\___//_/ \\_\\_/   \\_\\
\033[92m
[+] Noxa Çekirdeği Başlatılıyor...
[+] Ağ Protokolleri Yükleniyor...
[+] Uzayın derinliklerine bağlantı sağlandı!
\033[0m"""

# .noxa komutu (Terminal animasyonlu)
@app.on_message(filters.command("noxa", prefixes=".") & filters.me)
async def noxa_alive(client, message):
    # Terminal efekti için mesajı adım adım düzenliyoruz
    animation = [
        "`root@noxa:~#` `_`",
        "`root@noxa:~#` `ping space_station`",
        "`root@noxa:~#` `ping space_station`\n`[!] Uzay boşluğunda sinyal aranıyor...`",
        "`root@noxa:~#` `ping space_station`\n`[+] Sinyal yakalandı! Bağlantı şifreleniyor...`",
        "**[ 🛰 NOXA CORE SİSTEMİ ]**\n\n"
        "`>_ Durum     :` `AKTİF`\n"
        "`>_ Lokasyon  :` `Uzayın Derinlikleri 🌌`\n"
        "`>_ Sürüm     :` `v1.0.0-beta`\n"
        "`>_ Modüller  :` `Çevrimiçi`\n"
    ]
    
    # Animasyon karelerini 0.5 saniye arayla telegramda oynat
    for frame in animation:
        await message.edit(frame)
        await asyncio.sleep(0.5)

# .pinstall komutu (Yükleme çubuğu animasyonlu)
@app.on_message(filters.command("pinstall", prefixes=".") & filters.me)
async def pinstall_plugin(client, message):
    if not message.reply_to_message or not message.reply_to_message.document:
        await message.edit("`[HATA] > İndirilecek modül bulunamadı. Bir .py dosyasına yanıt verin.`")
        return

    file = message.reply_to_message.document
    
    if not file.file_name.endswith(".py"):
        await message.edit("`[HATA] > Sistem reddetti: Sadece .py uzantılı dosyalar entegre edilebilir.`")
        return

    # İndirme animasyonu
    await message.edit("`[+] Sunucudan paket çekiliyor... [■□□□□□]`")
    await asyncio.sleep(0.4)
    await message.edit("`[+] Veri blokları işleniyor...   [■■■□□□]`")
    
    os.makedirs("plugins", exist_ok=True)
    file_path = f"plugins/{file.file_name}"
    await message.reply_to_message.download(file_path)
    
    await message.edit("`[+] Sistem klasörüne yazılıyor...[■■■■■□]`")
    await asyncio.sleep(0.4)
    
    success_text = (
        f"**[ 📥 ENTEGRASYON TAMAMLANDI ]**\n\n"
        f"`>_ Dosya :` `{file.file_name}`\n"
        f"`>_ Dizin :` `/plugins/`\n"
        f"`>_ Durum :` `Sisteme Başarıyla Gömüldü.`\n\n"
        f"*(Değişikliklerin aktif olması için modülü yeniden başlatın)*"
    )
    await message.edit(success_text)

if __name__ == "__main__":
    # Bot açılırken terminali temizle (Windows için cls, Linux/Mac için clear)
    os.system('cls' if os.name == 'nt' else 'clear')
    # Havalı logomuzu ekrana bas
    print(NOXA_BANNER)
    # Botu çalıştır
    app.run()
