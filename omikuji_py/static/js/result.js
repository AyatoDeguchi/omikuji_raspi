function func(){
    location.href = "/webclose";
}

window.onload = function() {
  run_id_view.innerHTML = run_id.slice( -3 );
  /*var parameter = {"run_id": run_id,"num": num};
  exePHPFunc_deactivated(parameter).done(function(data_status){
    console.log("data_status:"+data_status);
  });*/
  setTimeout('func();', 4000);
}


// deactivatedにする
function exePHPFunc_deactivated(parameter)
{
  var defer = $.Deferred();
	$.ajax({
		url: "http://my-16421.azurewebsites.net/omikuji/api/deactivated.php",
		type: "POST",
  	data: parameter,
		scriptCharset: 'utf-8',
		success: defer.resolve,
	});
	return defer.promise();
}
