import urllib3
import json

def generar():
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://apinasa2021.azurewebsites.net/')
    s = json.loads(r.data)
    cadena = str(s)
    cadena = cadena.replace('\'', '"')
    arc = open('static/js/data.json', 'w')
    arc.write('data  = \'' + cadena  + '\';')
    arc.close()