import csv


csv_filename = "my_file.csv"

with open(csv_filename, 'r') as f:
    
    for row in csv.DictReader(f): # to open as a dictionary
        print(row)
        
with open(csv_filename, 'r') as f:        
    for line in csv.reader(f):  # to open as a list
            print(line)
       
    