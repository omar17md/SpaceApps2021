import urllib3
import json

def generar():
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://nasaapistellarbytes.azurewebsites.net/')
    s = json.loads(r.data)
    cadena = str(s)
    cadena = cadena.replace('\'', '"')
    arc = open('static/js/data.json', 'w')
    arc.write('data  = \'' + cadena  + '\';')
    arc.close()

def filtrar(id_norad):
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://nasaapistellarbytes.azurewebsites.net/id/' + str(id_norad))
    s = json.loads(r.data)
    cadena = str(s)
    cadena = cadena.replace('\'', '"')
    arc = open('static/js/dataf.json', 'w')
    arc.write('data1  = \'' + cadena  + '\';')
    arc.close()
