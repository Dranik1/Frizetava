import itertools
import sqlite3 as db
import re
from tkinter import *
from tkinter import messagebox, ttk
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


def kata_level():

    def reg_logs():

        def kata_list():
            global names
            try:

                conn = db.connect('karate.db')
                cursor = conn.cursor()
                cursor.execute("SELECT kata from Kata")
                names = []
                name_all=cursor.fetchall()
                for katas in name_all:
                    names.append(katas[0])
                conn.close()
                

            except Exception as e:
                messagebox.showerror("Error", f"Neizdevas nolasīt kata nosaukumus: {e}")



        def kata_reg():
            global dal
            vards = entry_vards.get()
            uzvards = entry_uzvards.get()
            dzimums = entry_dzimums.get()
            vecums = entry_vecums.get()
            masa = entry_masa.get()
            josta = entry_josta.get()
            pk = entry_pk.get()

            if vards and uzvards and dzimums and vecums.isdigit()>0 and masa.isdigit()>0 and josta and pk:
                try:
                    vecums = int(vecums)
                    masa = int(masa)
                    dal=Dalibnieks(vards, uzvards, dzimums, vecums, masa, josta, pk)
                    dal=Kata(vards, uzvards, dzimums, vecums, masa, josta, pk)
                    get_var = kata_combobox.get()
                    conn = db.connect('karate.db')
                    cursor = conn.cursor()
                    cursor.execute("SELECT id_kata from Kata where kata = ?;", (get_var,),)
                    id_kata = cursor.fetchone()
                    print(id_kata)
                    dal.Dalibnieka_kata_id=id_kata[0]
                    dal.registration()

                    messagebox.showinfo("Success", "Dalibnieks tik reģistrēts")

                except ValueError:
                    messagebox.showerror("Error")
            else:
                messagebox.showerror("Error")


        
        

        

        reg_log = Toplevel()
        reg_log.title("Registrācija")

        kata_list()

        Label(reg_log, text="Ievadiet datus", padx=10, pady=10).grid(column=0, row=0)


        v = Label(reg_log, text="Vards:").grid(column=0, row=1)
        entry_vards = Entry(reg_log)
        entry_vards.grid(column=1, row=1, padx=5, pady=5)


        u = Label(reg_log, text="Uzvards:").grid(column=0, row=2)
        entry_uzvards = Entry(reg_log)
        entry_uzvards.grid(column=1, row=2, padx=5, pady=5)
        

        d = Label(reg_log, text="Dzimums:").grid(column=0, row=3)
        entry_dzimums = Entry(reg_log)
        entry_dzimums.grid(column=1, row=3, padx=5, pady=5)
        

        ve = Label(reg_log, text="Vecums:").grid(column=0, row=4)
        entry_vecums = Entry(reg_log)
        entry_vecums.grid(column=1, row=4, padx=5, pady=5)
        

        m = Label(reg_log, text="Masa:").grid(column=0, row=5)
        entry_masa = Entry(reg_log)
        entry_masa.grid(column=1, row=5, padx=5, pady=5)
        

        j = Label(reg_log, text="Josta:").grid(column=0, row=6)
        entry_josta = Entry(reg_log)
        entry_josta.grid(column=1, row=6, padx=5, pady=5)
        

        p = Label(reg_log, text="Personas kods:").grid(column=0, row=7)
        entry_pk = Entry(reg_log)
        entry_pk.grid(column=1, row=7, padx=5, pady=5)

        kata_combobox = ttk.Combobox(reg_log, width=30, state="readonly", values=names)
        kata_combobox.grid(column=0, row=8)

        saglabat = Button(reg_log, text="Saglabat", padx=10, pady=10, command=kata_reg).grid(column=1, row=9)

    def upd_logs():
        pass

    def find_logs():

        def print_all():
            conn = db.connect('karate.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * from Dalibnieks_kata")
            info = cursor.fetchall()

            messagebox.showinfo("Visi dalibnieki", info)

        def find_by_id():

            id_dal = entry_id.get()
            try:

                conn = db.connect('karate.db')
                cursor = conn.cursor()
                cursor.execute("Select * from Dalibnieks_kata where id_dalibnieka_kata = ?", (id_dal,))
                info = cursor.fetchall()

                messagebox.showinfo("Dalibnieks", info)
            except Exception as e:
                messagebox.showerror('Error', e)


        find_log = Toplevel()

        all_btn = Button(find_log, text="Noprintēt visus", padx=10, pady=10, command=print_all).grid(column=0, row=0)
        entry_id = Entry(find_log)
        entry_id.grid(column=0, row=1)
        atrast = Button(find_log, text="Atrast ar id", padx=10, pady=10, command=find_by_id).grid(column=0, row=2)

    def del_logs():

        def del_dalib():
            id_dal = entry_del_id.get()
            try:

                conn = db.connect('karate.db')
                cursor = conn.cursor()
                cursor.execute("DELETE from Dalibnieks_kata where id_dalibnieka_kata = ?", (id_dal,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Dalibnieks tiek nodzēsts")

            except Exception as e:
                messagebox.showerror("Error", e)



        del_log = Toplevel()

        entry_del_id = Entry(del_log)
        entry_del_id.grid(column=0, row=0)
        Button(del_log, text="Dzēst", padx=10, pady=10, command=del_dalib).grid(column=0, row=1, padx=5, pady=5)

    kata_logs = Toplevel()
    kata_logs.title("Kata sacensības")
    
    reg_btn = Button(kata_logs, text="Registracija", padx=10, pady=10, command=reg_logs).grid(column=0, row=0)
    upd_btn = Button(kata_logs, text="Atjaunot datus", padx=10, pady=10).grid(column=0, row=1)
    find_btn = Button(kata_logs, text="Atrast", padx=10, pady=10, command=find_logs).grid(column=0, row=2)
    del_btn = Button(kata_logs, text="Nodzēst", padx=10, pady=10, command=del_logs).grid(column=0, row=3)



root = Tk()
root.geometry("200x250")
root.title("Sacensības sistēma")
label1 = Label(root, text="Izvēlies sacensības kategoriju: ", padx=10, pady=10).grid(column=2, row=0)

kat_btn = Button(root, text="Kata", padx=30, pady=20, command=kata_level).grid(column=2, row=1, padx=10, pady=10)
kumite_btn = Button(root, text="Kumite", padx=30, pady=20).grid(column=2, row=2, padx=10, pady=10)

root.mainloop()
           
           



