var entity = Array();
$('#secondrow').hide();
$('#thirdrow').hide();
$('#fourthrow').hide();
$('#formrow').hide();

function showsecondrow(a) {
    entity = "";
    $('#secondrow').hide();
    $('#thirdrow').hide();
    $('#fourthrow').hide();
    $('#formrow').hide();
    if(a == '#here' && $(a).hasClass('circle-text')){
        if (navigator.geolocation) {
            position = navigator.geolocation.getCurrentPosition(showPosition);
            $(a).removeClass('circle-text');
            $(a).addClass('circle-text-2');
            $('#formrow').hide();
            locationrequest();
        }else{
            $('#formrow').show();
            $(a).removeClass('circle-text-2');
            $(a).addClass('circle-text');
            console.log("hello position selected");
        }
    } else if(a == '#here'){
        $(a).removeClass('circle-text-2');
        $(a).addClass('circle-text');
    }else{
        $('#formrow').show();
        console.log("hello position selected");
    }
}
function locationrequest(){
    console.log(document.getElementById("input"));  
    $('#formrow').hide();
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

