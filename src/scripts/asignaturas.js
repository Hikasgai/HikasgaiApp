var $ = require('jquery'); //Importo la libreria jquery

$(document).ready(function() {
	var curso1 = $("#curso1");
	var curso2 = $("#curso2");
	var curso3 = $("#curso3");
	var curso4 = $("#curso4");

	var hideCourses = function(event){
		curso1.hide();
		curso2.hide();
		curso3.hide();
		curso4.hide();
	}

	$("curso1").on('click',hideCourses());
	$("curso2").on('click',hideCourses());
	$("curso3").on('click',hideCourses());
	$("curso4").on('click',hideCourses());
});


