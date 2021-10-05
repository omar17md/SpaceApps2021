# SpaceApps2021 -  Stellar - Bytes 🛰 
<img src="https://github.com/omar17md/SpaceApps2021/blob/main/img/logos/Logo_StellerBytes.png?raw=true">

# Tracking space debris in real time


## Integrantes:

    * Castillo Pérez Brian
    * Castro Sam Maria Magdalena
    * Jesús Omar Magaña Medina
    * Verdugo Domínguez Jesus Abdiel

[Application Link](https://appchallengestellar.azurewebsites.net/) 


## Documentacion de la API

### Descripción
Nuestra API toma los datos de la página [Space-Track](https://www.space-track.org/) que contienen informacion general de la basura espacial o tambien llamada Debris, sin embargo estos datos no nos sirve para graficar los en un globlo terraqueo virtual, para eso se ocupa coordenadas geograficas, el endpoint de nuestra API retorna estas coordenadas geograficas junto con el nombre y el NORAD ID(numero de objeto de la NASA) de todos los datos que se extraen de la página [Space-Track](https://www.space-track.org/), los datos son retornados en un formato tipo JSON.

Endpoint = https://nasaapistellarbytes.azurewebsites.net/ ➡️ Retornara todos los datos en formato JSON

## Buscar un objeto en particular
Tambien podemos buscar un objeto en especial, ya sea por su NORAD ID o su nombre, sin embargo utilizar uno o el otro traen diferentes resultados, por ejemplo si usas el NORAD ID solo te traera el objeto relacionado a ese ID, si usas el nombre te traera todos los objetos relacionados a ese nombre.
Esto se debe a que un Debris se puede dividir en varios pedazos debido a choques con otros Debris

Para realizar la consulta simpletemente usa este link:
https://nasaapistellarbytes.azurewebsites.net/id/xxxxx ➡️ Retornara el objeto relacionado al numero xxxxxx en formato JSON
https://nasaapistellarbytes.azurewebsites.net/id/nombre ➡️ Retornara los objetos relacionados al nombre en formato JSON


## Ejemplos
https://nasaapistellarbytes.azurewebsites.net/id/49251 ➡️ Retorna los datos del objeto con el NORAD ID 49251
https://nasaapistellarbytes.azurewebsites.net/id/SZ-12%20MODULE%20DEB ➡️ Retorna los datos del objeto con el nombre SZ-12 MODULE DEB
 
