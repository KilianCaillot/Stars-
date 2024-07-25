import os

# Spécifiez le répertoire et le nom du fichier
repertoire = './nfs/resultats'
nom_fichier = 'hello.txt'
chemin_fichier = os.path.join(repertoire, nom_fichier)

# Créez le répertoire s'il n'existe pas
if not os.path.exists(repertoire):
    os.makedirs(repertoire)
    print(f"Le répertoire {repertoire} a été créé.")

# Créez le fichier hello.txt avec un message
with open(chemin_fichier, 'w') as fichier:
    fichier.write("Hello, World!")
    print(f"Le fichier {chemin_fichier} a été créé avec succès.")
