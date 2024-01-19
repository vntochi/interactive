from tkinter import Frame, Label, Button

from avonturen.eind_scherm import maak_eind_scherm_aan

def ga_naar_avonturen_start_scherm(venster, avontuur):
    maak_avontuur_scherm_aan(venster, avontuur)

def ga_naar_avonturen_menu_scherm(venster):
    from avonturen.toon_avonturen_menu import toon_avonturen_menu
    toon_avonturen_menu(venster)

def ga_naar_eind_scherm(venster, vragen_lijst, gemaakte_keuzes, avontuur):
    maak_eind_scherm_aan(venster, vragen_lijst, gemaakte_keuzes, avontuur)

def avontuur_uitlezen(avontuur_nummer):
    path = "../avonturen/avontuur" + avontuur_nummer + ".txt"
    with open(path, "r") as bestand:
        data = bestand.read()

    vragen_lijst = data.splitlines()

    vraag_dict_lijst = []
    for vraag in vragen_lijst:
        vraag_data = vraag.split(";")
        keuze_1 = vraag_data[2].split("^")
        keuze_2 = vraag_data[3].split("^")
        if len(vraag_data) - 2 < 3:
            vraag_dict = {
                "nummer": int(vraag_data[0]),
                "vraag": str(vraag_data[1]),
                "keuze_1": keuze_1,
                "keuze_2": keuze_2
            }
        else:
            keuze_3 = vraag_data[4].split("^")
            vraag_dict = {
                "nummer": int(vraag_data[0]),
                "vraag": str(vraag_data[1]),
                "keuze_1": keuze_1,
                "keuze_2": keuze_2,
                "keuze_3": keuze_3
            }
        vraag_dict_lijst.append(vraag_dict)

    return vraag_dict_lijst

def toon_vraag(venster, huidige_vraag, vragen_lijst, gemaakte_keuzes, avontuur):
    for widget in venster.winfo_children():
        widget.destroy()

    frame_terug_naar_avontuur_scherm = Frame(venster)
    frame_terug_naar_avontuur_scherm.pack()

    button_terug_naar_avontuur_scherm = Button(frame_terug_naar_avontuur_scherm, text="Terug naar avontuur scherm",
                                              width=30, height=2,
                                              command=lambda: ga_naar_avonturen_start_scherm(venster, avontuur))
    button_terug_naar_avontuur_scherm.pack()

    for vraag in vragen_lijst:
        if vraag["nummer"] == huidige_vraag:
            button_width = 50

            label_frame = Frame(venster)
            antwoorden_frame = Frame(label_frame)

            answer1_button = Button(antwoorden_frame, text=vraag["keuze_1"][1], width=button_width,
                                    command=lambda: volgende_vraag_tonen(venster, huidige_vraag, vragen_lijst, 1, gemaakte_keuzes, avontuur))
            answer1_button.grid(row=0, column=0, padx=20)

            answer2_button = Button(antwoorden_frame, text=vraag["keuze_2"][1], width=button_width,
                                    command=lambda: volgende_vraag_tonen(venster, huidige_vraag, vragen_lijst, 2, gemaakte_keuzes, avontuur))
            answer2_button.grid(row=0, column=1, padx=20)

            antwoorden_frame.pack()

            vraag_frame = Frame(label_frame)
            if len(vraag) - 2 >= 3:
                answer3_button = Button(antwoorden_frame, text=vraag["keuze_3"][1], width=button_width,
                                        command=lambda: volgende_vraag_tonen(venster, huidige_vraag, vragen_lijst, 3,
                                                                             gemaakte_keuzes, avontuur))
                answer3_button.grid(row=0, column=2, padx=20)

            vraag_label = Label(label_frame, text=vraag["vraag"], font="helvetica 12")
            vraag_label.pack(pady=20)

            vraag_frame.pack()

            label_frame.pack(expand=True)

def volgende_vraag_tonen(venster, huidige_vraag, vragen_lijst, gebruiker_keuze, gemaakte_keuzes, avontuur):
    for vraag in vragen_lijst:
        if huidige_vraag == vraag["nummer"]:
            keuze = "keuze_" + str(gebruiker_keuze)
            print(f"Jij koos: {vraag[keuze]}")

    gemaakte_keuzes.append(str(gebruiker_keuze))

    if huidige_vraag < len(vragen_lijst):
        huidige_vraag += 1
        toon_vraag(venster, huidige_vraag, vragen_lijst, gemaakte_keuzes, avontuur)
    else:
        print("End of the adventure!")
        print(gemaakte_keuzes)
        ga_naar_eind_scherm(venster, vragen_lijst, gemaakte_keuzes, avontuur)



def maak_avontuur_scherm_aan(venster, avontuur):
    gemaakte_keuzes = []
    vragen_lijst = avontuur_uitlezen(avontuur)
    huidige_vraag = 1
    for widget in venster.winfo_children():
        widget.destroy()

    welkom_text = ""
    if avontuur == "1":
        welkom_text = "welkom dit is avontuur: reis in de gouw"
    elif avontuur == "2":
        welkom_text = "welkom dit is avontuur: zoektocht zwaard elendil"
    elif avontuur == "3":
        welkom_text = "welkom dit is avontuur: queeste erebor"

    frame_terug_naar_avonturen_menu = Frame(venster)
    frame_terug_naar_avonturen_menu.pack()

    button_terug_naar_avonturen_menu = Button(frame_terug_naar_avonturen_menu, text="Terug naar avonturen menu", width=30, height=2,
                                          command=lambda: ga_naar_avonturen_menu_scherm(venster))
    button_terug_naar_avonturen_menu.pack()

    label_frame = Frame(venster)

    welkom_label = Label(label_frame, text=welkom_text, font="Helvetica 16")
    welkom_label.grid(row=0, column=0, columnspan=2, pady=20)

    start_button = Button(label_frame, text="Start Avontuur",
                          command=lambda: toon_vraag(venster, huidige_vraag, vragen_lijst, gemaakte_keuzes, avontuur))
    start_button.grid(row=1, column=0, columnspan=2)

    label_frame.pack(expand=True)

