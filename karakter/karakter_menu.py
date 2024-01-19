from tkinter import Label, Button
from PIL import ImageTk, Image
from karakter.karakter_creatie import maak_karakter_creatie_scherm_aan
from karakter.karakter_selectie import maak_karakter_selectie_scherm_aan


def ga_naar_karakter_selectie_scherm(venster):
    maak_karakter_selectie_scherm_aan(venster)


def ga_naar_hoofdmenu(venster):
    from app.hoofdmenu import maak_hoofdmenu_scherm_aan
    maak_hoofdmenu_scherm_aan(venster)


def ga_naar_karakter_creatie_scherm(venster):
    maak_karakter_creatie_scherm_aan(venster)


def maak_karakter_menu_scherm_aan(venster):
    for widget in venster.winfo_children():
        widget.destroy()

    karakter_menu_titel = Label(venster, text="Karakter Menu", font=("Helvetica", 36))

    karakter_selectie_button = Button(text="Karakter Selectie", width=20,
                                      height=2, command=lambda: ga_naar_karakter_selectie_scherm(venster))

    karakter_creatie_button = Button(text="Karakter Creëren", width=20,
                                     height=2, command=lambda: ga_naar_karakter_creatie_scherm(venster))
    terug_button = Button(venster, text="Terug naar hoofdmenu", command=lambda: ga_naar_hoofdmenu(venster),
                          width=20,
                          height=2)

    karakter_menu_titel.pack()
    karakter_selectie_button.pack(expand=True, side="left")
    karakter_creatie_button.pack(expand=True, side="right")
    terug_button.pack()

