from tkinter import Button, Image, Label, Frame
from PIL import Image, ImageTk

from app.splash_scherm import ga_naar_hoofdmenu_scherm
from avonturen.avontuur_spelen import maak_avontuur_scherm_aan


def ga_naar_avontuur_1(venster):
    maak_avontuur_scherm_aan(venster, "1")



def ga_naar_avontuur_2(venster):
    maak_avontuur_scherm_aan(venster, "2")


def ga_naar_avontuur_3(venster):
    maak_avontuur_scherm_aan(venster, "3")


def toon_avonturen_menu(venster):
    for widget in venster.winfo_children():
        widget.destroy()

    original_image = Image.open('../images/Crown_pic_two-2939004554.png')
    resized_image = original_image.resize((100, 60), Image.LANCZOS)
    afbeelding_1 = ImageTk.PhotoImage(resized_image)

    frame_bovenaan = Frame(venster)
    frame_bovenaan.grid(row=0, column=1, pady=50)

    label_bovenaan = Label(frame_bovenaan, text="Kies een avontuur", bg="white",font=("Helvetica", 36))
    label_bovenaan.grid(row=0, column=1, padx=360, pady=30)

    frame_avontuur_1 = Frame(venster)
    frame_avontuur_1.grid(row=2, column=0, padx=100, pady=100)

    avontuur_1_label = Label(frame_avontuur_1, image=afbeelding_1)
    avontuur_1_label.pack()

    button_avontuur_1 = Button(frame_avontuur_1, text="Reis In De Gouw", command=lambda: ga_naar_avontuur_1(venster))
    button_avontuur_1.pack()

    frame_avontuur_2 = Frame(venster)
    frame_avontuur_2.grid(row=2, column=1, padx=100)

    avontuur_2_label = Label(frame_avontuur_2, image=afbeelding_1)
    avontuur_2_label.pack()

    button_avontuur_2 = Button(frame_avontuur_2, text="Zoektocht zwaard Elendil", command=lambda: ga_naar_avontuur_2(venster))
    button_avontuur_2.pack()

    frame_avontuur_3 = Frame(venster)
    frame_avontuur_3.grid(row=2, column=2, padx=100)

    avontuur_3_label = Label(frame_avontuur_3, image=afbeelding_1)
    avontuur_3_label.pack()

    button_avontuur_3 = Button(frame_avontuur_3, text="Queeste Erebor", command=lambda: ga_naar_avontuur_3(venster))
    button_avontuur_3.pack()

    frame_terug_naar_hoofdmenu = Frame(venster)
    frame_terug_naar_hoofdmenu.grid(row=4, column=0)

    button_terug_naar_hoofd_menu = Button(frame_terug_naar_hoofdmenu, text ="Terug naar hoofdmenu",width=30, height=2, command=lambda: ga_naar_hoofdmenu_scherm(venster))
    button_terug_naar_hoofd_menu.pack(pady= 450)
    venster.mainloop()

