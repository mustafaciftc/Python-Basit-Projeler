import sqlite3

con = sqlite3.connect("Hobilerim.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS hobilerim (Hobi_1 TEXT,Hobi_2 TEXT,Hobi_3 TEXT,Hobi_4 TEXT)")

tablo_olustur()
def veri_ekle():
    cursor.execute("Insert into hobilerim Values ('Gitar çalmak','Kitap okumak','Müzik dinlemek','Yürüyüş yapmak')")
    con.commit()
def veri_ekle2(Hobi_1,Hobi_2,Hobi_3,Hobi_4):
    cursor.execute("Insert into hobilerim Values (?,?,?,?)",(Hobi_1,Hobi_2,Hobi_3,Hobi_4))
    con.commit()

Hobi_1 = input("Hobi 1:")
Hobi_2 = input("Hobi 2:")
Hobi_3 = input("Hobi 3:")
Hobi_4 = input("Hobi 4:")

veri_ekle2(Hobi_1, Hobi_2, Hobi_3, Hobi_4)
con.close()





