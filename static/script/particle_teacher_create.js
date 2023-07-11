document.getElementById("id_lecture").hidden = true;
document.getElementById("id_practice").hidden = true;
document.getElementById('id_laboratory').hidden = true;
document.getElementById('id_seminar').hidden = true;
document.getElementById('id_coursework').hidden = true;

document.getElementById('check_lecture').onchange = function() {
    document.getElementById('id_lecture').hidden = !this.checked;
};
document.getElementById('check_practice').onchange = function() {
    document.getElementById('id_practice').hidden = !this.checked;
};

document.getElementById('check_laboratory').onchange = function() {
    document.getElementById('id_laboratory').hidden = !this.checked;
};

document.getElementById('check_seminar').onchange = function() {
    document.getElementById('id_seminar').hidden = !this.checked;
};

document.getElementById('check_coursework').onchange = function() {
    document.getElementById('id_coursework').hidden = !this.checked;
};

document.onchange = function(){
    document.getElementById('id_raiting').value = parseInt(document.getElementById('id_raiting').value) + 1
}