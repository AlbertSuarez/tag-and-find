var entity = Array();
var necessities = Array();
var first = 0;
$('#secondrow').hide();
$('#thirdrow').hide();
$('#fourthrow').hide();
$('#formrow').hide();
$('#formrow2').hide();

function showsecondrow(a) {
    entity = "";
    console.log("holi");
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
            locationrequest();
        }else{
            $('#formrow').show();
            $('#here').removeClass('circle-text-2');
            $('#here').addClass('circle-text');
            $('#another').removeClass('circle-text');
            $('#another').addClass('circle-text-2');
        }
    } else if(a == '#here'){
        $('#here').removeClass('circle-text-2');
        $('#here').addClass('circle-text');
        $('#another').removeClass('circle-text-2');
        $('#another').addClass('circle-text');
    }else if(a == '#another' && $(a).hasClass('circle-text')){
        $('#formrow').show();
        $('#here').removeClass('circle-text-2');
        $('#here').addClass('circle-text');
        $('#another').removeClass('circle-text');
        $('#another').addClass('circle-text-2');
    }else{
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
    var list_num = ['one','two','three','four'];
    var i = 0;
    if(first == 0){
        loadJSON(function(json) {
            var necessitiestags = json["tags"]["necessity"];
            for( pos in necessitiestags) {
                var need = necessitiestags[pos];
                var needid = need.replace(" ","-")
                $('#necessitiestags').append(`<div class="col"><button type="button" onclick="showthirdrow('${needid}')" class="btn tag-text color- ${list_num[i%4]} " id="${needid}"> ${need} </button></div>`);
                i = i + 1;
            }
        });
        first = 1;
    }
    $('#secondrow').show();
}
function showPosition(position) {
    console.log("Latitude: " + position.coords.latitude + "<br>Longitude: " + position.coords.longitude);
}
function showthirdrow(a) {
    b = "#" + a;
    console.log(b);
    if( $(b).hasClass('tag-text-2')){
        necessities.pop()
        $(b).removeClass('tag-text-2');
        $('#thirdrow').hide();
    }
    else{
        if(necessities.length != 0){
            c = necessities.pop();
            console.log(c)
            $(c).removeClass('tag-text-2');
        }
        necessities.push(b)
        $(b).addClass('tag-text-2');
        $('#thirdrow').show();
    }
    console.log(necessities);
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

