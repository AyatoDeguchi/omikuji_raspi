function omikuji_6(){
  console.log("fun_6");
  $('#fadein').fadeIn(1500);
  //$('#fadeout').addClass('fadeout');  // bodyに class="fadeout"を挿入
  setTimeout(function(){
    window.location = '/result/' + run_id + "?num=" + num;  // 秒後に取得したURLに遷移
  }, 1000);
}
function omikuji_5(){
  console.log("fun_5");
  $('.omikuji_img').children('img').attr('src', '/static/image/omikuji_bo_zoom.png');
  document.getElementById('num').innerHTML = num;
  setTimeout('omikuji_6();', 500);
}
function omikuji_4(){
  console.log("fun_4");
  $('.omikuji_img').children('img').attr('src', '/static/image/omikuji_bo_2.png');
  $('.omikuji_img').attr('class', 'omikuji_img');
  setTimeout('omikuji_5();', 500);
}
function omikuji_3(){
  console.log("fun_3");
  $('.omikuji_img').children('img').attr('src', '/static/image/omikuji_hako_inverse_3.png');
  setTimeout('omikuji_4();', 100);
}
function omikuji_2(){
  console.log("fun_2");
  $('.omikuji_img').children('img').attr('src', '/static/image/omikuji_hako_inverse_2.png');
  setTimeout('omikuji_3();', 100);
}
window.onload = function() {
   setTimeout('omikuji_2();', 3000);
   $('#fadeout').removeClass('fadeout');
}
