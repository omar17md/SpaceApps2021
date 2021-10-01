import requests
import pandas as pd

# Aqui van tus datos de acceso a Space-track.com
payload = {
    'identity': 'TU CORREO AQUI',
    'password': 'PASSWORD AQUI'
}

# Solicitud de POST y GET
with requests.Session() as s:
    p = s.post('https://www.space-track.org/ajaxauth/login', data=payload)

    r = s.get('https://www.space-track.org/basicspacedata/query/class/gp/OBJECT_TYPE/DEBRIS/orderby/OBJECT_TYPE asc/emptyresult/show')
    json_data = r.json()
    data_normalized = pd.json_normalize(json_data)
    df_data = pd.DataFrame.from_dict(data_normalized)
    s.get('https://www.space-track.org/ajaxauth/logout')
    df_data.head()
