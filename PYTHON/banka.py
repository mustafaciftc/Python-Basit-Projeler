print("""***************************Atm Uygulaması******************************

1. Kartı Yerleştirme 

2. Bakiye Sorgulama

3. Para Çekme

4. Para Yatırma

5. Fatura Ödemesi

6. Çıkış


""")

def Banka(bakiye):
    while True:
        islem = int(input("İşlem giriniz:"))
        if islem == 1:
            print("Hoşgeldiniz")
        elif islem == 2:
            print(f"Bakiyeniz {bakiye} tutarındadır")
        elif islem == 3:
            para_cekme = int(input("Çekmek istediğiniz tutarı girin:"))
            bakiye -= para_cekme
            print(f"Yeni bakiyeniz {bakiye} liradır.")
        elif islem == 4:
            para_yatirma = int(input("Yatırmak istediğiniz tutarı girin:"))
            bakiye += para_yatirma
            print(f"Yeni bakiyeniz {bakiye} liradır.")
        elif islem == 5:
            fatura_yatirma = int(input("Fatura borcunun tutarını girin:"))
            bakiye -= fatura_yatirma
            print(f"Yeni bakiyeniz {bakiye} liradır. ")
        elif islem == 6:
            print("Çıkış Yapıldı...")
            break
        else:
            print("Hatalı işlem!")

Banka(10000)






