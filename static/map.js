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
           
          
            
            var latlng = new google.maps.LatLng(predio.latitude, predio.longitude);

            marker = new google.maps.Marker({
                position: latlng,
                map: mymap,
                title : predio.nombre
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
                      title : nacimiento.identificador + '-' + predio.nombre
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
                  mymap.setZoom(12);
                  
             }, 1000);
             }, 3000);

                 
        }
    })();

          function info(predio){
                
                var html = "<li" + " class="+"list-group-item"+">";
                var thumb = "<li class='list-group-item thumbnail'>";
                var tag = "</li>";
                var text = /* thumb + "<img src='" + predio.photo + "' alt='thumb'" + tag + */
                            html + 'Nombre: ' + predio.nombre + tag +
                            html + "Catastro: " + predio.catastro+ tag +
                            html + 'Escritura :' + predio.escritura+ tag +
                            html +'Area: ' + predio.area+ tag +
                            html +'Corregimiento: ' + predio.corregimiento+ tag +
                            html +'Vereda: ' + predio.vereda+ tag +
                            html +'Cuenca: ' + predio.cuenca+ tag +
                            html +'Sub cuenca: ' + predio.sub_cuenca+ tag +
                            html +'Temperatura: ' + predio.temperatura+ tag +
                            html +'Via pavimentada: ' + predio.via_pavimentada+ tag +
                            html +'Via destapada: ' + predio.via_destapada+ tag +
                            html +'Via trocha: ' + predio.via_trocha+ tag +"</div>";

                return text

          }

          function infoNa(nacimiento){
              
              var html = "<li  class='list-group-item' >";
              var tag = "</li>";
              var text =  html + 'Identificador: ' + nacimiento.identificador + tag +
                          html + 'Caudal: ' + nacimiento.caudal+ tag +
                          html + 'Ph: ' + nacimiento.ph+ tag +
                          html + 'Color: ' + nacimiento.color+ tag +
                          html + 'Turbiedad: ' + nacimiento.turbiedad+ tag +
                          html + 'Dureza: ' + nacimiento.dureza+ tag +
                          html + 'Sulfatos: ' + nacimiento.sulfatos+ tag +
                          html + 'Nitratos: ' + nacimiento.nitratos+ tag +
                          html + 'Temperatura: ' + nacimiento.temperatura+ tag +
                          html + 'Dbo: ' + nacimiento.dbo+ tag +
                          html + 'Sólidos: ' + nacimiento.solidos+ tag +
                          html + 'Dqo: ' + nacimiento.dqo+ tag +
                          html + 'Coliformes: ' + nacimiento.coliformes+ tag +
                          html + 'Altura: ' + nacimiento.altura+ tag + "</div>" ;


                return text


          }

          $("#btn-back").click(function(){

            $("#lista").show("slow");
            infoNac.innerHTML="";
            infoPre.innerHTML="";
            $(this).hide();
          });

});

