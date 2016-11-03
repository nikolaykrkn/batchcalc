var oxides = ['SiO2', 'Al2O3', 'Na2O', 'K2O'];
var selecthtml = '<div><select name="material1"> <option value="ContentSiO2">SiO2</option><option value="ContentAl2O3">Al2O3</option><option value="ContentNa2O">Na2O</option><option value="ContentK2O">K2O</option></select></div><input type="text" name="amount1" >'

$(document).ready(function(){

	$(".glassComposition").prepend(selecthtml);
	$( ".glassComposition input" ).on( "click", function() {
        	$(".glassComposition").prepend(selecthtml);
	});

});