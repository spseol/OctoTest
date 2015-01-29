# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 21:04:50 2015

@author: Tom
"""
import urllib
import Tkinter as tk


def prihlasit():
    jmeno = jmeno_entry.get()
    heslo = heslo_entry.get()
    udaje = urllib.urlencode({"user": jmeno, "password": heslo})


def ulozit_udaje():             # uloží údaje
    jmeno = jmeno_entry.get()
    heslo = heslo_entry.get()
    jmeno_soubor = open("jmeno.txt", "w")
    heslo_soubor = open("heslo.txt", "w")
    jmeno_soubor.write(jmeno)
    heslo_soubor.write(heslo)
    jmeno_soubor.close()
    heslo_soubor.close()


def vyplnit_udaje():
    jmeno_soubor = open("jmeno.txt", "r")
    heslo_soubor = open("heslo.txt", "r")
    jmeno = jmeno_soubor.readline()
    heslo = heslo_soubor.readline()
    jmeno_entry.delete(0, tk.END)
    heslo_entry.delete(0, tk.END)
    jmeno_entry.insert(tk.END, jmeno)
    heslo_entry.insert(tk.END, heslo)


hl_okno = tk.Tk()
hl_okno.title("Odorik.cz")

jmeno_label = tk.Label(hl_okno, text="Jméno")       #Úvodní přihlašovací okno
jmeno_label.grid()

jmeno_entry = tk.Entry(hl_okno, justify="center")
jmeno_entry.grid(row=1)

heslo_label = tk.Label(hl_okno, text="Heslo")
heslo_label.grid(row=2)

heslo_entry = tk.Entry(hl_okno, justify="center")
heslo_entry.grid(row=3)

prihlaseni_button = tk.Button(hl_okno, text="Přihlásit", command=prihlasit, width=10)
prihlaseni_button.grid(row=4)

ulozeni_udaju_button = tk.Button(hl_okno, text="Uložit údaje", command=ulozit_udaje, width=10)
ulozeni_udaju_button.grid(row=5)

vyplneni_udaju_button = tk.Button(hl_okno, text="Vyplnit údaje", command=vyplnit_udaje, width=10)
vyplneni_udaju_button.grid(row=6)

hl_okno.mainloop()
