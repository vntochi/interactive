
from tkinter import Frame, Label, PhotoImage

from PIL import ImageTk, Image

from app.hoofdmenu import maak_hoofdmenu_scherm_aan


def ga_naar_hoofdmenu_scherm(venster):
    maak_hoofdmenu_scherm_aan(venster)


def maak_splash_scherm_aan(venster):
    for widget in venster.winfo_children():
        widget.destroy()


    frame = Frame(venster, height=venster.winfo_screenheight(), width=venster.winfo_screenwidth())
    frame.bind("<Button-1>", lambda click_event: ga_naar_hoofdmenu_scherm(venster))

    splash_scherm_titel = Label(venster, text="Splash menu", font=("Helvetica", 36))
    splash_scherm_titel.bind("<Button-1>", lambda click_event: ga_naar_hoofdmenu_scherm(venster))
    splash_scherm_titel.tkraise()

    original_image = Image.open("../images/schippi.png")
    resized_image = original_image.resize((400, 400), Image.LANCZOS)
    voorbeeld_image = ImageTk.PhotoImage(resized_image)

    label_image = Label(venster, image=voorbeeld_image)
    label_image.image = voorbeeld_image
    label_image.bind("<Button-1>", lambda click_event: ga_naar_hoofdmenu_scherm(venster))
    label_image.tkraise()

    frame.grid(row=0, column=0)
    label_image.grid(row=0, column=0)
    splash_scherm_titel.grid(row=0, column=0)

