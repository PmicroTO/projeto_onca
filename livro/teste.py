import csv

bib = open('biblioteca.csv', 'r')
bib_rows = csv.reader(bib)
for row in bib_rows:
    last_cod = row[0].strip("''")
bib.close

print(last_cod)
