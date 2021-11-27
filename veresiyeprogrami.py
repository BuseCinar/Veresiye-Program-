import random
import time

class kumanda():

    def __init__(self,tv_durum = "kapalı",tv_ses = 0,kanal_listesi = ["trt"],kanal = "trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal


    def tv_ac(self):
        if (self.tv_durum=="açık"):
            print("tv zaten açık")
        else:
            print("tv açılıyor")
            self.tv_durum = "açık"


    def tv_kapat(self):
        if(self.tv_durum=="kapalı"):
            print("tv zaten kapalı")
        else:
            print("tv kapanıyor")
            self.tv_durum = "kapalı"


    def ses_ayaları(self):


        while True:
            cevap = input("Sesi azalt : '<'\nSes arttır:'>'\nÇıkış:exit")


            if cevap == "<":
                if(self.tv_ses !=0):
                    self.tv_ses -= 1
                    print("ses:",self.tv_ses)
            elif cevap == ">":
                if(self.tv_ses!= 31):
                    self.tv_ses += 1
                    print("ses:",self.tv_ses)
            else:
                print("tv ses güncellendi:",self.tv_ses)
                break


    def kanal_ekle(self,kanal_isim):

        print("kanal ekleniyor...")
        time.sleep(1)


        self.kanal_listesi.append(kanal_ismi)

        print("kanal eklendi...")
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("şuanki kanal:",self.kanal)


    def __len__(self):
        return len(self.kanal_listesi)


    def __str__(self):
        return "tv durumu: {}\ntv ses: {}\nkanal listesi: {}\nşuanki kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda = kumanda()

print( """
televizyon uygulaması


1 - tv aç

2 - tv kapat

3 - ses ayarları

4 - kanal ekle

5 - kanal sayısı öğrenme 

6 - rastgele kanala geçme

7 - televizyon blgileri

çıkmak için 'q' ya basın






""" )


while True:
    işlem = input("işlem seçiniz:")
    if işlem == "q":
        print("program sonlandırılıyor...")
        break

    elif işlem == "1":
        kumanda.tv_ac()
    elif işlem == "2":
        kumanda.tv_kapat()
    elif işlem == "3":
        kumanda.ses_ayaları()
    elif işlem == "4":
        kanal_ismi = input("kanal isimlerini ',' ile ayırarak söyleyin:")
        kanal_listesi = kanal_ismi.split(",")


        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif işlem == "5":
        print("kanal sayısı:",len(kumanda))


    elif işlem == "6":
        kumanda.rastgele_kanal()


    elif işlem == "7":
        print(kumanda)


    else:
        print("geçersiz işlem...")






