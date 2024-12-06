import itertools
import datetime as dt
import json
import sqlite3 as db


conn = db.connect('karate.db')
curr = conn.cursor()            

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
    def __init__(self, vards, uzvards, dzimums, vecums, svars, josta, pk):
        super().__init__(vards, uzvards, dzimums, vecums, svars, josta, pk)
    id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    kategorijas_vir=[61, 68, 76, 85, 300]
    kategorijas_vir_name=["-60 kg", "61-67 kg", "68-75 kg", "76-84 kg", "85+ kg"]
    kategorijas_siev=[51, 56, 62, 69, 300]
    kategorijas_siev_name=["-50 kg", "51-55 kg", "56-61 kg", "62-68 kg", "69+ kg"]
    def svara_kategorija(self):
        self.id_reg = 0
        self.Dalibnieka_svara_kategorija=""
        if self.Dalibnieka_dzimums[0]=="s":
            stop=False
            a=0
            b=1
            c=1
            while stop!=True:
                if self.Dalibnieka_svars in range(1, self.kategorijas_siev[0]):
                    print(self.kategorijas_siev_name[c-1])
                    self.Dalibnieka_svara_kategorija=self.kategorijas_siev_name[c-1]
                    self.id_reg = self.id[c-1+5]
                    stop=True
                elif self.Dalibnieka_svars in range(self.kategorijas_siev[a], self.kategorijas_siev[b]):
                    c+=1
                    print(self.kategorijas_siev_name[c-1])
                    self.Dalibnieka_svara_kategorija=self.kategorijas_siev_name[c-1]
                    self.id_reg = self.id[c-1+5]
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
                    print(self.kategorijas_vir_name[c-1])
                    self.Dalibnieka_svara_kategorija=self.kategorijas_vir_name[c-1]
                    self.id_reg = self.id[c-1]
                    stop=True
                elif self.Dalibnieka_svars in range(self.kategorijas_vir[a], self.kategorijas_vir[b]):
                    c+=1
                    print(self.kategorijas_vir_name[c-1])
                    self.Dalibnieka_svara_kategorija=self.kategorijas_vir_name[c-1]
                    self.id_reg = self.id[c-1]
                    stop=True
                else:
                    a=a+1
                    b=b+1
                    c+=1
        else:
            print("Who are you?")


    def registration(self):
        if self.Dalibnieka_dzimums[0]=="v":
            self.gender="virietis"
        elif self.Dalibnieka_dzimums[0]=="s":
            self.gender="sieviete"
        else:
            self.gender=None
        '''dalibnieka_data={
            "name":self.Dalibnieka_vards,
            "surname":self.Dalibnieka_uzvards,
            "gender":self.gender,
            "age":self.Dalibnieka_vecums,
            "weight":self.Dalibnieka_svars,
            "belt":self.Dalibnieka_josta,
            "personal code":self.Dalibnieka_pk,
            "weight cathegory":self.Dalibnieka_svara_kategorija,
            "id":self.Dalibnieka_id
        }

        with open('dalibnieki.json') as f:
             data=json.load(f)
            
        data.append(dalibnieka_data)

        with open('dalibnieki.json', 'w') as f:
             json.dump(data, f, indent=2)'''
        
        curr = conn.execute("INSERT INTO Dalibnieks_kumite(id_dalibnieka_kumite, name, surname, age, belt, personal_code, id_weight_cathegory, gender) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (self.Dalibnieka_id, self.Dalibnieka_vards, self.Dalibnieka_uzvards, self.Dalibnieka_vecums, self.Dalibnieka_josta, self.Dalibnieka_pk, self.id_reg, self.gender))
        conn.commit()

class Kata(Dalibnieks):
    def __init__(self, vards, uzvards, dzimums, vecums, svars, josta, pk):
        super().__init__(vards, uzvards, dzimums, vecums, svars, josta, pk)
        self.Dalibnieka_kata=""
    
    def kata(self):
        kata = conn.execute("SELECT * from Kata")
        print("Kata list: ")
        for r in kata:
            print(r)
        
        stop= False
        while stop!=True:
            kata_num = int(input('Ievadiet kata id: '))
            for i in range(103):
                cur = conn.execute("SELECT * from Kata WHERE id_kata = ?", (i,))
                kata = cur.fetchall()
                if kata_num == i:
                    agree = input(f"{kata} ir jūsu kata? ")
                    if agree=='True':
                        self.Dalibnieka_kata_id=i
                        stop=True
                    else:
                        print("Mēģini vēl reiz")
        
    def registration(self):
        if self.Dalibnieka_dzimums[0]=="v":
            self.gender="virietis"
        elif self.Dalibnieka_dzimums[0]=="s":
            self.gender="sieviete"
        else:
            self.gender=None
        '''dalibnieka_data={
            "name":self.Dalibnieka_vards,
            "surname":self.Dalibnieka_uzvards,
            "gender":self.gender,
            "age":self.Dalibnieka_vecums,
            "weight":self.Dalibnieka_svars,
            "belt":self.Dalibnieka_josta,
            "personal code":self.Dalibnieka_pk,
            "kata":self.Dalibnieka_kata,
            "id":self.Dalibnieka_id
        }
        with open('dalibnieki.json') as f:
             data=json.load(f)
            
        data.append(dalibnieka_data)

        with open('dalibnieki.json', 'w') as f:
             json.dump(data, f, indent=2)'''
        
        curr = conn.execute("INSERT INTO Dalibnieks_kata(id_dalibnieka_kata, name, surname, age, belt, personal_code, id_kata, geneder) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (self.Dalibnieka_id, self.Dalibnieka_vards, self.Dalibnieka_uzvards, self.Dalibnieka_vecums, self.Dalibnieka_josta, self.Dalibnieka_pk, self.Dalibnieka_kata_id, self.gender))
        conn.commit()



        
        
while True:
    num=int(input("1.Reģistreties  2.Mainīt datus  3.Dzēst  4.Stop  5.Noprintet dalibniekus"))
    if num==1:
        kk=input("Kata vai kumite sacensībam: ")
        if kk.lower()=='kumite':
            vards = input()
            uzvards = input()
            dzimums = input()
            vecums = int(input())
            masa = int(input())
            josta = input()
            pk = input()
            dal=Dalibnieks(vards, uzvards, dzimums, vecums, masa, josta, pk)
            dal=Kumite(vards, uzvards, dzimums, vecums, masa, josta, pk)
            dal.svara_kategorija()
            dal.registration()
        elif kk.lower()=='kata':
            vards = input()
            uzvards = input()
            dzimums = input()
            vecums = int(input())
            masa = int(input())
            josta = input()
            pk = input()
            dal=Dalibnieks(vards, uzvards, dzimums, vecums, masa, josta, pk)
            dal=Kata(vards, uzvards, dzimums, vecums, masa, josta, pk)
            dal.kata()
            dal.registration()
            
    elif num==2:
        kk=input("Kata vai kimite dalibnieku: ")
        if kk.lower()=='kata':
            id_d = int(input("Ievadiet dalibnieka id: "))
            conn.execute("UPDATE Dalibnieks_kata set * Values(?, ?, ?, ?, ?, ?, ?) WHERE id_dalibnieka_kata = ?", (vards, uzvards, dzimums, vecums, masa, josta, pk, id_d))
        elif kk.lower()=='kumite':
            print('Ievadiet jaunus datus: ')
            vards = input()
            uzvards = input()
            dzimums = input()
            vecums = int(input())
            masa = int(input())
            josta = input()
            pk = input()
            id_d = int(input("Ievadiet dalibnieka id: "))
            conn.execute("UPDATE Dalibnieks_kumite set name=?, surname=?, gender=?, age=?, belt=?, personal_code=? WHERE id_dalibnieka_kumite = ?", (vards, uzvards, dzimums, vecums, josta, pk, id_d))

    elif num==3:
        kk=input("Kata vai kimite dalibnieku: ")
        if kk.lower()=='kata':
            id_d=int(input("Ievadiet dalibnieka id: "))
            conn.execute("DELETE from Dalibnieks_kata where id_dalibnieka_kata=?", (id_d,))
            conn.commit()
        elif kk.lower()=='kumite':
            id_d=int(input("Ievadiet dalibnieka id: "))
            conn.execute("DELETE * from Dalibnieks_kumite where id_dalibnieka_kumite=?", (id_d,))
            conn.commit()
        
    elif num==4:
        break

    elif num==5:
        kk=input("Kata vai kimite dalibnieku: ")
        if kk.lower()=='kata':
            cur = conn.execute("Select * from Dalibnieks_kata")
            cur.fetchall()
            print(cur)
        elif kk.lower()=='kumite':
            cur = conn.execute("Select * from Dalibnieks_kumite")
            cur.fetchall()
            print(cur.fetchall())

           
           
           




'''dal1=Dalibnieks("anna", "h", "sieviete", 17, 45, "3 Kyu", "123456-78900")
dal1.dalibnieka_info()
dal1=Kumite("anna", "h", "sieviete", 17, 45, "3 Kyu", "123456-78900")
dal1.svara_kategorija()
dal1.registration()

dal2=Dalibnieks("viktor", "h", "v", 17, 199, "3 Kyu", "123456-78900")
dal2.dalibnieka_info()
dal2=Kata("viktor", "h", "v", 17, 199, "3 Kyu", "123456-78900")
dal2.kata()
dal2.registration()

cur=conn.execute("SELECT * from Dalibnieks_kumite, Dalibnieks_kata")
a=cur.fetchall()
print(a)'''

