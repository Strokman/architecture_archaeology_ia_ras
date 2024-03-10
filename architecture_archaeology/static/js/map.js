ymaps.ready(function(){
    var map = new ymaps.Map("map", {
        center: [55.76, 37.64],
        zoom: 6,
        controls: ['rulerControl', 'searchControl', "zoomControl", "typeSelector", "searchControl"]
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
  
  });
      map.events.add('boundschange', function (event) {
        var currentZoom = event.get('newZoom');

        // Проверяем текущий масштаб
        if (currentZoom >= 10) {
            // Добавляем метки или что-то делаем, если масштаб меньше 10
            // В данном примере просто добавим метки на карту
            map.geoObjects.removeAll();
        } else {
            // Убираем метки, если масштаб больше или равен 10
                
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

});
        }
    });
    });


