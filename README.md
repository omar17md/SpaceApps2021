# SpaceApps2021 -  Stellar - Bytes 🛰 
<img src="https://github.com/omar17md/SpaceApps2021/blob/3d0b8dff8ecc7519e090fd67fc44444826ab82d9/img/logos/Logo_bebe.png">

# Tracking space debris in real time


## Developers:

    * Castillo Pérez Brian
    * Castro Sam Maria Magdalena
    * Jesús Omar Magaña Medina
    * Verdugo Domínguez Jesus Abdiel
    
    
## Detailed Project Description
Stellar-Bytes is a user-friendly visualization tool that uses data from space-track.org to track debris in real time. The globe is rendered from NASA WorldWide Web in order to make visualizations interactive. We hope that with this tool people interested might find a way to explore debris around Earth, as well to provide a fast way to access the information about satellites in a different manner, since our app displays latitud, altitude and elevation of the debris. The search bar allows searches by *NORAD ID* and *Name* and displays a table with the information.

Tools used in this project:

    * Python: Used for extracting the data and calculate the position of each debris with the library Skyfield.
    * Photoshop: Used for designing the logo and buttons on the web app.
    * Javascript: Used for the WorldWind interface and the interactive functions.
    * HTML: Used for the internal structure for the web page.
    * CSS: Used for styling.
    * Azure: Used to upload the final project online.

## App link

[Application Link](https://stellarbytesapp.azurewebsites.net/) 

## Photos of App Stellar - Bytes
<img src="https://github.com/omar17md/SpaceApps2021/blob/main/img/fotoApp/azureportal.png">
<img src="https://github.com/omar17md/SpaceApps2021/blob/main/img/fotoApp/app.png">



## API documentation

### Description
Our API takes data from the page Space-Track, it contains general information about space debris, but these data are not useful to plot their position in WorldWind Web page because we need geographic coordinates to plot them. The API’s endpoint returns these geographic coordinates with the name and the NORAD ID base on the data from Space-Track. Data are returned in JSON format.

Endpoint =  https://apistellarbyteschallenge.azurewebsites.net It returns all data in JSON format.

See the following example
<img src="https://github.com/omar17md/SpaceApps2021/blob/main/img/fotoApp/jsondata.png">

## Searching a particulary object
We can also search a particular object, for the NORAD ID or name, but if you use one or another you would get different results. For example, if you use the name to search them the API returns all objects related with this name. This happens because much debris could be produced for a collision between debris or came from the same satellite.

If you want to use the NORAD ID searching function use this link:
https://apistellarbyteschallenge.azurewebsites.net/id/xxxxx ➡️ It returns the objects related with the number xxxxx in JSON format.

https://apistellarbyteschallenge.azurewebsites.net/id/name ➡️  It returns the objects related with the name in JSON format.


## Examples
https://apistellarbyteschallenge.azurewebsites.net/id/49251 ➡️ It returns data of NORAD ID 49251

https://apistellarbyteschallenge.azurewebsites.net/id/SZ-12%20MODULE%20DEB ➡️ It returns data of an object related with the name SZ-12-MODULE DEB
 
