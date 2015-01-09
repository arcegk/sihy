  var searchMap;
  var resultMarkers = [];
  var directionsDisplay = new google.maps.DirectionsRenderer();
  var directionsService = new google.maps.DirectionsService(); 
  
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


/*
SET BUTTON , DONT FORGET!
*/



var center_point = new google.maps.LatLng(3.5834, -76.4952);

var bounds = new google.maps.LatLngBounds();
$().ready(function() {
var mymap = init(document.getElementById('map_canvas'), {
center: center_point
});

mark = new google.maps.Marker({

  position: center_point,
  map : mymap,
  icon : '/static/icon-blue.png'
});


$("#btn-back").hide();



var center_po = new google.maps.LatLng(3.5834, -76.4952);
var infoPre = document.getElementById("some");
var listLinks = document.getElementById("lista");
var infoNac = document.getElementById("info");
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
           

            google.maps.event.addListener(marker, 'click', function(e) {

                mymap.setZoom(18);
                mymap.panTo(latlng);


                 var request = {
                origin: center_po,
                destination: latlng,
                travelMode: google.maps.DirectionsTravelMode["DRIVING"],
                unitSystem: google.maps.DirectionsUnitSystem["METRIC"],
                provideRouteAlternatives: true
                  };

                directionsService.route(request, function(response, status) {
                      if (status == google.maps.DirectionsStatus.OK) {
                          directionsDisplay.setMap(mymap);
                          directionsDisplay.setDirections(response);
                          directionsDisplay.setOptions( { suppressMarkers: true , 
                                                          preserveViewport : true } );

                          
                      }
                  });


                for (var i = 0; i < markerse.length; i++) {
                markerse[i].setMap(null);
                }
                markerse = [];

                infoPre.style.visibility = 'visible'; 

                
                $("#lista").hide();
                //listLinks.innerHTML = "";
                infoNac.style.visibility = 'hidden';
                infoNac.innerHTML="";
                infoPre.className = "list-group col-md-12";
                infoPre.innerHTML = info(predio); 
                $("#btn-back").show();

               

                
                

              $.each(nacimientos, function(i, nacimiento) {
                 /* iterate through array or object 
                 al clickear sobre un marker crea los markers de los nacimientos */
                
                  if(nacimiento.predio === predio.id){
                  var latlng = new google.maps.LatLng(nacimiento.latitude, nacimiento.longitude);

                  marker = new google.maps.Marker({
                      position: latlng,
                      map: mymap,
                      icon: '/static/icon.png',
                  });

                  bounds.extend(latlng);

                  google.maps.event.addListener(marker, 'click', function() {
                        infoPre.className = "list-group col-md-6";
                        infoNac.style.visibility = "visible";
                        infoNac.innerHTML = infoNa(nacimiento);
                        


                         });

                  markerse.push( marker );
                  
               
                }
                
                
              });

              
          });



          
            markers.push( marker );
        });

        if (predios.length > 0) {
             window.setTimeout(function() {
                  mymap.setZoom(9);
                  window.setTimeout(function() {
                  mymap.setZoom(14);
                  
             }, 1000);
             }, 3000);

                 
        }
    })();

          function info(predio){
                
                var html = "<li" + " class="+"list-group-item"+">";
                var thumb = "<li class='list-group-item thumbnail'>";
                var tag = "</li>";
                var text =  thumb + "<img src='" + predio.photo + "' alt='thumb'" + tag +
                            html + 'Nombre: ' + predio.nombre + tag +
                            html + "catastro: " + predio.catastro+ tag +
                            html + 'escritura :' + predio.escritura+ tag +
                            html +'area: ' + predio.area+ tag +
                            html +'corregimiento: ' + predio.corregimiento+ tag +
                            html +'vereda: ' + predio.vereda+ tag +
                            html +'cuenca: ' + predio.cuenca+ tag +
                            html +'sub cuenca: ' + predio.sub_cuenca+ tag +
                            html +'temperatura: ' + predio.temperatura+ tag +
                            html +'presion antropica: ' + predio.presion_antropica+ tag +
                            html +'via pavimentada: ' + predio.via_pavimentada+ tag +
                            html +'via destapada: ' + predio.via_destapada+ tag +
                            html +'via trocha: ' + predio.via_trocha+ tag +"</div>";

                return text

          }

          function infoNa(nacimiento){
              
              var html = "<li  class='list-group-item' >";
              var tag = "</li>";
              var text =  html + 'identificador: ' + nacimiento.identificador + tag +
                          html + 'caudal: ' + nacimiento.caudal+ tag +
                          html + 'ph: ' + nacimiento.ph+ tag +
                          html + 'color: ' + nacimiento.color+ tag +
                          html + 'turbiedad: ' + nacimiento.turbiedad+ tag +
                          html + 'dureza: ' + nacimiento.dureza+ tag +
                          html + 'sulfatos: ' + nacimiento.sulfatos+ tag +
                          html + 'nitratos: ' + nacimiento.nitratos+ tag +
                          html + 'temperatura: ' + nacimiento.temperatura+ tag +
                          html + 'dbo: ' + nacimiento.dbo+ tag +
                          html + 'solidos: ' + nacimiento.solidos+ tag +
                          html + 'dqo: ' + nacimiento.dqo+ tag +
                          html + 'coliformes: ' + nacimiento.coliformes+ tag +
                          html + 'cabecera municipal: ' + nacimiento.cabecera_municipal+ tag +
                          html + 'topoespecificacion: ' + nacimiento.topo_especificacion+ tag +
                          html + 'altura: ' + nacimiento.altura+ tag + "</div>" ;


                return text


          }

          $("#btn-back").click(function(){

            $("#lista").show("slow");
            infoNac.innerHTML="";
            infoPre.innerHTML="";
            $(this).hide();
          });

});

