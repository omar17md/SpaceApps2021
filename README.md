# SpaceApps2021 -  Stellar - Bytes 🛰 
<img src="https://github.com/omar17md/SpaceApps2021/blob/3d0b8dff8ecc7519e090fd67fc44444826ab82d9/img/logos/Logo_bebe.png">

# Tracking space debris in real time


## Integrantes:

    * Castillo Pérez Brian
    * Castro Sam Maria Magdalena
    * Jesús Omar Magaña Medina
    * Verdugo Domínguez Jesus Abdiel

[Application Link](https://appchallengestellar.azurewebsites.net/) 


## Documentacion de la API

### Description
Our API takes data from the page Space-Track, it contains general information about space debris, but these data are not useful to plot their position in WorldWind Web page because we need geographic coordinates to plot them. The API’s endpoint returns these geographic coordinates with the name and the NORAD ID base on the data from Space-Track. Data are returned in JSON format.

Endpoint =  https://nasaapistellarbytes.azurewebsites.net/ It returns all data in JSON format.

## Searching a particulary object
We can also search a particular object, for the NORAD ID or name, but if you use one or another you would get different results. For example, if you use the name to search them the API returns all objects related with this name. This happens because much debris could be produced for a collision between debris or came from the same satellite.

If you want to use the NORAD ID searching function use this link:
https://nasaapistellarbytes.azurewebsites.net/id/xxxxx ➡️ It returns the objects related with the number xxxxx in JSON format.

https://nasaapistellarbytes.azurewebsites.net/id/name ➡️  It returns the objects related with the name in JSON format.


## Examples
https://nasaapistellarbytes.azurewebsites.net/id/49251 ➡️ It returns data of NORAD ID 49251

https://nasaapistellarbytes.azurewebsites.net/id/SZ-12%20MODULE%20DEB ➡️ It returns data of an object related with the name SZ-12-MODULE DEB
 
