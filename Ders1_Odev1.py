#Python da veri tiplerini aşağıdaki şekilde sıralayabiliriz.

#String yani Metin Veri Tipleri → str

#Numerik yani Sayısal Veri Tipleri → int, float, complex

#Sequence (sıralama) Veri Tipleri -> list, tuple, range

#Mapping (haritalama) Veri Tipleri -> dict

#Set Veri Tipleri -> set, frozenset

#Boolean Veri Tipleri -> bool

#Binary Veri Tipleri -> bytes, bytearray, memoryview

#---------------------------------------------------------------------------

#Eğitim Başlığı  -> string 
#Eğitmeniniz -> string 
#Eğitim Tamamlanma Durumu -> int 

#---------------------------------------------------------------------------



dersler = ["Ders 1", "Ders 2", "Ders 3"]
sorgu = input("Dersi giriniz :")
kayitDurum = False

for i in dersler:
    if i.startswith(sor):
        kayitDurum = True
        break
    else:
        kayitDurum = False

if kayitDurum == True:
    print("Kayıtlar aşağıda listelenmiştir")
    for i in dersler:
        if i.startswith(sor):
            print(i)
else:
    print("Kayıt Bulunamadı.")   

