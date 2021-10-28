// css/background.js
// Author: Maurice Vossen
// November 2021


let randomBackgroundImage = Math.floor(Math.random() * 2);

if(randomBackgroundImage == 0) {
    $('body').css('background-image', 'url('+encodeURIComponent("/static/img/hero-imageF.jpg")+')');
}
else {
    $('body').css('background-image', 'url('+encodeURIComponent("/static/img/hero-imageD.jpg")+')');
}