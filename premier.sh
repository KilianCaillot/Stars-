#!/bin/bash

# Chemin vers le répertoire contenant le script Python
SCRIPT_DIR="/chemin/vers/repertoire"

# Chemin complet vers le script Python
PYTHON_SCRIPT="$SCRIPT_DIR/calcul.py"

# Arguments pour le script Python
node_index = 0
toal_nodes = 1
total_threads = 1



# Exécuter le script Python avec les arguments
python3 $PYTHON_SCRIPT $node_index $total_nodes $total_threads 
