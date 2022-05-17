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
# Create Gitpod Workspace

1. Create the Github Repository from the `Python Essentials Template`
https://github.com/Code-Institute-Org/python-essentials-template

![image](/docs/images/setup-gitpodworkspace-1.png)

2. Name the project (repository) > click `Create repository`

![image](/docs/images/setup-gitpodworkspace-2.png)

3. Click the `Gitpod` button to build the workspace.

![image](/docs/images/setup-gitpodworkspace-3.png)

4. Add the google json credentials file to the workspace and rename it to `creds.json` so it’s easier to access the file for the project.

![image](/docs/images/setup-gitpodworkspace-4.png)

5. I need to share the Google Orders Sheet with the `Client email` from the generated credentials.
Change permissions to `Editor` > Untick `Notify People` > Click `Share`

![image](/docs/images/setup-gitpodworkspace-5.png)

## Update `.gitignore` with json credentials

The creds.json file contains sensitive information that should be kept secret.
I need to ensure that the json file is never committed or sent to Github.

The .gitignore file contains a list of files that should not be committed or sent to Github. I added the creds.json to the list to protect the file.

![image](/docs/images/gitignore.png)

Once saved I committed the changes and pushed to Github

![image](/docs/images/gitignore_deploy.png)

## Pin the workspace

Gitpod workspaces are not permanent by default, if they are unused for 14 days, they’re deleted unless the workspace is pinned. I pinned the workspace.
 
------

# Connecting to the Google Sheets API

In order to use Google Sheets API I need to install `two additional dependencies` in the project, as they are not part of the standard Python library.

`The first is Google Auth:` This uses the creds.json file to set up the authentication needed to access our Google Cloud Project.

`The second is Gspread:` This is a library of code that will use to access and update data on our spreadsheet.

I used the following command in the bach terminal to install the dependencies:

`pip3 install gspread google-auth`

Once installed, I need to import them into my python file: `import gspread`

This imports the entire gspread library so I can access any function, class or method within it.

`import credentials` imports the credentials class which is part of the service_account function from the Google auth library.

`from google.oauth2.service_account import Credentials`

![image](/docs/images/api-dependencies.png)

## Set the Scope

This configuration specifies what the user has access to.
The scope lists the APIs that the program should access in order to run.
The scope variable value will not change, it is a Constant variable and therefore written in capitals. 
This makes it easier for developers to identify variables that should not be changed.

![image](/docs/images/api-scope.png)

Additional Constant Variable settings to help access the spreadsheet data:

![image](/docs/images/api-access-to-sheet-data.png)

## Testing the API
Testing the API to try and access the data in the worksheet.

![image](/docs/images/api-testing.png)

------

# Setup Heroku



------
# Testing

## Responsive Testing

The user experience for a command line interface is not great and could lead to accedental input errors by thr users, making the user frustrated.

Therefore, I made the app is only visible and can be run on a laptop or desktop workstation.

### Breakpoint for laptop and desktop:

1. `max-width: 748px`

## User Stories

### Show Product Menu
`As a` Wired Coffee Employee.
`I want to` see what products are available to order in a table format. 
`So that` I can input the order data.

### Input Order Data 
`As a` Wired Coffee Employee
`I want to` be able to enter order details into the programme
`So that` my order can be processed.

### Data Validation
`As a` Wired Coffee Employee. 
`I want to` be told by the programme that my order details are incorrect `and` stop the order from being processed, `if` I enter invalid data. 
`So that` I am returned to the start of the programme.

### Preview Order Data
`As a` Wired Coffee Employee.
`I want to` see my order details displayed in the terminal before I confirm the order. 
`So that` I know my order details are correct. 

### Confirm Order
`As a` Wired Coffee Employee 
`I want to` be prompted to confirm my order before I submit the order.
`So that` I know my order was not submitted on it’s own by mistake.

### Send Order Data to Worksheet
`As a` 3rd Party Supplier.
`I want` the Wired Coffee order details to be added to the worksheet provided.
`So that` I can view and fulfil the order correctly. 

### Calculate Total price for the order
`As a` Wired Coffee Employee. 
`I want to` know the total price of the order based on the product `and` quantity selected.
`So that` I know how much I’m going to be charged by the supplier.

### Option to Send Order Email Confirmation
`As a` Wired Coffee Employee.
`I want` a confirmation email of the order sent to my email address.
`So I can` reference my order if needed.

## Test Cases

### Show Product Menu

The product menu shows in a table format is clearly legible `PASSED`

### Input Order Data
The input fields allow me to enter data. `PASSED`

## Data Validation
1. The data validation for each input works as expected. `PASSED` 
2. I cannot proceed with the order when invlaid data has been entered `PASSED`
3. I am presented with a `user friendly error message` related to the invalid data.`PASSED`

## Preview Order Data
I can see my all my order details printed in the terminal for me to check and is clearly legible `PASSED`

## Confirm Order
1. I am given the option to confirm my order with a simple ‘y’ for Yes and ‘n’ for No `PASSED`
2. If I say ‘y’ my order is processed `PASSED`
3. If I say ‘n’ my order is not processed `PASSED`
4. When I say 'n', I am directed my to the beginning with user friendly messaging telling me my order was not placed and I can place a new order. `PASSED`

## Send Order Data to Worksheet
1. The order data is sent to the google worksheet `PASSED`
2. The order data is added to the correct columns in the worksheet `PASSED`
3. The order data is in the correct format `PASSED`

## Calculate Total price for the order
1. The total price is being calculated using the product price and the quantity number selected `PASSED`
2. The total price is given two decimal places in the Order Preview `FAILED`. Possibly an edge case

![image](/docs/images/test-case-edge-case.png)

3. The total price is given two decimal places in the Worksheet `PASSED`

![image](/docs/images/worksheet-test.png)

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