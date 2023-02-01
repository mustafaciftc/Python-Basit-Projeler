import sqlite3

con = sqlite3.connect("Bilgilerim.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS bilgilerim (İsim TEXT,Soyisim TEXT,Yaşadığı_şehir TEXT,E_posta TEXT)")

tablo_olustur()
def deger_ekle(isim,soyisim,yasadigi_sehir,e_posta):
    cursor.execute("INSERT INTO bilgilerim VALUES (?,?,?,?)",(isim,soyisim,yasadigi_sehir,e_posta))
    con.commit()
isim = input("İsim:")
soyisim = input("Soyisim:")
yasadigi_sehir = input("Yaşadığı şehir:")
e_posta = input("E posta:")

deger_ekle(isim, soyisim, yasadigi_sehir, e_posta)
con.close()


