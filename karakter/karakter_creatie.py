from tkinter import Label, Entry, Frame, Listbox, StringVar, Button, messagebox
from tkinter.ttk import Style, Radiobutton


def karakter_opslaan_confirmatie(naam_karakter, gekozen_ras, lijst_eigenschappen):
    listbox_selection = lijst_eigenschappen.curselection()
    print(listbox_selection[0])
    selected_index = listbox_selection[0]
    eigenschap = lijst_eigenschappen.get(selected_index)

    gekozen_naam = naam_karakter.get()
    ras = gekozen_ras.get()
    if gekozen_naam != "" and len(listbox_selection) > 0 and ras != "":
        messagebox.askquestion("Karakter opslaan", "Weet je zeker?")
        compleet_gekozen_karakter_opslaan(gekozen_naam, ras, eigenschap)
    else:
        messagebox.showwarning("Iets niet ingevuld", "Er is iets niet ingevuld")


def compleet_gekozen_karakter_opslaan(gekozen_naam, ras, eigenschap):
    compleet_gekozen_karakter_van_gebruiker = f"{gekozen_naam};{ras};{eigenschap}\n"
    with open("../karakter/opgeslagen_karakters.txt", "a") as opslaan_bestand:
        opslaan_bestand.write(compleet_gekozen_karakter_van_gebruiker)


def ga_naar_karaktermenu(venster):
    from karakter.karakter_menu import maak_karakter_menu_scherm_aan
    maak_karakter_menu_scherm_aan(venster)


def maken_karakter(keuze_ras, welke_knop):
    keuze_ras["text"] = (f"Je gekozen ras is {welke_knop}\n\n"
                         f"Kies een eigenschap")


def toon_eigenschappen(lijst_eigenschappen, geselecteerd_ras, ras_dict_lijst):
    lijst_eigenschappen.delete(first=0, last="end")
    for ras in ras_dict_lijst:
        if ras["naam"] == geselecteerd_ras:
            eigenschappen_lijst = ras["eigenschappen"]
            for eigenschap_positie in range(len(eigenschappen_lijst)):
                eigenschap_value = eigenschappen_lijst[eigenschap_positie]
                lijst_eigenschappen.insert(eigenschap_positie, eigenschap_value)


def karakter_kiezen(keuze_ras, geselecteerd_ras, lijst_eigenschappen, ras_dict_lijst):

    toon_eigenschappen(lijst_eigenschappen, geselecteerd_ras, ras_dict_lijst)
    # tonen_ras_images(frame_rechts, geselecteerd_ras, ras_dict_lijst)
    maken_karakter(keuze_ras, geselecteerd_ras)


def maak_karakter_creatie_scherm_aan(venster):

    for widget in venster.winfo_children():
        widget.destroy()

    with open("../karakter/rassen.txt", "r") as bestand:
        data = bestand.read()
    ras_lijst = data.splitlines()

    ras_dict_lijst = []
    for ras in ras_lijst:
        ras_data = ras.split(";")
        eigenschappen_lijst = ras_data[1].split(",")

        ras_dict = {
            "naam": ras_data[0],
            "eigenschappen": eigenschappen_lijst
        }
        ras_dict_lijst.append(ras_dict)

    karakter_selectie_titel = Label(venster, text="karakter creëren", font=("Helvetica", 36))

    frame_links = Frame(venster, highlightbackground="black", highlightthickness=1)
    # frame_rechts = Frame(venster, bg="red")

    # Initialisatie linker frame
    hoofdlabel = Label(frame_links, text="Maak je eigen karakter!", font=30)
    labbel_rassen = Label(frame_links, text="Kies een ras!", font=30)

    # Veriabele geselecteerde ras voor het creeren eigen karakter
    ras = StringVar()
    gekozen_ras = ras

    style = Style()
    style.map("design1.Toolbutton",
              background=[('selected', 'yellow'), ('active', 'black'), ('!disabled', 'yellow')],
              foreground=[('selected', 'black  '), ('active', 'black'), ('!disabled', 'black')])

    mens_button = Radiobutton(frame_links, text="Mens", variable=ras, value="mens", style="design1.Toolbutton",
                              command=lambda: karakter_kiezen(keuze_ras, "mens", lijst_eigenschappen,
                                                              ras_dict_lijst))

    dwerg_button = Radiobutton(frame_links, text="Dwerg", variable=ras, value="dwerg", style="design1.Toolbutton",
                               command=lambda: karakter_kiezen(keuze_ras, "dwerg", lijst_eigenschappen,
                                                               ras_dict_lijst))

    hobbit_button = Radiobutton(frame_links, text="Hobbit", variable=ras, value="hobbit", style="design1.Toolbutton",
                                command=lambda: karakter_kiezen(keuze_ras, "hobbit", lijst_eigenschappen,
                                                                ras_dict_lijst))

    elf_button = Radiobutton(frame_links, text="Elf", variable=ras, value="elf", style="design1.Toolbutton",
                             command=lambda: karakter_kiezen(keuze_ras, "elf", lijst_eigenschappen,
                                                             ras_dict_lijst))

    raskeuze_frame = Frame(frame_links)
    naamkeuze_frame = Frame(frame_links)

    keuze_ras = Label(raskeuze_frame, text="\n\n")
    lijst_eigenschappen = Listbox(raskeuze_frame)
    # listbox_selection = lijst_eigenschappen.curselection()

    label_naam = Label(naamkeuze_frame, text="Geef je karakter een naam")
    naam_karakter = Entry(naamkeuze_frame)

    opslaan_button = Button(naamkeuze_frame, text="Opslaan", width=20, height=2, command=lambda:
                            karakter_opslaan_confirmatie(naam_karakter, gekozen_ras, lijst_eigenschappen))

    karakter_selectie_titel.pack()

    frame_links.pack(side="left", expand=True)
    # frame_rechts.pack(side="right")

    # Positionering linker frame children
    hoofdlabel.grid(row=0, columnspan=2, pady=10)
    labbel_rassen.grid(row=1, columnspan=2, pady=10)

    mens_button.grid(row=2, column=0, padx=20)

    dwerg_button.grid(row=2, column=1, padx=20)

    hobbit_button.grid(row=3, column=0, padx=20)

    elf_button.grid(row=3, column=1, padx=20)

    raskeuze_frame.grid(row=4, column=0)
    naamkeuze_frame.grid(row=4, column=1)

    keuze_ras.pack()

    lijst_eigenschappen.pack()
    label_naam.pack()
    naam_karakter.pack()
    opslaan_button.pack(pady=20)

    terug_button = Button(text="Terug naar karakter menu", width=20, height=2, command=lambda:
                          ga_naar_karaktermenu(venster))
    terug_button.pack()
