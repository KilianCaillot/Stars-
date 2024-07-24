#!/bin/bash

# Mettre à jour la liste des paquets disponibles
sudo apt-get update

# Installer Python3 et pip3
sudo apt-get install -y python3 python3-pip

# Installer les packages Python nécessaires
pip3 install numpy pandas
