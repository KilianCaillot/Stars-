mport sys
import os

def process_file(file_index, total_nodes):
    fits_dir = "./fichiers"
    result_dir = "./resultats"
   

    start_index = (file_index * 100) // total_nodes + 1
    end_index = ((file_index + 1) * 100) // total_nodes

    for i in range(start_index, end_index + 1):
        file_path = os.path.join(fits_dir, f"{i}.txt")
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

    node_index = int(sys.argv[1])
    total_nodes = int(sys.argv[2])
    process_file(node_index, total_nodes)
