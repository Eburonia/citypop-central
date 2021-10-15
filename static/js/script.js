// css/script.js
// Author: Maurice Vossen
// November 2021

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