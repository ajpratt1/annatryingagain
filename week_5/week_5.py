# import json

# nationality_writers = {}

# with open('Artworks.json') as file:
#     processed_json = json.load(file)
#     header_row = next(processed_json,None)
#     for row in processed_json:
#         nationalities_str = row[4]
#         nationalities = nationalities_str.split(' ')
#         for nat in nationalities:
#             if nat in nationality_writers:
#                 nationality_writers[nat]['json'].write
#                 nat_file = open(f'res/{nat}.json', 'w')
#                 nat_json = json.writer(nat_file)
#                 nat_json.writerow(header_row)
#                 nat_json.writerow(row)
#                 nationality_writers[nat] = {
#                     'file': nat_file,
#                     'csv': nat_json
#                 }
# for files in nationality_writers:
#     nationality_writers[files]['file'].close()

# import json

# f = open('Artworks.json')

# data = json.loads(f.read())

# for i in data['Nationality']:
#     print(i)

import json
 
# Opening JSON file
result = []
with open('Artworks.json', 'r') as file:
     json_file= json.load(file)
     for nat in json_file:
        nationality = (nat['Nationality'])