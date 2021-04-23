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
      - [*Accessibility User Stories*](#accessibility-user-stories)
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
        - [*Consistency, conventions and predictability*](#consistency-conventions-and-predictability)
        - [*Learnability and Communication of Functionality*](#learnability-and-communication-of-functionality)
        - [*Feedback*](#feedback)
        - [*Flash Messages*](#flash-messages)
        - [*Form Validation Messages*](#form-validation-messages)
        - [*Deletion Confirmation Modals*](#deletion-confirmation-modals)
        - [*Small Specific Messages*](#small-specific-messages)
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

## Accessibility User Stories
- __*As a user who is colourblind*__, I want the colours and design elements used to employ sufficient contrast so that any visual cues are easily apparent.
- __*As a keyboard user*__, I want to be able to navigate the application using the keyboard.
- __*As a user using screen reader technology*__, I want my screen reader to describe the page elements correctly.

## Application Creator User Stories
### *As the application creator and Lionize business stakeholder I want to be able to...*
- Create and maintain a user-friendly platform allowing business owners, stakeholders and employees to easily see and understand the services on offer.
- Ensure that the application is as accessible as possible to include as wide a variety of users as possible.
- Increase Lionize's client base and profits through use of the website and associated ease of online orders.

# Strategy

## Project Goals
To create a web application that successfully showcases Lionize's services and offers clients access to a B2B order and payment portal, that both enhances their user experience *and* increases Lionize's customer loyalty and trust.

## Target Users
As outlined above Lionize's target market are businesses in need of digital marketing services. SMEs, sole traders and larget corporations all fall under this umbrella. 

## Research
The user registration / dashboard formula for web applications has been around a good while now. It is a tried and tested structure for client communication and engagement. 

To research the best design and structural mechanisms to use for this project, I visited a number of Saas and online store websites to see how they present their information and how they structure their payment portals.

## Value to the User
All classes of users benefit from a versatile online ordering and payment system. It streamlines the design process for website orders and it cuts out needless administration for orders that are recurring such as social media management. 

The informational aspects of the website deliver value insofar as they communication information about the services on offer, allowing potential clients to make informed decisions on whether or not they want to work with Lionize. 

The user dashboard access, after registration delivers a more personalized service to clients, but in an efficient digital way in keeping with the fast pace of technological innovation.