from tkinter import Label, Button, Tk, Entry, Toplevel

import configparser

authentication_status = False
config = configparser.ConfigParser()

def print_naar_console():
    welkom_admin_label["text"] = "Welkom admin!"
    config['AUTHENTICATION'] = {'authenticated': 'True'}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def open_password_window(venster):
    password_window = Toplevel(venster)
    password_window.title("Admin")

    password_label = Label(password_window, text="Voer wachtwoord in:")
    password_entry = Entry(password_window, show="*")
    submit_button = Button(password_window, text="Indienen",
                           command=lambda: check_password(password_entry.get(), password_window))

    password_label.pack()
    password_entry.pack()
    submit_button.pack()

def check_password(password, window):
    global authentication_status
    if password == "admin":  # Hier kan je het ww aanamaken!!
        window.destroy()
        authentication_status = True
        print_naar_console()
    else:
        print("Fout wachtwoord")


def maak_admin_scherm(venster):
    global welkom_admin_label
    welkom_admin_label = Label(venster, text="")

    def on_admin_button_click():
        if not authentication_status:
            open_password_window(venster)
        else:
            password_button.destroy()

    password_button = Button(venster, text="admin modus", command=on_admin_button_click)
    welkom_admin_label.pack()


    venster.mainloop()

