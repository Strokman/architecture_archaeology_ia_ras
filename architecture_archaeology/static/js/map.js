ymaps.ready(function(){
    // Указывается идентификатор HTML-элемента.
    var map = new ymaps.Map("map", {
        center: [55.76, 37.64],
        zoom: 6
    });
  
    fetch('/map/get/').then(function(response) {
          response.json().then(function(data) {
            data.forEach(element => {
                var myGeoObject = new ymaps.Placemark([element.fields.lat, element.fields.long], {
                    // Задаем содержимое балуна метки.
                    // Это содержимое будет отображаться при клике по кластеру.
                    balloonContentHeader: element.fields.name,
                    balloonContentBody: element.fields.description +'<br>' + '<a href="/arch-site/detail/' + element.fields.slug + '/">Карточка объекта</a>',
                    hintContent: element.fields.name
                });
                map.geoObjects.add(myGeoObject);
            });
 
            });
  //   var myGeoObject = new ymaps.GeoObject({
  //     geometry: {
  //         type: "Point", // тип геометрии - точка
  //         coordinates: [data.fields.lat, data.fields.long] // координаты точки
  //     }
  // });
  // map.geoObjects.add(myGeoObject);
  
  });
    });
