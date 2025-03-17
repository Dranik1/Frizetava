import tkinter as tk
from tkinter import messagebox
import re

def paarbaude_vaardu():
    vaards = vaards_entry.get()
    pattern=r'^[A-ZĀČĒĢĪĶĻŅŠŪŽ]{1}[a-zāčēģīķļņšūž]+$'
    #pattern=r'^([A-ZĀČĒĢĪĶĻŅŠŪŽ]{1}[a-zāčēģīķļņšūž])|([0-9\d]{3,})+$'
    #pattern = r'^[A-Z]{1}[a-z]{1,}'
    
    if re.match(pattern, vaards):
        messagebox.showinfo("Rezultāts", "Vards ir derīgs!")
    else:
        messagebox.showerror("Rezultāts", "Vārds nav derīgs!")

def paarbaude_uzvaardu():
    uzvaards = uzvaards_entry.get()
    pattern=r'^[A-ZĀČĒĢĪĶĻŅŠŪŽ\s]{1}[a-zāčēģīķļņšūž\s]+$'
    #pattern = r'^[A-Z]{1}[a-z]{1,}'
    
    if re.match(pattern, uzvaards):
        messagebox.showinfo("Rezultāts", "Uzvārds ir derīgs!")
    else:
        messagebox.showerror("Rezultāts", "Uzvārds nav derīgs!")

def paarbaude_talrunis():
    talrunis = entryt.get()
    pattern = pattern=r'^[+][3][7][1][0-9\d]{8}+$'
    
    if re.match(pattern, talrunis):
        messagebox.showinfo("Rezultāts", "Tālrunis ir derīgs!")
    else:
        messagebox.showerror("Rezultāts", "Tālrunis nav derīgs!")

def paarbaude_email():
    email = entry.get()
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        messagebox.showinfo("Rezultāts", "E-pasta eadrese ir derīga!")
    else:
        messagebox.showerror("Rezultāts", "E-pasta eadrese nav derīga!")

def paarbaude_adrese():
    adrese = entry_adr.get()
    pattern=r'^[A-Z]{1}[a-z]+[/s]{1}+[0-9]+$'
    #pattern=r'^[A-Z]{1}[a-z] [0-9]$'
    #pattern = r'^[A-Z][a-z]+$'
    
    if re.match(pattern, adrese):
        messagebox.showinfo("Rezultāts", "Adrese ir derīga!")
    else:
        messagebox.showerror("Rezultāts", "Adrese nav derīga!")

def paarbaude_kods():
    personc = entry_kods.get()
    #pattern = r'^\d{6,6}$+[-]+^\d{5,5}$'
    #pattern =r'\d{6}-\d{5}$'
    pattern =r'[0-9]{6}-[0-9]{5}$'
    #pattern = r'^[\d]{6}[-][\d]{5}$'
    
    if re.match(pattern, personc):
        messagebox.showinfo("Rezultāts", "Personas kods ir derīgs!")
    else:
        messagebox.showerror("Rezultāts", "Personas kods nav derīgs!")

root = tk.Tk()
root.title("Personas koda pārbaude")

tk.Label(root, text="Ievadiet vārdu:").pack(pady=5)
vaards_entry = tk.Entry(root, width=30)
vaards_entry.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbaude_vaardu).pack(pady=5)

tk.Label(root, text="Ievadiet uzvārdu:").pack(pady=5)
uzvaards_entry = tk.Entry(root, width=30)
uzvaards_entry.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbaude_uzvaardu).pack(pady=5)

tk.Label(root, text="Ievadiet talruni:").pack(pady=5)
entryt = tk.Entry(root, width=30)
entryt.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbaude_talrunis).pack(pady=5)

tk.Label(root, text="Ievadiet personas kodu :").pack(pady=5)
entry_kods = tk.Entry(root, width=30)
entry_kods.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbaude_kods).pack(pady=5)

tk.Label(root, text="Ievadiet adresi:").pack(pady=5)
tk.Label(root, text="(Dzīvoklis/iela/mājas nosaukums)").pack(pady=5)
entry_adr = tk.Entry(root, width=30)
entry_adr.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbaude_adrese).pack(pady=5)

tk.Label(root, text="Ievadiet email :").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)
tk.Button(root, text="Pārbaudīt", command=paarbaude_email).pack(pady=5)

root.mainloop()
