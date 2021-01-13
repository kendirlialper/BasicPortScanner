import threading
import socket
import os
import time
os.system("clear")

print('\n\n\t\t\t\t---Açık port bulucu---')
print('''
    Bu program mevcut websitelerde açık olan portların bulunması amacıyla kodlanmıştır.

    YASAL UYARI: BU SİSTEM TAMAMEN EĞİTİM AMAÇLI OLARAK ÜRETİLMİŞTİR, EĞİTİM HARİCİ KULLANILAMAZ!!!

    Geliştirici: Alper KENDİRLİ

                     ''')
print("\n\n")
target = input("Lütfen portları taranacak hedef websiteyi giriniz: ")
#ip = socket.gethostbyname(target)

def portscan(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)# 

    try:
        con = s.connect((target,port))

        print('Port :',port,"\t Açık")
        con.close()
    except: 
        pass
r = 1 
for x in range(1,1500): 

    t = threading.Thread(target=portscan,kwargs={'port':r}) 
    r += 1     
    t.start() 


time.sleep(3)
print("\n\n\n\n")    