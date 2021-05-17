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
    - [*Content Requirements*](#content-requirements)
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
        - [Users Collection](#users-collection)
        - [Photos Collection](#photos-collection)
        - [Files Collection](#files-collection)
        - [Chunks Collection](#chunks-collection)
    - [Non-Relational Design](#non-relational-design)
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
3. Quickly and easily see what services and products are on offer.
4. View further details of each of the services on offer, on specific pages dedicated to that service, so as to decide if I want to avail of any of them.
5. View a website that is visually and creatively appealing and physically easy to look at.
6. Notice the login/register options and easily navigate to those pages.
7. Understand the purpose of user registration and the benefits thereof.

## Returning User Stories
## *As a returning user I want to be able to...*

### Registration, Login & User Dashboard
1. Easily register a free account using my email.
2. Receive an email confirmation of my registration.
3. Login to my user account, using my email and password.
4. View my personalized user dashboard. 
5. Edit my account information: change my password, username & other details.
6. Recover my password if I forget it.
7. Delete my account.
8. Receive email confirmation of my account deletion, outlining the data to be deleted, including all order information.

### Pricing
1. View a transparent pricing structure for services and digital products.
2. Use quote calculators to determine a reliable estimate for more detailed custom services.

### Information Gathering
1. Gather more in depth information about the services and products on offer.
2. Easily contact Lionize to ask for specific information about the services and products on offer.

### Orders: One off payment
1. Easily and quickly see how to order a service or product that I'm interested in.
2. Order the product/service online and pay via a payment portal on the application.
3. Receive confirmation of my order via email.
4. See that confirmation and order reflected on my user dashboard.

### Orders: Subscriptions
1. Subscribe to a service and set up a monthly recurring payment via a secure payment portal.
2. Alter my subscription (downgrade or upgrade).
3. Cancel my subscription.
4. Easily view information about my subscription billing.

### Orders: Communication
1. Email Lionize about specific details regarding the service(s) they are providing to me.
2. View wireframes, designs and other files Lionize have created as part of the service they are providing me.


## Persona Based User Stories

### Tom Lynch - Hipster Coffee Shop Owner
### *As a sole trading small business owner I want to be able to...*
1. Order a professional looking website for my small business.
2. See some examples of Lionize's web design work prior to ordering.
3. Easily understand all the various web design options available to me.
4. Create a custom estimate/quote that reflects my requirements, so as to get a solid idea of pricing.
5. Easily communicate with Lionize about my requirements, my order and my billing.

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
3. Easily set up an online recurring payment for the social media management services so that I don't need to worry about it every month.

## Accessibility User Stories
- __*As a user who is colourblind*__, I want the colours and design elements used to employ sufficient contrast so that any visual cues are easily apparent.
- __*As a keyboard user*__, I want to be able to navigate the application using the keyboard.
- __*As a user using screen reader technology*__, I want my screen reader to describe the page elements correctly.

## Application Creator User Stories
### *As the application creator and Lionize business stakeholder I want to be able to...*
- Create and maintain a user-friendly platform allowing business owners, stakeholders and employees to easily see and understand the services on offer.
- Ensure that the application is as accessible as possible to include as wide a variety of users as possible.
- Accept online one-off and recurring payments from users.
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
. | __*USER REGISTRATION FUNCTIONALITY & FEATURES*__ 
1.| Register as a new user  | 10 | 10 | 20
2.| Register using an email address | 7 | 10 | 17
3.| Confirm password when registering | 7 | 7 | 14
4.| Register a username as separate from login email | 3 | 9 | 12
5.| Receive an email link to confirm the user is supplying a genuine email address |3 | 5 | 8
6.| Receive an email confirmation of registration. |3 | 5 | 8
. | __*USER LOGIN / LOGOUT FUNCTIONALITY & FEATURES*__ 
1.| Users can login with email and password |10 | 10 | 20
2.| When a user logs in, they are brought to their user dashboard |7 | 10 | 17
3.| A session is started and the user's login status is remembered as they use the application |9 | 9 | 18
4.| When a user is logged in they can view their account information.  |10 | 9 | 19
5.| A user has to be logged in, in order to acccess their dashboard. |10 | 9 | 19
6.| A user can logout to end their session. |10 | 10 | 20
. | __*USER DASHBOARD FUNCTIONALITY & FEATURES*__ 
1.| The user dashboard is divided into service sections. |6 | 10 | 16
2.| Individual service sections on the user dahsboard include custom quote calculators. |6 | 6 | 12
3.| Users can order digital products directly from their dashboards. |6 | 6 | 12
4.| Users can send in web design consultation requests directly from their dashboards. |4 | 5 | 9
5.| Users can view their orders and payments in a billing section on their dashboards. |8 | 8 | 16
6.| The status of any orders is communicated to users via their dashboards.  |5 | 5 | 10
7.| When a user creates a custom quote, the consultation form is pre-filled with the quote details. |3 | 3 | 6
8.| A user can view & update their account information directly from their dashboard. |6 | 6 | 12
9.| Lionize can upload designs, contracts and other files so that they are accessible to users from their dashboards. |2 | 3 | 5
. | __*ORDER & PAYMENT PORTAL FUNCTIONALITY & FEATURES*__ 
1.| When an initial order consultation with Lionize has been completed and a price is agreed upon for a custom service, the user can view a link to pay the service deposit. |8 | 9 | 17
2.| Clicking the "PAY" link next to the deposit amount in the account section of the user dashboard, will bring the user to a Stripe payment portal where they can complete the payment. |9 | 9 | 18
3.| Once paid, users will receive email confirmation of payment. |8 | 8 | 16
4.| When an initial order consultation with Lionize has been completed, users can subscribe to social media management services via a link on their user dashboard. They are brought to a Stripe payment portal and can sign up for a monthly recurring payment.  |8 | 9 | 17
5.| Users receive an email confirmation each time the subscription payment occurs. |7 | 8 | 15
. | __*OTHER FUNCTIONALITY & FEATURES*__ 
1.| Users can upload / select palettes & typography they like for their web design projects. |2 | 2 | 4

<br>

 ## List of Final Features 
 *(for a MVP)*

 #### back to [contents](#table-of-contents) 
 <br>

# Structure

## Interaction Design

### Navigation

### Consistency and conventions

### Learnability and communication of functionality

### Feedback

### Messages Framework

### Form Validation Messages

### Deletion Confirmation Modals 

### State Changes 

### Error Pages 

### Pre-Loader

## Information Architecture

## User Flow
<br>

#### back to [contents](#table-of-contents) 
<br>

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

## 3. JavaScript

- ### [Integrating a Modern JavaScript Pipeline into a Django Application](https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/integrating-javascript-pipeline/)

    - Very succinct and accurate guide to the above.

## 4. Python

## 5. Django

- ### [Django Sass](https://medium.com/@issacsurendar/django-sass-3a8b5b52e89b)

    Information on how to set up Sass files to work with Django.

- ### [Automated Tests - Day 6 - Django Bootcamp](https://www.youtube.com/watch?v=5E_xLmQXOZg)

    Great tutorial on how to write Automated tests for Django.

- ### [What is reverse()?](https://stackoverflow.com/questions/11241668/what-is-reverse)

    SO explanation of django 'reverse()'.

## 6. Jinja

## 7. General

- ### [Temp Mail](https://temp-mail.org/)

    Used to test email functionality for registrations and logins. 

<br>

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

