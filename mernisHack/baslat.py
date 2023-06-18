import mailsend
from time import sleep
import smtplib
import os
import json
import random
from colorama import init, Fore, Back, Style
import threading
import string
import keyboard
import datetime
import requests
from email.mime.text import MIMEText

init()




print()
print()
print(f"İnstagram: {Fore.YELLOW} 👑  @ll.fatihbey 👑{Fore.RESET}")
sleep(1)
print()
print(f"{Fore.YELLOW}👑 Kralda Biziz Kuralda? 😏{Fore.RESET}")
sleep(0.1)
print(f"""{Fore.YELLOW}
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆
⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁{Fore.RESET}""")
sleep(0.2)
print()
print(f"Sorgu yapmak için {Fore.MAGENTA}Ad, Soyad, İl{Fore.RESET} {Fore.YELLOW}Büyük{Fore.RESET} harf olacak şekilde yazınız.")
print()
sleep(0.3)



while True:

    # API endpoint adresi
    api_url = "https://648393c2f2e76ae1b95cabf2.mockapi.io/Kullanicilar"

    # GET isteği göndermek
    response = requests.get(api_url)

    ad_gir = input(f"{Fore.MAGENTA + Style.BRIGHT}──[pasha㉿panel]──(AD)─# {Fore.RESET}{Fore.GREEN}")
    print()
    soyad_gir = input(f"{Fore.MAGENTA + Style.BRIGHT}──[pasha㉿panel]──(SOYAD)─# {Fore.RESET}{Fore.GREEN}")
    print()
    il_gir = input(f"{Fore.MAGENTA + Style.BRIGHT}──[pasha㉿panel]──(İL)─# {Fore.RESET}{Fore.GREEN}")
    print()
    print(Fore.RESET)

    # İstek yanıtını kontrol etmek
    if response.status_code == 200:
        # Yanıt verisi JSON formatındaysa
        data = response.json()
        is_match_found = False
        # Veriyi kullanma veya işleme devam etme
        for item in data:
            ad_api = item.get("ad")
            soyad_api = item.get("soyad")
            il_api = item.get("il")

            if ad_gir == ad_api and soyad_gir == soyad_api and il_gir == il_api:
                for key, value in item.items():
                    print(f"{Fore.WHITE}{Back.BLUE}{key}:{Back.RESET}{Fore.RESET}{Fore.CYAN} {value}{Fore.RESET}")
                print("--------------------") 
                print()
                print()
                is_match_found = True

            elif (ad_gir == "FATİH" or ad_gir == "RAVZA" or ad_gir == "ELİFE" or ad_gir == "MUHAMMET" or ad_gir == "MİHRİCAN") and soyad_gir == "KORUCU" and il_gir == "KONYA":
                print()
                print(f"{Fore.RED}(-) Geçersiz işlem! {Fore.YELLOW}👑 Fatih Korucu Hazretlerinin 👑{Fore.RESET}  ve 👑 {Fore.YELLOW}Fatih Oğulları Hanedanının{Fore.RESET} 👑 {Fore.RED} Bilgilerini Görüntülemeye Cürret etmek = KALICI BAN{Fore.RESET}")
                print()
                is_match_found = True
                break

            elif ad_gir == "HASAN NAİL" and soyad_gir == "CANBOY" and il_gir == "KONYA":
                print(f"{Fore.RED}(-) Geçersiz işlem!{Fore.RESET}{Fore.YELLOW}👑 Fatih Korucu Hazretlerinin 👑{Fore.RESET} Dostu {Fore.YELLOW}✨ Hasan Nail Canboy Hazretlerinin ✨{Fore.RESET} {Fore.RED} Bilgilerini Görüntülemeye Cürret etmek = KALICI BAN{Fore.RESET}")
                is_match_found = True
                break

        if not is_match_found:
            api_url_gelen_veri = "https://648393c2f2e76ae1b95cabf2.mockapi.io/gelen_veri"
            datam = {'Ad': ad_gir, 'Soyad': soyad_gir, 'İl': il_gir}
            response = requests.post(api_url_gelen_veri, data=datam)
            json_response = response.json()
        
        import baslat

        
    else:
        print("API isteği başarısız. Hata kodu:", response.status_code)
