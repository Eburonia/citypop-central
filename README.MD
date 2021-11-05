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




#### Colour Scheme
The following colours were used throughout the webpage:
- rgba(0, 0, 0, 0.9): black transparent, used as background colour in the header and forms, and buttons.
- rgba(251, 213, 168, 1): gold, used for logo, login button, division frame borders, textfields, form texts, and socials.
- rgba(255, 113, 151, 1): pink, used for logo, headings, comments forms, register button, hover colour, pagination, buttons.
- rgba(238, 238, 238, 1): white, used for logo, search record information fields, comments on forms.
- rgba(255, 255, 255, 0.2): gray transparent, used in textfields background colour.
- rgba(255, 0, 0, 1): red, used on critial links e.g. deleting your profile or deleting a song.
- rgba(135, 206, 235, 1): skyblue, used for flash messages in case passwords don't match on the register page. 

<img src="" alt="Colour scheme"><br>
<sub>Colour scheme</sub>



#### Typography
The '[Nunito](https://fonts.google.com/specimen/Nunito)' font was implemented from the Google Fonts website and used throughout the whole website including the website logo.
Sans-serif has been set as back-up font.

<img src="" alt="Nunito font-type"><br>
<sub>Nunito font-type</sub>


#### Imagery
- Five different implemented background images. Background images are all street scenes from Tokyo made by the website owner. Colours adjusted in such a way it won't distract the information in the foreground.
- All Album Cover images are implemented from the Discogs.com website. This is not a proper way of doing this because we are using somebody else its data, but because we don't have a server where we can upload and read images it's the only solution for the moment.


#### Wireframes
Wireframes beloning to the website's project have been made in [Adobe XD](https://www.adobe.com/products/xd.html).
The wireframes are implemeted in markdown files and can be found over here:
- Wireframes of the 'Index' Page - [link]()
- Wireframes of the 'Results' Page - [link]()
- Wireframes of the 'Register' Page - [link]()
- Wireframes of the 'Login' Page - [link]()
- Wireframes of the 'About' Page - [link]()
- Wireframes of the 'Profile' Page - [link]()
- Wireframes of the 'My Songs' Page - [link]()
- Wireframes of the 'Add Song' Page - [link]()
- Wireframes of the 'Userinfo' Page - [link]()


All wireframes were designed for three different devices:
- Desktop - Web: maximum viewport width 1920px
- iPad - Nexus 9: maximum viewport width 768px
- iPhone - 12 Pro Max: maximum viewport width 428px


#### Mockups
Due to the limited available time of the web developer, mockups have not been created.
Instead, an image of the responsive design has been added on top of this README file.


<!-- User Experience (UX) -->
<a id="features"></a>
## Features


### Header
A header has been added on top of every page and exists out of the website logo, and a navigation bar. The background colour used for the header is a black transparent colour as described in the colour scheme section in this README file. The navigation bar will change to a 'hamburger-style' navigation menu on smaller devices (e.g. iPad or smartphone). By hovering the navigation bar anchor links, the links will highlight and make it clear to the end-user this is a clickable link.
The company logo on the top left-hand side of the header has a clickable anchor link assigned to it which will always redirect the website to the index page. The Company logo will automatically resize for smaller devices. 


