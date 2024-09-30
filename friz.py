import itertools
import datetime
from datetime import time

class Pakalpojums:
    Pakalpojuma_kategorija=""
    Pakalpojuma_nosaukums=""
    Pakalpojuma_atlaide=""
    Pakalpojuma_cena=0

    id_iter=itertools.count()

    def __init__(self, pak_kat=None, pak_nos=None, pak_atl=None, pak_cena=10):
        self.Pakalpojums_id=next(self.id_iter)+1
        self.Pakalpojuma_kategorija=pak_kat
        self.Pakalpojuma_nosaukums=pak_nos
        self.Pakalpojuma_atlaide=pak_atl
        self.Pakalpojuma_cena_stunda=pak_cena
        self.Laiks_pieejams=True

    def Pakalpojums_info(self):
        return [
            self.Pakalpojuma_kategorija, self.Pakalpojuma_nosaukums, self.Pakalpojuma_atlaide, self.Pakalpojuma_cena_stunda
        ]
    
    def Pakalpojuma_info_print(self):
        print("Pakalpojums kategorija: "+str(self.Pakalpojuma_kategorija))
        print("Pakalpojums nosaukums: "+str(self.Pakalpojuma_nosaukums))
        print("Pakalpojums atlaide: "+str(self.Pakalpojuma_atlaide))
        print("Pakalpojums cena par stundu: "+str(self.Pakalpojuma_cena_stunda))
        print("Laiks pieejams: "+str(self.Laiks_pieejams)+"\n")



    

class Klients:
    Klienta_vards=""
    Klienta_uzvards=""
    Klienta_PK=""
    Klienta_tel_numurs=""

    id_iter_kl=itertools.count()

    def __init__(self, vards, uzvards, pk, tel_num):
        self.Klienta_id=next(self.id_iter_kl)+1
        self.Klienta_vards=vards
        self.Klienta_uzvards=uzvards
        self.Klienta_PK=pk
        self.Klienta_tel_numurs=tel_num

    def klienta_info(self):
        return[
            self.Klienta_vards, self.Klienta_uzvards, self.Klienta_PK, self.Klienta_tel_numurs
        ]

    def klienta_info_print(self):
        print("Klienta vards: "+str(self.Klienta_vards))
        print("Klienta uzvards: "+str(self.Klienta_uzvards))
        print("Klienta personas kods: "+str(self.Klienta_PK))
        print("Klienta personas telefona numurs: "+str(self.Klienta_tel_numurs)+'\n')


class Izmantosana:
    Pakalpojuma_sakuma_laiks=0
    Pakalpojuma_beigu_laiks=0
    Pakalpojuma_datums=0
    Izmantosanas_cena_stunda=10
    id_pakalpojums=0
    id_klients=0
    izmantosana_id=0

    id_iter_izmantosana=itertools.count()

    def Cena_kopa(self):
        kopeja_cena=self.Izmantosanas_cena_stunda*(((self.Pakalpojuma_beigu_laiks-self.Pakalpojuma_sakuma_laiks)))
        return kopeja_cena
    
    def izmantosana_info_print(self):
        print("Pakalpojuma sakuma laiks: "+str(self.Pakalpojuma_sakuma_laiks))
        print("Pakalpojuma beigu laiks: "+str(self.Pakalpojuma_beigu_laiks))
        print("Pakalpojums id: "+str(self.id_pakalpojums))
        print("Klients id: "+str(self.id_klients))
        print("Pakalpojuma cena stunda, EUR: "+str(self.Izmantosanas_cena_stunda)+'\n')

pak1=Pakalpojums("Frizetava", "Matu griesana", "20%", 30)
print(pak1.Pakalpojums_id)
pak1.Pakalpojums_info()
pak1.Pakalpojuma_info_print()
kl1=Klients("John", "Ivanov", "123456-78900", "20000000")
print(kl1.Klienta_id)
kl1.klienta_info()
kl1.klienta_info_print()