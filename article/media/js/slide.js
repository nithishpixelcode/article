$(document).ready(function() {
	
	// Expand Panel
	$("#open").click(function(){
		if ($(this).attr('status') != "loggedin"){
			$("div#panel").slideDown("slow");
		}
	
	});	
	
	// Collapse Panel
	$("#close").click(function(){
		$("div#panel").slideUp("slow");	
	});		
	
	// Switch buttons from "Log In | Register" to "Close Panel" on click
	$("#toggle a").click(function () {
		if ($(this).attr('status') != "loggedin"){
			$("#toggle a").toggle();
		}
	});		
		
});