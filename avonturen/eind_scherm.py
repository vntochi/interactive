from tkinter import Label, Frame, Button


def einde_uitlezen(avontuur_nummer):
    path = "../avonturen/eindes" + avontuur_nummer + ".txt"
    with open(path, "r") as bestand:
        data = bestand.read()

    eindes_lijst = data.splitlines()

    return eindes_lijst


def ga_naar_avonturen_menu_scherm(venster):
    from avonturen.toon_avonturen_menu import toon_avonturen_menu
    toon_avonturen_menu(venster)

def maak_eind_scherm_aan(venster, vragen_lijst, gemaakte_keuzes, avontuur):
    for widget in venster.winfo_children():
        widget.destroy()

    eindes_lijst = einde_uitlezen(avontuur)

    keuze_dict_list = []
    for teller in range(len(vragen_lijst)):
        for keuze in gemaakte_keuzes[teller]:
            vraag_keuze = "keuze_" + keuze
            vraag = vragen_lijst[teller]
            values = vraag[vraag_keuze][0]
            keuze_dict_list.append(values)

    aantal_goed = keuze_dict_list.count("goed")
    aantal_slecht = keuze_dict_list.count("slecht")

    frame_terug_naar_avonturen_menu = Frame(venster)
    frame_terug_naar_avonturen_menu.pack()

    button_terug_naar_avonturen_menu = Button(frame_terug_naar_avonturen_menu, text="Terug naar avonturen menu",
                                              width=30, height=2,
                                              command=lambda: ga_naar_avonturen_menu_scherm(venster))
    button_terug_naar_avonturen_menu.pack()

    label_frame = Frame(venster)

    if aantal_goed >= 5:
        einde_label = Label(label_frame, text="Goed einde", font="helvetica 20")
        einde_label.pack(pady=20)
        vraag_label = Label(label_frame, text=eindes_lijst[0], font="helvetica 12")
        vraag_label.pack(pady=20)
    else:
        einde_label = Label(label_frame, text="Slecht einde", font="helvetica 20")
        einde_label.pack(pady=20)
        vraag_label = Label(label_frame, text=eindes_lijst[1], font="helvetica 12")
        vraag_label.pack(pady=20)

    label_frame.pack(expand=True)
