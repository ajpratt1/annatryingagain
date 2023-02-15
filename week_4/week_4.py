import csv

nationality_writers = {}

with open('Artworks.csv') as file:
    processed_csv = csv.reader(file)
    header_row = next(processed_csv,None)
    for row in processed_csv:
        nationalities_str = row[4]
        nationalities = nationalities_str.split(' ')
        for nat in nationalities:
            if nat in nationality_writers:
                nationality_writers[nat]['csv'].writerow(row)
            else:
                nat_file = open(f'res/{nat}.csv', 'w')
                nat_csv = csv.writer(nat_file)
                nat_csv.writerow(header_row)
                nat_csv.writerow(row)
                nationality_writers[nat] = {
                    'file': nat_file,
                    'csv': nat_csv
                }
for files in nationality_writers:
    nationality_writers[files]['file'].close()