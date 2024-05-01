import os
import csv

# Read phrases from the CSV file using utf-8-sig encoding
with open("remove.txt", 'r', encoding='utf-8-sig') as f:
    phrases = [row[0] for row in csv.reader(f)]

# Get all files in the directory and its subdirectories
for root, _, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(('.js', '.css', '.html')):
            filepath = os.path.join(root, file)
            # Read file contents
            with open(filepath, 'r', encoding='utf-8-sig') as f:
                lines = f.readlines()
            # Remove phrases from file contents
            with open(filepath, 'w', encoding='utf-8-sig') as f:
                for line in lines:
                    for phrase in phrases:
                        line = line.replace(phrase, '')
                    f.write(line)

print("Phrases removed successfully from files.")
