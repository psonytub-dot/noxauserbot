#!/bin/bash

clear
echo -e "\e[96m"
echo " _   _  ___  __  __  _    "
echo "| \ | |/ _ \ \ \/ / / \   "
echo "|  \| | | | | >  < / _ \  "
echo "| |\  | |_| |/ . \/ ___ \ "
echo "|_| \_|\___//_/ \_\_/   \_\\"
echo -e "\e[0m"

echo -e "\e[92m[+] Noxa Core Kurulum Protokolü Başlatıldı...\e[0m"
sleep 1

echo -e "\e[93m[~] Gerekli kütüphaneler yükleniyor...\e[0m"
pip install pyrogram tgcrypto > /dev/null 2>&1

echo -e "\e[93m[~] Klasörler oluşturuluyor...\e[0m"
mkdir -p noxa_bot/plugins
cd noxa_bot

echo -e "\e[93m[~] Noxa Core dosyaları sunucudan çekiliyor...\e[0m"
# İşte anahtar kısım burası:
curl -sL "https://raw.githubusercontent.com/psonytub-dot/noxauserbot/main/noxa.py" -o noxa.py

echo -e "\e[92m[+] Kurulum Tamamlandı!\e[0m"
echo -e "\e[96m[>] Botu başlatmak için şu komutu girin:\e[0m"
echo -e "    python noxa.py\n"
