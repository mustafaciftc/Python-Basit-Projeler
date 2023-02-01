import random
sayi = random.randint(1,50)
sayac = 0

while True:
    sayac += 1
    tahmin = int(input("Lütfen tahminde bulunun:\nÇıkış için 0'a basın:"))

    if tahmin == 0:
        print("Çıkış yapıldı")
        break
    elif tahmin < sayi:
        print("Yukarı")
        continue
    elif tahmin > sayi:
        print("Aşağı")
        continue
    elif tahmin == sayi:
        print(f"Tebrikler {str(sayac)}. seferde bildiniz.")
        break
    else:
        print("Hatalı işlem!")
