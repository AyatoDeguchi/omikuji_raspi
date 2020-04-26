function func(){
  location.href = "/animation/" + run_id;
}
window.onload = function() {
  setTimeout('func();', 3000);
}
/*
document.getElementById("omikuji_click").onclick = function() {
  setTimeout('func();', 500);
};
*/