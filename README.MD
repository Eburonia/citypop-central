<h1 align="center">Citypop Central - Japanese Songs Database</h1>

<!-- Responsive Image -->
<img src="assets/images-readme/responsive.png" alt="Responsive design of the website">


<!-- Links -->
View the Live project on Heroku [link](https://citypop-central.herokuapp.com/)<br>
View the GitHub Respository [link](https://github.com/Eburonia/citypop-central/)

<!-- About -->
## About
Citypop Central is a database storing information about Japanese songs. Most of the songs stored in our database are a mix of Japanese Jazz, Soul, Funk, Disco, or Synth-Pop from the '70s and '80s. These songs are better known under the genre Citypop. 

Back in the '80s, Japan had a very strong economy and this era was known as the 'Bubble economy' after. Everybody had a good income, poverty almost did not exist and a lot of money was spent during those years. Life was good, especially in the nightlife districts of Tokyo and other big Japanese cities. It was during those years that the Citypop genre became very popular. 

The lyrics in a Citypop song translated the spirit of the Japanese people at that time. Most songs are about a bright future, optimism, and a glamorous lifestyle. This all ended around the year 1991 when the Tokyo stock exchange, the Nikkei had plummeted to half. The glamorous lifestyle of the 80s was over and many Japanese people had lost their job and did not know what the future would bring. Together with this economic crash, the City pop genre disappeared making space for new types of music genres at that time.

Citypop was never popular in the Western world in the '80s. But thanks to Youtube these days, people from the West are discovering this music genre in the last couple of years. This database was mainly made to target these people who want to know more about the Citypop genre.

#### More Information
For more information about Citypop, check the following videos on YouTube:  
- A Brief History of Citypop [link](https://www.youtube.com/watch?v=ouXHiSSYwZY)  
- Western Tourists Buying Old Citypop LPs [link](https://www.youtube.com/watch?v=QZsRsccMDm8)  


<!-- Table of Contents -->
## Table of Contents

[User Experience (UX)](#UX)

[Features](#features)

[Data Scheme](#scheme)

[Technologies Used](#technologies)

[Testing](#testing)

[Known Bugs](#bugs)

[Deployment](#deployment)

[Credits](#credits)


<!-- User Experience (UX) -->
<a id="UX"></a>
## User Experience (UX)

### User Stories

#### First-time Visitor Goals

1. As a first-time visitor of the website, I want to understand what the website's purpose is, so I have an idea of whether I ended up in the right place.
   + In the upper left corner of the website's header, the website logo tells the visitor the website name: 'Citypop Central 70's and 80's Japanese Music'.
   + For Japanese visitors or people who can read Japanese, also the Citypop Central was written in Hiragana: 'シティ・ポップ・セントラル.'
   + The search songs text field together with the search button on the index page tells the visitor he can search for songs on the website.
   + Certain keywords are added above the search songs text field to help the visitor use the search function on the website.
   + A link to the 'About Citypop Central' page has been added, here the visitor can find more information about the Citypop genre.
   + The Login and Register buttons in the header's upper right corner, tell the visitor this is a website you have to login to add your own songs to the database.


2. As a first-time visitor of the website, I want to navigate easily throughout the website, so I don't get frustrated not knowing where to click.
   + A navigation bar is available on every webpage, in the upper right corner.
   + The website is easily usable for visitors who are only searching for songs. It only has one search page and links to YouTube songs will be opened on a blank page.
   + Search results are limited to a maximum of 10 songs per page. Pagination has been introduced to switch to the next or previous pages.
   + Every search result has a (?) button that expands less relevant information about the song.


3. As a first-time visitor of the website, I want to target specific songs, so I don't need to scroll through a whole list of songs before I find my desired end result.
   + Visitors can search under the following keywords: Artist name, Song name, Genre, Release Year, Album Name, Uploaded By, and Upload Date.


4. As a first-time visitor of the website, I not only want to find information about songs, but I also want to listen to the songs in a convenient way.
   + Every search record indicates the Artist's name and Song name at the top of every search record. A YouTube icon in front of the Artist's name has been implemented telling the      + visitor this is a clickable link. This link will redirect you to the song's Youtube page.
   + The visitor stays on the website and will be redirected to a blank Citypop Central webpage including the embedded YouTube video. Every song automatically starts so visitors don't have to press the YouTube play button.


5. As a first-time visitor of the website, I want to see the album cover.
   + For every search record, you can press the album image and a larger size image will appear on the screen.


6. As a first-time visitor of the website, I might want to contact the website owner, so I can ask them a question or give them some recommendations.
   + On the bottom of the index page, inside the search function division, links to the website's social media accounts are indicated. By clicking on the links the visitor will be      + redirected to them on a blank page. Here the visitor can send direct messages to the website owner.



#### Returning Visitor Goals
1. As a returning visitor of the website, I want to be able to not only search song information, but also add my own (favorite) songs to the database.
   + Every visitor first needs to create their own user account in order to add and manage songs. In the upper right corner of the header, it clearly states a 'Register' button. By clicking on this button, a visitor can create his own user account.
   + When registered, visitors become users and are now able to maintain their profile information, add songs, edit songs, delete songs. This means only songs you have added to the database, not songs uploaded by other users. 


2. As a returning visitor of the website, I want to log out from my user account for safety reasons.
   + When logged in into your user account, it clearly states a logout button in the header's upper right corner.


3. As a returning visitor of the website, I want to know which songs I have uploaded in the past.
   + When logged in, in the upper right side of the navigation bar, a link to 'My Songs' will be available. By clicking this link the user will be redirected to a page that gives a summary of all your added songs in the past.


4. As a returning visitor of the website, I want to delete my profile whenever I want.
   + When logged in, at the bottom of your 'Profile' page, a link has been added which gives you the option to delete your user account. A second link has to be clicked to confirm you want to delete your profile. Your profile will be deleted, but the songs you added to the database will stay inside the database.


5. As a returning visitor of the website, I want to be able to update my user account in case some information about me (e.g. location) has been changed.
   + When logged in, on the 'Profile' page you are able to update your e-mail and the country you live in.


6. As a returning visitor of the website, I want to be able to see information about other users of the website and contact them when needed.
   + Every song record has an information field in the expanded information section of the record stating who uploaded the song record 'Uploaded by'. Visitors and Users can click on the 'Uploaded by' link to see more information about the person. Here is the e-mail of the person who uploaded the song is indicated.



### Colour Scheme
The following colours were used throughout the webpage:
- rgba(): black, used as background colour in the header and forms, and buttons.
- rgba(251, 213, 168, 1): gold, used for logo, login button, division frame borders, textfields, form texts, and socials.
- rgba(255, 113, 151, 1): pink, used for logo, headings, comments forms, register button, hover colour, pagination, buttons.
- rgba(238, 238, 238, 1): white, used for logo, search record information fields, comments on forms.
- rgba(): gray, used in textfields background colour.
- rgba(): red,


    --yellow: rgb(251, 213, 168);
    --pink: rgb(255, 113, 151);
    --white: rgb(238, 238, 238);

<!-- User Experience (UX) -->
<a id="features"></a>
## Features


<!-- Data Scheme -->
<a id="scheme"></a>
## Data Scheme


<!-- Technologies Used -->
<a id="technologies"></a>
## Technologies Used


<!-- Testing -->
<a id="testing"></a>
## Testing


<!-- Known Bugs -->
<a id="bugs"></a>
## Known Bugs


<!-- Deployment -->
<a id="deployment"></a>
## Deployment


<!-- Credits -->
<a id="credits"></a>
## Credits





<!-- Credit: https://www.html5pattern.com/Passwords -->
