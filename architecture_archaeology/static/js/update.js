var buildingSelect = document.getElementById("id_building");

function getInitialValue(model, slug) {
    fetch('/helpers/get-building-by-artwork/' + model + '/' + slug).then(function(response) {
    response.json().then(function(data) {
        var opt = document.createElement('option');
        opt.value = data.building.id;
        opt.innerHTML = data.building.name;
        buildingSelect.appendChild(opt);
        data.other.forEach(elem => {
            var opt = document.createElement('option');
            opt.value = elem.id;
            opt.innerHTML = elem.name;
            buildingSelect.appendChild(opt);
        });
    });
    });
};

const url = window.location.href.split('/');

getInitialValue(url.at(-2), url.at(-1));

var newSelect = document.getElementById('id_site');

newSelect.setAttribute('onchange', 'run(this.value)');

function run(value) {
    var siteId = value;
    const opt = document.createElement('option');
opt.value = 'default';
opt.innerHTML = '---------';
buildingSelect.appendChild(opt);
    buildingSelect.innerHTML = '';
    buildingSelect.appendChild(opt);
    if (siteId) {
    fetch('/building/get-building/' + siteId).then(function(response) {
    response.json().then(function(data) {
                data.forEach(element => {
                    var opt = document.createElement('option');
                    opt.value = element.pk;
                    opt.innerHTML = element.fields.name;
                    buildingSelect.appendChild(opt);
                });
    });
    });
}
}