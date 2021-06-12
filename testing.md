# Testing

# Testing Table Of Contents

* [**User Story Testing**](#user-story-testing)
  * [1. First Time User Goals Testing](#first-time-user-goals-testing)
  * [2. Returning User Goals Testing](#returning-user-goals-testing)
  * [3. Accessibility User Goals Testing](#accessibility-user-goals-testing)
  * [4. Application Creator User Goals Testing](#application-creator-user-goals-testing)
* [**Issues and bugs caught during testing**](#issues-and-bugs-caught-during-testing)
    * [1. Toast Initialization](#toast-initialization)
* [**Status Code Testing**](#status-code-testing)
    * [1. 200 Status Code Testing](#200-status-code-testing)
    * [2. 302 Status Code Testing](#302-status-code-testing)
    * [3. 403 Status Code Testing](#403-status-code-testing)
    * [4. 404 Status Code Testing](#404-status-code-testing)
* [**Functionality Testing**](#functionality-testing)
  * [**Base Functionality**](#base-functionality)
    * [1. Navigation](#1-navigation)
    * [2. Login](#2-login)
    * [3. Links](#3-links)
    * [4. Buttons](#4-buttons)
    * [5. Forms](#5-forms)
    * [6. Input Validations](#6-input-validations)
    * [7. Email](#7-email)
    * [8. Logout](#8-logout)
  * [**CRUD Functionality**](#crud-functionality)
    * [Create](#create)
        * [1. New User Registration](#1-new-user-registration)
        * [2. Entering the Competition](#2-entering-the-competition)
    * [Read](#read)
      
    * [Update](#update)
     
    * [Delete](#delete)

* [**Security Testing**](#security-testing)
    * [Testing the CSRF Protection](#testing-the-csrf-protection)
    * [Access Control Testing](#access-control-testing)
* [**Browser Testing**](#browser-testing)
    * [Desktop Browser Testing](#desktop-browser-testing)
    * [Mobile Browser Testing](#mobile-browser-testing)
* [**Responsivity Testing**](#responsivity-testing)
* [**Code Validators**](#code-validators)
    * [1. HTML Validators](#1-html-validators)
        * [W3C HTML Validator](#w3c-html-validator)
        * [W3C Link Checker](#w3c-link-checker)
    * [2. CSS Validators](#2-css-validators)
        * [W3C CSS Validator](#w3c-css-validator)
    * [3. JavaScript Validators](#3-javascript-validators)
        * [JSHint](#jshint)
    * [4. Python Validators](#4-python-validators)
        * [PEP8 Online](#pep8-online)
* [**Performance and Web Development Tools Testing**](#performance-and-web-development-tools-testing)

# User Story Testing

## First Time User Goals Testing

## Returning User Goals Testing

## Accessibility User Goals Testing

## Application Creator User Goals Testing

# Issues and bugs caught during testing

## Toast Initialization

### __Issue:__ When trying to connect Bootstrap Toasts to the Django messages framework, the toasts were not showing. The connection was working as evidenced below, but the call to .show() was not working.

<br>

This image shows that the connection is functional, as the elements are present with the correct number of items in the bag.
<p align="center">
  <img src="static/images/issues/invisible-toast2.png">
</p>

However the toast was not visible.
<p align="center">
  <img src="static/images/issues/invisible-toast.png">
</p>

Inspection of its CSS illustrates that it is the .show() method that is not working. 

<p align="center">
  <img src="static/images/issues/invisible-toast-3.png">
</p>

<br>

### __Fix__: Calling the .show() function inside the toast initialization as below, fixed the issue:


        var toastElList = [].slice.call(document.querySelectorAll('.toast'))
            var toastList = toastElList.map(function (toastEl) {
                return new bootstrap.Toast(toastEl, autohide=false).show()
            })

<br>

## Removing Items from Shopping Bag

### __Issue:__ Clicking to remove an item from the shopping bag was resulting in a 500 Internal Server Error, with no obvious errors in the code or logic. 

The remove from bag view:

<p align="center">
  <img src="static/images/issues/remove-from-bag-code-1.png">
</p>

The error in the console:
<p align="center">
  <img src="static/images/issues/remove-from-bag-e-1.png">
</p>

### __Fix:__ By removing the code from the try & except blocks, I was able to get a clearer picture of the reason for the error, which happened to be the lack of a trailing '/':

<p align="center">
  <img src="static/images/issues/remove-from-bag-e-2.png">
</p>

<br>

Adding a trailing slash in the javascript to match the urls.py file fixed the issue:

    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),


    $('.remove-item').click(function(e) {
        console.log("Remove item clicked")
        var csrfToken = "{{ csrf_token }}";
        var itemId = $(this).attr('id').split('remove_')[1];
        var url = `/bag/remove/${itemId}/`;
        var data = { 'csrfmiddlewaretoken': csrfToken };

        $.post(url, data)
            .done(function() {
                location.reload();
            });
    })

## Development version of application css not loading.

__Issue:__ Static files stopped serving locally once I had successfully deployed to Heroku. 

__Fix:__ As part of the CI Django tutorial I had added the code ```DEBUG = 'DEVELOPMENT' in os.environ``` in my settings.py file which effectively stopped Django serving static files locally if the DEVELOPMENT variable was not present in the environment settings. Adding that variable to my env.py file fixed the issue. 

## Deployed version of application css not loading.

__Issue:__ Static files stopped serving in production once I had successfully solved the above issue. 

__Fix:__ I noticed that the S3 url for serving static files was different to the url I had in my settings. The S3 version included the region, so changing it to the variable below worked to fix this issue.

      AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3-eu-west-1.amazonaws.com'


## Passing Data from the Homepage to an external JavaScript File.

__Issue:__ In order to prefill the contact form for users who have not yet availed of their free consultation, I needed a way to pass the various pieces of user data from Django to JavaScript, as request.user.etc... did not work in an external script file.

__Fix:__ I used the data*- attribute on hidden input fields and gave the fields ids with which to reference them in the JavaScript file. In this way I was able to collect all the user data and manipulate the contact form with JavaScript as below:


        <input id="user-email" type="hidden" data-user-email="{{ request.user.email }}">
        <input id="user-first-name" type="hidden" data-user-first-name="{{ request.user.first_name }}">
        <input id="user-last-name" type="hidden" data-user-last-name="{{ request.user.last_name }}">

## Product "Review" Model Errors

__Issue:__ When creating my product "Review" model the following errors were thrown. 

<br>

<p align="center">
  <img src="static/images/issues/error-userprofile.png">
</p>

<br>

__Fix:__ I had referenced the UserProfile as below and I had omitted the "profiles" reference in the field definition. Changing this:

      user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='review_user')

To this:

      user = models.ForeignKey('profiles.UserProfile', on_delete=models.CASCADE, related_name='review_user')

Fixed the issue.