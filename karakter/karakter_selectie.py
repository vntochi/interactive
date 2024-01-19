# functie die hoort bij het karakter selectie menu en verwijsd naar de dictionary van opgeslagen karakters
from tkinter import Frame, Listbox, Scrollbar, Label, Button, messagebox
import os

# roept functie aan om terug te keren naar het karaktermenu
def ga_naar_karaktermenu(venster):
    from karakter.karakter_menu import maak_karakter_menu_scherm_aan
    maak_karakter_menu_scherm_aan(venster)

# roept functie aan om terug te keren naar het hoofdmenu
def ga_naar_hoofdmenu(venster):
    from app.hoofdmenu import maak_hoofdmenu_scherm_aan
    maak_hoofdmenu_scherm_aan(venster)

# maakt het venster voor karakter selectie aan
def maak_karakter_selectie_scherm_aan(venster):
    for widget in venster.winfo_children():
        widget.destroy()

    # pakt karakters uit de textfile met gecreeerde karakters
    def lees_karakters_uit_bestand():
        karakters = []
        try:
            with open("../karakter/opgeslagen_karakters.txt", "r") as bestand:
                for line in bestand:
                    parts = line.strip().split(";")
                    lengte_karakter_info = 3
                    if len(parts) == lengte_karakter_info:
                        naam, ras, speciale_eigenschap = parts
                        karakters.append({"naam": naam, "ras": ras, "speciale_eigenschap": speciale_eigenschap})
        except FileNotFoundError as e:
            print(f"Error: {e}")
        return karakters

    # titel plaatsing
    title_frame = Frame(venster, pady=20)
    title_frame.pack(side="top", fill="both")

    # label voor karakter selectie
    karakter_selectie_titel = Label(venster, text="Karakter Selectie", font=("Helvetica", 36))
    karakter_selectie_titel.pack(side="top", pady=20)

    # knop naar hoofdmenu
    terug_button_hoofd_menu = Button(venster, text="Terug naar hoofdmenu", command=lambda: ga_naar_hoofdmenu(venster), width=20, height=2)
    terug_button_hoofd_menu.pack()

    # knop naar karakter menu
    terug_button_karakter_menu = Button(venster, text="Terug naar karakter menu", command=lambda: ga_naar_karaktermenu(venster), width=20, height=2)
    terug_button_karakter_menu.pack()

    class KarakterViewer:
        def __init__(self, opgeslagen_karakters):
            self.opgeslagen_karakters = opgeslagen_karakters
            self.karakters = lees_karakters_uit_bestand()
            print("Loaded characters", self.karakters)

            # frame voor listbox, scrollbar, en button
            frame = Frame(venster)
            frame.pack(fill="both")

            # listbox met scrollbar
            self.listbox = Listbox(frame, selectmode="SINGLE", width=100)
            self.scrollbar = Scrollbar(frame, command=self.listbox.yview)
            self.listbox.config(yscrollcommand=self.scrollbar.set)

            # grid zetten
            self.listbox.grid(row=0, column=1, sticky="nsew")
            self.scrollbar.grid(row=0, column=2, sticky="ns")

            # karakters laden in listbox met naam, ras, eigenschap
            for karakter in self.karakters:
                item_text = f"{karakter['naam']}, {karakter['ras']}, {karakter['speciale_eigenschap']}"
                self.listbox.insert("end", item_text)

            # opslaan knop
            self.opslaan_button = Button(frame, text="Sla karakter op", command=self.opslaan_karakter)
            self.opslaan_button.grid(row=1, column=1, columnspan=2, pady=10)

            # grid kolommen aanpassen
            frame.grid_columnconfigure(0, weight=1)
            frame.grid_columnconfigure(3, weight=1)

            # listbox selectie binden
            self.listbox.bind('<<ListboxSelect>>', self.on_select)

        def on_select(self, event):
            selected_index = self.listbox.curselection()
            if selected_index:
                selected_item = self.listbox.get(selected_index)
                selected_item = selected_item.split(",")[0]
                karakter = self.zoek_karakter_met_naam(selected_item[0])


        def zoek_karakter_met_naam(self, naam):
            for karakter in self.karakters:
                if karakter["naam"] == naam:
                    return karakter

        def opslaan_karakter(self):
            selected_index = self.listbox.curselection()
            if selected_index:
                selected_item = self.listbox.get(selected_index)

                # pakt de directory van het script
                current_directory = os.path.dirname(__file__)

                # maakt file path
                karakter_file_path = os.path.join(current_directory, "geselecteerd_karakter.txt")

                with open(karakter_file_path, "w") as selected_file:
                    selected_file.write(selected_item.replace(",", ";") + "\n")
                messagebox.showinfo("Karakter opgeslagen", "Karakter is opgeslagen voor je avontuur!")
            else:
                print("No character selected.")

        # def opslaan_karakter(self):
        #     selected_index = self.listbox.curselection()
        #     if selected_index:
        #         selected_item = self.listbox.get(selected_index)
        #         with open("geselecteerd_karakter.txt", "w") as selected_file:
        #             selected_file.write(selected_item.replace(",", ";") + "\n")
        #         messagebox.showinfo("Karakter opgeslagen", "Karakter is opgeslagen voor je avontuur!")
        #
        #     else:
        #         print("No character selected.")

    # hier moet de kloppende file path voor opgeslagen_karakters komen
    karakter_viewer = KarakterViewer("opgeslagen_karakters.txt")


