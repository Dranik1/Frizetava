from tkinter import Tk, Button, Label, Entry, messagebox
import re


def parbaude():
    vards=entry_vards.get()
    dzg=entry_dzg.get()
    vieta=entry_vieta.get()

    vards_patt = r'^[A-ZĀ-Ž]{1}[a-zā-ž]+$|^[A-ZĀ-Ž]{1}[a-zā-ž]+\s+[A-ZĀ-Ž]{1}[a-zā-ž]+$'
    dzg_patt = r'^\d{2}/\d{2}/\d{4}$|^\d{2}.\d{2}.\d{4}$'
    vieta_patt = r'^[A-ZĀ-Ž]{1}[a-zā-ž]+\s+[iela, prospekts, aleja]+\s+\d{1,}'

    if re.match(vards_patt, vards):
        pass
        if re.match(dzg_patt, dzg):
            pass
            if re.match(vieta_patt, vieta):
                messagebox.showinfo("", "Viss ir kartībā")
            else:
                messagebox.showerror("Error", "Vieta")
        else:
            messagebox.showerror("Error", "Dzimšana")
    else:
        messagebox.showerror("Error", "Vards")




root = Tk()
root.geometry('300x300+500+300')

Label(root, text="Sūņa reģistrācija", font=("Helvetica", 10)).pack()

Label(root, text="Sūņa vārds:", padx=10, pady=3).pack()
entry_vards = Entry(root)
entry_vards.pack(padx=10, pady=3)

Label(root, text="Sūņa dzimšanas diena, mēnesis in gads:", padx=10, pady=10).pack()
entry_dzg = Entry(root)
entry_dzg.pack(padx=10, pady=3)

Label(root, text="Sūņa atrašanas vieta:", padx=10, pady=3).pack()
entry_vieta = Entry(root)
entry_vieta.pack(padx=10, pady=3)

Button(root, text="Reģistrācija", padx=10, pady=10, command=parbaude).pack(pady=10)

root.mainloop()