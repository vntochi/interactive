
from tkinter import Label, Button
from karakter.karakter_menu import maak_karakter_menu_scherm_aan
from PIL import ImageTk, Image

BUTTON_WIDTH= 40
BUTTON_HEIGHT= 2
IMAGE_HEIGHT = 700
IMAGE_WIDTH = 1200
def ga_naar_admin_scherm(venster):
    from admin.admin_button import maak_admin_scherm
    maak_admin_scherm(venster)
def ga_naar_avontuurmenu(venster):
    from avonturen.toon_avonturen_menu import toon_avonturen_menu
    toon_avonturen_menu(venster)


def ga_naar_karakter_menu_scherm(venster):
    maak_karakter_menu_scherm_aan(venster)


def maak_hoofdmenu_scherm_aan(venster):
    for widget in venster.winfo_children():
        widget.destroy()

    hoofdmenu_titel = Label(venster, text="Welkom, avonturier!", font=("Helvetica", 36))

    karakter_button = Button(text="Karakter Menu",width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command=lambda : ga_naar_karakter_menu_scherm(venster))

    avontuur_kiezen = Button(text="Avontuur Kiezen", width=BUTTON_WIDTH, height=BUTTON_HEIGHT,command=lambda : ga_naar_avontuurmenu(venster))

    admin_button = Button(text="Admin login", width= BUTTON_WIDTH, height=BUTTON_HEIGHT,command=lambda : ga_naar_admin_scherm(venster))



    original_image = Image.open("../images/rivendell.png")
    resized_image = original_image.resize((IMAGE_WIDTH, IMAGE_HEIGHT), Image.LANCZOS)
    voorbeeld_image = ImageTk.PhotoImage(resized_image)
    label_image = Label(venster, image=voorbeeld_image)
    label_image.image = voorbeeld_image
    label_image.tkraise()

    hoofdmenu_titel.pack()
    label_image.pack()
    karakter_button.pack()
    avontuur_kiezen.pack()
    admin_button.pack()


