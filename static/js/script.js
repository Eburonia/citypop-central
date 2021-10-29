// css/script.js
// Author: Maurice Vossen
// November 2021


let randomBackgroundImage = Math.floor(Math.random() * 5);

if(randomBackgroundImage == 0) {
    $('body').css('background-image', 'url('+encodeURIComponent("/static/img/background1.jpg")+')');
}

else if(randomBackgroundImage == 1) {
    $('body').css('background-image', 'url('+encodeURIComponent("/static/img/background2.jpg")+')');
}

else if(randomBackgroundImage == 2) {
    $('body').css('background-image', 'url('+encodeURIComponent("/static/img/background3.jpg")+')');
}

else if(randomBackgroundImage == 3) {
    $('body').css('background-image', 'url('+encodeURIComponent("/static/img/background4.jpg")+')');
}

else {
    $('body').css('background-image', 'url('+encodeURIComponent("/static/img/background5.jpg")+')');
}



$('.delete-link').hide();


$(document).on('click', '.delete-song-check', function(){

    let x = $('.delete-song-check').index(this);

    if($('.delete-link').is(':visible')) {

        $('.delete-link').eq(x).hide();
    }

    else {

        $('.delete-link').eq(x).show();

    }

});









$('#confirm-delete-profile-button').hide();


$(document).on('click', '#delete-profile-button', function() {

    if($('#confirm-delete-profile-button').is(":hidden")) {
        $('#confirm-delete-profile-button').show();
    }
    else {
        $('#confirm-delete-profile-button').hide();
    }
    
});



// hides toggle navigation menu awehen website is loaded
$('#toggle-menu').hide();


// toggle navigation menu
$('#toggle-button').on('click', function() {

    $('#toggle-menu').slideToggle('slow');

});





$( ".toggle-part" ).hide();


$(document).on('click', '.song-toggle-button', function(){

    let x = $('.song-toggle-button').index(this);

    $(".toggle-part").eq(x).slideToggle();

});



$('.song-info-toggle').hide();


$(document).on('click', '.expand-info', function() {


    $('.song-info-toggle').hide();

  let x = $('.expand-info').index(this);

  if($('.song-info-toggle').is(':visible')) {
      $('.song-info-toggle').eq(x).hide();
      }
  else {
   
      $('.song-info-toggle').eq(x).show();
      
      }

});





$(document).on('click', '.fa-times', function() {

    let flashMessage = $('.fa-times').index(this);

    $(".flash-messages").eq(flashMessage).hide();

});




// hides toggle navigation menu awehen website is loaded
$('.hidden-info').hide();


// toggle navigation menu
$('.expand-info').on('click', function() {

    let x = $('.expand-info').index(this);

    $(".hidden-info").eq(x).slideToggle('slow');

});



// Check whether the passwords are used
$('#password').blur(function() {


    if($('#password').val() != $('#password-confirm').val()) {
        $(".form-message").css("display", "block");
    }
    else {
        $(".form-message").css("display", "none");
    }

});



// Check whether the passwords are used
$('#password-confirm').blur(function() {


    if($('#password').val() != $('#password-confirm').val()) {
        $(".form-message").css("display", "block");
    }
    else {
        $(".form-message").css("display", "none");
    }

});



// Check whether the passwords are used
$('#album_image').blur(function() {

    $('#album-cover-img').attr("src", "https://img.discogs.com/Z_SZTPoyahu-UB2y_IsuaIWsURE=/fit-in/600x593/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-6870389-1444305354-8612.jpeg.jpg");

});


