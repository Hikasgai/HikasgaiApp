var $ = require('jquery'); //Importo la libreria jquery

var descargarCalendario = function() {
  //var loadingDiv = $(".loading")[0]; //Cacheo el el bloque donde ira el loading
  var textFile = null,
  //Toda esta funcion es la que se encarga de crear el fichero
  makeTextFile = function(text) {
    var data = new Blob([text], {
        type: 'text/plain'
    });
    if (textFile !== null) {
      window.URL.revokeObjectURL(textFile);
    }
    textFile = window.URL.createObjectURL(data);
    return textFile;
  };
  // Formatea fecha
  function myFunction(fecha) {
    var days = ["SUN","MON","TUE","WED","THU","FRI","SAT"];
    var dia = days[fecha.getDay()];
    return ;
  }
  // Se leen los campos de la pagina
  var create = document.getElementById('create')
  //var save = document.getElementById('save')
  //var cursoAcademico = document.getElementById(' ');
  //var inicioCuatrimestreUno = document.getElementById('id_inicioPrimerCuatrimestreDia');
  //
  //var inicioCuatrimestreDos = document.getElementById('');
  //var finCuatrimestreUno = document.getElementById('');
  //var finCuatrimestreDos = document.getElementById('');
  // Se crea un evento, a la espera de click en el boton create
  // En caso de activarse se
  create.addEventListener('click', function() {
    // Se hace visible el logo de cargar
    //$(loadingDiv).removeClass("hidden");
    //
    var link = document.getElementById('downloadlink');
    var url = "/disenarcalendario";
    // Creamos una variable en formato JSON para el diccionario
    var data = {
      "cursoAcademico":"2016/2017",
      "inicioCuatrimestreUno":"2016/09/05 MON",
      "inicioCuatrimestreDos":"2017/01/24 TUE",
      "finCuatrimestreUno":"2016/12/23 FRI",
      "finCuatrimestreDos":"2017/05/23 WED"
    }
    //Si todo tira bien se ejecuta esto
    var success = function(data) {
      link.href = makeTextFile(data);
      link.style.display = 'block';
      //$(loadingDiv).addClass("hidden", 500);
    };
    //Si hay algun error se ejecuta el siguiente bloque
    var error = function(request, status, error){
      console.log(request);
      console.log(request.responseText);
      //$(loadingDiv).addClass("hidden", 500);
      alert("Error, mira la consola para ver los logs");
    };
    //
    $.ajax({
      type: "POST",
      url: url,
      data: JSON.stringify(data),
      success: success,
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      error: error
    });

  }, false);
}

exports.descargarCalendario = descargarCalendario;
