#!/bin/bash

# Définir les répertoires d'entrée et de sortie
INPUT_DIR="./fichiers"
OUTPUT_DIR="./resultats" 

node_index = 0
total_nodes = 4 
total_threads = 64

# Activer l'environnement virtuel Python si nécessaire
# source venv/bin/activate

# Exécuter le script principal Python avec le nombre de threads spécifié
python3 calcul.py --node_index $node_index --total_nodes $total_nodes --total_threads $total_threads 

# Désactiver l'environnement virtuel si nécessaire
# deactivate

# Notifier l'utilisateur que le processus est terminé
echo "Traitement des fichiers FITS terminé. Les spectres extraits sont enregistrés dans $OUTPUT_DIR."
