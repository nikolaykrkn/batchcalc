$(document).ready(function(){

	var i = 0;
	var options = '';
	var html = '';
	var lines = 1;
	var matOptions='';

	for (let k=0; k < oxides.length; k++){
	    options += '<option value="content' + oxides[k] + '">' + oxides[k] + '</option>'
	};

	for(let k=0; k < mats.length; k++){
		matOptions += '<option value="' + mats[k]['id'] + '">' + mats[k]['Name'] + '</option>'
	};

	function SelectHtml (fieldNum) {
		return '<div class="oxideDetails"><select name="Oxide' + fieldNum + '" class= "name_component">' + options + 
		'</select><input  type="number" step="0.01" name="content' + fieldNum + '" required>' +
		'<select name="Material' + fieldNum + '">' + matOptions + '</select></div>'
	};

	function addElem() {
		if (lines < 20){
		$(".glassComposition").append(SelectHtml(lines));
		lines ++
		};
	};

	$(".glassComposition").append(SelectHtml(0));
	$(".addElem").on("click", addElem);

	function getData(){
		$('#results').empty();
		var Glass = {};
		var RawMat = {};
		for (let i = 0; i < $(".oxideDetails").length; i++){
			Glass[$("select[name='Oxide"+i+"'").val()] = $("input[name='content"+i+"'").val();
			RawMat[$("select[name='Oxide"+i+"'").val()] = $("select[name='Material"+i+"'").val();
		};
		var UsedMats = [];
		var UsedMatsNames = [];
		for (let i = 0; i < mats.length; i++){
			for (let key in RawMat) {
				if (RawMat.hasOwnProperty(key)) {
					if (mats[i]['id'] == RawMat[key]){
						UsedMats.push(mats[i]);
						UsedMatsNames.push(mats[i].Name);
					};
				};
			};
		};
		var matrixOxides = [];
		var vectorNames = [];
		var vectorGlass = [];

		for (var key1 in Glass){
			if (Glass.hasOwnProperty(key1)){
				vectorNames.push(key1);
				vectorGlass.push(Glass[key1]);
				var materialOxides=[];

				for (var m of UsedMats){
					materialOxides.push(m[key1]);
				};
			};
			matrixOxides.push(materialOxides)
		};
		var result = math.lusolve(matrixOxides, vectorGlass);
		// console.log(result);
		// console.log(UsedMatsNames);

		function resultTableHTML (name, array_table, tag='td', percent = 0){
			this.tabContent = '';
			for (let element of array_table){
				if (tag === 'td'){
					if(percent === 1){
						element = (element[0]*100/math.sum(result)).toFixed(2);

					} else {
						element = (element[0]*100).toFixed(2);
					};
				};
					this.tabContent += `<${tag}>${element}</${tag}>`;
			};
				this.html = `<tr><${tag}>${name}</${tag}>${this.tabContent}</${tag}></tr>`;	
		};

		var resultHeader = new resultTableHTML('Raw material', UsedMatsNames, tag='th').html;
		var resultNumbers = new resultTableHTML('Weight Fraction', result).html;
		var resultPercent = new resultTableHTML('Percentage', result, tag='td', percent=1).html;
		
		$('#results').append(resultHeader).append(resultNumbers).append(resultPercent);
	};

	$("input[type='submit']").on("click", getData);
});