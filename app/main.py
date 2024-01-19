
from tkinter import Tk
from muziek import achtergrond_muziek
from app.splash_scherm import maak_splash_scherm_aan


def main():


    # maak venster aan
    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.title("Lord of the Rings Game")
    root.geometry("%dx%d" % (width, height))

    achtergrond_muziek.speel_achtergrond_muziek()

    # Begin met splash scherm
    maak_splash_scherm_aan(root)

    root.mainloop()


if __name__ == '__main__':
    main()

