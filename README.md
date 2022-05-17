<h1 align="center">Wired Coffee - B2B Ordering Platform</h1>

# Contents

* [**Introduction**](<## Introduction>)
* [**User Experience UX**](<#user-experience-ux>)
    * [Design Prototype](<#design-prototype>)
    * [Site Structure](<#site-structure>)
    * [Python Logic](<#python-logic>)
    * [Data Model](<#data-model>)
    * [Design Choices](<#design-choices>)
    *  [Typography](<#typography>)
    *  [Colour Scheme](<#colour-scheme>)
    * [Project Management](<#project-management>)
* [**Features**](<#features>)


# Introduction

This is a `Business-to-business (B2B)` Ordering Platform for a national coffeehouse chain called ‘Wired Coffee’ which I made up.
The solution is a simple command line interface, designed for the individual coffee branches/shops to place orders for supplies directly with the wholesalers/suppliers. The system focuses on the users placing orders for the most commonly used supplies so they never run out.

The orders are captured in an external worksheet which the supplier would use to use and fulfil the orders.

Branch Orders are submitted here in this <a href="https://docs.google.com/spreadsheets/d/1umzQeyeoHA8ijs8EIf7sGU_tvIjNHKc8SBv6D_VCceE/edit?usp=sharing" target="_blank" rel="noopener">Google Sheet</a>

This solution can be used for any business sector that adopts a B2B business model. It can be upscaled to tailor any business at enterprise and local levels.


![image](/docs/images/i-am-responsive-screenshot.png)

[Back to top](<#contents>)

------

# Accessibility Score: Google Lighthouse Test

The site ran through `Google Lighthouse` for Desktop and Mobile:

Each of these categories are judged on the following:

* `Performance` is judged on how quick it takes your webpage to load.
* `Accessibility` is judged by how accessible your website is. Especially for users who might require technology such as a screen reader or have difficulty with colours.
* `Best Practices` are judged by factors which will usually only be apparent to developers. This will be on code health, for example, Using deprecated Libraries/APIs.
* `SEO (Search Engine Optimisation)` is judged by making sure the page is optimised for search engine results.


## Desktop Scores:

![Image](/docs/images/Google_Lighthouse_desktop_result.png)


## Mobile Scores:

![Image](/docs/images/Google_Lighthouse_mobile_result.png)


------

# Advanced SEO

This solution is not for public use and therefore should not be crawlable in search engines. 
Therefore, I’ve implemented the `noindex` `meta tags` to the head section in the layout.html file, to prevent most search engine web crawlers, including Google’s from indexing the page.

------

# Features List

## 1. Welcome message + Product Menu to Display

When the program runs the user is greeted with a `Welcome Message` and Instructions on how to use the program.

There is also a `Product Menu` so the user knows what products are available to order.


![image]()

## 2. User Input Validation

There are safeguards functions to protect the integrity of the order data. This is to prevent orders being placed with incorrect details and disrupting order process flow.

* When a user enters an invalid name, they are presented with an error message:

* When a user enters an invalid product sku, they are presented with an error message:

* When a user enters an invalid branch number, they are presented with an error message:

* When a user enters an invalid quantity, they are presented with an error message:

* If the user does not want to proceed with the order, then the user is redirected back to the beginning of the program Otherwise the order is processed.



![image](/)

## 3. Order Preview

After the user has entered the order details, the user can `preview the order` before submitting the order.

![image](/)

## 4. Calculate total price exVat on Order Preview

The total price of the order is `calculated` using the price assigned to each sku number, multiplied by the quantity number the user inputs into the programme.

![image](/)

## 5. Confirm Order

The user has the option to proceed with the order or terminate the order. This is a `safe guard function` to avoid the order being placed without user consent.


![image](/)

## 6. API Integration - Send Order Data to External Google Worksheet

When the user confirms the order, the order is sent to an `external worksheet` for the suppliers.

You can view the worksheet <a href="https://docs.google.com/spreadsheets/d/1umzQeyeoHA8ijs8EIf7sGU_tvIjNHKc8SBv6D_VCceE/edit?usp=sharing" target="_blank" rel="noopener">here.</a>

------

# Setting Up Google Cloud API Integration:

## Activate Google API Credentials

### Steps to get your credentials file for users with the "new" form UI:

1. From the "Which API are you using?" dropdown menu, choose `Google Drive API`
2. For the "What data will you be accessing?" question, select `Application Data`.
3. For the "Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions?" question, select `No, I'm not using them`.
4. Click `Next`

### Create a new project

![image](/docs/images/google-api-create-new%20project.png)

### Enable APIs for Google Drive and Google Sheets

![image](/docs/images/enable-api-for-googl-sheet.png)
![image](/docs/images/enable-api-for-googl-sheet_2.png)

### Generate API Credentials for Google Drive

![image](/docs/images/create-api-credentials.png)

### Enter a Service Account name - then click `Create`

![image](/docs/images/service-account-name.png)

### In the Role Dropdown box choose `Basic` > `Editor` then press `Continue`

![image](/docs/images/grant-service-access.png)

### These options can be left blank, click `Done`

![image](/docs/images/service-account-name_2.png)

### On the Credentials page, click on the `Service Account` that has been created and click on it.

![image](/docs/images/credentials-page.png)

### On the next page, click on the `Keys` tab

![image](/docs/images/api-keys.png)

### Click on the `Add Key` dropdown and select `Create New Key`
### Select `JSON` and then click `Create`. This will trigger the json file with your API credentials in it to download to your machine. 

![image](/docs/images/create-private-key.png)


------
# Testing

### Responsive Testing

I have tested that the site is responsive by applying specific styles for the most common `CSS breakpoints`

#### Breakpoints used for mobile devices:

1. `max-width: 480px`
2. `max-width: 320px`

#### Breakpoints used for tablet devices:

1. `max-width: 820px`
2. `max-width: 768px`

I used the Chrome inspect element to check the different CSS breakpoints.

## User Stories

### Welcome Screen

`As a` Player.
`I want to` see the welcome screen.
`So that` i know the quiz is ready for me to start.
`Also` i should be able to click 'Hot to play' to see instructions before playing.

### Quiz Logic

`As a` Player.
`I want to` answer five multi-choice questions.
`So that` i can complete the quiz.

### Correct and Incorrect Answer Logic

`As a` Player.
`I want to` see if the answers i select turn red or green.
`So that` during the quiz i can see which of my answers are right or wrong.

### Countdown Timer

`As a` Player.
`I want to` click 'START' to start the countdown timer.
`So that` i have sixty seconds to complete the quiz.

### Window Alert

`As a` Player.
`I want to` be shown a window alert if I do not complete the quiz in time.
`So that` the game tells me that I have ran out of time.
`Otherwise` I will not be shown the alert.

### Dark Mode

`As a` Player.
`I want to` be able to toggle between dark mode and light mode.
`So that` i can view the game at night to reduce eye strain.

### How to Play Modal

`As a` Player.
`I want to` be able to see a modal displayed.
`So that` i can see instrucitons how to play the quiz.

### Reset Button

`As a` Player.
`I want to` be able to restart the quiz and the countdown timer.
`So that` i can see try to complete the quiz on time.

### Social Share functionality

`As a` Player.
`I want to` share the game on social media and see the icons in the footer.
`So that` i can share the game with my family and friends.

### Score area

`As a` Player.
`I want to` see my final score out of five.
`So that` i know how many questions i got right.

### Check Answers area

`As a` Player.
`I want to` be able to see my answers `but not` the actual answers.
`So that` i know what questions i may have gotten wrong.

### Privacy Policy

`As a` Player.
`I want to` control what data of mine is tracked and shared.
`So that` i know what data of mine being tracked and shared.

### Responsive Layout

`As a` Player.
`I want to` be able to play the quiz on my mobile phone, tablet and laptop.
`So that` i can play the quiz anywhere and anytime i choose.


## Test Cases

### Welcome Screen

1. I can see the welcome screen on page load `PASSED`
2. I cannot start the quiz until i click 'START' which starts the quiz and the timer. `PASSED`
3. I can click 'How to play' before starting the game.`PASSED`

### Quiz Logic
I can go through the quiz which has five multiple-choice questions `PASSED`

![image](/docs/images/fith-question.png)

### Correct and Incorrect Answer Logic
I should see my selection highlightd in red or green to show which answers are right and wrong. `PASSED`

![image](/docs/images/correct-answer-green.png)
![image](/docs/images/wrong-answer-red.png)

### Countdown Timer

When I click 'START' the countdown timer starts and I have sixty seconds.`PASSED`

![image](/docs/images/countdown-timer.png)


### Window Alert

1. The window alert is displayed if I run out of tie to complete the quiz `PASSED`
2. The alert should not display if I complete the quiz on time. `PASSED`

![image](/docs/images/window-alert-times-up.png)

### Dark Mode

I should be able to toggle between normal and dark mode. `PASSED`

### How to Play Modal

I should be able to open and close the modal via the button. `PASSED`

### Reset Button

I should be able to restart the quiz by clicking the button `PASSED`

### Social Share functionality

I can see the social share icons in the footer `PASSED`


### Score area

I can see my final score out of five. `PASSED`

### Check Answers area

I can see my answers in the dedicated area. `PASSED`

### Privacy Policy

I can manage my privacy settings `FAILED`. 
Not able to see the privacy link on certain devices and layouts.

### Responsive Layout

I can view the game on the standard reponsive views. `PASSED`


## HTML and CSS Code Validation

Both the W3C Markup HTML Validator and W3C CSS Validator were used to to confirm there are no errors in the codebase.

<a href="https://validator.w3.org/nu/?doc=https%3A%2F%2Fkslg.github.io%2Fpp2-spider-quiz%2F" target="_blank">W3C Markup Validator Report</a>

![image](/docs/images/html-validation.png)

<a href="https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fkslg.github.io%2Fpp2-spider-quiz%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en" target="_blank">W3C CSS Validator Report</a>

![image](/docs/images/css-validation.png)

------

## Deployment

I worked on my local repository before deploying the code to Staging and then Production (Live Site).

### Deployment to Staging

I first deploy my changes to the `Staging Area` so I can preview the changes before deploying to Production.

`$ git add .` - Adding this to the editor terminal commits files to the Staging area.
The period (.) at the end will add all files to the commit.

`$ git commit -m “{Commit Details}”` - Pushes the latest changes to the GIT Repository.
`-m` means "message" which is common practice to add so you and other developers know what changes were being made.


### Deployment to Production

Once I verified and tested by changes, I then deploy thr changes to Production.

`$ git push` deploys the code to the GitHub and into the main branch of code which is connected to Production (the Live Public URL).

## Bugs Encountered during Testing

### Issue 1 - Stop the window alert from displaying

The window alert was still displaying even when you completed the quiz on time. 

![image](/docs/images/window-alert-issue.png)

## Fix

I had to delete the window alert after the quiz was over by using the `delete keyword` for the window object.

![image](/docs/images/window-alert-fix.png)

### Issue 2 - Modal code conflict

Added a Javascript/CSS Modal to the quiz but this broke the answers section as the colours on the answers did not clear after you select an answer. There was a conflict in the code. 
I was using the modal from W3C https://www.w3schools.com/howto/howto_css_modals.asp

![image](/docs/images/modal-issue.png)

## Fix

I found a simple Javascript CCS Modal workaround instead and styled it. 

## UX Planning

I used the 5 Planes of UX to provide a conceptual framework. 

### The Strategy Plane

#### Mission Objectives / The What:

 - Trivia Quiz game for Spider-man enthusiasts.
 - Fun and visually entertaining.
 - An unofficial quiz game.

 #### The Why:

- To celebrate the comic book hero.
- For fans to test their general knowledge about Spider-man.


### Ideas & Inspiration Mind Map
![image](/docs/images/mindmap-screenshot.png)

### Demographic

 - Target Audience between: 9 years - 40 years
 - All genders Welcome.


### Colour Palette Ideas
- Primary colours for easy accessibility and clear communication.
- Also, matches the theme of the quiz.

![image](/docs/images/colour-pallette-ideas.png)

### Content Strategy
- Challening questions for the quiz
- Instructions for the user
- Clear and simple language for the users to understand and operate the quiz.

### Typography
Fonts selected are `Heebo` and `Bebas Neue` from Google Fonts which are clear and easy to read. https://fonts.google.com/

![image](/docs/images/google-fonts-screenshot.png)

---

## The Scope Plane

### Functional Requirements

1. Problem: If the users want to play the quiz at night, they may strain their eyes playing this. 

    Solution: Implement night/dark mode for the quiz UI.

2. Problem: To move to the next question, the user needs to click next to display the next question.

    Solution: Make an event where the user clicks or taps on an answer which then moves on to
the next question.

3. Problem: Users need to be limited to a certain amount of time to play the quiz. This is one of the challenge aspects of the quiz

    Solution: Add a countdown timer for one minute. 
    If the time runs out before the quiz ends then the user is prompted with a message “Oh no! Times Up. Don’t worry, you can try again.”
    Users can restart the quiz.
    If the user completes the quiz within one minute the timer stops and the user sees the scores page.

4. Problem: If the player wants to start the quiz they would need to refresh the browser.

    Solution: Create a more intuitive refresh function by having a button to refresh the quiz.

5. Problem: The player might not understand the aim of the game i.e how to play.

    Solution: Create a popup with instructions on how to play.

6. Problem: The player has no method to share the game with friends.

    Solution: Add a share functionality so users can share the game with friends and family.

### Content Requirements

- Quiz questions and answers which can be easily updated via js file. 
- Content on the site will be a mix of copy text and a background image.

### Interaction Design

- All CTA (Call to Action) buttons will change colour to let the customers know that the buttons and links are clickable. 

- Once all five questions have been answered the player is directed to the score area.

- Once the timer has run out the player is notified. 

- The player is presented with an alert when the time has run out. Player has to click on the alert to close it.

- The player cna find out how to play the game by opening up a modal popup giving instructions on how to play the game.

### Scope of MVP

Using the `MoSCoW prioritisation method` which is used in Agile project delivery to outline the importance of each requirement and what needs to be delivered in the MVP.

#### MoSCoW Definition:
![image](/docs/images/moscow-screenshot.png)
 
---
## The Structure Plane

### Site Architecture
- Only one page is presented to the user with a dynamic elements being the question area, and the scoreboard area.

![image](/docs/images/site-structure-screenshot.png)

### Header and Footer
- Normal Mode: Light Blue Background and Yellow Gold Text. 
- Dark Mode: Dark Blue Background and Red Text. 

Examples

![image](/docs/images/header-mock-up.png)

![image](/docs/images/footer-mock-up.png)

## CTA Buttons
Non-clicked State: 
- White text box
- Dark Blue text

Hover State:
- Dark Blue text box
- Yellow Gold text

![image](/docs/images/hover-state-screenshot.png)

## Colour Palette:

![image](/docs/images/colour-pallette-screenshot.png)

## Iconography:

- Toggle icons will match the colours from normal and dark mode.
- Social share icons/buttons will be served by the 3rd party ShareThis widget.

![image](/docs/images/darkmode-toggle-icons.png)
![image](/docs/images/sharethis-preview.png)

## The Surface Plane / Final Concept

### Game Area Wireframe
![image](/docs/images/gamearea-wireframe.png)

### Score Area Wireframe
![image](/docs/images/scorearea-wireframe.png)

------

### Credits / Borrowed Resources / Tools

- Favicon 
https://www.pngaaa.com/ - PNG Images For Free

- Font Library 
https://fonts.google.com/

- Quiz Questions
https://www.funtrivia.com/en/Movies/Spider-Man-4653.html


- Share This widget
https://sharethis.com/platform/share-buttons/
- Dark Mode Functionality
https://www.futurecodersweb.com/2021/06/create-dark-and-light-mode-toggle.html
- Setup Alerting for the timer
https://techfunda.com/howto/595/stop-timer
https://stackoverflow.com/questions/31106189/create-a-simple-10-second-countdown
https://developer.mozilla.org/en-US/docs/Web/JavaScript
- Restart Button Functionality: 
https://stackoverflow.com/questions/5611119/how-to-make-a-refresh-button-using-javascript
- Quiz Structure Inspiration
https://www.youtube.com/watch?v=2jwdyO_UunE&t=2421s
- Javascript CCS Modal Inspiration
https://www.youtube.com/watch?v=uUCpopjPZdI
- Spider-Man Background Image:
https://wallpapersafari.com/w/19SZQb
- RGBA Generator
https://rgbacolorpicker.com/hex-to-rgba
- Dark Mode Research
https://blog.weekdone.com/why-you-should-switch-on-dark-mode/
- Agile User Stories Support Documentation
https://www.atlassian.com/agile/project-management/user-stories 
- Inspired by the Love Maths Project. 
- Wireframes produced using Balsamic
- Support from my mentor Gerard McBride, Slack Community and Tutor Support (Ger)
- Online Code Support and References: W3C Schools and Stackoverflow Community.

------

### Descoped Requirements / Future Enhancements
- Some requirements had to be descoped from the project due to time contraints. 
- Descoping is a process which is part or Agile Project Management, and can be requirements that are brought back into a sprint or project at a later date.

1. You can go to the next question without answering any of them. Conditional logic needed.
2. Add more questions to the question bank and serve random questions to the player.
3. Share your score with friends.
4. Display a cover page intrducing the quiz. 
5. A 3,2,1 countdown before starting the quiz.

------

### Unfixed Bug
 Due to time constraints the following bugs are still unfixed. Following Agile practises, these bugs can go into a backlog of requirements and prioritised accordingly.

- Make sure Privacy Policy link is displayed on all layouts.

------

<p align="center">End of document.</p>