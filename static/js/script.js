// css/script.js
// Author: Maurice Vossen
// November 2021

// hides toggle navigation menu awehen website is loaded
$('#toggle-menu').hide();


// toggle navigation menu
$('#toggle-button').on('click', function() {

    $('#toggle-menu').slideToggle('slow');

});


$(document).on('click', '.toggle-menu-item', function(){
    
    let clickedItem = $('.toggle-menu-item').index(this);

    switch(clickedItem) {

        case 0:
            window.open('/', '_parent');
            break;

        case 1:
            window.open('/about', '_parent');
            break;

        case 2:
            window.open('/contact', '_parent');
            break;

        case 3:
            window.open('/login', '_parent');
            break;
          
      } 

});
