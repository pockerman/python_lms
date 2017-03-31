

function show_syllabus(){
	var elem = document.getElementById("id_show_more_btn");

  if (elem.value=="Show More"){
			 $('#syllabus').removeClass('hidden');
			 elem.value = "Show Less";
	}
  else{
		 elem.value = "Show More";
		 $('#syllabus').addClass('hidden');
	}	
}

function show_subtitles(){

	var elem = document.getElementById("id_delivery_mode");
	var delivery_mode = elem.options[elem.selectedIndex].value;

	if(delivery_mode=='2' || delivery_mode=='3'){

		$('#video-subs').removeClass('hidden');
	}
	else{

		$('#video-subs').addClass('hidden');

	}

}
		

function show_modules(){

	var nmodules = document.getElementById("id_nmodules");
	var nModulesSelected = nmodules.options[nmodules.selectedIndex].value;
	var nChoices = 10;

	if(nModulesSelected==='1'){

		//if only one module hide all the remaining
		//modules
		for(var i=2; i<=nChoices; ++i){
			$("#module-"+i).addClass('hidden');
			$('#id_title-'+i).prop('required',false);
			$('#id_overview-'+i).prop('required',false);
		}
	}
	else{

		for(var i=2; i<=parseInt(nModulesSelected); ++i){		
			module= "#module-"+i; 
			$(module).removeClass('hidden'); 
			$('#id_title-'+i).prop('required',true);
			$('#id_overview-'+i).prop('required',true);
		}

		var hide_start_index = parseInt(nModulesSelected)+1;
		for(var i=hide_start_index; i<=nChoices; ++i){
			$("#module-"+i).addClass('hidden');

			console.log("unsetting required for: ",i);
			$('#id_title-'+i).prop('required',false);
			$('#id_overview-'+i).prop('required',false);
		}
	}
}

function show_questions(){

	var nquestions = document.getElementById("id_nquestions");
	var nQuestionsSelected = nquestions.options[nquestions.selectedIndex].value;
	var nChoices = 10;

	if(nQuestionsSelected==='1'){

		//if only one module hide all the remaining
		//modules
		for(var i=2; i<=nChoices; ++i){
			$("#q-"+i).addClass('hidden');
		}
	}
	else{

		for(var i=2; i<=parseInt(nQuestionsSelected); ++i){		
			module= "#q-"+i; 
			$(module).removeClass('hidden'); 
			
		}

		var hide_start_index = parseInt(nQuestionsSelected)+1;
		for(var i=hide_start_index; i<=nChoices; ++i){
			$("#q-"+i).addClass('hidden');	
		}
	}

}

function show_noptions(qindex){

		console.log("Question index: ",qindex);

		var option = document.getElementById("id_qtype_"+qindex);
		var optionSelected = option.options[option.selectedIndex].value;

		var noptions=5;

		if(optionSelected==='radio' || optionSelected==='checkbox'){
			$('#qselect_q_'+qindex).removeClass('hidden');
			$('#qselect_q_'+qindex).prop('required',true); 
		}
		else{

				$('#qselect_q_'+qindex).addClass('hidden');
				$('#qselect_q_'+qindex).prop('required',false); 

				for(var i=1; i<=noptions; ++i){
					var id = '#q-'+qindex+'-opt-'+i;
					$(id).addClass('hidden');
					$(id).prop('required',false);
			}
				
		}
}

function show_option_fields(qindex){

		console.log("Question index: ",qindex);

		var strIdx = "id_qtypeopts-"+qindex;
		var option = document.getElementById(strIdx);
		var optionSelected = option.options[option.selectedIndex].value;
		var noptions=5;

		if(optionSelected==='none-n-opts'){

			for(var i=1; i<=noptions; ++i){
				var id = '#q-'+qindex+'-opt-'+i;
				$(id).addClass('hidden');
				$(id).prop('required',false);
			}

			return;
		}

		var noptions_selected = parseInt(optionSelected);

		for(var i=1; i<=noptions_selected; ++i){
			var id = '#q-'+qindex+'-opt-'+i;
			console.log("showing field: ",id);
			$(id).removeClass('hidden');
			$(id).prop('required',true);

		}

		for(var i=noptions_selected+1; i<=noptions; ++i){

			var id = '#q-'+qindex+'-opt-'+i;
			$(id).addClass('hidden');
			$(id).prop('required',false);
		}
}
