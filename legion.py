import mechanize

url = "http://httpbin.org/forms/post"
browser = mechanize.Browser()

# Désactiver la vérification de robots.txt
browser.set_handle_robots(False)

# Ajouter des en-têtes pour imiter un navigateur réel
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')]

attacknumber = 1

# Créer un fichier de test avec des vecteurs d'attaque
with open('attack-vector.txt', 'w') as f:
    f.write("test1\n")
    f.write("test2\n")
    f.write("test3\n")

# Lire les vecteurs d'attaque
with open('attack-vector.txt', 'r') as f:
    for line in f:
        browser.open(url)
        # Sélectionner le formulaire
        try:
            browser.select_form(nr=0)
        except mechanize.FormNotFoundError:
            print("Form not found on the page.")
            continue

        # Remplir le formulaire avec les données du vecteur d'attaque
        browser["custname"] = line.strip()  # Remplacer 'custname' par le nom réel du champ
        browser["custtel"] = "1234567890"  # Ajouter des données fictives pour les autres champs
        browser["custemail"] = "test@example.com"
        browser["delivery"] = "20:00"
        browser["comments"] = "Test comment"
        
        res = browser.submit()
        content = res.read()
        
        # Écrire la réponse dans un fichier
        with open(f'response_{attacknumber}.txt', 'w') as output:
            output.write(content.decode('utf-8'))
        
        print(f"Attack number {attacknumber} submitted.")
        attacknumber += 1
