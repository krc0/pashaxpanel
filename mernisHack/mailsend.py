import smtplib
from email.message import EmailMessage
import random
from colorama import init, Fore, Back
from time import sleep


def send_email(sender, password, recipient, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From']= sender
    msg['To']= recipient
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender, password) 
        server.send_message(msg)  # encoding parametresini ekledik
        print(f"{Fore.GREEN}E-posta başarıyla gönderildi ✓{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}(-) E-posta gönderilirken bir hata oluştu: {Fore.RESET}", str(e))
    finally:
        server.quit()


print("""
    1. Anahtar al
    2. Anahtar ile Giriş yap
""")


tercih = input("--# ")

if tercih != "1" and tercih != "2":
    print(f"{Fore.RED}(-) Komut bulunamadı!{Fore.RESET}")

keys = ["2023", "2006", "pashaTR", "tht", "akp>chp", "fatihbey", "$dolmaz", "3729za", "gonya", "yorgunum", "uluhakan", "yılanxadam", "dodohando", "fatihxkraldır", "pashaxpanel", "hackerx", "amigdala", "zihinxsarayı"]
def login():
    """Kullanıcının şifreyle giriş yapmasını sağlar."""
    key = input("Anahtar: ")
    if key in keys:
        import baslat
    else:
        print(f"{Fore.RED}(-) Geçersiz işlem yapıldı!{Fore.RESET}")
        print()
        login()


if tercih == "1":
    alici_eposta_adresi = input(f"{Fore.MAGENTA}E-posta adresi (Sadece sana özel Anahtar oluşturacağız): {Fore.RESET}")
    sender_email = 'fatihkoruc36@gmail.com'
    sender_password = 'eixugyqoudlqswyr'
    recipient_email = alici_eposta_adresi
    email_subject = 'Pasha㉿Panel'
    email_body = f'Kralda biziz Kuralda? 👑 \n Sadece sana özel Anahtar almak için bu siteye giderek https://krc0.github.io/pashacom/ Anahtar alabilirsin'



    send_email(sender_email, sender_password, recipient_email, email_subject, email_body)
    dogrulama_kodu_gir = input("Anahtar: ")

elif tercih == "2":
    login()

else:
    print(f"{Fore.RED}(-) Komut bulunamadı!")
