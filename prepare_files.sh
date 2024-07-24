#!/bin/bash

# Directory to store files 

DIRECTORY="fichiers"
HELLO="resultats"

# Create the directory if it doesn't exist 

if [ ! -d "./nfs/$DIRECTORY" ]; then
  # Si le répertoire n'existe pas, le créer
  mkdir -p ./nfs/"$DIRECTORY"
  echo "Le répertoire $DIRECTORY a été créé."
else
  echo "Le répertoire $DIRECTORY existe déjà."
fi

if [ ! -d "./nfs/$HELLO" ]; then
  # Si le répertoire n'existe pas, le créer
  mkdir -p ./nfs/"$HELLO"
  echo "Le répertoire $HELLO a été créé."
else
  echo "Le répertoire $HELLO existe déjà."
fi


# Create 100 files with values from 1 to 100

if [ ! -d "./nfs/$DIRECTORY" ]; then
  for i in $(seq 1 100); do
    echo $i > ./nfs/fichiers/$i.txt
  done
  echo "Le répertoire $DIRECTORY a été modifié."
else
  echo "Le répertoire $DIRECTORY a déjà été modifé."
fi

