import itertools
import sqlite3 as db
import re
import tkinter as tk
from tkinter.simpledialog import askinteger





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
        
        conn.execute("INSERT INTO Dalibnieks_kumite(name, surname, age, belt, personal_code, id_weight_cathegory, gender) VALUES(?, ?, ?, ?, ?, ?, ?)", (self.Dalibnieka_vards, self.Dalibnieka_uzvards, self.Dalibnieka_vecums, self.Dalibnieka_josta, self.Dalibnieka_pk, self.Dalibnieka_svara_kategorija, self.gender))
        conn.commit()

    def update(self):
        if self.Dalibnieka_dzimums[0]=="v":
            self.gender="virietis"
        elif self.Dalibnieka_dzimums[0]=="s":
            self.gender="sieviete"
        else:
            self.gender=None
        id_d = int(input("Ievadiet dalibnieka id: "))
        conn.execute("INSERT INTO Dalibnieks_kumite(id_dalibnieka_kumite, name, surname, age, belt, personal_code, id_weight_cathegory, gender) VALUES(?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT(id_dalibnieka_kumite) DO UPDATE SET name=excluded.name, surname=excluded.surname, age=excluded.age, belt=excluded.belt, personal_code=excluded.personal_code, id_weight_cathegory=excluded.id_weight_cathegory, gender=excluded.gender;", (id_d, self.Dalibnieka_vards, self.Dalibnieka_uzvards, self.Dalibnieka_vecums, self.Dalibnieka_josta, self.Dalibnieka_pk, self.Dalibnieka_svara_kategorija, self.gender))
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
        
        conn.execute("INSERT INTO Dalibnieks_kata(name, surname, age, belt, personal_code, id_kata, geneder) VALUES(?, ?, ?, ?, ?, ?, ?)", (self.Dalibnieka_vards, self.Dalibnieka_uzvards, self.Dalibnieka_vecums, self.Dalibnieka_josta, self.Dalibnieka_pk, self.Dalibnieka_kata_id, self.gender))
        conn.commit()


    def update(self):
        if self.Dalibnieka_dzimums[0]=="v":
            self.gender="virietis"
        elif self.Dalibnieka_dzimums[0]=="s":
            self.gender="sieviete"
        else:
            self.gender=None
        id_d = int(input("Ievadiet dalibnieka id: "))
        conn.execute("INSERT INTO Dalibnieks_kata(id_dalibnieka_kata, name, surname, age, belt, personal_code, id_kata, geneder) VALUES(?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT(id_dalibnieka_kata) DO UPDATE SET name=excluded.name, surname=excluded.surname, age=excluded.age, belt=excluded.belt, personal_code=excluded.personal_code, id_kata=excluded.id_kata, geneder=excluded.geneder;", (id_d, self.Dalibnieka_vards, self.Dalibnieka_uzvards, self.Dalibnieka_vecums, self.Dalibnieka_josta, self.Dalibnieka_pk, self.Dalibnieka_kata_id, self.gender))
        conn.commit()

def upd():
    kk=input("Kata vai kumite sacensībam: ")
    if kk.lower()=='kumite':
        vards = input("Ievadiet jauno vārdu: ")
        uzvards = input("Ievadiet jauno uzvārdu: ")
        dzimums = input("Ievadiet jauno dzimumu: ")
        vecums = int(input("Ievadiet jauno vecumu: "))
        masa = int(input("Ievadiet jauno svaru: "))
        josta = input("Ievadiet jauno jostu: ")
        pk = input("Ievadiet jauno pesonalo kodu: ")
        dal=Dalibnieks(vards, uzvards, dzimums, vecums, masa, josta, pk)
        dal=Kumite(vards, uzvards, dzimums, vecums, masa, josta, pk)
        dal.svara_kategorija()
        dal.update()
    elif kk.lower()=='kata':
        vards = input("Ievadiet jauno vārdu: ")
        uzvards = input("Ievadiet jauno uzvārdu: ")
        dzimums = input("Ievadiet jauno dzimumu: ")
        vecums = int(input("Ievadiet jauno vecumu: "))
        masa = int(input("Ievadiet jauno svaru: "))
        josta = input("Ievadiet jauno jostu: ")
        pk = input("Ievadiet jauno pesonalo kodu: ")
        dal=Dalibnieks(vards, uzvards, dzimums, vecums, masa, josta, pk)
        dal=Kata(vards, uzvards, dzimums, vecums, masa, josta, pk)
        dal.kata()
        dal.update()

