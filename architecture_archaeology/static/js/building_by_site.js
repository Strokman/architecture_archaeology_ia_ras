var newSelect = document.getElementById('id_site');
var buildingSelect = document.getElementById("id_building");
newSelect.setAttribute('onchange', 'run(this.value)');

const opt = document.createElement('option');
opt.value = 'default';
opt.innerHTML = '---------';
buildingSelect.appendChild(opt);


    function run(value) {
        var siteId = value;
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