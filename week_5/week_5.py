

import json
 
nationality_data = {}

with open('Artworks.json', 'r') as file:
     json_file = json.load(file)
     for artwork in json_file:
      nationalities = artwork['Nationality']
      for nat in nationalities:
         if nat in nationality_data:
            nationality_data[nat].append(artwork)
         else:
            nationality_data[nat] = []
            nationality_data[nat].append(artwork)

for nat in nationality_data:
   with open(f'res/{nat}.json', 'w') as out_file:
      json.dump(nationality_data[nat], out_file, indent=2)
