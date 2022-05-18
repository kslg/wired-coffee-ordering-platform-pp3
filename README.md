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

The total price of the order is `calculated` using the price assigned to each sku number, multiplied by the quantity number the user inputs into the program.

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
`I want to` be able to enter order details into the program
`So that` my order can be processed.

### Data Validation
`As a` Wired Coffee Employee. 
`I want to` be told by the program that my order details are incorrect `and` stop the order from being processed, `if` I enter invalid data. 
`So that` I am returned to the start of the program.

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

### Data Validation
1. The data validation for each input works as expected. `PASSED` 
2. I cannot proceed with the order when invlaid data has been entered `PASSED`
3. I am presented with a `user friendly error message` related to the invalid data.`PASSED`

### Preview Order Data
I can see my all my order details printed in the terminal for me to check and is clearly legible `PASSED`

### Confirm Order
1. I am given the option to confirm my order with a simple ‘y’ for Yes and ‘n’ for No `PASSED`
2. If I say ‘y’ my order is processed `PASSED`
3. If I say ‘n’ my order is not processed `PASSED`
4. When I say 'n', I am directed my to the beginning with user friendly messaging telling me my order was not placed and I can place a new order. `PASSED`

### Send Order Data to Worksheet
1. The order data is sent to the google worksheet `PASSED`
2. The order data is added to the correct columns in the worksheet `PASSED`
3. The order data is in the correct format `PASSED`

### Calculate Total price for the order
1. The total price is being calculated using the product price and the quantity number selected `PASSED`
2. The total price is given two decimal places in the Order Preview `FAILED`. Possibly an edge case

![image](/docs/images/test-case-edge-case.png)

3. The total price is given two decimal places in the Worksheet `PASSED`

![image](/docs/images/worksheet-test.png)

### Responsive Layout

1. I can view the app on laptop and desktop. `PASSED`
2. I cannot view the app on tablet and mobile `and` I am presented with a notice that my device is not supported.`PASSED`

## Python Code Validation

I inspected the code using a <a href="http://pep8online.com/" target="_blank" rel="noopener">PEP8 Inpector</a> to confirm my python code is following best practices.

![image](/docs/images/pep8-validation.png)

------

## Deployment

### Running the code in the GitPod Terminal

I worked in the editor and checked my work via the gitpod terminal. I ran the run.py file using the following command `python3 run.py`

### Deployment to Git

I deployed my changes to Git:

`$ git add .` - Adding this to the editor terminal commits files to the Git.
The period (.) at the end will add all files to the commit.

`$ git commit -m “{Commit Details}”` - Pushes the latest changes to the Git Repository.
`-m` means "message" which is common practice to add so you and other developers know what changes were being made.


### Deployment to Production

Once I verified and tested by changes, I then deploy the changes to Production.

`$ git push` deploys the code to the GitHub and into the main branch of code which is connected to Production (the Live Public URL).

## Bugs Encountered during Testing

### Issue 1 - Not printing out the final order data into the terminal

I'm was trying to print out order data after multiple inputs from the users and passed validation.
The code was not printing out the final order data into the terminal.

![image](/docs/images/issue-1.png)

### Fix

There was a 'break' statement that seemed to be out of place:

![image](/docs/images/fix-1.png)

### Issue 2 - Keep getting a Syntax error

I was asking the user to confirm their order with a boolean (y/n)
But I kept getting a Syntax error which I couldn't seem to fix.

![image](/docs/images/issue-2.png)

### Fix

Decided not to force it as a boolean, and created and if statement with conditions.
Added this inside the while loop.

![image](/docs/images/issue-2-fix.png)

### Issue 3 - Invalid data is still sent to the worksheet

When I run the py file with invalid data, the error is caught but the invalid data is still sent to the worksheet.

![image](/docs/images/issue-3.png)

### Fix

I had to `return` the get_order_data function on the false statement.

![image](/docs/images/issue-3-fix.png)


## UX Planning

I used the 5 Planes of UX to provide a conceptual framework. 

### The Strategy Plane

#### Mission Objectives / The What:

- A simple command line interface, designed for the individual coffee branches/shops to place orders 
- The orders are captured in an external worksheet which the supplier would use to use and fulfil the orders.

#### The Why:

- The system focuses on the users placing orders for the most commonly used supplies so they never run out.

### Demographic

 - Designed for Businesses.
 - Not for public use.

### Data Flow Diagram (DFD)

Here is a visual representation of the information flow through a process. DFDs help us better understand the process or system operation to discover potential problems, improve efficiency, and develop better processes.

![image](/docs/images/dataflow-diagram.png)

---

## The Scope Plane

### Functional Requirements

1. Problem: The supplier needs to know when the order was placed.

    Solution: Add a `Date Stamp` as part of the order data which is then sent to the suppliers google worksheet.

2. Problem: The supplier needs to know Coffee Branch Details for the order.

    Solution: Add `Branch Number` and `Name` as part of the order data which is then sent to the suppliers google worksheet. The supplier will then know the location using their own systems, and who to address the the order to.

3. Problem: The supplier needs to know product details got thr order.

    Solution: Add a `Product SKU`, `Product Name`, `Product Quantity` and 'Product Price' as part of the order data which is then sent to the suppliers google worksheet.

4. Problem: The supplier needs to know how much to charge the Branch for the order.

    Solution: Calculate the total cost programmatically based on product price and quantity requested.

5. Problem: The Branch User must not give order data which is incorrect or not making any sense.

    Solution: Add validation rules to the data inputs which check the order data programmatically.

6. Problem: The Branch user has to check the order details before sending them off to the supplier.

    Solution: Add an Order Preview Section so the user can check before submitting the order.

7. Problem: The Branch User needs to know what products they can purchase and how.

    Solution: Present a Product List displaying Product Details and give instructions on how to place orders.

### Content Requirements

- Input strings, telling the users what data is required.
- Error messages, letting the user know when certain data is invalid.
- Status information, informing the user what is happening at each stage of the ordering process.
- Content on the site must be easy to read. Simple langauge with User Friendly messaging and tones.

### Interaction Design

- Using Heroku App ther will be a CTA (Call to Action) to help the user run the program.

- Interaction is simple and mainly terminal based.

### Scope of MVP

Using the `MoSCoW prioritisation method` which is used in Agile project delivery. This outlines the importance of each requirement and what needs to be delivered in the MVP (Minimum Viable Product).

#### MoSCoW Definition:
![image](/docs/images/moscow.png)
 
---
## The Structure Plane

### Site Architecture
- Only one page is presented to the user with a CTA Button, and the Terminal Interface.

![image](/docs/images/wireframe.png)

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