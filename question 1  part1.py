import csv


csv_filename = "my_file.csv"

with open(csv_filename, 'r') as f:
    
    #for row in csv.DictReader(f):
    #    print(row)
        
    for line in csv.reader(f):
            print(line)
       