var $ = require('jquery'); //Importo la libreria jquery


$( document.getElementById("id_email") ).keyup(function () {
	var email = document.getElementById("id_email").value;
	if (email.indexOf("@ikasle.ehu.eus") > -1) {
		document.getElementById("formAlumno").setAttribute("class", "show");
		document.getElementById("tipoformulario").setAttribute("value", "alumno");
		document.getElementById("formProfesor").setAttribute("class", "hide");
		return 0;
	}
	else if(email.indexOf("@ehu.eus") > -1) {
		document.getElementById("formProfesor").setAttribute("class", "show");
		document.getElementById("tipoformulario").setAttribute("value", "profesor");
		document.getElementById("formAlumno").setAttribute("class", "hide");
		return 0;
	}
	else{
		document.getElementById("tipoformulario").setAttribute("value", "not_valid");
		document.getElementById("formAlumno").setAttribute("class", "hide");
		document.getElementById("formProfesor").setAttribute("class", "hide");
		return 1;
	}
})

$( document.getElementById("id_grado") ).keyup(function () {
	    var availableTags = [
      "ActionScript",
      "AppleScript",
      "Asp",
      "BASIC",
      "C",
      "C++",
      "Clojure",
      "COBOL",
      "ColdFusion",
      "Erlang",
      "Fortran",
      "Groovy",
      "Haskell",
      "Java",
      "JavaScript",
      "Lisp",
      "Perl",
      "PHP",
      "Python",
      "Ruby",
      "Scala",
      "Scheme"
    ];
    $( document.getElementById("id_grado") ).autocomplete({
        source: function(request, response) {
        	var results = $.ui.autocomplete.filter(availableTags, request.term);
        response(results.slice(0, 5));
    	}
    });
  });


var descargarCalendario = function() {
  var loadingDiv = $(".loading")[0]; //Cacheo el el bloque donde ira el loading

  var textFile = null,
    makeTextFile = function(text) {
      var data = new Blob([text], {
        type: 'text/plain'
      });


      if (textFile !== null) {
        window.URL.revokeObjectURL(textFile);
      }

      textFile = window.URL.createObjectURL(data);

      return textFile;
    }; //Toda esta funcion es la que se encarga de crear el fichero


  var create = document.getElementById('create'),
    textbox = document.getElementById('textbox'); //Sigo cacheando objetos

  create.addEventListener('click', function() {
    $(loadingDiv).removeClass("hidden");
    var link = document.getElementById('downloadlink');
    var url = "/course_detail";
    //TODO: Esto es lo que teneis que hacer:
    /* 1. La variable data tiene que ser un objeto JSON, con un atributo
    * llamado "asignaturas" que tendra un array con objetos donde ira la informacion de la asignaturas
    * Este es el ejemplo de data
    * data = {
    *   "asignaturas": [
    *     {
    *       "campus": "GI",
    *       "codigoGrado": "GINFOR20",
    *       "codigoAsig": "25972",
    *       "idioma": "es",
    *       "grupo": "01"
    *     },
    *     {..}
    *  ]
    * }
    *
    * Os he dejado ya una variable data creada a mano pero teneis que gestionarlo para recibir
    * los datos desde el template, lo haria yo pero no me pagan lo suficiente.
    *
    * Puede que tengais algun problema porque no os pilla el codigo, teneis que ejecutar antes
    * el comando: "npm install" o "npm install i -D jquery", el segundo funciona seguro, porque he metido jquery en los modulos de node.
    *
    */
    var success = function(data) { //Si todo tira bien se ejecuta esto
      link.href = makeTextFile(data["calendario"]);
      link.style.display = 'block';
      $(loadingDiv).addClass("hidden", 500);
    };

    var error = function(request, status, error){ //Si hay algun error pues esto
      console.log(request);
      console.log(request.responseText);
      $(loadingDiv).addClass("hidden", 500);
      alert("Error, mira la consola para ver los logs");
    };

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
