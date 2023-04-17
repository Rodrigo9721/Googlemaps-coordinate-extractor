import requests
import json

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

url = 'https://progresol.com/' ## Looks like this page is down as of 17/05/2023
resp = requests.get(url,headers=headers)

start = 'allTiendasPdv = '
end = 'allTiendasPdv = allTiendasPdv.filter'

s = resp.text
dirty_json = s[s.find(start)+len(start):s.rfind(end)].strip() #get the json out the html
dirty_json = dirty_json[:-1]

clean_json = json.loads(dirty_json)

dict = {}
for i in range(len(clean_json)):
    dict[clean_json[i]['NombreComercial']] = {k: clean_json[i][k] for k in ('Longitud', 'Latitud', 'Direccion', 'Provincia', 'Distrito')}


print(dict)

with open('progresol.json', 'w', encoding='UTF-8') as _file:
    json.dump(dict, _file, ensure_ascii=True, indent=3)