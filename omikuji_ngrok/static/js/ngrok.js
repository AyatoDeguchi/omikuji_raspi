window.onload = function() {
    var parameter = {"ngrok_url": ngrok_url};
    exePHPFunc_ngrok_update(parameter).done(function(data_status){
      console.log("data_status:"+data_status);
    });
}


// deactivatedにする
function exePHPFunc_ngrok_update(parameter)
{
  var defer = $.Deferred();
	$.ajax({
		url: "http://my-16421.azurewebsites.net/omikuji/api/ngrok_update.php",
		type: "POST",
  	    data: parameter,
		scriptCharset: 'utf-8',
		success: defer.resolve,
	});
	return defer.promise();
}