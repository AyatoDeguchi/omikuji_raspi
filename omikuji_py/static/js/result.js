function func(){
    location.href = "/webclose";
  }
window.onload = function() {
    setTimeout('func();', 4000);
 }