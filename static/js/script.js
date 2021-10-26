// css/script.js
// Author: Maurice Vossen
// November 2021



let x = Math.floor(Math.random() * 2);


if(x == 0) {
    $('body').css('background-image', 'url('+encodeURIComponent("/static/img/hero-imageF.jpg")+')');
}
else {
    $('body').css('background-image', 'url('+encodeURIComponent("/static/img/hero-imageF.jpg")+')');
}






// hides toggle navigation menu awehen website is loaded
$('#toggle-menu').hide();


// toggle navigation menu
$('#toggle-button').on('click', function() {

    $('#toggle-menu').slideToggle('slow');

});


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





$(document).on('click', '#flash-messages', function() {

    

});




// hides toggle navigation menu awehen website is loaded
$('.hidden-info').hide();


// toggle navigation menu
$('.expand-info').on('click', function() {


    let x = $('.expand-info').index(this);

    $(".hidden-info").eq(x).slideToggle('slow');


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