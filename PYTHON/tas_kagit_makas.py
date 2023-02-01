import random

secenekler = ["Taş","Kağıt","Makas"]

tas = secenekler[0]
kagit = secenekler[1]
makas = secenekler[2]

kullanici_skoru = 0
bilgisayar_skoru = 0
genel_skor = 0

while True:
    islem = input("Taş mı Kağıt mı Makas mı, genel Skoru görmek için 'a'ya basın:")
    bil_islem =random.choice(secenekler)
    if islem == tas:
        if bil_islem == tas:
            print("Bilgisayarın seçimi: Taş\nBerabere")
        elif bil_islem == kagit:
            print("Bilgisayarın seçimi: Kağıt\nKaybettiniz")
            bilgisayar_skoru += 10
        else:
            print("Bilgisayarın seçimi: Makas\nKazandınız")
            kullanici_skoru += 10
    elif islem == kagit:
        if bil_islem == tas:
            print("Bilgisayarın seçimi: Taş\nKazandınız")
            kullanici_skoru += 10
        elif bil_islem == kagit:
            print("Bilgisayarın seçimi: Kağıt\nBerabere")
        else:
            print("Bilgisayarın seçimi: Makas\nKaybettiniz")
            bilgisayar_skoru += 10
    elif islem == makas:
        if bil_islem == tas:
            print("Bilgisayarın seçimi: Taş\nKaybettiniz")
            bilgisayar_skoru += 10
        elif bil_islem == kagit:
            print("Bilgisayarın seçimi: Kağıt\nKazandınız")
            kullanici_skoru += 10
        else:
            print("Bilgisayarın seçimi: Makas\nBerabere")
    elif islem == "a":
        print("Kullanıcı skoru: {}\nBilgisayar skoru: {}".format(kullanici_skoru,bilgisayar_skoru))

        if kullanici_skoru < bilgisayar_skoru:
            print("Kazanan Bilgisayar")
            break
        elif kullanici_skoru == bilgisayar_skoru:
            print("Sonuç berabere")
            break
        else:
            print("Kazanan Kullanıcı")
            break
    else:
        print("Hatalı işlem!")

