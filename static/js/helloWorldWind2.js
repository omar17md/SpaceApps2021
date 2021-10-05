// Create a WorldWindow for the canvas.
var wwd = new WorldWind.WorldWindow("canvasOne3");

wwd.addLayer(new WorldWind.BMNGOneImageLayer());
wwd.addLayer(new WorldWind.BMNGLandsatLayer());

wwd.addLayer(new WorldWind.CompassLayer());
wwd.addLayer(new WorldWind.CoordinatesDisplayLayer(wwd));
wwd.addLayer(new WorldWind.ViewControlsLayer(wwd));

// Add a placemark
var placemarkLayer = new WorldWind.RenderableLayer();
wwd.addLayer(placemarkLayer);

var placemarkAttributes = new WorldWind.PlacemarkAttributes(null);

placemarkAttributes.imageOffset = new WorldWind.Offset(
    WorldWind.OFFSET_FRACTION, 0.3,
    WorldWind.OFFSET_FRACTION, 0.0);

placemarkAttributes.labelAttributes.offset = new WorldWind.Offset(
    WorldWind.OFFSET_FRACTION, 0.5,
    WorldWind.OFFSET_FRACTION, 1.0);




// Add a COLLADA model
var modelLayer = new WorldWind.RenderableLayer();
wwd.addLayer(modelLayer);

function load2() {
    var mydata = JSON.parse(data1);
    var length = Object.keys(mydata).length; 
    var config = {dirPath: 'https://raw.githubusercontent.com/omar17md/SpaceApps2021/main/img/models/'};
    if(length <= 1){
        for(var i = 0; i < length; i++){
            var position = new WorldWind.Position(mydata[i].latitude, mydata[i].longitude, mydata[i].elevation * 1000.0);
            var colladaLoader = new WorldWind.ColladaLoader(position, config);
            // desde aqui
            var placemark = new WorldWind.Placemark(position, false, placemarkAttributes);

            placemark.label = mydata[i].name;
            placemark.alwaysOnTop = true;

            placemarkLayer.addRenderable(placemark);
            // hasta aqui
            colladaLoader.load("apple.dae", function (colladaModel) {
            colladaModel.scale = 200000;
            modelLayer.addRenderable(colladaModel);
            })
            document.getElementById("Names").value = mydata[i].name
            document.getElementById("Ids").value = mydata[i].norad
            document.getElementById("Latitudes").value = mydata[i].latitude.toFixed(2)
            document.getElementById("Longitudes").value = mydata[i].longitude.toFixed(2)
            document.getElementById("Elevations").value = mydata[i].elevation.toFixed(2)
             
        }
    }else{
        for(var i = 0; i < length; i++){
            var position = new WorldWind.Position(mydata[i].latitude, mydata[i].longitude, mydata[i].elevation * 1000.0);
            var colladaLoader = new WorldWind.ColladaLoader(position, config);
            // desde aqui
            var placemark = new WorldWind.Placemark(position, false, placemarkAttributes);

            placemark.label = mydata[i].name;
            placemark.alwaysOnTop = true;

            placemarkLayer.addRenderable(placemark);
            // hasta aqui
            colladaLoader.load("apple.dae", function (colladaModel) {
            colladaModel.scale = 200000;
            modelLayer.addRenderable(colladaModel);
            })
            document.getElementById("labelnames").style.visibility = "hidden"
            document.getElementById("Names").style.visibility = "hidden"
            document.getElementById("labelid").style.visibility = "hidden"
            document.getElementById("Ids").style.visibility = "hidden"
            document.getElementById("labellatitue").style.visibility = "hidden"
            document.getElementById("Latitudes").style.visibility = "hidden"
            document.getElementById("labellongitude").style.visibility = "hidden"
            document.getElementById("Longitudes").style.visibility = "hidden"
            document.getElementById("labelelevation").style.visibility = "hidden"
            document.getElementById("Elevations").style.visibility = "hidden"
        }
    }
}


// Add WMS imagery
var serviceAddress = "https://neo.sci.gsfc.nasa.gov/wms/wms?SERVICE=WMS&REQUEST=GetCapabilities&VERSION=1.3.0";
var layerName = "MOD_LSTD_CLIM_M2";

var createLayer = function (xmlDom) {
    var wms = new WorldWind.WmsCapabilities(xmlDom);
    var wmsLayerCapabilities = wms.getNamedLayer(layerName);
    var wmsConfig = WorldWind.WmsLayer.formLayerConfiguration(wmsLayerCapabilities);
    var wmsLayer = new WorldWind.WmsLayer(wmsConfig);
    wwd.addLayer(wmsLayer);
};

var logError = function (jqXhr, text, exception) {
    console.log("There was a failure retrieving the capabilities document: " +
        text +
    " exception: " + exception);
};

$.get(serviceAddress).done(createLayer).fail(logError);