### Footer
A footer has been added on the bottom of the 'Index' and 'Results' page and exists out of social media links, and a copyright notice. The social media links are styled in gold colour. By hovering the social media link icons, the colour will highlight in pink colour as described in the colour scheme section of this README file and makes it clear to the end-user these are clickable links. The icons used for the social media links are directly loaded from the [fontawesome](https://www.fontawesome.com) website. All social media links will be opened on a new blank page. A clear copyright notice is visible at the bottom of the footer.


### About Page
The 'About' page gives information about the purpose of the website. Some history and background information about the Citypop genre are stated on this page. Also embedded are two YouTube videos about the history of Citypop and a video of Western tourists buying Citypop records at a local used record store in the Shibuya district of Tokyo. 


### Index Page
The 'Index' page is the most important page on the website and starts with a welcoming statement to every visitor. Below the statement, a search bar indicated to search songs. To help new visitors to add correct keywords in the search bar, example search keywords are indicated above the search bar.  Then a summary of the 8 latest songs added to the database is shown to the visitor. These are clickable and will open a new blank page to the YouTube embedded video. The bottom of the page ends with links to the website's socials pages.

### Results Page
The 'Results' page will show up at the moment a visitor has added a search query. The results found in the database will then show up on the screen. Pagination implemented limiting the number of search results to 10 search records per page. The top of the page indicates the number of results found in the database. The current indicated results are shown on-screen also. All search records show the following information: Artist Name, Song Name, Genre, Release Year, Album Name. An expanded information button (question mark icon) to show more additional information about the song is introduced. By clicking this icon more information will show up on the screen. This information is: Song Length, Uploaded By, Upload Date, Edit Date. By clicking the Artist Name and Song Title at the top of every search query, the visitor will be automatically redirected to the YouTube song page which will run the song automatically. An image of the Album Cover of the song's album is indicted. By clicking the album image a larger image will show op on screen.



### Register Page

### Login Page

### Profile Page

### My Songs Page

### Add Song Page

### User Info Page

### Flash Messages




<!-- Data Scheme -->
<a id="scheme"></a>
## Data Scheme


<!-- Technologies Used -->
<a id="technologies"></a>
## Technologies Used


<!-- Testing -->
<a id="testing"></a>
## Testing

### Functionality Checklist

#### Common

**(checked)**

- Check aria labels.
- Check aria labels start with capitalized letter.
- Check alternative 'alt' text images.
- Check available title tags.
- Check title tags all start with capitalized letter.


#### Background Images
- Check whether background images size are around 500 kB.
- Check whether all 5 background images randomize will show up.
- Check whether background images show up properly show up on smaller devices.


#### Header/Navigation Var
- Check whether the header is always on top of the page.
- Check whether website logo links back to the index page.
- Check for dead links.
- Check the responsiveness of the navigation bar (change to hamburger-style navigation for minimum 320px width).
- Check whether there is overflow while reducing the screen size.
- Check navigation hover links.
- Check 'About' link always shows up.
- Check 'Profile', 'My Songs', 'Add Song' links show up when logged in.
- Check 'Logout' button shows up when logged in.
- Check whether toggle button functions.


#### Footer
- Check whether footer is on the bottom of the 'Index' and 'Results' page.
- Check whether all social media links are working properly and are opening a new blank page.
- Check whether the social links change colour when hovering.
- Check for dead links.
- Check the responsiveness on smaller devices (min. 320px width).


#### About Page
- Check spelling of the page.
- Check responsiveness of page.
- Check sizing of the embedded Youtube videos.
- Check funtionality of videos.
- Check the video description.


#### Index Page
- Check responsiveness of page.
- Check latest song links function and open in new screen.


#### C.R.U.D. Index Page
- Check whether records show up when searching the following keywords: Artist Name, Song Name, Genre, Release Year, Album Name, Uploaded By, Upload Date.
- Check whether a song added to the database show up to the latest songs summary.


#### Results Page
- Check responsiveness of page.
- Check whether the 'Expand for more information' icon (question mark) functions properly.
- Check whether 'Uploaded By' link opens a new blank page.
- Check whether all show song information is correct.
- Check whether there is no text overflow.
- Check whether the Youtube link functions and opens a new blank page.
- Check whether 'Edit' and 'Delete' icon show up when logged in and check whether the function properly.


#### C.R.U.D. Results Page
- Check number of results (records) indicated match the real shown results on screen.
- Check pagination functions properly.
- Check whether maximum 10 records show up on screen.
- Check whether 'Edit Date' shows up when the song has been edited.
- Check manipulation of the searchbar search keys won't give wrong results or errors. 

<img src="" alt="Edit and Delete Icons"><br>
<sub>Edit and Delete Icons</sub>


#### Profile Page
- Check responsiveness of page.
- Check all country names are capitalized and alphabatically sorted.
- Check the defensive pattern functions properly for the email textfield.
-

#### C.R.U.D. Profile Page
- Check correct username shows up.
- Check whether delete you profile function works properly.
- Check whether all fields are updated in the database when changed.

<img src="" alt="Profile Page"><br>
<sub>Edit and Delete Icons</sub>


#### My Songs Page
- Check responsiveness of page.
- Check whether Artist Name and Songs Name are properly indicated.
- Check whether upload date and edit date are indicated.
- Check colour changes when hovering.
- Check alphabetical sort.


#### C.R.U.D. My Songs Page
- Check whether all your songs show up.
- Check whether links open in new blank page and loads the correct information form the database.


<img src="" alt="My Songs Page"><br>
<sub>My Songs Page</sub>





#### Add Song Page


#### Login Page


#### Register Page


#### Youtube Page


#### Userinfo Page


#### Flash Messages

<img src="" alt="">
<span>Show header result image here</span>



<!-- Known Bugs -->
<a id="bugs"></a>
## Known Bugs


<!-- Deployment -->
<a id="deployment"></a>
## Deployment


<!-- Credits -->
<a id="credits"></a>
## Credits



### Acknowledgements
- Thanks to my personal mentor Victor Miclovich for answering my questions and giving feedback to this project.
- The many free coding forums on the internet, especially [Stackoverflow.com](https://www.stackoverflow.com/) for providing answers to my coding questions. Most of my questions were already asked by other users of the stackoverflow website, making it easy to find quick answers.



<!-- Credit: https://www.html5pattern.com/Passwords -->
