var entity = Array();
$('#secondrow').hide();
$('#thirdrow').hide();
$('#fourthrow').hide();
$('#formrow').hide();
$('#formrow2').hide();

function showsecondrow(a) {
    entity = "";
    $('#secondrow').hide();
    $('#thirdrow').hide();
    $('#fourthrow').hide();
    $('#formrow').hide();
    $('#formrow2').hide();
    if(a == '#here' && $(a).hasClass('circle-text')){
        console.log("other select");
        if (navigator.geolocation) {
            position = navigator.geolocation.getCurrentPosition(showPosition);
            $('#here').removeClass('circle-text');
            $('#here').addClass('circle-text-2');
            $('#another').removeClass('circle-text-2');
            $('#another').addClass('circle-text');
            $('#formrow').hide();
            locationrequest();
        }else{
            $('#formrow').show();
            $('#secondrow').hide();
            $('#here').removeClass('circle-text-2');
            $('#here').addClass('circle-text');
            $('#another').removeClass('circle-text');
            $('#another').addClass('circle-text-2');
            console.log("hello position selected");
        }
    } else if(a == '#here'){
        console.log("other diselect");
        $('#here').removeClass('circle-text-2');
        $('#here').addClass('circle-text');
        $('#another').removeClass('circle-text-2');
        $('#another').addClass('circle-text');
        locationrequest();
    }else if(a == '#another' && $(a).hasClass('circle-text')){
        console.log("another select");
        $('#here').removeClass('circle-text-2');
        $('#here').addClass('circle-text');
        $('#another').removeClass('circle-text');
        $('#another').addClass('circle-text-2');
        $('#formrow').show();
    }else{
        console.log("another diselect");
        $('#here').removeClass('circle-text-2');
        $('#here').addClass('circle-text');
        $('#another').removeClass('circle-text-2');
        $('#another').addClass('circle-text');
    }
}
function locationrequest(){
    console.log(document.getElementById("input"));  
    $('#formrow').hide();
    chargesecondrow();
}
function chargesecondrow(){
    var jsondoc = open('../../tags/tags.json');
    jsonfile = JSON.parse(requestURL);
    necessitiestags = jsonfile["tags"]["necessity"]

    $('#secondrow').show();
}
function showPosition(position) {
    console.log("Latitude: " + position.coords.latitude + "<br>Longitude: " + position.coords.longitude);
}
function showthirdrow() {
    $('#thirdrow').show();
}

function showfourthrow(a) {
    if($('#fourthrow').hide()){
        $('#fourthrow').show()
    }
    b = "#" + a;
    if ( $(b).hasClass('tag-text') ) {
        entity.push(a)
        $(b).removeClass('tag-text');
        $(b).addClass('tag-text-2');
    } 
    else {
        $(b).removeClass('tag-text-2');
        $(b).addClass('tag-text')
        entity = entity.filter(value => value != a)
    }
    console.log("Entity = " + entity)
}
/*
var header = document.getElementById("b13");
var btns = header.getElementsByClassName("btn btn-outline-primary tag-text");
for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function() {
        var current = document.getElementsByClassName("active");
        this.className += " active";
    });
}
*/
function passinfo() {
}

