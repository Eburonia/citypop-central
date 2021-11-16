// css/script.js
// Author: Maurice Vossen
// November 2021


// Random number between 0 and 4
let randomBackgroundImage = Math.floor(Math.random() * 5);


// Set one of the five random background images
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


// Hides delete song link
$('.delete-link').hide();


// Shows conformation link to delete the song (trash icon)
$(document).on('click', '.delete-song-check', function(){

    let clickedSongToDelete = $('.delete-song-check').index(this);

    if($('.delete-link').is(':visible')) {

        $('.delete-link').eq(clickedSongToDelete).hide();
    }

    else {

        $('.delete-link').eq(clickedSongToDelete).show();

    }

});



// Hides confirmation delete song link
$('#confirm-delete-song').hide();


// Shows conformation delete song link
$(document).on('click', '#delete-song-link', function() {

    if($('#confirm-delete-song').is(":hidden")) {
        $('#confirm-delete-song').show();
    }
    else {
        $('#confirm-delete-song').hide();
    }
    
});


// Hides confirmation delete profile link
$('#confirm-delete-profile-link').hide();


// Shows conformation delete profile link
$(document).on('click', '#delete-profile-button', function() {

    if($('#confirm-delete-profile-link').is(":hidden")) {
        $('#confirm-delete-profile-link').show();
    }
    else {
        $('#confirm-delete-profile-link').hide();
    }
    
});


// Hides toggle navigation menu when website is loaded
$('#toggle-menu').hide();


// Toggle navigation menu
$('#toggle-button').on('click', function() {

    $('#toggle-menu').slideToggle('slow');

});


// Toggle more information about song on results page
$(document).on('click', '.expand-info', function() {

    $('.song-info-toggle').hide();
    let clickedIcon = $('.expand-info').index(this);

    if($('.song-info-toggle').is(':visible')) {
        $('.song-info-toggle').eq(clickedIcon).hide();
        }

    else {
        $('.song-info-toggle').eq(clickedIcon).show();
      }

});


// hides flash message when close icon is clicked
$(document).on('click', '.fa-times', function() {

    let flashMessage = $('.fa-times').index(this);

    $(".flash-messages").eq(flashMessage).hide();

});


// hides toggle navigation menu when a website is loaded
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


// Load album image when loading the edit or add song page
let album_image = $('#album_image').val();
$('#album_image_added > img').attr("src", album_image);


// Show album image when leaving album image field
$('#album_image').blur(function() {

    album_image = $('#album_image').val();

    if(album_image == '') {
        $('#album_image_added > img').attr("src","static/img/no-cover.jpg");
    }
    else {
        $('#album_image_added > img').attr("src", album_image);
    }

});