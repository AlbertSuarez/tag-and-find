var entities = Array();
var necessities = Array();
var first = 0;
var response = {
    'location': '',
    'necessity': '',
    'features': ''
};
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
            locationrequest(0);
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
function locationrequest(a){
    if(a == 1) {
        response['location'] = document.getElementById('input-location').value;
    }else{
        response['location'] = "Bremen";
    }
    loadsecondrow();
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
function loadsecondrow(){
    var list_num = ['one','two','three','four'];
    var i = 0;
    if(first == 0){
        loadJSON(function(json) {
            var necessitiestags = json["tags"]["necessity"];
            for( pos in necessitiestags) {
                var need = necessitiestags[pos];
                var needid = need.replace(" ","-")
                $('#necessitiestags').append(`<div class="col"><button type="button" onclick="showthirdrow('${needid}')" class="btn tag-text color-${list_num[i%4]} " id="${needid}"> ${need} </button></div>`);
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
    if( $(b).hasClass('tag-text-2')){
        necessities.pop()
        $(b).removeClass('tag-text-2');
        $('#thirdrow').hide();
    }
    else{
        if(necessities.length != 0){
            c = necessities.pop();
            $(c).removeClass('tag-text-2');
        }
        necessities.push(b)
        $(b).addClass('tag-text-2');
        loadthirdrow(a);
    }
}
function loadthirdrow(b){
    loadJSON(function(json) {
        var a = b.replace("-"," ")
        var featurestags = json["tags"]["features"][a];
        response["necessity"] = b;
        $('#featurestags').empty();
        for( pos in featurestags) {
            var need = featurestags[pos];
            var needid = need.replace(" ","-");
            $('#featurestags').append(`<div class="col"><button type="button" onclick="showfourthrow('${needid}')" id="${needid}" class="btn tag-text">${need}</button></div`);
        }
    });
    $('#thirdrow').show();
} 
function showfourthrow(a) {
    if($('#fourthrow').hide()){
        $('#fourthrow').show()
    }
    b = "#" + a;
    if (! $(b).hasClass('tag-text-2') ) {
        entities.push(a);
        $(b).addClass('tag-text-2');
    } 
    else {
        $(b).removeClass('tag-text-2');
        entities = entities.filter(value => value != a);
    }
}
function passinfo() {
    $('#submit-button').addClass('invisible');
    $('#loading-message').removeClass('invisible');
    for(i = 0; i < entities.length; i++){
        response["features"] += entities[i] + "_";
    }
    window.location = "/search?location=" + response["location"] + "&necessity=" + response["necessity"] + "&features=" + response["features"];
}

