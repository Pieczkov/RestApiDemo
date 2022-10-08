function get_ids_from_check_box() {
    var markedCheckbox = document.querySelectorAll('input[type=checkbox]:checked');
    var ids =[];
    markedCheckbox.forEach(box => ids.push(box.value));
    return ids;
}

function aport(){
    var array = get_ids_from_check_box();
    var addresURL = "/get_car_by_type?";
    var params = new URLSearchParams();
    array.forEach(id => params.append("type_ids", id));
    addresURL = addresURL + params.toString();  // to robi z arry = [1,2] --> type_ids=1&type_ids=2
    console.log(addresURL);
    var test = document.getElementById('cars');
    fetch(addresURL)
        .then(response => response.json())
        .then(data => {
            // while (test.firstChild){
            //     test.removeChild(test.lastChild);
            // }
            data.forEach(function (element) {
                const li = document.createElement("li"); // do test przekazujemy dane data do wyswietlenia
                const h2 = document.createElement('h2');
                const h3 = document.createElement('h3');
                h2.innerHTML = element.name;
                h3.innerHTML = element.type;
                li.appendChild(h2);
                li.appendChild(h3);
                test.appendChild(li);
            })
        })
}

document.addEventListener("DOMContentLoaded", function (){
    const checkboxes = document.querySelectorAll('input[type = checkbox]');
    checkboxes.forEach(function (checkbox){
        checkbox.addEventListener('change', aport);
        });
});