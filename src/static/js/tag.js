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
function loadJSON(callback) {   
    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', 'https://raw.githubusercontent.com/AlbertSuarez/tag-and-find/master/src/tags/tags.json', true);
    xobj.onreadystatechange = function () {
      if (xobj.readyState == 4 && xobj.status == "200") {
        callback(JSON.parse(xobj.responseText));
      }
    };
    xobj.send(null);  
}
function chargesecondrow(){
    loadJSON(function(json) {
        console.log(json); // this will log out the json object
        var necessitiestags = json["tags"]["necessity"];
        var html_out = '';
        necessitiestags.forEach(element => {
            //console.log(element)
            html_out += "<div class='col'><button type='button' onclick='showthirdrow('" + element + "')' class='btn tag-text' id='" + element +"'>Tourism attractions</button></div>";
        
        });
        $('#necessitiestags').append(html_out);
        /*
        for( pos in necessitiestags) {
            var need = necessitiestags[pos];
            console.log(need)
            $('#necessitiestags').append("<div class='col'><button type='button' onclick='showthirdrow('" + need + "')' class='btn tag-text' id='" + need +"'>Tourism attractions</button></div>");
        }*/
    });
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

