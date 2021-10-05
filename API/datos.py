import requests
import pandas as pd
from skyfield.api import load, wgs84
from skyfield.api import EarthSatellite
from skyfield.api import datetime

def positions(line1, line2, name, norad):
  ts = load.timescale()
  t = ts.now()
  satellite = EarthSatellite(line1, line2, name, ts)
  geocentric = satellite.at(ts.now())
  subpoint = wgs84.subpoint(geocentric)
  latitude = subpoint.latitude.degrees
  longitude = subpoint.longitude.degrees
  elevation = subpoint.elevation.km
  return name, latitude, longitude, elevation, norad


#################################### Aqui van tus datos de acceso a Space-track.com
payload = {
    'identity': 'correo registrado en Space-track.com',
    'password': 'password asociado a la ciuenta'
}

# Solicitud de POST y GET
with requests.Session() as s:
    p = s.post('https://www.space-track.org/ajaxauth/login', data=payload)

    r = s.get('https://www.space-track.org/basicspacedata/query/class/gp/OBJECT_TYPE/DEBRIS/orderby/OBJECT_TYPE asc/limit/3500/emptyresult/show')
    json_data = r.json()
    data_normalized = pd.json_normalize(json_data)
    print(json_data)
    df_data = pd.DataFrame.from_dict(data_normalized)
    s.get('https://www.space-track.org/ajaxauth/logout')


posiciones = df_data.apply(lambda x: positions(x['TLE_LINE1'], x['TLE_LINE2'], x['OBJECT_NAME'], x['NORAD_CAT_ID']), axis=1)
datos_posicion = [{'name':x[0], 'latitude':x[1], 'longitude':x[2], 'elevation': x[3], 'norad':x[4]} for x in posiciones if str(x[1]) != 'nan']
