# ------------Veresiye Programı v1.0------------- #
#SINIRLAR : 100 TL VERESİYEDEN SONRA %10 ZAMLI ÜRÜN SATIMI.
#150 TL SON SINIR FAZLA ALIŞVERİŞ YAPILAMAZ.


print("*ÜRÜNLER*")
print("""-ÇİKOLATA
-MEYVE SUYU
-KEK
-SÜT
-PRİL
""")
print("-------------------")


print("*KİŞİLER*")
print("""-İbrahim
-Şengül
-Emine
""")

cikolata = 5
meyve_suyu = 10
kek = 5
sut = 10
pril = 20
ibrahim = 0
sengul = 0
emine = 0

urun_fiyat = [cikolata,meyve_suyu,kek,sut,pril]
urun = ["Çikolata","Meyve Suyu","Kek","Süt","Pril"]
kisiler = ["İbrahim","Şengül","Emine"]
kisi_parasi = [ibrahim,sengul,emine]

while True:
    islem1 = input("Borç Yazılacak Kişinin Adını Giriniz : ")
    islem2 = input("Alınacak Ürünü Seçiniz : ")

    if islem1 == "q":
        break
    if islem1 == kisiler[0]:
        if islem2 == urun[0]:
            kisi_parasi[0] += urun_fiyat[0]
        elif islem2 == urun[1]:
            kisi_parasi[0] += urun_fiyat[1]
        elif islem2 == urun[2]:
            kisi_parasi[0] += urun_fiyat[2]
        elif islem2 == urun[3]:
            kisi_parasi[0] += urun_fiyat[3]
        elif islem2 == urun[4]:
            kisi_parasi[0] += urun_fiyat[4]
    elif islem1 == kisiler[1]:
        if islem2 == urun[0]:
            kisi_parasi[1] += urun_fiyat[0]
        elif islem2 == urun[1]:
            kisi_parasi[1] += urun_fiyat[1]
        elif islem2 == urun[2]:
            kisi_parasi[1] += urun_fiyat[2]
        elif islem2 == urun[3]:
            kisi_parasi[1] += urun_fiyat[3]
        elif islem2 == urun[4]:
            kisi_parasi[1] += urun_fiyat[4]
    elif islem1 == kisiler[2]:
        if islem2 == urun[0]:
            kisi_parasi[2] += urun_fiyat[0]
        elif islem2 == urun[1]:
            kisi_parasi[2] += urun_fiyat[1]
        elif islem2 == urun[2]:
            kisi_parasi[2] += urun_fiyat[2]
        elif islem2 == urun[3]:
            kisi_parasi[2] += urun_fiyat[3]
        elif islem2 == urun[4]:
            kisi_parasi[2] += urun_fiyat[4]

for i in kisi_parasi:
    if i >= 100 and i <= 150:
        for x in urun_fiyat:
            x = x + ((x*10)/100)
        if i >= 150:
            print("Lütfen Borcunuzu Ödedikten sonra Alışveriş Yapınız.")
            i = 150
print("İbrahim Borç : {}  Şengün Borç : {}  , Emine Borç : {}".format(kisi_parasi[0],kisi_parasi[1],kisi_parasi[2]))
