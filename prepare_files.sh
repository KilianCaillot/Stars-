#!/bin/bash

# Directory to store files
FILESDIR="./fichiers"

# Create the directory if it doesn't exist


# Create 100 files with values from 1 to 100
for i in $(seq 1 100); do
  echo $i > fichiers/$i.txt
done
