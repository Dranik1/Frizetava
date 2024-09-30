import itertools
import datetime as dt


class Kata:
    pass


            

class Dalibnieks:
    Dalibnieka_vards=""
    Dalibnieka_uzvards=""
    Dalibnieka_dzimums=""
    Dalibnieka_vecums=""
    Dalibnieka_svars=0
    Dalibnieka_josta=""
    Dalibnieka_pk=""

    id_iter_dalibnieks=itertools.count()

    def __init__(self, vards, uzvards, dzimums, vecums, svars, josta, pk):
        self.Dalibnieka_vards=vards
        self.Dalibnieka_uzvards=uzvards
        self.Dalibnieka_dzimums=dzimums
        self.Dalibnieka_vecums=vecums
        self.Dalibnieka_svars=svars
        self.Dalibnieka_josta=josta
        self.Dalibnieka_pk=pk
        self.Dalibnieka_id=next(self.id_iter_dalibnieks)+1

    def dalibnieka_info(self):
        return[
            self.Dalibnieka_vards, self.Dalibnieka_uzvards, self.Dalibnieka_dzimums, self.Dalibnieka_vecums, self.Dalibnieka_svars, self.Dalibnieka_josta, self.Dalibnieka_pk
        ]

    

class Kumite(Dalibnieks):
    kategorijas_vir=[61, 68, 76, 85, 300]
    kategorijas_siev=[51, 56, 62, 69, 300]
    def svara_kategorija(self):
        if self.Dalibnieka_dzimums[0]=="s":
            stop=False
            a=0
            b=1
            c=1
            while stop!=True:
                if self.Dalibnieka_svars in range(1, self.kategorijas_siev[0]):
                    print(c)
                    stop=True
                elif self.Dalibnieka_svars in range(self.kategorijas_siev[a], self.kategorijas_siev[b]):
                    c+=1
                    print(c)
                    stop=True
                else:
                    a=a+1
                    b=b+1
                    c+=1
        elif self.Dalibnieka_dzimums[0]=="v":
            stop=False
            a=0
            b=1
            c=1
            while stop!=True:
                if self.Dalibnieka_svars in range(1, self.kategorijas_vir[0]):
                    print(c)
                    stop=True
                elif self.Dalibnieka_svars in range(self.kategorijas_vir[a], self.kategorijas_vir[b]):
                    c+=1
                    print(c)
                    stop=True
                else:
                    a=a+1
                    b=b+1
                    c+=1
        else:
            print("Who are you?")
            

dal1=Dalibnieks("anna", "h", "sieviete", 17, 45, "3 Kyu", "123456-78900")
dal1.dalibnieka_info()
dal1=Kumite("anna", "h", "sieviete", 17, 45, "3 Kyu", "123456-78900")
dal1.svara_kategorija()


