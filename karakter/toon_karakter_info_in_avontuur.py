# deze functie toont welk karakter je speel, en zijn/haar info, tijdens je avontuur
from tkinter import Frame, LEFT, Label

import tkinter as tk

def toon_karakter_info(frame, filepath):
    # Read the characters from the text file
    characters = []
    with open(filepath, 'r') as file:
        for line in file:
            name, race, skill = line.strip().split(';')
            characters.append((name, race, skill))

    # Display the characters in a tkinter Label within the provided frame
    for i, (name, race, skill) in enumerate(characters):
        character_label = tk.Label(frame, text=f"{name} ({race}) - Skill: {skill}")
        character_label.grid(row=i, column=0, sticky='w')



# dit is code snippet die geplaatst kan worden in alle avontuur schermen om het karakter te tonen in een kleine frame, op losse labels
import tkinter as tk
from toon_karakter_info_in_avontuur import toon_karakter_info

# Create the main tkinter window
root = tk.Tk()
root.title("Main Window")

# Create a frame to display characters
character_frame = tk.Frame(root)
character_frame.pack(padx=10, pady=10)

# Call the function and provide the path to your text file and the character frame
toon_karakter_info(character_frame, "../karakter/geselecteerd_karakter.txt")  # Replace with your file path

# Your other tkinter components and main loop here
root.mainloop()