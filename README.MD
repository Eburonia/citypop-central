<h1 align="center">Citypop Central - Japanese Songs Database</h1>

<!-- Responsive Image -->
<img src="static/readme-images/responsive.jpg" alt="Responsive design of the website">


<!-- Links -->
View the Live project on Heroku [link](https://citypop-central.herokuapp.com/)<br>
View the GitHub Respository [link](https://github.com/Eburonia/citypop-central/)


<!-- About -->
## About
The Citypop Central website contains information about Japanese songs and a link to the song's YouTube page. In our database, you find songs that are a mix of Jazz, Soul, Funk, Disco, or Synth-Pop from the '70s and '80s.  Combined with Japanese lyrics is this genre better known under the name 'Citypop.'

Back in the '70s and '80s, Japan had a strong economy that eventually would collapse. This era was better known as the 'Bubble economy.' Everybody had a good income, poverty almost did not exist, and a lot of money was made and spent during those years. Life was good, especially in the nightlife districts of Tokyo and other big Japanese cities. It was during those years that 'Citypop' became very popular in Japan.

The lyrics in a typical 'Citypop' song translated the spirit of the Japanese people at that time. The songs are about a bright future, optimism, and a glamorous lifestyle. All this ended around 1991 when the Tokyo stock exchange, the 'Nikkei' had plummeted to half. The glamorous lifestyle of the '80s was over. Many Japanese people lost their job, many lost money in a housing crisis,  and most did not know what the future would bring. Together with this economic tragedy, the 'Citypop' genre disappeared from the mainstream, making space for new types of music genres.

'Citypop' was never popular in the Western world in the '70s and '80s. But thanks to Youtube, people from the West are discovering this music genre. The purpose of this website is to target those people who want to know more about the 'Citypop' genre and who want to listen to typical 'Citypop' songs.


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

#### Visitor User Goals

1. As a visitor of the website, I want to understand what the website's purpose is.
2. As a visitor of the website, I want to navigate easily throughout the website, so I don't get frustrated not knowing where to click.
3. As a visitor of the website, I want to target specific songs, so I don't get lost when I have to scroll through all available songs on the website.
4. As a visitor of the website, I not only want to find information about the songs, but I also want to listen to the songs.
5. As a visitor of the website, I want to see the album cover of the song.
6. As a visitor of the website, I might want to contact the website owner, so I can ask a question or give some feedback.


#### Returning Visitor User Goals
1. As a returning visitor of the website, I want to be able to not only search for song information or listen to the songs but also want to add my own (favorite) songs to the database.
2. As a returning visitor of the website, I want to log out from my user account for safety reasons.
3. As a returning visitor of the website, I want to know which songs I have uploaded in the past.
4. As a returning visitor of the website, I want to delete my profile whenever I want.
5. As a returning visitor of the website, I want to be able to update my user account in case some information about me (e.g. location) has been changed.
6. As a returning visitor of the website, I want to be able to see information about other users of the website and contact them when needed.


#### Administrator User Goals
1. As an administrator of the website, I want to be able to adjust all uploaded songs, so I can change them for whatever reason.
2. As an administrator of the website, I want to adjust other information which is relevant to the website.


#### Colour Scheme
The following colours were used throughout the webpage:
- rgba(0, 0, 0, 0.9): black transparent, used as background colour in the header and forms, and buttons.
- rgba(251, 213, 168, 1): gold, used for logo, login button, division frame borders, textfields, form texts, and socials.
- rgba(255, 113, 151, 1): pink, used for logo, headings, comments forms, register button, hover colour, pagination, buttons.
- rgba(238, 238, 238, 1): white, used for logo, search record information fields, comments on forms.
- rgba(255, 255, 255, 0.2): gray transparent, used in textfields background colour.
- rgba(255, 0, 0, 1): red, used on critial links e.g. deleting your profile or deleting a song.
- rgba(135, 206, 235, 1): skyblue, used for flash messages in case passwords don't match on the register page. 

<img src="static/readme-images/colour-scheme.jpg" alt="Colour scheme"><br>
<sub>Colour scheme</sub>



#### Typography
The '[Nunito](https://fonts.google.com/specimen/Nunito)' font was implemented from the Google Fonts website and used throughout the whole website including the website logo.
Sans-serif has been set as back-up font.

<img src="static/readme-images/font-type.jpg" alt="Nunito font-type"><br>
<sub>Nunito font-type</sub>


#### Imagery
- Five different implemented background images. Background images are all street scenes from Tokyo made by the website owner. Colours adjusted in such a way it won't distract the information in the foreground.
- All Album Cover images are implemented from the Discogs.com website. This is not a proper way of doing this because we are using somebody else its data, but because we don't have a server where we can upload and read images it's the only solution for the moment.


#### Wireframes
Wireframes beloning to the website's project have been made in [Adobe XD](https://www.adobe.com/products/xd.html).
The wireframes are implemeted in markdown files and can be found over here:
- Wireframes of the '404' Page - [link]()
- Wireframes of the 'About' Page - [link]()
- Wireframes of the 'Add Song' Page - [link]()
- Wireframes of the 'Edit Song' Page - [link]()
- Wireframes of the 'Login' Page - [link]()
- Wireframes of the 'My Songs' Page - [link]()
- Wireframes of the 'Profile' Page - [link]()
- Wireframes of the 'Register' Page - [link]()
- Wireframes of the 'Results/Index' Page - [link]()
- Wireframes of the 'Settings' Page - [link]()
- Wireframes of the 'Userinfo' Page - [link]()
- Wireframes of the 'Users' Page - [link]()
- Wireframes of the 'Youtube' Page - [link]()


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
On the 'Register' page, you can create a Citypop Central user account. Indicated are necessary information fields like username, password, email address, the country you live in, and gender. On top of every text field, given is some extra information to the end-user to add the correct information. When submitting the form, the back-end of the website checks whether the submitted username already exists or not. There is a double check when adding a password. New users have to add the passwords twice. This is to check whether the user did not make a typo when adding the password. A blue message will pop up under the password text field, warning the user both passwords don't match. Add a valid email address. Select the country you are currently living in. The summary of all countries and genders is coming from the database, making it easy to update them in case needed in the future. For now, users can communicate with each other by email. Maybe new users don't want this and for that reason, an option is given to not share your email address on your user information page. Indicated is a link to the login page in case a user already has an account.


### Login Page
On the 'Login' page, existing users login into their Citypop Central account. The correct username or password needs to be added to the form to access the user account. A flash message will pop up when submitted an incorrect username, or password. The flash message will not tell whether the username or password was incorrect.


### Profile Page
On the 'Profile' page, you can update some of your user information like your email address, the country you are living in, and whether you want to share your email address with other users or not. You cannot update your username and gender. You are also able to delete your profile by clicking the link at the bottom of the form. By clicking this link, a second link will pop up to confirm to delete your profile. The songs you have added to the database will stay in the database under your username.


### My Songs Page
The 'My Songs' page indicates a summary of the uploaded songs by the user. Alphabetically sorted the Artist's name and Song name. By clicking on one of the songs, the user will be re-directed to the edit page of the song. Here the user can change information or even delete the song.


### Add Song Page
On the 'Add song' page, the user can add songs to the Citypop Central database. The user needs to add the necessary song information into a form. On top of every text field, given is some extra information to the end-user to add the correct information. Regular expression is introduced to force the user to add correct data to the database. Because it is not possible to store images in the database, all album images have to be loaded from the discogs.com website by adding the link to the image.
All songs can be listened to on Youtube by adding the video link ID. This link can be found in the address bar of every YouTube video and will look like this: 'yOulloW7lEA'.


### User Info Page
The 'User Information' page gives information about a user to other users and is not visible for only visitors of the website. Users need to be logged in to see user information. A user is able to turn off the visibility of their email address on their profile page. To access the user information page, click on the expand link (?) of a song to see which user uploaded the song. By clicking on the username the user information page will pop up.


### Flash Messages
Flash messages will pop up with useful information for the user and can be closed by clicking the cross button.


### 404 Page
The 404 page is a simple-looking page stating the 404 error message and link to re-direct the visitor/user back to the index page.


### Responsiveness
All pages are responsive on all devices. Designed for minimum viewport width of: 320px.


### Accessibility
* All images have been foreseen with an alternative (alt) text in case the image cannot be loaded. This also helps the screen readers.
* Aria-labels have been introduced where needed to give important information to the screen readers.


### Future Features
* A message function for users to communicate with each other instead of using e-mail communication.
* Implementation of an image database instead of loading album images from the discogs.com website.
* Sub-divide the JavaScript code, all code is now loaded on all pages.


<!-- Data Scheme -->
<a id="scheme"></a>
## Data Scheme

The MongoDB Data Scheme Citypop Central
<img src="static/readme-images/data-scheme.jpg" alt="Data Scheme">


<!-- Technologies Used -->
<a id="technologies"></a>
## Technologies Used

### Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [jQuery](https://en.wikipedia.org/wiki/JQuery)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine))


### Frameworks, Libraries and Programs Used
- [jQuery v3.5.1](https://jquery.com/download/) - jQuery which is a JavaScript Library mainly used for manipulating the HTML DOM tree, is used throughout the website especially on the 'Practice' and 'Editor' page.
- [Font Awesome](https://www.fontawesome.com/) - Font Awesome icons are used on the website for linking to the social media pages and in h2 headings.
- [Git](https://git-scm.com/) - Git was used for version control and code change tracking of the website project. The terminal in Gitpod was used to commit and to push the project to the Github repository.
- [Github](https://github.com/) - The project code has been stored on the Github website.
- [GitPod](https://www.gitpod.io/) - GitPod was used for creating the code, testing of the website, commiting, and pushing the code to the github repository.
- [Heroku](https://www.heroku.com/) - The project has been imported from the Github website to the Heroku website which allows Python related projects.
- [Adobe XD](https://www.adobe.com/products/xd.html) - Adobe XD was used to create the website's Wireframes. To see the Wireframes, go to the Design section above to see the results.
- [Photopea.com](https://www.photopea.com/) - The Photopea website is used for creating the website logo, 'Manual' page images and README images.
- [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) - Flask is a micro web framework written in Python used for interaction between front-end and back-end of the website.


### Database
- [MongoDB](https://en.wikipedia.org/wiki/MongoDB) - The website uses the document-oriented database MongoDB.


<!-- Testing -->
<a id="testing"></a>
## Testing

### Functionality Checklist

#### Common

**(checked)**

- Check aria labels.
- Check aria labels start with a capitalized letter.
- Check alternative 'alt' text images.
- Check available title tags.
- Check title tags all start with a capitalized letter.
- Check whether page titles are loaded correctly.
- Check all needed CSS files are imported properly.
- Check ghost CSS code.
- Check commented out code.
- Check comments added to code files.
- Check for non-functioning Python code.
- Turn off Flask debug mode.


#### Background Images
- Check whether background image sizing is around 500 kB.
- Check whether all 5 background randomized images will show up.
- Check whether background images show up properly show up on smaller devices.


#### Header/Navigation Bar
- Check whether the header is always on top of the pages.
- Check whether the website logo links back to the index page.
- Check for dead links.
- Check the responsiveness of the navigation bar (change to hamburger-style navigation for minimum 320px width).
- Check whether there is overflow while reducing the screen size.
- Check navigation hover-links.
- Check the 'About' link always shows up.
- Check the 'Profile,' 'My Songs,' 'Add Song' links show up when logged in.
- Check the 'Logout' button shows up when logged in.
- Check whether the toggle button functions properly.


#### Footer
- Check whether the footer is on the bottom of the 'Index' and 'Results' page.
- Check whether all social media links are working properly and are opening a new blank page.
- Check whether the social links change colour when hovering.
- Check for dead links.
- Check the responsiveness on smaller devices (min. 320px width).


#### About Page
- Check the spelling of the page.
- Check the responsiveness of the page.
- Check the sizing of the embedded Youtube videos.
- Check the functionality of the videos.
- Check the video description.

<img src="" alt="About Page"><br>
<sub>About Page</sub>


#### Index Page
- Check the responsiveness of the page.
- Check the latest song links function and open in a new screen.


#### C.R.U.D. Index Page
- Check whether records show up when searching the following keywords: Artist Name, Song Name, Genre, Release Year, Album Name, Uploaded By, Upload Date.
- Check whether a song added to the database shows up to the latest songs summary.

<img src="" alt="Index Page"><br>
<sub>Index Page</sub>


#### Results Page
- Check the responsiveness of the page.
- Check whether the 'Expand for more information' icon (question mark) functions properly.
- Check whether the 'Uploaded By' link opens a new blank page.
- Check whether all show song information is correct.
- Check whether there is no text-overflow.
- Check whether the Youtube link functions and opens a new blank page.
- Check whether the 'Edit' and 'Delete' icons show up when logged in and check whether they function properly.


#### C.R.U.D. Results Page
- Check the number of results (records) indicated to match the real shown results on the screen.
- Check pagination functions properly.
- Check whether a maximum of 10 records shows up on the screen.
- Check whether 'Edit Date' shows up when the song has been edited.
- Check manipulation of the search bar search keys won't give wrong results or errors. 

<img src="" alt="Edit and Delete Icons"><br>
<sub>Edit and Delete Icons</sub>


#### Profile Page
- Check the responsiveness of the page.
- Check all country names are capitalized and alphabetically sorted.
- Check the regular expression functions properly for the email text field.


#### C.R.U.D. Profile Page
- Check correct username shows up.
- Check whether the 'Delete your profile' link function works properly.
- Check whether all fields are updated in the database when changed.

<img src="" alt="Profile Page"><br>
<sub>Profile Page</sub>


#### My Songs Page
- Check the responsiveness of the page.
- Check whether Artist Name and Songs Name are properly indicated.
- Check whether the upload date and edit date are indicated.
- Check colour changes when hovering.
- Check alphabetical sort.


#### C.R.U.D. My Songs Page
- Check whether all your songs show up.
- Check whether links open on a new blank page and loads the correct information form the database.

<img src="" alt="My Songs Page"><br>
<sub>My Songs Page</sub>


#### Add Song Page
- Check the responsiveness of the page.
- Check whether the input fields match with the Edit Songs Page.
- Check field description is understandable for a visitor.
- Check the regular expressions.


#### C.R.U.D. Add Song Page
- Check whether the added song is in the database.

<img src="" alt="Add Song Page"><br>
<sub>Add Song Page</sub>


#### Login Page
- Check the responsiveness of the page.
- Check the link to the Register page functions.


#### C.R.U.D. Login Page
- Check whether login functions.

<img src="" alt="Login Page"><br>
<sub>Login Page</sub>


#### Register Page
- Check the responsiveness of the page.
- Check the link to the Login page functions.
- Check the regular expressions.
- Check password match functionality.

<img src="" alt="Register Page"><br>
<sub>Register Page</sub>


#### Youtube Page
- Check the responsiveness of the page.
- Check song autoplay.

<img src="" alt="Youtube Page"><br>
<sub>Youtube Page</sub>


#### Userinfo Page
- Check the responsiveness of the page.
- Check all showed information is correct.
- Check e-mail address is hidden for non-users (visitors).
- Check e-mail address is hidden when the user turned it off on the Profile page.
- Check non-existing user return message.

<img src="" alt="Userinfo Page"><br>
<sub>Userinfo Page</sub>


#### Flash Messages
- Check the responsiveness of the flash messages.
- Check flash messages all start with a capitalized letter.
- Check close message is functioning.
- Check whether flash messages appear after a user action. 

<img src="" alt="Flash messages">
<span>Flash Messages</span>


#### 404-Page
- Check the responsiveness of the page.
- Check 404-page loads when a non-existing page is loaded.
- Check of link redirects to homepage.

<img src="" alt="404 Page">
<span>404 Page</span>


### Usability Testing
- Family and friends were asked to test the website and to navigate through all website pages. Buttons, links, and contact form were tested by them.


### Compatibility Testing
The following browsers were used for compatibility testing:
- Firefox
- Google Chrome
- Microsoft Edge


### Further Testing
The following devices were used for testing the website:
- Desktop: Asus ZenBook (viewport: 1920px * 1080px) 
- Smartphone: Samsung S9+ (viewport: 360px * 740px)
- Smartphone: iPhone 11 (viewport: 414px * 896px)

During the building of the website, [Google Chrome DevTools](https://developer.chrome.com/) was used to simulate different viewport sizes.
The website is designed for a minimum viewport width of 320px (iPhone 5 size).


### Testing Code
The following online validators were used to check whether the website generated any Javascript, html and CSS syntax errors:

#### W3C Markup Validator
[website](https://validator.w3.org/)

W3C Markup Validator, the following pages were checked:
Make sure you are logged in as Admin onto the website when clicking on the links below.
* [about](https://validator.w3.org/nu/?doc=http%3A%2F%2Fcitypop-central.herokuapp.com%2Fadd_song)
* [add_song](https://validator.w3.org/nu/?doc=http%3A%2F%2Fcitypop-central.herokuapp.com%2Fadd_song)
* [edit_song](https://validator.w3.org/nu/?doc=http%3A%2F%2Fcitypop-central.herokuapp.com%2Fedit_song%3Fsong_id%3D617bc16c312ed7617ea2acb4)
* [login](https://validator.w3.org/nu/?doc=http%3A%2F%2Fcitypop-central.herokuapp.com%2Flogin)
* [my_songs](https://validator.w3.org/nu/?doc=http%3A%2F%2Fcitypop-central.herokuapp.com%2Fmy_songs)
* [profile](https://validator.w3.org/nu/?doc=http%3A%2F%2Fcitypop-central.herokuapp.com%2Fprofile%3Fusername%3Dadmin)
* [register](https://validator.w3.org/nu/?doc=http%3A%2F%2Fcitypop-central.herokuapp.com%2Fregister)
* [index](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcitypop-central.herokuapp.com%2F)
* [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcitypop-central.herokuapp.com%2Fresults%3Fsearch%3Dcitypop%26page%3D0)
* [settings](https://validator.w3.org/nu/?doc=http%3A%2F%2Fcitypop-central.herokuapp.com%2Fsettings)
* [userinfo](https://validator.w3.org/nu/?doc=http%3A%2F%2Fcitypop-central.herokuapp.com%2Fuserinfo%3Fuser%3Dmaurice)
* [users](https://validator.w3.org/nu/?doc=http%3A%2F%2Fcitypop-central.herokuapp.com%2Fusers)
* [youtube](https://validator.w3.org/nu/?doc=http%3A%2F%2Fcitypop-central.herokuapp.com%2Fyoutube%3Flink%3Dv6VmbmlUyww)
* 404 Checked by direct input into the validator.

The 'base'html page is loaded into all webpages.

Errors found:
All pages generate Jinja related errors (Validator does not recognize Jinja code).


#### W3C CSS Validator
[website](https://jigsaw.w3.org/css-validator/)

W3C CSS Validator, the following files were checked:
* [about.css](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcitypop-central.herokuapp.com%2Fstatic%2Fcss%2Fabout.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
* [error404.css](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcitypop-central.herokuapp.com%2Fstatic%2Fcss%2Ferror404.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
* [footer.css](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcitypop-central.herokuapp.com%2Fstatic%2Fcss%2Ffooter.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
* [forms.css](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcitypop-central.herokuapp.com%2Fstatic%2Fcss%2Fforms.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
* [header.css](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcitypop-central.herokuapp.com%2Fstatic%2Fcss%2Fheader.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
* [my-songs.css](https://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Fcitypop-central.herokuapp.com%2Fstatic%2Fcss%2Fmy-songs.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=enn)
* [profile.css](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcitypop-central.herokuapp.com%2Fstatic%2Fcss%2Fprofile.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
* [random-songs.css](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcitypop-central.herokuapp.com%2Fstatic%2Fcss%2Frandom-songs.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
* [results.css](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcitypop-central.herokuapp.com%2Fstatic%2Fcss%2Fresults.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
* [settings](https://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Fcitypop-central.herokuapp.com%2Fstatic%2Fcss%2Fsettings.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
* [users](https://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Fcitypop-central.herokuapp.com%2Fstatic%2Fcss%2Fusers.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
* [userinfo.css](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcitypop-central.herokuapp.com%2Fstatic%2Fcss%2Fuserinfo.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
* [youtube.css](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcitypop-central.herokuapp.com%2Fstatic%2Fcss%2Fyoutube.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

Errors found:
Validator does not recognize CSS variables.


#### JSHint Validator
[website](https://www.jshint.com/)

JSHint Validator, the following file was checked:
* script.js

Errors found:
No important errors found.


#### PEP8 Online Check [link](http://pep8online.com)
[website](http://www.pep8online.com/)

PEP8 Online Check, the following file was checked:
* app.py

Errors found:
No important errors found.

### Testing Grammar and Spelling 
- [Grammarly.com](https://www.grammarly.com/) was used to check grammar and spelling.


### Testing User Stories from User Experience (UX) Section

#### Visitor User Goals

1. As a visitor of the website, I want to understand what the website's purpose is.
   * In the upper left corner of the website's header, the website logo tells the visitor the website name: 'Citypop Central 70's and 80's Japanese Music'.
   * For Japanese visitors or people who can read Japanese, also Citypop Central was written in Japanese Hiragana: 'シティ・ポップ・セントラル.'
   * The 'Search songs in our database' search field and button on the 'Index' page tells it is possible to search for songs on the website.
   * Certain keywords are added above the search songs field to help the visitor use the correct keywords.
   * A link to the 'About the citypop central website' page has been added. Here the visitor finds information about the Citypop genre.
   * The 'Register' page tells the visitor you can add your songs into the database.

2. As a visitor of the website, I want to navigate easily throughout the website, so I don't get frustrated not knowing where to click.
   * A navigation bar is available on every page in the upper right corner.
   * The website is easily usable for visitors who are only searching for songs. All links and buttons are foreseen with a title explaining the purpose which can be excessed when hovering.
   * Search results are limited to a maximum of 10 songs per page. Pagination has been introduced to switch to the next or previous pages.
   *Every search result has a (?) button that expands less relevant information about each song.

3. As a visitor of the website, I want to target specific songs, so I don't get lost when I have to scroll through all available songs on the website.
   * Visitors can search under the following keywords: Artist name, Song name, Genre, Release Year, Album Name, Uploaded By, and Upload Date.

4. As a visitor of the website, I not only want to find information about the songs, but I also want to listen to the songs.
   * At the top of every search record, the Artist's name and Song name are indicated. A YouTube icon in front of the Artist's name has been implemented telling the visitor this is a clickable link. By clicking this link, the visitor will be redirected to a blank page that includes the embedded Youtube video. For convenience reasons, all records will play automatically. By hovering the link the text 'Watch on YouTube' will pop up.

5. As a visitor of the website, I want to see the album cover of the song.
   * For every search record, you can press the album image and a larger size image will appear on the screen.

6. As a visitor of the website, I might want to contact the website owner, so I can ask a question or give some feedback.
   * On the bottom, inside the search function division of the 'Index' and 'Youtube' pages, hyperlinks to the website's social media accounts are indicated. By clicking on one of the links, the visitor will be redirected to these social media accounts. Here the visitor can send direct messages to the website owner.

#### Returning Visitor User Goals
1. As a returning visitor of the website, I want to be able to not only search for song information or listen to the songs but also want to add my own (favorite) songs to the database.
   * By clicking the 'Register' button, every visitor can create a user account. When done, the visitor will get access to an 'Add Song' form. Here the user can add all information needed to upload a song: Artist Name, Song Name, Genre, Release Year, Album Name, Song Length, and the YouTube video ID.
   * Next to adding songs to the website, the user will also be able to 'Update' and 'Delete' the added songs.
   * The username will appear below the navigation bar when the user is logged-in. 
   * A summary of all uploaded songs is available on the 'My Songs' page. By clicking on one of the song's hyperlinks, the user will be automatically redirected to the page where the song can be edited.
   * When a user account is created, visitors become users and will also have access to a 'Profile' page. Here some additional information about the user is added.
   * When registered, visitors become users and are now able to maintain their profile information, add songs, edit songs, delete songs. This means only songs you have added to the database, not songs uploaded by other users.
   * Regular expressions have been added where needed, to help the user understand what input is expected, additional information has been added above every data field.

2. As a returning visitor of the website, I want to log out from my user account for safety reasons.
   * When logged in into your user account, it clearly states a logout button in the header's upper right corner.

3. As a returning visitor of the website, I want to know which songs I have uploaded in the past.
   * When logged in, in the upper right side of the navigation bar, a link to 'My Songs' will be available. By clicking this link the user will be redirected to a page that gives a summary of all your added songs in the past.

4. As a returning visitor of the website, I want to delete my profile whenever I want.
   * When logged in, at the bottom of your 'Profile' page, a link has been added which gives you the option to delete your user account. A second link has to be clicked to confirm you want to delete your profile. Your profile will be deleted, but the songs you added to the website will stay on the website under your name.

5. As a returning visitor of the website, I want to be able to update my user account in case some information about me (e.g. location) has been changed.
   * When logged in, on the 'Profile' page you can update your e-mail and the country you live in.
   *The option to change your password has been added.

6. As a returning visitor of the website, I want to be able to see information about other users of the website and contact them when needed.
   * Every song record has an information field in the expanded information section of the record stating who uploaded the song  'Uploaded by'. Only users can click on the 'Uploaded by' link to see more information about the other user. Here is the e-mail address of the user who uploaded the song is indicated. The user has the option to hide this e-mail address for other users on the 'Profile' page.


#### Administrator User Goals
1. As an administrator of the website, I want to be able to adjust all uploaded songs, so I can change them for whatever reason.
   * The administrator has access to the 'All songs' page, here all songs on the website will be alphabetically summarized. The administrator can edit and delete all songs on the website.
   * The administrator has access to the 'Users' page, here all users are alphabetically summarized. The administrator can delete every user who has access to the website.
3. As an administrator of the website, I want to adjust other information which is relevant to the website.
   * The administrator has access to the 'Settings' page, here it is possible to adjust the following information: Country settings, add or delete country names from the website. Country names are indicated on the user's profile page, telling in which country the user is currently living.
   * The administrator can add or delete other genders to the website. For now only male and female are available. A gender has to be selected by a new user when creating a user account.
   * The administrator can add or delete other genres to the website. For now, 10 different genres are available on the website. A genre is selected by a user when adding a song to the website.
   * The administrator can add or delete other release years to the website. For now, only the years 1970 to 1990 can be selected on the website. A release year is selected by a user when adding a song to the website.


<!-- Known Bugs -->
<a id="bugs"></a>
## Known Bugs
No known bugs found so far.


<!-- Deployment -->
<a id="deployment"></a>
## Deployment

### Publishing
'Herokuapp' was used for publishing the website. The procedure was as follows:
1. Login to the [Heroku](https://www.heroku.com/) website.
2. Click the 'Create New App' button.
3. Give your app a new unique name, choose your region and then click the 'Create App' button.
4. The app dashboard will appear now.
5. Click the 'GitHub' button in the 'Deployment Method' section.
6. Add your repository name in the 'Search for a Repository to Connect to' text field, then click the 'Search' button. When your repository appears, click the 'Connect' button.
7. Click on the 'Settings' tab, then click on the 'Reveal Config Vars' button.
8. Add the following KEY-VALUES:
- IP -> 0.0.0.0
- PORT -> 5000
- SECRET_KEY -> Copy from env.py file
- MONGO_URI -> Copy from env.py file
- MONGO_DBNAME -> Add from your mongoDB database
9. Make sure there is a 'Procfile' and a 'requirements.txt' file pushed into your GitHub repository.
10. Click on the 'Deploy' tab.
11. Click on the 'Enable Automatic Deploys' button.
12. Click on the 'Deploy Branch' button.
13. Wait until the website got deployed.
14. Click the 'View' button to see your deployed website on Heroku.

<img src="assets/images-readme/publishing.png" alt="github pages publishing">


### Forking
If you want to make a copy of the repository you can Fork it without changing the original repository by following the next procedure:
1. Login to the [GitHub](https://www.github.com/) website.
2. On the left side of your screen, you can find a summary of all repositories. Select [Eburonia/citypop-central](https://github.com/Eburonia/citypop-central)
3. On the right side of your screen, next to 'Unwatch' pull-down menu, and the 'Star' button, you can find the 'Fork' button.
4. By clicking this button, it will create a copy of the website in your repository.

<img src="static/readme-images/forking.png" alt="forking webpage">


### Cloning
You can clone the repository by following the next procedure:
1. Login to the [GitHub](https://www.github.com/) website.
2. On the left side of your screen, you can find a summary of all repositories. Select [Eburonia/citypop-central](https://github.com/Eburonia/citypop-central)
3. Click on the 'Code' button next to the Green 'GitPod' button.
4. Click on 'HTTPS' and copy the hyperlink below it.
5. Go to the repository where you want to make a clone of the website. Or create a new repository.
6. When in this repository, select the folder or create a folder where you want to clone the directory.
7. Go to the terminal and type: 'Git Clone (copied link)' and press enter. The directory has been cloned now.

<img src="static/readme-images/cloning.png" alt="cloning webpage">


### Downloading
You can download the repository by following the next procedure:
1. Login to the [GitHub](https://www.github.com/) website.
2. On the left side of your screen, you can find a summary of all repositories. Select [Eburonia/citypop-central](https://github.com/Eburonia/citypop-central)
3. Click on the 'Code' button next to the Green 'GitPod' button and then click on 'Download ZIP'.
4. A .zip file of the repository content will be downloaded. 

<img src="static/readme-images/downloading.png" alt="downloading webpage">

<!-- Credits -->
<a id="credits"></a>
## Credits

### Code
- Most of all HTML, CSS, jQuery, JavaScript, Python, and Jinja code was written by the website creator: Maurice Vossen.
- Regular Expressions. [link](https://www.html5pattern.com/Passwords)
- Pagination example code for Flask and MongoDB. [link](https://www.youtube.com/watch?v=Lnt6JqtzM7I)
- Understanding how aspect-ratio works in CSS for the iframe Youtube Video Screen. [link](https://www.youtube.com/watch?v=FF3fuYLnApQ)

### Content

#### README file
For consistency reasons, the README file of the website creator's previous project [Japanese Restaurant Shibuya](https://github.com/Eburonia/japanese-restaurant-shibuya) was used as a basis for the README file of this project.

#### About Page
All content on the 'About' page was written by the website creator.

### Media

#### Images
- The website logo was created by the website creator.
- All album images are directly loaded from the [discogs.com](https://www.discogs.com/) website.
- All images in this README file were created by the website creator.

<img src="assets/images/logo.png" alt="website logo"><br>
<sub>Logo of the website</sub>

### Acknowledgements
- Thanks to my personal mentor Victor Miclovich for answering my questions and giving feedback to this project.
- The many free coding forums on the internet, especially [Stackoverflow.com](https://www.stackoverflow.com/) for providing answers to my coding questions. Most of my questions were already asked by other users of the stackoverflow website, making it easy to find quick answers.




