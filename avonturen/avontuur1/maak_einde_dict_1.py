def maak_einde_dict_1():
    with open("../eindes1.txt", "r") as bestand:
        data = bestand.read()
        eindes_1_list = data.splitlines()
        eindes_dict = {
            "goed_einde": eindes_1_list[0].replace(". ", ".\n"),
            "slecht_einde": eindes_1_list[1].replace(". ", ".\n").replace(", ", ",\n")
        }

        return eindes_dict

