import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import library as mp
from mouse_hover import *
import csv
import random


def lire_csv_dicton():
    result = []
    with open('test.csv', encoding= 'utf8') as file:
        reader= csv.reader(file, delimiter= ';')
        i=0
        for row in reader:
            i+= 1
            result.append(row)
            my_str= "* ".join(row)
            result = my_str.split('*')       
    return result

def choose_random_dicton():
    dictons= lire_csv_dicton()
    nombre_dicton= len(dictons)
    nombre_aleatoire = random.randint(0, nombre_dicton -1)
    return dictons[nombre_aleatoire]


def switch_for_events_scripts(i:int):
    match i:
        case 0: 
            return mp.run_keylogger
        case 1:
            return mp.run_scanner_port
        case 2:
            return mp.run_venom
        case 3:
            return mp.run_vision
        case 4:
            return mp.run_splinter_cell
        case 5:
            return mp.run_nuke
        case 6:
            return mp.run_legion
        case _:
            return lambda: print("aucune fonction associé")

def switch_message_event(i:int):
     match i:
        case 0: 
            return """ Scripte capable d’enregistrer les touches sur la machine victime qui s'enregistre dans un fichier txt keylogger
            """
        case 1: 
            return """ analyse des ports en localhost selon la range donnée  """
        case 2:
            return """exemple de spoofing ARP (Address Resolution Protocol)
            , qui est une technique utilisée pour usurper l'identité d'un appareil sur un réseau local
            en envoyant des messages ARP falsifiés."""
        case 3:
            return """  Analyse les adresses IP et mac des terminaux dans le réseau local """
        case 4:
            return """
envoie  de commandes à distance et possibilité de télécharger des fichiers """
        case 5:
            return """ Ce script est conçu pour effectuer une attaque par force brute sur une page de connexion d'un site web   """
    
        case 6:
            return """ tentative de DDOS en envoyant des formulaires """
        case _:
             return " "

def create_button(new_window, i, text):
    button = tk.Button(new_window, text=text, command=switch_for_events_scripts(i))
    button.grid(row=i, column=0, pady=10, padx=10)
    
    label = tk.Label(new_window, text="")
    label.grid(row=i, column=1, pady=10, padx=10)
    button.bind("<Enter>", lambda event, my_t=switch_message_event(i), l=label: l.configure(text=my_t))
    button.bind("<Leave>", lambda event, l=label: l.configure(text=""))

# Fonction appelée lorsque le bouton "Attaquant" (鬼) est cliqué
def fantome_mode():
    messagebox.showinfo("Sélection", "Vous avez choisi d'être un fantome!")
    open_new_menu()

# Fonction appelée lorsque le bouton "Défenseur" (保护) est cliqué
def guardian_mode():
    messagebox.showinfo("Sélection", "Vous avez choisi d'être un gardien!")

# Ouvrir un nouveau menu avec 7 boutons
def open_new_menu():
    new_window = tk.Toplevel(root)
    new_window.title("Nouveau Menu")
    new_window.geometry("400x400")
    
    boutton_menu = [
        "keylogger", "port_ouvert", "Venom",
        "vision", "splinter cell", "nuke", "legion"
    ]

    for i, text in enumerate(boutton_menu):
        create_button(new_window, i, text)
        new_window.grid_rowconfigure(i, minsize=80)


def on_closing():
    messagebox.showinfo("wise:", choose_random_dicton())
    root.destroy()



# Créer la fenêtre principale
root = tk.Tk()
root.title("Soul Unity")
root.protocol("WM_DELETE_WINDOW", on_closing)

# Charger l'image de fond
image_path = "soul_unity_background.jpg"  # Assurez-vous que cette image est dans le même répertoire que ce script
image = Image.open(image_path)
background_image = ImageTk.PhotoImage(image)

# Créer un canvas pour afficher l'image de fond
canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.pack(fill="both", expand=True)

# Afficher l'image de fond sur le canvas
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Afficher le message de bienvenue sur le canvas avec une police plus petite et largeur maximale
welcome_message = canvas.create_text(image.width // 2, 75, text="Bienvenue dans la Soul Unity. Voulez-vous être le fantome ou le gardien ?", fill="black", font=('Helvetica', 12, 'bold'), width=image.width - 40)

# Créer les boutons
mode1 = tk.Button(root, text="鬼", command=fantome_mode, bg="black", fg="white")
mode2 = tk.Button(root, text="保护", command=guardian_mode, bg="white", fg="black")

# Ajouter les boutons sur le canvas, en les plaçant plus bas
id_mode1 = canvas.create_window(image.width // 2, image.height - 100, anchor="n", window=mode1)
id_mode2 = canvas.create_window(image.width // 2, image.height - 50, anchor="n", window=mode2)

# Lancer la boucle principale de Tkinter
root.mainloop()

