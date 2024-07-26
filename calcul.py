import sys
import os
from src.preprocess_fits import preprocess_fits  # Assurez-vous que l'importation est correcte

def process_file(file_index, total_nodes):
    fits_dir = "./nfs/fichiers"
    result_dir = "./nfs/resultats"

    # Vérifier et créer le répertoire result_dir s'il n'existe pas
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
        print(f"Le répertoire {result_dir} a été créé.")

    # Calculer les indices de départ et de fin pour chaque nœud
    start_index = (file_index * 100) // total_nodes + 1
    end_index = ((file_index + 1) * 100) // total_nodes

    for i in range(start_index, end_index + 1):
        file_path = os.path.join(fits_dir, f"{i}.txt")
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                value = int(file.read().strip())
            result = value + i
            result_path = os.path.join(result_dir, f"{i}.txt")
            with open(result_path, 'w') as result_file:
                result_file.write(str(result))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python calcul.py <node_index> <total_nodes>")
        sys.exit(1)

    node_index = 0
    total_nodes = 1
    
    process_file(node_index, total_nodes)
