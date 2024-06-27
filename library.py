import subprocess
import os

def run_keylogger():
    subprocess.run(["python", "keylogger.py"])

def run_scanner_port():
    subprocess.run(["python", "port_scanner.py"])

def run_venom():
    subprocess.run(["python", "venom_poison.py"])


def run_vision():
    subprocess.run(["python", "vision.py"])

def run_nuke():
    subprocess.run(["python", "nuke.py"])

def run_splinter_cell():
    subprocess.run(["python", "advanced_hacker.py"])

def run_legion():
    subprocess.run(["python", "legion.py"])

  #création du fichier rapport
def create_rapport(file_name, contenu):
   with open(file_name, "w") as file:
        file.write(contenu)
        
#ouvre le rapport
def open_rapport(file_name):
    os.startfile(file_name)







