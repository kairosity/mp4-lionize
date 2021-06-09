# Lionize

## Digital Marketing Solutions

## Code Institute Milestone Project 4

This project is an application and company website for a digital marketing business called "Lionize". The application both showcases the digital services offered and also allows clients to register a free account. Once registered the client is given access to further information about the services, as well as quote calculators and they also have the ability to order and pay for certain digital products online.
 

# Table of Contents

- [1. UX](#ux)
    * [User Personas - Four Examples](#user-personas-four-examples)
    * [User Stories](#user-stories)
      - [*First Time User Stories*](#first-time-user-stories)
      - [*Returning User Stories*](#returning-user-stories)
      - [*Persona Based User Stories*](#persona-based-user-stories)
      - [*Accessibility User Stories*](#accessibility-user-stories)
      - [*Application Creator User Stories*](#application-creator-user-stories)
  * [Strategy](#strategy)
      - [*Project Goals*](#project-goals)
      - [*Target Users*](#target-users)
      - [*Research*](#research)
      - [*Value To The User*](#value-to-the-user)
  * [Scope](#scope)
    - [*Core Theme*](#core-theme)
    - [*Feature Ideas Table*](#feature-ideas-table)
    - [*List of Final Features*](#list-of-final-features)
  * [Structure](#structure)
      - [*Interaction Design*](#interaction-design)
        - [*Navigation*](#navigation)
        - [*Consistency and conventions*](#consistency-and-conventions)
        - [*Learnability and Communication of Functionality*](#learnability-and-communication-of-functionality)
        - [*Feedback*](#feedback)
        - [*Messages Framework*](#messages-framework)
        - [*Form Validation Messages*](#form-validation-messages)
        - [*Deletion Confirmation Modals*](#deletion-confirmation-modals)
        - [*State Changes*](#state-changes)
        - [*Error Pages*](#error-pages)
        - [*Pre-Loader*](#pre-loader)
      - [*Information Architecture*](#information-architecture)
      - [*Application Sections*](#application-sections)
        - [Guest Users (not logged in)](#guest-users-not-logged-in)
        - [Guest User Flow](#guest-user-flow)
        - [Logged in Users](#logged-in-users)
  * [Skeleton](#skeleton)
      - [*Progressive Disclosure*](#progressive-disclosure)
      - [*Metaphorical Thinking*](#metaphorical-thinking)
      - [*Establishing Value Through Design*](#establishing-value-through-design)
      - [*Reassuring Conventions*](#reassuring-conventions)
      - [*Contextually Organised Content*](#contextually-organised-content)
      - [*Wireframes*](#wireframes)
  * [Surface](#surface)
      - [*Design Considerations*](#design-considerations)
      - [*Colour Palette*](#colour-palette)
      - [*Typography*](#typography)
      - [*Design Mockups*](#design-mockups)
- [2. Database Architecture](#database-architecture)
    - [Schema](#schema)
- [3. Features](#features)
- [4. Responsivity](#responsivity)
    - [Mobile Devices](#mobile-devices-materialize-sm-breakpoint)
    - [Tablet Devices](#tablet-devices-materialize-m-breakpoint)
    - [Desktop Devices](#desktop-devices-materialize-l-breakpoint)
    - [Wide Desktop Devices](#wide-desktop-devices-materialize-xl-breakpoint)
- [5. Accessibility](#accessibility)
    - [1. Accessibility for Users with Visual Impairments](#1-accessibility-for-users-with-visual-impairments)
    - [2. Accessibility for Keyboard Users](#2-accessibility-for-keyboard-users)
    - [3. Accessibility for Users with Hearing Impairments](#3-accessibility-for-users-with-hearing-impairments)
    - [4. Accessibility for Users with Cognitive Impairments](#4-accessibility-for-users-with-cognitive-impairments)
    - [5. Accessibility for Users with Slow Internet Connections](#5-accessibility-for-users-with-slow-internet-connections)
- [6. Security](#security)
    - [1. CSRF Protection](#1-csrf-protection)
    - [2. Flask-Talisman and Content Security policy](#2-flask-talisman-and-content-security-policy)
    - [3. Access Control](#3-access-control)
    - [4. Request Methods](#4-request-methods)
- [7. Testing](#testing)
- [8. Future Features To Implement and Issues Remaining](#future-features-to-implement-and-issues-remaining)
- [9. Attribution](#attribution)
- [10. Deployment](#deployment)
- [11. Tools and Other Resources Used](#tools-and-other-resources-used)
    - [1. Design](#1-design)
    - [2. HTML and CSS](#2-html-and-css)
    - [3. JavaScript](#3-javascript)
    - [4. Python](#4-python)
    - [5. Django](#5-django)
    - [6. Jinja](#6-jinja)
    - [7. General](#7-general)
- [12. Libraries](#libraries)
- [13. Technology Used](#technology-used)
- [14. Acknowledgements](#acknowledgements)

# UX

## User Personas - Four Examples

1. __Tom Lynch__ is a __sole trader__. He runs a tiny, stylish hipster coffee shop in Kinsale, Co. Cork. He is fairly tech-savvy and enjoys managing his social media accounts, but does not have the inclination or the time to develop his own website. A friend made one for him using a template site, but he doesn't feel like it reflects the quality of his business. He wants to hire a professional developer to better align his online presence with his offline business. He has a budget of €2,500 for this purpose.

2. __Annalise Maior__ is the __marketing manager__ of the national branch of a global real estate company. She is tasked with increasing the company's social media presence in Ireland, as several Irish companies have a much stronger following. Her budget for this goal is flexible but she expects a tangible, measurable improvement in their social media KPIs, specifically she wants to outdo the national businesses in terms of engagement and follows.

3. __Rosemary Geoghan__ is the __CEO__ of a mid-sized plumbing company based in Dublin. The business already has a strong industry reputation and its primary clients are large construction firms. Rosemary wants a client portal added to the business's existing website so that detailed and customized project information can be viewed easily by clients.

4. __David Murphy__ is a makeup artist based in Kildare. He is expanding his business and has launched a product line of branded makeup brushes. He wants to delegate both his social media management and his content creation, so that he can focus on strategy and his day-to-day business.

#### back to [contents](#table-of-contents) 
<br>

## User Stories

This application is targeted at Sole Traders, SMEs and larger businesses who are looking to outsource aspects of their digital marketing strategy. The services on offer include website creation, SEO services, social media management and content creation.

## First Time User Stories
## *As a first time user I want to be able to...*

1. Easily understand the purpose of the web application.
2. Quickly and easily understand how to navigate and access information on the website.
3. Quickly and easily have an idea of what kinds of products are offered.
4. View further details of each of the services on offer, on specific pages dedicated to that service, so as to decide if I want to avail of any of them.
5. View a website that is visually and creatively appealing and physically easy to look at.
6. Notice the login/register options and easily navigate to those pages.
7. Understand the purpose of user registration and the benefits thereof.
8. Easily register a free account using my email.
9. Receive an email confirmation of my registration.

## Returning User Stories
## *As a returning user I want to be able to...*

### Registration, Login, Logout, Update & Delete Data

1. Login to my user account, using my email and password.
2. Be redirected to the User Portal and easily view the various custom user pages.
3. Edit my account information: change my password, username & other details.
4. Recover my password if I forget it.
5. Delete my account.
6. Be prompted to confirm my request to delete my account.
7. Receive email confirmation of my account deletion, outlining the data to be deleted, including all order information.
8. Logout of my account.

### Information Gathering

1. Quickly navigate to the products / services information pages from anywhere on the website.
2. Gather more in depth information about the services and products on offer.
3. Easily contact Lionize to ask for specific information about the services and products on offer.
4. View a transparent pricing structure for all products.

### User Portal

1. View / add / updated my profile details easily on a page specifically for that purpose.
2. Navigate to my shopping bag quickly from the user portal side bar.
3. Easily view all my past orders, and all their attendent details.

### Shopping

1. Browse all products.
2. Easily view the prices & specific details of each product by clicking into a product details page.
3. Browse products by category.
4. Filter products by keyword using a search form.
5. Add products to my shopping bag and have this visually confirmed for me.
6. Easily view all the items in my shopping bag.
7. Update the items in my shopping bag, by adding more or less of an item.
8. Remove any item from my shopping bag. 
9. Make changes to my shopping bag and see these changes reflected immediately without having to visit the shopping bag page.
10. Email Lionize with a custom quotation request for a specific product that I do not see on the site.

### Purchasing

1. Purchase the products I have added to my shopping bag.
2. Use my credit card to pay for my items.
3. Be confident in the knowledge that my payment is being handled securely.
4. View the VAT added to both the individual products and the total cost before paying.
5. See confirmation of my order after completing the checkout process.
6. Have the VAT reflected on the order confirmation.
7. Navigate to my order history page and easily see a list of past orders processed with all associated information clearly outlined.
8. Have my personal details such as name, email, phone number & address saved to my profile and automatically populate the checkout form.

## Persona Based User Stories

### Tom Lynch - Hipster Coffee Shop Owner
### *As a sole trading small business owner I want to be able to...*

1. Order a professional looking website for my small business.
2. See some examples of Lionize's web design work prior to ordering.
3. Easily understand all the various web design options available to me.
4. Easily communicate with Lionize about my requirements, my order and my billing.

### Annalise Maior - Real Estate Marketing Manager
### *As a regional marketing manager of a large corporation I want to be able to...*

1. Delegate the social media management of our Irish branch to specialists.
2. Improve all social media KPIs and see a measurable return on investment.

### Rosemary Geoghan - Plumbing Co. CEO
### *As the CEO of a plumbing company seeking to future-proof how we communicate with clients, I want to be able to...*

1. Get a custom quotation for integrating a client portal into our current website.
2. Get the project up and running and then delegate the project management to our marketing dept.

### David Murphy - Entrepreneurial Make-up Artist
### *As a createive professional whose brand is focused around my personality, I want to be able to...*

1. Confidently delegate social media management, secure in the knowledge that tone and content will be in keeping with my personal brand.
2. Delegate the content creation of blog posts for my website and to share on social media to increase and maintain follower engagement.
3. Easily pay for content creation products as I need them. 

## Accessibility User Stories

- __*As a user who is colourblind*__, I want the colours and design elements used to employ sufficient contrast so that any visual cues are easily apparent.
- __*As a keyboard user*__, I want to be able to navigate the application using the keyboard.
- __*As a user using screen reader technology*__, I want my screen reader to describe the page elements correctly.

## Admin User Stories
### *As an application admin user I want to be able to...*

- Add a new product to the shop.
- Edit an existing product.
- Delete a product from the shop. 
- See a list of registered users.

## Application Creator User Stories
### *As the application creator and Lionize business stakeholder I want to be able to...*

- Create and maintain a user-friendly platform allowing business owners, stakeholders and employees to easily see and understand the services on offer.
- Ensure that the application is as accessible as possible to include as wide a variety of users as possible.
- Accept online payments from users.
- Increase Lionize's client base and profits through use of the website and associated ease of online orders.

#### back to [contents](#table-of-contents) 
<br>

# Strategy

## Project Goals
To create a web application that successfully showcases Lionize's services and offers clients access to a B2B order and payment portal, that both enhances their user experience *and* increases Lionize's customer loyalty and trust.

## Target Users
As outlined above Lionize's target market are businesses in need of digital marketing services. SMEs, sole traders and larget corporations all fall under this umbrella.

## Research
The user registration / dashboard formula for web applications has been around a good while now. It is a tried and tested structure for client communication and engagement.

To research the best design and structural mechanisms to use for this project, I visited a number of Saas and online store websites to see how they present their information and how they structure their payment portals.

## Value to the User
All classes of users benefit from a versatile online ordering and payment system. It streamlines the design process for website orders and it cuts out needless administration for orders that are recurring, such as social media management. 

The informational aspects of the website deliver value insofar as they communicate information about the services on offer, allowing potential clients to make informed decisions on whether or not they want to work with Lionize. 

The user dashboard access, after registration delivers a more personalized service to clients, but in an efficient digital way in keeping with the fast pace of technological innovation.

#### back to [contents](#table-of-contents) 
<br>

# Scope

## Core Theme
The crux of this application's purpose is as a B2B service provider that allows clients to register and login and access an order and payments portal that makes doing business with Lionize streamlined and easy.

## Feature Ideas Table

 #|Opportunity/Potential Feature | Importance | Viability | Score
---|------------ | -------------|--------------|------------------
. | __*GUEST USER FUNCTIONALITY & FEATURES*__ 
1.| Browse the website easily and view separate pages for each service offered.  | 10 | 10 | 20
2.| Contact Lionize with questions. | 9 | 10 | 19
. | __*APP NAVIGATION FUNCTIONALITY & FEATURES*__
1.|  There is a main navbar with links to the homepage, the service details pages & the contact form for unregistered users. |10|10|20
2.| The main navbar changes to include links to the Shop & the User Portal for logged in users. |9|8|17
3.| When a user has navigated to any of the user portal or shop pages, there is a second side navigation on desktop with all the attendent links. | 8 | 8 |16
4.| On mobile the above links are nested within the hamburger navigation. 
. | __*USER REGISTRATION FUNCTIONALITY & FEATURES*__ 
1.| Register as a new user  | 10 | 10 | 20
2.| Register using an email address | 7 | 10 | 17
3.| Confirm password when registering | 7 | 7 | 14
4.| Register a username as separate from login email | 3 | 9 | 12
5.| Receive an email link to confirm the user is supplying a genuine email address |3 | 5 | 8
6.| Receive an email confirmation of registration. |3 | 5 | 8
. | __*USER LOGIN / LOGOUT FUNCTIONALITY & FEATURES*__ 
1.| Users can login with email and password |10 | 10 | 20
2.| When a user logs in, they are brought to a user portal |7 | 10 | 17
3.| A session is started and the user's login status is remembered as they use the application |9 | 9 | 18
4.| When a user is logged in they can view their account information.  |10 | 9 | 19
5.| A user has to be logged in, in order to acccess their user portal. |10 | 9 | 19
6.| A user can logout to end their session. |10 | 10 | 20
. | __*USER PORTAL FUNCTIONALITY & FEATURES*__ 
1.| The user portal consists of any information personal to that specific user. |6 | 10 | 16
2.| Users can view a form of their profile / billing information and they can edit the same. |6 | 6 | 12
3.| Users can view their current shopping bag. |8 | 8 | 16
4.| Users can view a list of all their past orders. |5 | 8 | 13
5.| Users can click into view the details of any of these past orders. |5 | 7 | 12
6.| When a user logs out their shopping bag information is saved to their user profile and remembered when they log back in. | 4 | 2 | 6
7.| Lionize can upload designs, contracts and other files so that they are accessible to users from their dashboards. |2 | 3 | 5
8.| Users can add widgets of their social media accounts to their user portal to view their accounts while inside the application. | 2 | 3 | 5
. | __*SHOP FUNCTIONALITY & FEATURES*__ 
1.| Users can order digital products directly from the user portal / shop area. |6 | 6 | 12
2.| The shop is divided into 4 categories of products: Web Design, SEO, Social Media Management & Content Creation. |4 | 5 | 9
3.| Users can filter the products on the "All Products" shop page by searching for a particular keyword.  |6 | 6 | 12
4.| Users can view an overview of all the products in a specific category on that categories. |9 | 8 | 17
5.| Users can click in to see details of the products they are interested in. |7 | 8 | 15
6.| Users can see the VAT amount added to each product. |6|7|13
7.| Users can add products they want into a shopping bag. |10|10|20
8.| Users can navigate to a shopping bag page and easily see all the products they have added. |10|10|20
9.| Users can update & remove items from their shopping bag. |9|9|18
10.| Users get immediate feedback in the form of messages on screen when they alter their shopping bag in any way. |8|8|16
11.| The VAT added to the products is visible for each individual product & the total amount of VAT on the shopping bag page. |7|7|14
12.| Users can pay securing using a credit card. |10|10|20
13.| If a user has saved their profile / billing information, the checkout page form is auto-populated with this info. |8|8|16
14.| When a user successfully purchases a product, a confirmation email is sent to their email. |8|8|16
15.| If a user enters incorrect card information they are informed of this immediately via an error message. |8|6|14
. | __*ADMIN FUNCTIONALITY & FEATURES*__ 
1.| Admin can add, edit & delete products on the backend of the application. |9 | 10 | 19
2.| Admin can add, edit & delete products on the frontend of the application. |6 | 9 | 15
3.| There is an admin dashboard page where they can add new products & view a list of users. |4 | 4 | 8
4.| Admin can mark a product as "on sale". |4 | 4 | 8
5.| Admin can mark a product as "new". |4 | 4 | 8
. | __*OTHER FUNCTIONALITY & FEATURES*__ 
1.| Users can upload / select palettes & typography they like for their web design projects. |2 | 2 | 4
2.| Users can create a mood board from images they upload to help Lionize with the design process. |2|1|3
3.| When "new" products are added by admin, the application automatically adds them to a promotional banner that sits across the top of the "All Products" page in the shop. |3|6|9

<br>

 ## List of Final Features 
 *(for an MVP)*

 The features I decided to create an MVP version of this application with are the following:

1. Guest users should be able to easily browse the website and view general information on the kinds of services/products on offer. 
2. They should be able to use a fully functioning contact form to contact Lionize with any questions. 
3. The navigation should be slightly different with more options for logged in users, including a second side nav for the user portal & shop sections of the site. 
4. Users are able to register easily using an email address and separate username, and they must confirm their password when registering.
5. Once registered they should receive an email confirmation link to ensure they are supplying a genuine email address and then they should receive an email confirmation of successful registration.
6. Users should be able to login and logout.
7. When a user starts a session they login status and shopping bag should be remembered as they use the application.
8. Once logged in a user should be able to view the user portal pages which include: their profile/billing details, their current shopping bag and a list of their past orders. 
9. When logged in users also have access to the Shop.
10. Users MUST be logged in to access the user portal pages and the shop. 
11. Users can shop directly from the user portal / shop area of the application.
12. Users can view categories of products to shop using a side navigation bar.
13. Users can perform a keyword search against the product names, descriptions & features. 
14. When shopping users can view the lists of all products (whether in the all products section of divided by category) and they can click into view the specific product details and to add it to their shopping bag if they want. 
15. Users can see the VAT amount on individual products in their shopping bag as well as the total VAT being charged.
16. Users get instant confirmation of any changes to their shopping bag via a modal message on the page.
17. Users can alter their shopping bag directly from this modal or they can close the modal.
18. Users can navigate to a checkout page when they are ready to pay securely using a credit card.
19. The user's billing details will be auto-populated in the checkout form if they have previously saved them. 
20. When a user successfully purchases a product they are sent a confirmation email with all the details. 
21. If any errors occur during the checkout process the user is informed of the error.
22. Admins can add, edit or delete products on the front & backend of the application.
23. Admins can view a list of all users on the front-end of the application.
24. Admins can mark products as "on sale" or "new".
25. "New" products are automatically promoted on a banner that sits over the "All Products" page.

These are the features I determined necessary for the first iteration of this application, with scope to increasing them down the road.


 #### back to [contents](#table-of-contents)
 <br>

# Structure

The structure is somewhat non-linear as the navigation is flexible and depedent on whether a user is registered and logged in or not. Navigation and user flow also differs for admin vs. regular users.  I was aware of the importance of maintaining a level of simplicity as because of its' multi-layered structure I wanted all the pages to be evident and easily accessible for users. I was careful to ensure that both the information architecture and design was intuitive and as simplified as possible. To this end I was careful to include amble feedback in the form of toast messages as well as confirmation modals of any deletion possible. 

## Interaction Design

### Navigation

Navigation is straightforward: for unregistered users there is a top navigation bar on desktops and a hamburger dropdown on mobile & tablets. The navigation for unregistered users directs them to register & then login to their account.

Once logged in, the user is brought to the user portal / shop pages, where a side nav bar is added to the top navigation.

The back button is never relied on, but it is used for the user's convenience on occasion when they have navigated to the product details page for instance. The user can just use the sidebar, but the back button is more directly connected to where they may want to go.

When on the "All Products" page, users can perform a keyword search against the product name, description and features. I also chose to give the different categories of products their own separate pages and views (rather than using Q Objects as with the keyword search) to ensure the best possible SEO performance.

### Consistency and conventions

All content, navigation, typography and information hierarchy are consistent and predictable in nature. The user shopping experience does not deviate from what most users will be used to from their online shopping experience to date. The checkout process likewise follows a predictable formula. 

- All of the most important content is visible on the page and should a user need to scroll this is made amply evident to them. 
- The application's aethetics are consistent throughout the site and rely on the same small set of colours and fonts. 
- Spacing is used to create a clean aethestic and the application never feels crowded or claustrophobic. 
- All fonts used a clean and elegant sans-serif. 
- Icons (such as the search magnifying glass and the airplane send email icon ) are used to enhance metaphorical thinking. 
- Images are used to the same effect as above. Each product has an associated illustration that reflects the content of the product itself to futher reassure the user. 
- All forms rely on labels and / or placeholders to guarantee the user knows what they are doing at all times. 
- The formula of long product list ---> product detail page is used because users will be familiar and happy with this structure. 


### Learnability and communication of functionality

- Because of all of the above consistent and convention attributes, learnability is very high and quick for this application.
- There is very little about it that the user will not be expecting or anticipating. 
- On all pages that require the user to *do* something clearly explain what they are expected to do.

The name of the application itself communicates the essence of what the business does. "Lionize" means to enhance something's or someone's fame and standing in the world. This is followed by a further explanation of the business's raison d'etre. Scrolling down further elucidates what is on offer by succinctly grouping and summarizing the four different categories of products. Each of these product / services introductions can be clicked on to view more details. This process of unfolding follows formulaic lines and is structured this way so as to first pique the user's interest and then slowly feed them more information without overloading them. Once they learn about the products they are then told explicitly why they should register and ideally the homepage user flows ends here, with them clicking the "Register" button. Should they choose to keep scrolling there is an introduction to the main stakeholders in the business and then a contact form should they wish to get in touch.


### Feedback

- Most actions a user can do on the application are followed by various forms of immediate feedback. 
- Clicking the logout button brings the user to a logout confirmation page and then when they confirm their logout intent, they see a toast message telling them they have successfully signed out.
- Registration is confirmed via email.
- Logging in brings the user directly to their user portal as well as delivering a login confirmation message via toast that communicates both the action and reassures them of its accuracy with the inclusion of their username in the message content itself.
- Adding anything to the shopping bag pops up a small toast modal that confirms the addition.
- On the shopping bag page, if a user chooses to remove an item from their bag, this is also confirmed via a toast message.
- When the order is being processed after checkout, a page loading icon informs the user that something is happening.
- When the order is processed the user is brought to the order success page and also sees an order success toast. A confirmation email is also sent to them.
- If a user emails Lionize using the contact form, they also see a message telling them that the email was successfully sent.


### Messages Framework

- The user is given feedback in the form of Bootstrap's toast messages after all major actions.
- This reassures them that they have done what they wanted to do.

### Form Validation Messages

- The register, login and checkout forms include form validation that immediately communicates a message back to the user if they either fail to complete a required field or complete a field incorrectly.
- If the user attempts to log in with incorrect details the message delivered is above the form and in red to communicate the error clearly.

### Deletion Confirmation Modals

- If a user chooses to delete their account completely or if an admin goes to delete a product, they are prompted to confirm these deletions by a modal.


### State Changes 

- All buttons have hover styles applied to reassure the user of their action.
- All links and interactions have visible state changes to ensure the user knows their action is working properly.

### Error Pages 

There are a number of specific error pages that cover the gamut of common errors a user might encounter. The pages are all clear as to what the error was and why it was thrown.

### Pre-Loader

## Information Architecture & User Flow

This application is mostly non-linear in its narrative form. Both first time and logged in users are able to browse the application at their leisure and any linearity is limited to the intended encouragement for first time users to register. This can be simply illustrated by:

        Information ---> Registration

That is the intended user flow for unregistered users, but it is not reflected in the structure, they are free to navigate within the site parameters available to them.

For registered users, this flexibility is enhanced further, they are able to browse, navigate the user portal and there is only lineaity of flow when it comes to actually purchasing a product or products. Then the flow is:

            Shopping Bag ---> Checkout ---> Payment ---> Order Confirmation

And then they are free to browse the application again.

<br>

#### back to [contents](#table-of-contents) 
<br>

# Skeleton 

## Progressive Disclosure

As touched upon in the Structure section the homepage utilizes progressive disclosure to slowly unveil what the application is about, what kind of services/products are for sale and what is expected of the user. The information is delivered piecemeal at first and expanded only *if* the user is interested enough to click on the "Learn More" buttons.

## Metaphorical Thinking

Icons and illustrations are used throughout the application to enhance and reinforce the messages behind the actions required. 

## Establishing Value Through Design

Value is established by ensuring consistency in design and typography, the colour scheme and design elements are consistence throughout and thus the user knows to trust the quality of what is on offer. Space is also used to create a feeling of freedom and clarity, which I think is very important when it comes to ecommerce. Nothing is more off-putting than a crammed online shop.

## Reassuring Conventions

As aforementioned in design and structure and feedback, I've kept everything about the application predictable and conventional. The level of user trust needs to be exceptionally high for any application that is seeking to sell something and take user payment information. 

## Contextually Organised Content

I've also been careful to organise the content and information in contextually appropriate ways. On the homepage for example, all the information pertaining to the categories of products are grouped under a "Services" navigation dropdown menu, rather than displayed separately. Within the user portal the user portal pages are clearly separated from the Shop pages by a line divider on desktop and they are under a separate heading on mobile.

## Wireframes

The best way to view all the wireframes, user flows, mockups, colour palette & typography for this application is by visiting my [public Figma workspace here.](https://www.figma.com/file/PeEEgePG0JpxThhMTRARTu/lionize?node-id=13%3A41)

Alternatively here are the individual wireframes:

1. [Mobile Wireframes]()
2. [Tablet Wireframes]()
3. [Desktop Wireframes]()

If you do opt to view them this way, please click download as the GitHub viewer can expand the smaller files to an uncomfortably large zoom ratio.

<br>

#### back to [contents](#table-of-contents) 
<br>

# Surface

## Design Considerations

My aim was keep the design as simple, clear and open as possible. I think light tones have a more transparent and trustworthy quality for e-commerce and as the business is service / digital based, I thought a light blue tone worked perfectly with yellow as the main colours. Space and clarity were the two driving factors behind the design I opted for and I think they achieve those perception aims well.

## Colour Palette

<p align="center">
  <img src="static/images/colour-palette/lionize-colour-palette.png">
</p>

## Typography

I played it really safe with the typography, I thought Quicksilver worked well for the headings and everything else is a permutation of Open Sans. My intent was to use typography to deliver the message of consistency and safety. Perhaps a little dull, but I think that's ok for ecommerce.

<p align="center">
  <img src="static/images/typography/lionize-typography.png">
</p>

## Design Mockups

I haven't done extensive mockups, rather I have chosen a selection of important pages and limited my mockups to them. 
As the colour theme and typography vary so little and the application as a whole is so consistent, I felt that limited mockups would suffice.

Again, the best way to view these is by visiting my [public Figma workspace here.](https://www.figma.com/file/PeEEgePG0JpxThhMTRARTu/lionize?node-id=13%3A41)

Alternatively here are the individual mockups:

1. [Mobile Mockups]()
2. [Tablet Mockups]()
3. [Desktop Mockups]()

Again, please remember to click download as the GitHub viewer can expand the smaller files to an uncomfortably large zoom ratio.

<br>

#### back to [contents](#table-of-contents) 
<br>

# Database Architecture

## Schema

A relational database was used to structure this project. For development SQLite was used and Postgres was used for the deployed project. 

The following models were integrated:

### __Account__

The allauth Django Account app includes a number of models however as I did not create these, I will not expand on them here, their purpose is to act as the basis for user authentication.

### __Category Model__

I intentionally created a Category model separate from the Product model for allowing an easier expansion of product types / services offered down the line. My thinking is that were I to eventually add subscription services, the Category model can be added as a Foreign Key, and not duplicated.

<br>

| Name | Data Type | Purpose |
| ---- | ----- | --------------- |
| name | string | The product category's "unfriendly" name. |
| friendly_name | string | The product category's human readable name.|


<br>

### __Product Model__

The product model stores the product specific data and is mainly used for product display purposes on the site, but is connected to both the Category & the Order Line Item models.

| Name | Data Type | Purpose |
| ---- | ----- | --------------- |
| category | foreign key | The product's category. A foreign key identifying which of the 4 categories this product belongs in. |
| name | string | The product's "unfriendly" name. Keyword searchable to users. |
| friendly_name | string | The product's human readable name. Keyword searchable to users. |
| description | string | The product's description. Keyword searchable to users. |
| features | string | A list of the product's key features. Keyword searchable to users. |
| price | decimal | The product's price as a decimal number with two decimal places. |
| image_url | string | The product's url. |
| image | string | An image associated with the product. Stored as a varchar file path. |

<br>

### __Order Model__

The order model stores the specific order details and is connected to the order line item model and the user profile.

| Name | Data Type | Purpose |
| ---- | ----- | --------------- |
| order_number | string | A unique order number created by a method on this model using UUID. |
| user_profile | foreign key | A many to one foreign key relationship with a user profile. A user may have many orders. |
| full_name | string | The user's full name. |
| email | string | The user's email address. |
| phone_number | string |  The user's phone number. |
| country | string | The user's country, selected from a dropdown menu. |
| postcode | string | The user's postcode. |
| town_or_city | string | The user's town or city. |
| street_address1 | string | The first line of the user's address. |
| street_address2 | string | The second line of the user's address. |
| county | string | The user's county. |
| date | date object | The date the order was placed. |
| order_total | decimal | The total price of the order ex. VAT to 2 decimal places. |
| vat_total | decimal | The total VAT attached to the order to 2 decimal places. |
| grand_total | decimal | The total price of the order incl. VAT to 2 decimal places. |
| original_bag | string | The user's shopping bag stringified. |
| stripe_pid | string | The user's stripe pid (payment intent id). |


<br>

### __Order Line Item Model__

The order line item model stores the specific details of each unique item in an order, if the order contains multiple items of the same product it stores those as 1 line item but increases the quantity. It is connected to the Order and Product models.

| Name | Data Type | Purpose |
| ---- | ----- | --------------- |
| order | foreign key | A many to one relationship with the order itself. One order can have many line items. |
| product | foreign key | A many to one foreign key relationship with a product. A product may be ordered many times. |
| quantity | integer | The number of this product ordered for this order. |
| lineitem_total | decimal | The total price ex. VAT for this item to 2 decimal places.  |
| lineitem_vat | decimal | The total VAT for this item to 2 decimal places.  |
| lineitem_grand_total | decimal | The total price incl. VAT for this item to 2 decimal places.  |

<br>

### __Profile Model__

The Profile model stores additional user data for information and billing that is not saved by the allauth User model. It is connected on a one to one basis to said User model as well one a one to many basis with the Order model.

| Name | Data Type | Purpose |
| ---- | ----- | --------------- |
| user | foreign key | A one to one relationship between the profile model and the allauth User model |
| default_phone_number | string | The user's phone number. |
| default_street_address1 | string | The first line of the user's address. |
| default_street_address2 | string | The second line of the user's address. |
| default_town_or_city | string | The user's town or city. |
| default_postcode | string | The user's postcode. |
| default_county | string | The user's county. |
| default_country | string | The user's country, selected from a dropdown menu. |
| instagram_handle | string | The user's Instagram username. |
| linkedin_handle | string | The user's LinkedIn username. |
| twitter_handle | string | The user's Twitter username. |
| facebook_handle | string | The user's Facebook username. |

<br>

## Entity Relationship Diagram
<br>



[Click here to view my ERD on Figma.](https://www.figma.com/file/PeEEgePG0JpxThhMTRARTu/lionize?node-id=39%3A2) I have also added it below, but the Figma link is zoomable.


<br>

#### back to [contents](#table-of-contents) 
<br>

# Features 

## 1. Home

The landing page's aim is to deliver a strong and positive first impression to the user and to clearly explain the application's purpose and how it works. It also guides the user towards registering.

<details>
<summary><b>click for features</b></summary>

### Guest User

- Introduces the concept of the website by starting with a strong title and clean elegant design. 
- A business synopsis is featured directly under the main heading. 
- Login & Register buttons are clearly visible both on the top navbar (desktop) and as the user scrolls down in the "Benefits of Registration section."
- Links to each of the services / product categories are present early on in the user's homepage scrolling. 
- Information about the main stakeholders in the company is also outlined on the homepage to increase trust in the business and to put human faces on the company.
- At the bottom of the page is a contact form to communicate with the business.

### Registered & Logged in User

- The only main differences are that the "Login" & "Register" buttons disappear from the navbar and the "Benefits of Registration" changes into a "Thank you for Registering" section with pertinent information and a link to set up the client's free consultation.
- Clicking the link will pre-fill the contact form to email about a consultation. 

</details>

<br>

## 2. Contact 

<details>
<summary><b>click for features</b></summary>


</details>

## 3. Services Information Pages 

<details>
<summary><b>click for features</b></summary>


</details>

## 4. Register

<details>
<summary><b>click for features</b></summary>


</details>

## 5. Login

<details>
<summary><b>click for features</b></summary>


</details>

## 6. User Portal: Profile

<details>
<summary><b>click for features</b></summary>


</details>

## 7. User Portal: Shopping Bag

<details>
<summary><b>click for features</b></summary>


</details>

## 8. User Portal: Order History

<details>
<summary><b>click for features</b></summary>


</details>

## 9. Shop

<details>
<summary><b>click for features</b></summary>


</details>

## 10. Payment Portal

<details>
<summary><b>click for features</b></summary>


</details>

- [4. Responsivity](#responsivity)
    - [Mobile Devices](#mobile-devices-materialize-sm-breakpoint)
    - [Tablet Devices](#tablet-devices-materialize-m-breakpoint)
    - [Desktop Devices](#desktop-devices-materialize-l-breakpoint)
    - [Wide Desktop Devices](#wide-desktop-devices-materialize-xl-breakpoint)

# Future Features To Implement and Issues Remaining

## Adding Features to Products

The addition of specific features to the products works perfectly as long as the administrator adding the products formats them correctly with commas after each new feature. There is potential here for errors, and one way around this would be to incorporate a tag block using JavaScript. 

## Adding Subscription Services for Social Media Management

There is the potential to add monthly subscription services and connect them to the Stripe subscription payment system.
This would streamline the social media management services in particular and allow for better customer retention. 

# Deployment 

## Application deployment using Heroku

1. I created a new Heroku account, then created a new Heroku application selecting Europe as my region, as below: 

<p align="center">
  <img src="static/images/deployment/heroku-deployment-1.png">
</p>

<br>

2. I provisioned a new Postgres database, as below:

<p align="center">
  <img src="static/images/deployment/heroku-deployment-postgres-db.png">
</p>

3. I installed dj_database_url & psycopg2 to enable the connection between Django and Postgres.

4. Then I ran: ``` pip3 freeze > requirements.txt ```

    <p align="center">
        <img src="static/images/deployment/deployment-psyco-djdb.png">
    </p>

5. I imported dj_database_url into my project's settings.py file and then added the POSTGRES database connection as the default database when in production mode alongside the sqlite database, when in development:

<p align="center">
    <img src="static/images/deployment/deployment-db-connection.png">
</p>

6. I created a superuser using ```python3 manage.py createsuperuser```

7. Then I installed gunicorn.

8. I created a Procfile with the following code ```web: gunicorn lionize.wsgi:application``` to tell Heroku to create a web dyno to run gunicorn and serve the application.

9. I temporarily disabled COLLECTSTATIC in the Heroku CLI

<p align="center">
    <img src="static/images/deployment/disable-collectstatic.png">
</p>

10. I added the application's Heroku hostname to ALLOWED_HOSTS in settings.py:

<p align="center">
    <img src="static/images/deployment/deployment-allowed-hosts.png">
</p>


11. I added a SECRET_KEY config variable in Heroku. 

12. I initialized an heroku git remote as below:

<p align="center">
    <img src="static/images/deployment/deploy-heroku-remote.png">
</p>

13. I pushed to Heroku master to deploy using ```git push heroku master```

14. I set up automatic deployments in Heroku by connecting to the Lionize github repo as below:

<p align="center">
    <img src="static/images/deployment/github-heroku-deploy-1.png">
</p>

15. I then enabled automatic deploys by selecting the master branch and clicking the button as below:

<p align="center">
    <img src="static/images/deployment/enable-auto-deploys.png">
</p>

## Setting up AWS S3 

1. I set up an AWS account. 

2. In the AWS Management Console I searched for S3

3. In the S3 Management Console I clicked on "Create bucket" to create a new bucket. I named the bucket lionize-ms4 and selected Europe as my region. I also allowed public access, as below:

<p align="center">
    <img src="static/images/deployment/s3-setup-aws.png">
</p>

4. Once the new bucket was created, I navigated to the properties tab of the bucket and scrolled down to "Static website hosting", clicked "Edit", and then I selected "Enable" under the "Static website hosting" option. I entered index.html & error.html as default values, as below:

<p align="center">
    <img src="static/images/deployment/s3-static-website-hosting1.png">
</p>

<p align="center">
    <img src="static/images/deployment/s3-static-website-hosting2.png">
</p>

5. On the bucket's permissions tab, I added a CORS configuration, as below:

<p align="center">
    <img src="static/images/deployment/s3-cors.png">
</p>

6. On the bucket's policy tab, I clicked on "policy generator" and created a new policy which I added to my bucket.

7. After saving the bucket policy, I scrolled to the "Access control list (ACL)" tab and I checked the list objects box under the "Everyone (public access)" header.

## Setting up AWS Identity and Access Management Configuration

1. In the IAM dashboard I navigated to the "User Groups" tab and created a new group. 

2. Under the policies tab, I clicked on the JSON tab and then "Import managed policy"

<p align="center">
    <img src="static/images/deployment/iam-import-managed-policy.png">
</p>

3. I selected the S3FullAccess policy and clicked import.

<p align="center">
    <img src="static/images/deployment/s3-full-access-policy.png">
</p>

4. I edited the imported JSON code to allow full access to the lionize bucket and its' associated files, using the lionize bucket's arn.

5. I gave the policy a name and description and then created the policy:

<p align="center">
    <img src="static/images/deployment/s3-policy-created.png">
</p>

6. I went back to the "User groups" tab and clicked on the "manage-lionize" group. Then I went to the "permissions" tab and clicked the dropdown menu "Add permission" and then "Attach Policies", I checked the policy just created and then clicked to "Add permissions".

<p align="center">
    <img src="static/images/deployment/iam-policy-attached.png">
</p>


7. I created a user to add to the group with programmatic access.

<p align="center">
    <img src="static/images/deployment/iam-new-user.png">
</p>

8. I downloaded the CSV file containing the new user's access key and secret access key in order to add them to Django to authenticate this user.

9. I then installed boto3 & django-storages, freezing them into requirements.txt and then adding 'storages' to the installed apps list in settings.py

10. I also added the following AWS config variables to my settings.py file for use *only* if the USE_AWS var is found in os.environ:

        AWS_STORAGE_BUCKET_NAME = 'lionize-ms4'
        AWS_S3_REGION_NAME = 'eu-west-1'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'

        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

11. I then added the Access Keys as well as the USE_AWS=TRue to the Heroku config vars.

12. I committed these changes and pushed to github & thus Heroku (because of automatic deployments) and the build collected all the Static files and placed them in the S3 bucket and Heroku served them successfully. 

13. I then created a new folder in my S3 bucket called Media and set permissions to grant publin-read access as below:

<p align="center">
    <img src="static/images/deployment/s3-media-files-permissions.png">
</p>

14. I then uploaded all my in-app images into that folder.

## Setting up Stripe for Deployment

1. I added the STRIPE_PUBLIC_KEY & the STRIPE_SECRET_KEY as config variables in Heroku. 

2. I created a new Production Webhook Endpoint in my Stripe Dashboard by clicking on the "Developers" tab and then "Webhooks" and then "Add endpoint". I then added my application's heroku url + checkout/wh/ to "receive all events", as below:

<p align="center">
    <img src="static/images/deployment/stripe-webhook.png">
</p>

3. I then added the webhook's signing secret to my Heroku config variables.

## Setting up Django Emails for Deployment

1. In the application's associated Gmail account I set up 2-step verification. 

2. Then I generated a new app password and added it to my application's config variables in Heroku alongside a EMAIL_HOST_USER variable that stored the associated email. 

3. Then in settings.py I 

# Tools and Other Resources Used

## 1. Design

## 2. HTML, CSS & SASS

- ### [SASS Button Mixin by Olga](https://codepen.io/OlgaFil/pen/JxjbOb)

    Used for Mixin inspo when designing my buttons.

- ### [ W3 Color Picker](https://www.w3schools.com/colors/colors_picker.asp)

    Used to select colours.

- ### [Responsive Data Tables](https://css-tricks.com/responsive-data-tables/)

    Used to make the shopping bag responsive.

- ### [A Complete Guide To Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

## 3. JavaScript

- ### [Integrating a Modern JavaScript Pipeline into a Django Application](https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/integrating-javascript-pipeline/)

    - Very succinct and accurate guide to the above.

## 4. Python

## 5. Django

- ### [Django Documentation](https://docs.djangoproject.com/en/3.2/)

    I referenced this about every 10 minutes while building this project.

- ### [Django Sass](https://medium.com/@issacsurendar/django-sass-3a8b5b52e89b)

    Information on how to set up Sass files to work with Django.

- ### [Automated Tests - Day 6 - Django Bootcamp](https://www.youtube.com/watch?v=5E_xLmQXOZg)

    Great tutorial on how to write Automated tests for Django.

- ### [What is reverse()?](https://stackoverflow.com/questions/11241668/what-is-reverse)

    Stack Overflow explanation of django 'reverse()'

- ### [How to Include Django Templates from another App](https://python.web.id/posts/detail/django-how-to-include-templates-from-another-app/)

- ### [Django crispy forms - Set label text for multiple fields](https://stackoverflow.com/questions/38724012/django-crispy-forms-set-label-text-for-multiple-fields)

    Used to customise profile form labels.

- ### [Getting the request origin in a Django request](https://stackoverflow.com/questions/21168981/getting-the-request-origin-in-a-django-request)

    Used to work out how to reference the referring page, for back buttons.

- ### [Advanced Form Rendering with Django Crispy Forms](https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html)

    Used to customise the layout and content of all forms on the application.

## 6. Jinja

## 7. General

- ### [Temp Mail](https://temp-mail.org/)

    Used to test email functionality for registrations and logins. 

- ### [Unsplash](https://unsplash.com/)

    Used for the "Who Are We" Bio Photos.

<br>

# Unsplash Images Used

- Photo by <a href="https://unsplash.com/@wocintechchat?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Christina @ wocintechchat.com</a> on <a href="https://unsplash.com/s/photos/women-headshot?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

- Photo by <a href="https://unsplash.com/@wocintechchat?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Christina @ wocintechchat.com</a> on <a href="https://unsplash.com/s/photos/women-headshot?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

- Photo by <a href="https://unsplash.com/@wocintechchat?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Christina @ wocintechchat.com</a> on <a href="https://unsplash.com/s/photos/women-at-work?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

- Photo by <a href="https://unsplash.com/@anikinearthwalker?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Dimitry Anikin</a> on <a href="https://unsplash.com/s/photos/industry?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

- Photo by <a href="https://unsplash.com/@impatrickt?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Patrick Tomasso</a> on <a href="https://unsplash.com/s/photos/cafe?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

- Photo by <a href="https://unsplash.com/@guipetri?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Guilherme Petri</a> on <a href="https://unsplash.com/s/photos/salon?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>


- Photo by <a href="https://unsplash.com/@israelandrxde?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Israel Andrade</a> on <a href="https://unsplash.com/s/photos/office?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

- Photo by <a href="https://unsplash.com/@kellysikkema?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Kelly Sikkema</a> on <a href="https://unsplash.com/s/photos/empty-bag?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  

#### back to [contents](#table-of-contents) 
<br>

# Libraries, extensions and packages

## [Bootstrap v5](https://getbootstrap.com/)

## [Django Compressor](https://django-compressor.readthedocs.io/en/stable/)

Compresses linked and inline JS or CSS into a single cached file.


## [Django Libsass](https://pypi.org/project/django-libsass/)

A django-compressor filter to compile Sass files using libsass.

<br>

#### back to [contents](#table-of-contents) 
<br>

