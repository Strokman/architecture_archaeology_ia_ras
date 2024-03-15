ymaps.ready(function(){
    var map = new ymaps.Map("map", {
        center: [55.76, 37.64],
        zoom: 6,
        controls: ['rulerControl', 'searchControl', "zoomControl", "typeSelector", "searchControl"]
    });

    var marks = fetch('/map/get/').then(function(response) {
        return response.json();
    });

    var isAuth;
    fetch('/map/user/').then(response => response.json())
    .then(data => {
        isAuth = data;
    })
    .then(() => {
        isAuth = isAuth.is_authenticated;
    });

    function renderMarks(data){
        data.then(function(data) {
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
  
        };

    renderMarks(marks);

    map.events.add('boundschange', function (event) {
        var currentZoom = event.get('newZoom');
        // Проверяем текущий масштаб и залогинен ли пользователь
        if (currentZoom >= 10 && isAuth === false) {
            // Удаляем метки, если зум больше или равно 10 и пользователь не залогинен
            map.geoObjects.removeAll();
        } else {
            // Возвращаем метки на место

            renderMarks(marks);
        }
    });

});
