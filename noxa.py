from pyrogram import Client, filters
import asyncio
import os
import sys
import subprocess

# ==========================================
# AYARLAR (Buraya kendi bilgilerinizi girin)
# ==========================================
API_ID = 36417573  # Kendi API ID'niz
API_HASH = "0729c97fd294441920d5e242b58eaed1"

# Userbot istemcisi (plugins klasöründeki .py dosyalarını otomatik okuması için ayarlandı)
app = Client("noxa_session", api_id=API_ID, api_hash=API_HASH, plugins=dict(root="plugins"))

# --- KONSOL İÇİN HAVALI AÇILIŞ EKRANI (ASCII ART) ---
NOXA_BANNER = """\033[96m
 _   _  ___  __  __  _    
| \\ | |/ _ \\ \\ \\/ / / \\   
|  \\| | | | | >  < / _ \\  
| |\\  | |_| |/ . \\/ ___ \\ 
|_| \\_|\\___//_/ \\_\\_/   \\_\\
\033[92m
[+] Noxa Çekirdeği Başlatılıyor...
[+] Ağ Protokolleri Yükleniyor...
[+] Eklenti modülleri aktif edildi.
[+] Uzayın derinliklerine bağlantı sağlandı!
\033[0m"""

# ==========================================
# KOMUTLAR
# ==========================================

# 1. .noxa KOMUTU (Terminal animasyonlu)
@app.on_message(filters.command("noxa", prefixes=".") & filters.me)
async def noxa_alive(client, message):
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
    for frame in animation:
        await message.edit(frame)
        await asyncio.sleep(0.5)


# 2. .pinstall KOMUTU (Yükleme çubuğu animasyonlu)
@app.on_message(filters.command("pinstall", prefixes=".") & filters.me)
async def pinstall_plugin(client, message):
    if not message.reply_to_message or not message.reply_to_message.document:
        await message.edit("`[HATA] > İndirilecek modül bulunamadı. Bir .py dosyasına yanıt verin.`")
        return

    file = message.reply_to_message.document
    
    if not file.file_name.endswith(".py"):
        await message.edit("`[HATA] > Sistem reddetti: Sadece .py uzantılı dosyalar entegre edilebilir.`")
        return

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
        f"*(Değişikliklerin aktif olması için .yenile yazabilirsiniz)*"
    )
    await message.edit(success_text)


# 3. .yenile KOMUTU (Botu terminal üzerinden kapatıp açar)
@app.on_message(filters.command("yenile", prefixes=".") & filters.me)
async def restart_bot(client, message):
    await message.edit("`[+] Sistem yeniden başlatılıyor... Lütfen bekleyin.`")
    os.execl(sys.executable, sys.executable, *sys.argv)


# 4. .calistir veya .run KOMUTU (Harici python kodlarını terminalde test eder)
@app.on_message(filters.command(["calistir", "run"], prefixes=".") & filters.me)
async def run_script(client, message):
    if len(message.command) < 2:
        await message.edit("`[!] Hata: Çalıştırılacak dosyayı belirtin. (Örn: .calistir eklenti.py)`")
        return
        
    dosya_adi = message.command[1]
    await message.edit(f"`[+] {dosya_adi} işleniyor...`")
    
    try:
        islem = subprocess.run([sys.executable, dosya_adi], capture_output=True, text=True, timeout=15)
        cikti = islem.stdout if islem.stdout else islem.stderr
        
        if not cikti:
            cikti = "İşlem başarılı, ancak terminale yansıyan bir çıktı yok."
            
        await message.edit(f"**[ 🚀 {dosya_adi} ÇIKTISI ]**\n```python\n{cikti}\n```")
    except FileNotFoundError:
        await message.edit(f"`[!] Hata: {dosya_adi} adında bir dosya bulunamadı.`")
    except Exception as e:
        await message.edit(f"**[ ❌ SİSTEM HATASI ]**\n```python\n{e}\n```")


# ==========================================
# ÇALIŞTIRMA MERKEZİ
# ==========================================
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(NOXA_BANNER)
    app.run()
