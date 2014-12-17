  var searchMap;
  var resultMarkers = [];
  var defaults = {
    map: {
      mapTypeId: google.maps.MapTypeId.ROADMAP,
      zoom: 3

    }
  };
  /*
  * Initialize
  */
  function init (mapElem, options){
    var mapOptions = $.extend(mapOptions, defaults.map, options);
    searchMap = new google.maps.Map(mapElem, mapOptions);

    return searchMap;
  }



var center_point = new google.maps.LatLng(3.43722, -76.5225);

var bounds = new google.maps.LatLngBounds();
$().ready(function() {
var mymap = init(document.getElementById('mymap'), {
center: center_point
});

mark = new google.maps.Marker({

  position: center_point
  
});






var infoPre = document.getElementById("some");
var listLinks = document.getElementById("lista");
var markers = [];
var markerse = [];
    (function (){

        $.each(predios, function(i, predio) {
           /* iterate through array or object */
          
            
            var latlng = new google.maps.LatLng(predio.latitude, predio.longitude);

            marker = new google.maps.Marker({
                position: latlng,
                map: mymap
            });

            bounds.extend(latlng);

            google.maps.event.addListener(marker, 'click', function() {

                for (var i = 0; i < markerse.length; i++) {
                markerse[i].setMap(null);
                }
                markerse = [];

                 infoPre.style.visibility = 'visible'; 
                 listLinks.style.visibility = 'hidden';
                 infoPre.innerHTML = info(predio); 

              $.each(nacimientos, function(i, nacimiento) {
                 /* iterate through array or object 
                 al clickear sobre un marker crea los markers de los nacimientos */
                
                  if(nacimiento.predio === predio.id){
                  var latlng = new google.maps.LatLng(nacimiento.latitude, nacimiento.longitude);

                  marker = new google.maps.Marker({
                      position: latlng,
                      map: mymap
                  });

                  bounds.extend(latlng);

                  google.maps.event.addListener(marker, 'click', function() {
                         });

                  markerse.push( marker );
                  
               
                }
                
                
              });

              if (nacimientos.length > 0) {
                  mymap.fitBounds(bounds);
                  mymap.panToBounds(bounds);

              }
          });

          
            markers.push( marker );
        });

        if (predios.length > 0) {
            mymap.fitBounds(bounds);
            mymap.panToBounds(bounds);

        }
    })();

          function info(predio){
                var html = "<li" + " class="+"list-group-item"+">";
                var tag = "</li>";
                var text =  html + "catastro:" + predio.catastro+ tag +
                            html + 'escritura:' + predio.escritura+ tag +
                            html +'area:' + predio.area+ tag +
                            html +'corregimiento:' + predio.corregimiento+ tag +
                            html +'vereda:' + predio.vereda+ tag +
                            html +'cuenca:' + predio.cuenca+ tag +
                            html +'sub cuenca:' + predio.sub_cuenca+ tag +
                            html +'temperatura:' + predio.temperatura+ tag +
                            html +'presion antropica:' + predio.presion_antropica+ tag +
                            html +'via pavimentada:' + predio.via_pavimentada+ tag +
                            html +'via destapada:' + predio.via_destapada+ tag +
                            html +'via trocha:' + predio.via_trocha+ tag ;

                return text

          }


});

