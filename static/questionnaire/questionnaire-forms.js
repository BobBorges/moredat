console.log('js file loaded');



var radios = document.querySelectorAll('input[name$="answer"]');
var otherdivs = document.querySelectorAll('div[id$="_div_other_field"]');
var othertxt = document.getElementById('id_other_field');



radios.forEach(radio => radio.addEventListener('change', function(){ 	
	var checkBoxInfo = radio.id.split('_');
	var checkBoxVal = radio.value;

	if (checkBoxVal == 'other') {
		if (otherdivs.item('div[id=`${checkBoxInfo[0]}_div_other_field`')){
			var othrtxt = document.getElementById(`${checkBoxInfo[0]}_other_field`)
			
			if (radio.checked) {
				var ckbxidx = `${checkBoxInfo[0]}_div_other_field`;
				for (const j of otherdivs) {
					if (j.id == ckbxidx){
						// othrtxt.name = ckbxidx;
						j.style.display = 'block';
						othrtxt.required = true;
					}
				}				
			} else {
				var ckbxidx = `${checkBoxInfo[0]}_div_other_field`;
				for (const j of otherdivs) {
					if (j.id == ckbxidx){
						// j.name = 'other_field';
						j.style.display = 'none';
						othrtxt.required = false;
					}
				}
			}
		}
	}
}));
