function func(){
  location.href = "/animation/" + run_id;
}
window.onload = function() {
  run_id_view.innerHTML = run_id.slice( -3 );
  setTimeout('func();', 3000);
}
/*
document.getElementById("omikuji_click").onclick = function() {
  setTimeout('func();', 500);
};
*/