def reg():
    kk=input("Kata vai kumite sacensībam: ")
    if kk.lower()=='kumite':
        vards = input("Ievadiet vārdu: ")
        uzvards = input("Ievadiet uzvārdu: ")
        dzimums = input("Ievadiet dzimumu: ")
        vecums = int(input("Ievadiet vecumu: "))
        masa = int(input("Ievadiet svaru: "))
        josta = input("Ievadiet jostu: ")
        pk = input("Ievadiet pesonalo kodu: ")
        dal=Dalibnieks(vards, uzvards, dzimums, vecums, masa, josta, pk)
        dal=Kumite(vards, uzvards, dzimums, vecums, masa, josta, pk)
        dal.svara_kategorija()
        dal.registration()
    elif kk.lower()=='kata':
        vards = input("Ievadiet vārdu: ")
        uzvards = input("Ievadiet uzvārdu: ")
        dzimums = input("Ievadiet dzimumu: ")
        vecums = int(input("Ievadiet vecumu: "))
        masa = int(input("Ievadiet svaru: "))
        josta = input("Ievadiet jostu: ")
        pk = input("Ievadiet pesonalo kodu: ")
        dal=Dalibnieks(vards, uzvards, dzimums, vecums, masa, josta, pk)
        dal=Kata(vards, uzvards, dzimums, vecums, masa, josta, pk)
        dal.kata()
        dal.registration()

def find():
    kk=input("Kata vai kumite dalibnieku: ")
    if kk.lower()=='kata':
        choice = input("Vai jūs gribāt atrast dalibnieku ar id vai ar kata: ")
        if choice=='id':
            id_d=int(input("Ievadiet dalibnieka id: "))
            c = conn.execute("Select * from Dalibnieks_kata WHERE id_dalibnieka_kata=?",(id_d,))
            c = c.fetchall()
            for i in c:
                print(c)
        elif choice=='kata':
            kata = conn.execute("SELECT * from Kata")
            print("Kata list: ")
            for r in kata:
                print(r)
            kata_d = input("Ievadiet kata id: ")
            c = conn.execute("SELECT * from Dalibnieks_kata WHERE id_kata=?", (kata_d,))
            c = c.fetchall()
            for i in c:
                print(c)
    elif kk.lower()=='kumite':
        choice = input("Vai jūs gribāt atrast dalibnieku ar id vai ar svara kategoriju: ")
        if choice=='id':
            id_d=int(input("Ievadiet dalibnieka id: "))
            c = conn.execute("Select * from Dalibnieks_kumite WHERE id_dalibnieka_kumite=?",(id_d,))
            c = c.fetchall()
            for i in c:
                print(c)
        elif choice[0]=='s':
            svars_d = input("Ievadiet svara kategoriju: ")
            c = conn.execute("SELECT * from Dalibnieks_kumite WHERE id_weight_cathegory=?", (svars_d,))
            c = c.fetchall()
            for i in c:
                print(c)
    else:
        pass

def delete():
    kk=input("Kata vai kumite dalibnieku: ")
    if kk.lower()=='kata':
        id_d=int(input("Ievadiet dalibnieka id: "))
        conn.execute("DELETE from Dalibnieks_kata where id_dalibnieka_kata=?", (id_d,))
        conn.commit()
    elif kk.lower()=='kumite':
        id_d=int(input("Ievadiet dalibnieka id: "))
        conn.execute("DELETE * from Dalibnieks_kumite where id_dalibnieka_kumite=?", (id_d,))
        conn.commit()
    print("Dalibnieks tik izdzēsts!")



root = tk.Tk()
root.geometry("200x250")
root.title("Sacensības sistēma")
label1 = tk.Label(root, text="Izvēlies sacensības kategoriju: ", padx=10, pady=10).grid(column=2, row=0)

kat_btn = tk.Button(root, text="Kata", padx=30, pady=20).grid(column=2, row=1, padx=10, pady=10)
kumite_btn = tk.Button(root, text="Kumite", padx=30, pady=20).grid(column=2, row=2, padx=10, pady=10)

root.mainloop()
           
           



