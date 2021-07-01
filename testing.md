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

### *As a first time user I want to be able to...*

1. __Easily understand the purpose of the web application.__

  - The landing page is elegant and clear. The name of the business is center-stage and the tagline clearly outlines the purpose of the application: *"A digital agency with fresh ideas to enhance your online presence & brand identity"*

      __PASS__

2. __Quickly and easily understand how to navigate and access information on the website.__

  - The navbar at the top of the application is conventional and intutitive. 

- The content of the homepage itself clearly tells the user what is expected of them and what "next steps" to take i.e. registering.
- The top navbar is mirrored by a footer, which also has links to all pages available to a first-time user.

    __PASS__

3. __Quickly and easily have an idea of what kinds of products are offered.__

  - The four categories of products / services are outlined under the main page heading and "Learn More" buttons are clearly visible.

    __PASS__

4. __View further details of each of the services on offer, on specific pages dedicated to that service, so as to decide if I want to avail of any of them.__

- Clicking on the "Learn More" buttons brings the user to an information page specific to that category of product, which has a further link and CTA to register.

  __PASS__

5. __View a website that is visually and creatively appealing and physically easy to look at.__

- The website is bright, colourful, but without being garish, and user experience is enhanced by its' design, not burdened.

    __PASS__

6. __Notice the login/register options and easily navigate to those pages.__

- The register and login links along the top navbar are set to the right hand side so as to distinguish them from informational pages. 
- This also makes them more noticeable. 
- The login button is also style differently to draw further attention to it and its' use.

    __PASS__

7. __Understand the purpose of user registration and the benefits thereof.__

- There is a section on the homepage called "Benefits of Registration" that covers this question for first-time users.

    __PASS__

8. __Easily register a free account using my email.
Receive an email confirmation of my registration.__

- Registration via the registration form asks for a user's email and then send a confirmation email to the user asking them to confirm their address. 

    __PASS__

## Returning User Goals Testing

### *As a returning user I want to be able to...*

### Registration, Login, Logout, & Update Data

1. __Login to my user account, using my email and password.__

- Registered users can login successfully using email and password, or indeed using their username and password.

    __PASS__

2. __Be redirected to the User Portal and easily view the various custom user pages.__

- On successful login, users are immediately redirected to their profile page, from which (on larger screens) they can view the other User Portal pages from the side navigation, or on mobile from the dropdown menus. 

    __PASS__

3. __Edit my account information.__

- Profile details can be edited and updated via the Profile Page.

  __PASS__

4. __Recover my password if I forget it.__


- Passwords can be changed, whether by choice or because they have been forgotten, via the link present on the login page. A confirmation link is sent to the user's email address and they click it to select a new password.

    __PASS__
  

5. __Logout of my account.__

- User can logout at any time using the "Logout" link in the navigation.

    __PASS__


### Information Gathering

1. __Quickly navigate to the products / services information pages from anywhere on the website.__

- The links to the information pages are available to all users and are ever-present on the main navigation bar.

    __PASS__

2. __Gather more in depth information about the services and products on offer.__

- For unregistered un-authenticated users, the information pages offer good introductory information about the services and products on offer. 

- Logged in users can navigate to the shop, where they can see all the various products listed, and clicking on any of them will bring them to the products details page, where the most in-depth information can be viewed.

- Users also have the option of contacting Lionize via the contact form (also linked separately in the navigation) to ask for clarification or for any more information that they might require.

    __PASS__

3. __Easily contact Lionize to ask for specific information about the services and products on offer.__

- As abovementioned, all users have the option to contact Lionize via the Contact Form.

    __PASS__

4. __Easily find the prices of all products.__

- Users can view the product prices both in the "All Products" and category product listing pages *and* on the specific product details page. 

- The product details page also displays the VAT and the Total incl. VAT. 

- The Shopping Bag dropdown menu and shopping Bag page also display the prices of items a user has selected for purchase. 

- The Checkout Page also displays the full prices of items a User is about to purchase. 

- The order history page displays the prices of items a user has purchased previously.

    __PASS__

5. __View the reviews of other users on products/services I am interested in.__

- The product details page includes any reviews users have added for that particular product. 

    __PASS__

### User Portal

1. __View / add / update my profile details easily on a page specifically for that purpose.__

- Users are brought to their profile page immediately after they sign in. They can edit many of their profile details easily from this page.

    __PASS__

2. __Navigate to my shopping bag quickly from the user portal side bar.__

- Clicking on the "Your Shopping Bag" brings users to their shopping bag. If empty they will see an image of an empty paper bag.

    __PASS__

3. __Easily view all my past orders, and all their attendent details.__

- Clicking on the "Your Orders" link under User Portal, brings users to an exhaustive list of their past orders.
- Each individual order can also be clicked on for more details.

    __PASS__

4. __View a list of my ordered and purchased products that I can review.__

- Clicking on the "Your Reviews" link brings the user to 2 lists: 1. A list of products they can review. 2. A list of products reviews they have written. 

    __PASS__

5. __View a list of all the reviews I have written.__

- As abovementioned this is displayed on the "Your Reviews" Page.

    __PASS__


### Shopping

1. __Browse all products.__

- Users can browse all products on the "Shop All Products" shopping page. 

    __PASS__

2. __Easily view the prices & specific details of each product by clicking into a product details page.__

- By clicking on the "More Details" button on any of the five shopping pages, users are brought to that product's details page.

    __PASS__

3. __Browse products by category.__

- Clicking on any of the category shop pages allow users to shop by category. 

    __PASS__

4. __Filter products by keyword using a search form.__

- The search input on the "All Products" Page fulfils this role.

    __PASS__
  
5. __Add products to my shopping bag and have this visually confirmed for me.__

- Clicking "Add to Bag" on any of the product details page add that product to the user's shopping bag and prompts a toast pop-up confirming this and displaying the current bag contents.

    __PASS__

6. __Easily view all the items in my shopping bag.__

- Shopping bag contents can be viewed in 3 ways: 

  1. The toast pop-up mentioned above displays the current bag contents anytime a user updates their bag in any way. 
  2. Clicking the shopping cart icon opens a dropdown box with the shopping bag contents displayed. 
  3. Navigating to the shopping bag page under the User Portal navigation link, brings the user to the most detailed shopping bag view.

    __PASS__

7. __Update the items in my shopping bag, by adding more or less of an item.__

- A user can achieve this easily by using the quantity selector buttons on the shopping bag page.

    __PASS__

8. __Remove any item from my shopping bag.__

- Users can click the "remove" icon that sits at the end of each item row on the shopping bag page, to delete all quantities of that item from their bag.

    __PASS__


9. __Make changes to my shopping bag and see these changes reflected immediately without having to visit the shopping bag page.__

- When an item is added to the shopping bag, those changes are reflected in the toast pop-up that follows the action. 

    __PASS__

10. __Email Lionize with a custom quotation request for a specific product/service I have in mind that I cannot find in the shop.__

- The contact form link is readily available to all users.

    __PASS__

### Purchasing

1. __Purchase the products I have added to my shopping bag.__

- Clicking on the "Secure Checkout" button from the shopping bag page, or the "Checkout" button from the shopping cart dropdown will bring the user to the checkout page, where they can input their payment details and purchase their item(s).

    __PASS__

2. __Use my credit card to pay for my items.__

- The checkout page accepts credit cards. 

    __PASS__

3. __Be confident in the knowledge that my payment is being handled securely.__

- The payment portal is handled by Stripe which is secure.
- The payment portal sits under HTTPS which the user's browser will designate as secure. 
- The link to the checkout page reads "Secure Checkout" which will reassure users.
- The brief intro text on the checkout page itself tells the user it is secure. 

    __PASS__

4. __View the VAT added to both the individual products and the total cost before paying.__

- The VAT breakdown is fully detailed on the shopping bag page, and the VAT total is outlined on the checkout page.

    __PASS__

5. __Have my personal details such as name, email, phone number & address saved to my profile and automatically populate the checkout form.__

- If the user has completed the profile page form, their personal details will be prefilled on the checkout page.
- If not, when they complete the checkout page form, they can tick the box to "save this information to my profile", so it will be auto-populated the next time around.

    __PASS__

6. __See confirmation of my order after completing the checkout process.__

- An order confirmation is the first thing users see after purchasing any products successfully.

    __PASS__

7. __Receive an email confirming my order after completing the checkout process.__

- An email is sent with the order details after any product is purchased. 

    __PASS__
  
8. __Have the VAT reflected on the order confirmation.__

- The VAT charged is present on the order confirmation.

    __PASS__

9. __Navigate to my order history page and easily see a list of past orders processed with all associated information clearly outlined.__

- The order history page is accessible via the User Portal and lists orders from most recent to oldest. 

## Persona Based User Stories

### Tom Lynch - Hipster Coffee Shop Owner
### *As a sole trading small business owner I want to be able to...*

1. __Order a professional looking website for my small business.__

- There are multiple web-design products on offer. 

    __PASS__

2. __See some examples of Lionize's web design work prior to ordering.__

- There are a few examples on display on the web-design inforamational page.
- Users are free to contact Lionize via the contact form to request any further details they might want.

    __PASS__

3. __Easily understand all the various web design options available to me.__

- These are clearly outlined in the product details. Including a name, description and list of features. 
- If a user has any other questions, they can contact Lionize via the contact form.

    __PASS__

4. __Easily communicate with Lionize about my requirements, my order and my billing.__

- If a user has any questions, they can contact Lionize via the contact form.

    __PASS__

### Annalise Maior - Real Estate Marketing Manager
### *As a regional marketing manager of a large corporation I want to be able to...*

1. __Delegate the social media management of our Irish branch to specialists.__

- Lionize offers multiple social media management options.

2. __Improve all social media KPIs and see a measurable return on investment.__

- Creating a social media strategy using Lionize products would lead to a measurable return on investment. 

    __PASS__

### Rosemary Geoghan - Plumbing Co. CEO
### *As the CEO of a plumbing company seeking to future-proof how we communicate with clients, I want to be able to...*

1. __Order a new ecommerce site, with an easy-to-use CMS.__

- Ecommerce websites are offered as part of Lionize's web-design products.

    __PASS__

2. __Get the project up and running and then delegate the project management & website administration to our marketing dept.__

- With a CMS attached to the website, other members of staff are able to manage it.

    __PASS__

### David Murphy - Entrepreneurial Make-up Artist
### *As a createive professional whose brand is focused around my personality, I want to be able to...*

1. __Confidently delegate social media management, secure in the knowledge that tone and content will be in keeping with my personal brand.__

- Lionize's various social media management products will fulfill this.

    __PASS__

2. __Delegate the content creation of blog posts for my website and to share on social media to increase and maintain follower engagement.__

- Lionize offers many content creation products including blog post writing that would increase follower engagement. 

    __PASS__

3. __Easily pay for content creation products as I need them.__

- The shopping and checkout sections of the application are fully functional. 

    __PASS__

## Accessibility User Goals Testing

1. __*As a user who is colourblind*__, __I want the colours and design elements used to employ sufficient contrast so that any visual cues are easily apparent.__

- The application has been fully tested for colourblind users and employs sufficient contrast across the board.

- Testing was done using the ["Web Disability Simulator"](https://chrome.google.com/webstore/detail/web-disability-simulator/olioanlbgbpmdlgjnnampnnlohigkjla?hl=en), a very useful and important tool.

__Total Colourblindness__:
<br>

<p align="center">
  <img src="static/images/accessibility/total-cb.png">
</p>

<br>

__Red / Green Colourblindness__:

<br>

<p align="center">
  <img src="static/images/accessibility/red-green-cb.png">
</p>

<br>

__Yellow / Blue Colourblindness__:

<br>

<p align="center">
  <img src="static/images/accessibility/yellow-blue-cb.png">
</p>

<br>

  __PASS__
  
2. __*As a keyboard user*__, __I want to be able to navigate the application using the keyboard.__

- The application is fully keyboard accessible and has been thouroughly tested using just the keyboard to navigate. 
- It employs "skip to main" links on all pages.
- Focus elements are clear.

    __PASS__

3. __*As a user using screen reader technology*__, I want my screen reader to describe the page elements correctly.

- Aria-Labels have been used extensively.
- [Screen Reader](https://chrome.google.com/webstore/detail/screen-reader/kgejglhpjiefppelpmljglcjbhoiplfn?hl=en) tech has been used to test the application.

    __PASS__

## Admin User Stories
### *As an application admin user I want to be able to...*

1. __Add a new product to the shop.__

- Under the Admin "Products" tab, admins can click on the "Add Product" button, fill out the form and a new product is easily and quickly added to the shop. 

    __PASS__

2. __Edit an existing product.__

- By navigation to the Products dashboard, under the Admin Portal navigation option, admin users can click to "Edit" any aspect of a product's listing. 

    __PASS__

3. __Delete a product from the shop.__

- Again, by navigating to the admin product dashboard, admin users can click the black "Delete" button. 
- They will be prompted by a modal asking them to confirm deletion, and when they do so that product is deleted. 

- However, in a late addition to the original application design, I also decided to include "Add to Shop" and "Remove from Shop" options, which are less destructive than the "Delete" option. 

    __PASS__

4. __See a list of registered users and any emails they have sent to Lionize.__

- By navigating to the User Dashboard under the Admin Portal, admin users can view an exhaustive list of the application's users.
- Various important details are also listed here. 

- By navigating to the Messages Dashboard under the Admin Portal, admin users can view an exhaustive list of messages sent by users to Lionize via the contact form.

- Admin can opt to mark each message as "Resolved" or they can "Re-Open" them if the issue needs re-opening. 

    __PASS__

## Application Creator User Goals Testing
### *As the application creator and Lionize business stakeholder I want to be able to...*

1. __Create and maintain a user-friendly platform allowing business owners, stakeholders and employees to easily see and understand the services on offer.__

- This has been achieved by this application. It is user-friendly, has prioritized a high positive user experience and the services and products on offer have been displayed and outlined in a simple, effective and aesthetically pleasing manner.

    __PASS__


2. __Ensure that the application is as accessible as possible to include as wide a variety of users as possible.__

- As already delved into during accessibility user testing, care was given to ensure the application is accessible for a wide variety of users.

    __PASS__

3. __Accept online payments from users.__

- Payments are accepted securely and records are saved to the database.

    __PASS__

4. __Increase Lionize's client base and profits through use of the website and associated ease of online orders.__

- This would be a natural corollary of the application's functionality and design. 

    __PASS__

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

## Development version of application css not loading.

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

## First & Last Name Disconnect Issue

__Issue:__ I needed a way to allow users to add/edit their first & last names on their profile page and have this reflected and updated on the Django auth user model as well as the UserProfile Model. This was important as the checkout page form specifically asks for the first & last names and it gets them from calling the ```get_full_name()``` method on the Django auth User object. 

<br>

__Fix:__ I intially tried to combine two forms on the User Portal's Profile Page, but that was overly complicated. Eventually I added code to the POST method on the User Profile form. So that when the users update their first & last names on the User Profile Model, the POST method automatically updates the User auth model as well:

            User = get_user_model()
            user_to_update = get_object_or_404(User, username=request.user)
            user_to_update.first_name = form.cleaned_data['default_first_name']
            user_to_update.last_name = form.cleaned_data['default_last_name']
            user_to_update.save()


## Error in Console When Attempting to Fire Bootstrap Modal

__Issue:__ When attempting to integrate a Bootstrap modal, it refused to fire and the following error showed in the Console:

<p align="center">
  <img src="static/images/issues/modal-error.png">
</p>

<br>

__Fix:__ I found [this Stack Overflow Post](https://stackoverflow.com/questions/67440523/bootstrap-v5-modal-show-issue) describing the error exactly and it directed me to place the bootrap.bundle.min.js link just before the closing body tag, instead of in the head of the page. Doing so fixed the issue.


## Changing Site Domain & Name

__Issue:__ To change my site domain from example.com to lionize.com & likewise name from example.com to Lionize, I deleted the example.com site and replaced it with a new one for lionize.com, which immediately created the following error anytime I navigated anywhere relating to the database:

<p align="center">
  <img src="static/images/issues/site-error.png">
</p>

<br>

__Fix:__ First I tried to re-add example.com using the django shell by doing:

      manage.py shell
      from django.contrib.sites.models import Site
      site = Site.objects.create(domain='example.com', name='example.com')
      site.save()

This had no effect and when I tried to add the same site again, I got a uniqueness Integrity error, so it DID add it successfully, but it still wasn't working. <br>

Then I found [this issue report](https://github.com/maxking/docker-mailman/issues/12) on github that referred to the SITE_ID variable in the Django settings file. Changing that from 1 to (I assumed 2), worked and I regained access to the admin page.

Then of course I had the issue of local vs. deployed version of the site, as I realised the dangers of just deleting the site in the database, I didn't want to risk repeating that for the deployed version of the application. Instead I added a conditional SITE_ID setting, and then edited (instead of deleting) the domain & name for the deployed version, so its SITE_ID remained 1. The conditional code in settings uses the DATABASE_URL variable, as that was already present:

<p align="center">
  <img src="static/images/issues/site-id-fix.png">
</p>


## Communicating effectively with the user on the Reviews Page

__Issue:__ If the user has no current products to review, it was important to me, not to just leave the left hand column on the review page blank. If the user has yet to purchase any products the message renders as "You have not ordered any products yet." This was easily achieved in the template as the "else" clause to ```{% if orders %}```, however it was more complicated to template a message to a user who *had* orders attached to their profile, but who had already reviewed all the orders. If you look at the code below you can see why:

      {% if orders %}
        {% for order in orders %}
            {% for item in order.lineitems.all %}
                {% if not item.reviewed %}
                    <div class="review-border container orders-to-review">
                        <small><strong>Order #:</strong> {{order.order_number|truncatechars:12}}</small>
                        <small><strong>Order Date:</strong> {{order.date}}</small>
                        <p></p>
                        <p><strong>Category:</strong> {{item.product.category.friendly_name}}</p>
                        <p><strong> Product: </strong> {{item.product.friendly_name}}</p>
                        <a class="review-product-button button button-accent" href="{% url 'product_detail' item.product.id %}#add-review">Review</a>
                    </div>
                {% endif %}
            {% endfor %}
        {% endfor %}
    {% else %}
        <div class="review-border container orders-to-review text-align-center">
            <p>You have not ordered any products yet.</p>
        </div>  
    {% endif %}

There is no possibility of an "else" clause against "if not item.reviewed" because it looks at all the orders in the order collection. 

__Fix:__ To add a conditional message I therefore decided that I would use JavaScript to check whether the class "orders-to-review" was present in the document, as that would only be present *if* there were orders to review and if not I programmed the following to write to the page:

      if (!ordersPresent){
    ordersNotPresent.innerHTML = `<p>You have no orders to review.</p>`
    }

## Skip To Main & Autofocus 

__Issue:__ This is more of a note than an issue, when integrating the "skip to main" links on each page, I found that the autofocus widget on the forms interfered with its functioning, which has led me to conclude that autofocus itself as a mechanism is not accessibility friendly. 

It forces keyboard users to engage with whatever form is on the page, so in an example whereby they might no longer wish to be on that page, they would have to tab through an entire form before being able to access the navigation again.

__Fix:__ I deleted the autofocus functionality from my forms, instead trusting the user to click into them manually.

## Gmail Connection Issue

__Issue:__ This application is connected to a Gmail email account via 2-factor authorization and a secure app password. Everything was working perfectly and emails were delivering and then it stopped working for no apparent reason.


<br>

<p align="center">
  <img src="static/images/issues/smtp-error.png">
</p>

<br>

- It would seem that gmail disabled the account because of the app connection.

<br>

<p align="center">
  <img src="static/images/issues/gmail_disabled.png">
</p>

<br>

__Fix:__ I changed the email address I was using and reconnected everything from scratch for the new email lionizedigitalmarketing56@gmail.com and at the time of writing this, everything is functional, however as there was no obvious trigger for the last disconnection, there is no way of guaranteeing that the same won't happen again. This is unfortunate because the registration process is depedent on there being that functional email connection present.



## Messages Date Updating

__Issue:__ During testing I discovered that marking messages as Resolved and Re-Opened was overwriting their date attribute, thus making it useless in terms of organising the messages by original date of receipt.

__Fix:__ I changed the date option on the model from 

        date = models.DateField(auto_now=True)

to:

        date = models.DateField(auto_now_add=True)

Which stopped the date being overwritten each time the instance of the model was saved.


<br>

<div align="center">
    <img src="static/images/issues/messagesbug.gif" width="600">
</div>

<br>

# Status Code Testing

## 200 Status Code Testing

<details>
<summary><b>click for details</b></summary>

<br>

## Guest Users

- / - __PASS__
- /webdesign - __PASS__
- /seo - __PASS__
- /social-media-management - __PASS__
- /content-creation - __PASS__
- /#contact-us - __PASS__
- /accounts/signup/ - __PASS__
- /accounts/login/ - __PASS__


<br>

<p align="center">
  <img src="static/images/status-code/200-guest.png">
</p>

<br>

- /accounts/confirm-email/ - __PASS__
- /accounts/confirm-email/<confirmation_code>/ - __PASS__

<br>

<p align="center">
  <img src="static/images/status-code/200-guest-2.png">
</p>

<br>

## Logged in Regular Users

- / - __PASS__
- /webdesign - __PASS__
- /seo - __PASS__
- /social-media-management - __PASS__
- /content-creation - __PASS__
- /#contact-us - __PASS__
- /user-portal/profile/ - __PASS__
- /bag/ - __PASS__
- /user-portal/orders - __PASS__
- /user-portal/order_history/<order_number> - __PASS__
- /user-portal/reviews - __PASS__
- /products/ - __PASS__
- /products/?q=seo - __PASS__
- /products/web-design-products/ - __PASS__
- /products/seo-products/ - __PASS__
- /products/social-media-management/ - __PASS__
- /products/content-creation-products/ - __PASS__
- /products/<product_id>:int/ - __PASS__

<br>

<p align="center">
  <img src="static/images/status-code/200-logged-user-1.png">
</p>

<br>


- /checkout/ - __PASS__
- /checkout/checkout_success/<order_number> - __PASS__
- /accounts/logout/ - __PASS__

<br>

<p align="center">
  <img src="static/images/status-code/200-logged-user-2.png">
</p>

<br>

## Logged in Admin Users

- / - __PASS__
- /webdesign - __PASS__
- /seo - __PASS__
- /social-media-management - __PASS__
- /content-creation - __PASS__
- /#contact-us - __PASS__
- /user-portal/profile/ - __PASS__
- /bag/ - __PASS__
- /user-portal/orders - __PASS__
- /user-portal/order_history/<order_number> - __PASS__
- /user-portal/reviews - __PASS__
- /products/ - __PASS__
- /products/?q=seo - __PASS__
- /products/web-design-products/ - __PASS__
- /products/seo-products/ - __PASS__
- /products/social-media-management/ - __PASS__
- /products/content-creation-products/ - __PASS__
- /products/<product_id>:int/ - __PASS__
- /checkout/ - __PASS__
- /checkout/checkout_success/<order_number> - __PASS__
- /accounts/logout/ - __PASS__

- /admin-product-dashboard - __PASS__
- /admin-product-dashboard?q=seo - __PASS__
- /products/add/ - __PASS__
- /products/edit/ - __PASS__

<br>

<p align="center">
  <img src="static/images/status-code/200-admin-1.png">
</p>

<br>

- /products/delete/<int:product_id>/ - __PASS__
- /products/remove/<int:product_id>/ - __PASS__
- /products/addtoshop/<int:product_id>/ - __PASS__

<br>

<p align="center">
  <img src="static/images/status-code/200-admin-2.png">
</p>

<br>

- /admin-user-dashboard - __PASS__
- /admin-user-dashboard?q=mariella - __PASS__
- /admin-messages-dashboard - __PASS__
- /user-portal/mark-closed/<int:message_id> - __PASS__
- /user-portal/mark-active/<int:message_id> - __PASS__


<br>

<p align="center">
  <img src="static/images/status-code/200-admin-3.png">
</p>

<br>

</details>

<br>

## 302 Status Code Testing

The following url requests by the following categories of users should return a 302 redirect status code:

<details>
<summary><b>click for details</b></summary>

<br>

### Guest Users

- /user-portal/profile/ - __PASS__
- /bag/ - __PASS__
- /user-portal/orders - __PASS__
- /user-portal/order_history/<order_number> - __PASS__
- /user-portal/reviews - __PASS__

<br>

<p align="center">
  <img src="static/images/status-code/302-guest-1.png">
</p>

<br>

- /products/ - __PASS__
- /products/?q=seo - __PASS__
- /products/web-design-products/ - __PASS__
- /products/seo-products/ - __PASS__
- /products/social-media-management/ - __PASS__
- /products/content-creation-products/ - __PASS__
- /products/<product_id>:int/ - __PASS__


<br>

<p align="center">
  <img src="static/images/status-code/302-guest-2.png">
</p>

<br>

- /checkout/ - __PASS__
- /checkout/checkout_success/<order_number> - __PASS__
- /admin-product-dashboard - __PASS__
- /admin-product-dashboard?q=seo - __PASS__
- /admin-messages-dashboard
- /products/add/ - __PASS__

<br>

<p align="center">
  <img src="static/images/status-code/302-guest-3.png">
</p>

<br>

- /products/edit/<int:product_id>/ (8) - __PASS__
- /products/delete/<int:product_id>/ (51) - __PASS__ 
- /products/remove/<int:product_id>/ (8) - __PASS__
- /products/addtoshop/<int:product_id>/ (51) - __PASS__
- /admin-user-dashboard?q=mariella - __PASS__
- /user-portal/mark-closed/<int:message_id>/ (4) - __PASS__
- /user-portal/mark-active/<int:message_id>/ (5) - __PASS__

<br>

<p align="center">
  <img src="static/images/status-code/302-guest-4.png">
</p>

<br>

## Logged in Regular Users

- /accounts/login/
- /accounts/signup/

<br>

<p align="center">
  <img src="static/images/status-code/302-logged-1.png">
</p>

<br>

## Admin Users

- /accounts/login/
- /accounts/signup/

<br>

<p align="center">
  <img src="static/images/status-code/302-admin-1.png">
</p>

<br>


</details>

<br>

## 403 Status Codes

The following url requests by the following categories of users should return a 403 Forbidden status code:

<details>
<summary><b>click for details</b></summary>

<br>

## Logged in Regular Users

- /user-portal/order_history/<order_number>/ (not their own) - __PASS__
- /admin-product-dashboard - __PASS__
- /admin-product-dashboard?q=seo - __PASS__
- /admin-user-dashboard - __PASS__
- /admin-user-dashboard?q=mariella - __PASS__
- /admin-messages-dashboard - __PASS__
- /products/add/ - __PASS__
- /products/edit/<int:product_id>/ (8) - __PASS__
- /products/delete/<int:product_id>/ (51) - __PASS__ 
- /products/remove/<int:product_id>/ (8) - __PASS__
- /products/addtoshop/<int:product_id>/ (51) - __PASS__
- /user-portal/mark-closed/<int:message_id>/ (4) - __PASS__
- /user-portal/mark-active/<int:message_id>/ (5) - __PASS__

<br>

<p align="center">
  <img src="static/images/status-code/403-logged-1.png">
</p>

<br>

## Logged in Admin (Staff) Users

- /products/delete/<int:product_id>/ (51) - __PASS__  (only superusers are allowed delete products completely)

<br>

<p align="center">
  <img src="static/images/status-code/403-admin-1.png">
</p>

<br>

</details>

<br>

## 404 Status Codes

The following url requests by the following categories of users should return a 403 Forbidden status code:

<details>
<summary><b>click for details</b></summary>

<br>

Any time any user types in an incorrect URL - they should receive a 404 status code.

Specifically important is that urls that are almost correct, as in they have the correct prefix, but lead to a non-existent order number for example, also return a 404 status code.

## Guest Users

- /totally-incorrect-url - __PASS__


<br>

<p align="center">
  <img src="static/images/status-code/404-guest-1.png">
</p>

<br>


## Logged in Regular Users

- /totally-incorrect-url - __PASS__
- /user-portal/order_history/<incorrect order number>/ - __PASS__

<br>

<p align="center">
  <img src="static/images/status-code/404-logged-1.png">
</p>

<br>

## Logged in Admin Users

- /totally-incorrect-url - __PASS__
- /user-portal/order_history/<incorrect order number>/ - __PASS__
- /products/edit/<int:incorrect_product_id>/ (999) - __PASS__
- /products/delete/<int:incorrect_product_id>/ (999) - __PASS__ 
- /products/remove/<int:incorrect_product_id>/ (999) - __PASS__
- /products/addtoshop/<int:incorrect_product_id>/ (999) - __PASS__
- /user-portal/mark-closed/<int:incorrect_message_id>/ (999) - __PASS__
- /user-portal/mark-active/<int:incorrect_message_id>/ (999) - __PASS__

<br>

<p align="center">
  <img src="static/images/status-code/404-admin-1.png">
</p>

<br>

</details>

<br>

# Functionality Testing

## Base Functionality

## 1. Navigation

__PASS__

Testing process:

- Clicked through each main navbar link to ensure they directed the user to the correct page. -- __PASS__
- Clicked through each mobile navigation link to ensure they directed the user to the correct page. -- __PASS__
- Clicked through each side navigation link to ensure they directed the user to the correct page. -- __PASS__
- Checked every navigation link on the site to ensure they linked to the correct page. -- __PASS__
- Clicked throught every external link to ensure they opened in a new browser tab. -- __PASS__
- Used W3 Link Checker to ensure there were no broken links on the page. -- __PASS__

## 2. Login 

__PASS__

Testing Process:

- I created 2 dummy users, one regular user: Mariella Devalle, and one staff user: Alexandra Marsden. -- __PASS__
- I logged into each account individually to ensure that the login was functional. -- __PASS__
- I used Chrome Dev Tools in both instances to ensure that new sessions were created. -- __PASS__

<br>

<p align="center">
  <img src="static/images/functionality-testing/session-creation.png">
</p>

<br>

<div align="center">
    <img src="static/images/feature-gifs/login.gif" width="600">
</div>

<br>

## 3. Links

Testing Process

__PASS__

- I checked each link on the page to ensure they linked to the correct page. -- __PASS__
- I used W3 Link Checker to ensure there were no broken links. -- __PASS__


## 4. Buttons

Testing Process:

__PASS__

- Checked to ensure that all buttons with no text contained aria-labels for screen reader accessibility. -- __PASS__
- Checked that all form submit buttons, successfully POST(ed) their data, but manually confirming that data's presence in the Django backend. -- __PASS__
- Manually checked each button to ensure that they are only used to submit data and not as a substitute for link tags. -- __PASS__


## 5. Forms 

__PASS__

Testing Process:

- Submitted all forms and then immediately checked the Django backend and the application response to ensure they submitted successfully. -- __PASS__
- Submitted each form with various incorrect or forbidden inputs to ensure that the form was not submitted, and that the appropriate error message was displayed to the user. -- __PASS__

## 6. Input Validations

__PASS__

Bootstrap comes with a useful set of input/form validations, which have been used in this application to supplement Django validations. 

1. Contact Form Validations.

  - Django automatically uses an email validator on EmailFields, so text input in a non-email format will throw a validator error message. 


<br>

<p align="center">
  <img src="static/images/validations/emailvalidator.png">
</p>

<br>

- The subject field has 3 validators:

  - It is a required field.
  - It must have a minimum length of 1
  - It must have a maximum length of 100

- The message field has 3 validators:

  - It is a required field.
  - It must have a minimum length of 20
  - It must have a maximum length of 2000

<br>

<p align="center">
  <img src="static/images/validations/min-length-validator.png">
</p>

<br>

2. Register Form Validations

- These are part and parcel of the Django allauth models, but briefly here are the validations attached:

- The Email field must be in a valid email format.

<br>

<p align="center">
  <img src="static/images/validations/register-form-validation-email.png">
</p>

<br>

<br>

<p align="center">
  <img src="static/images/validations/email-valid-2.png">
</p>

<br>

- The emails entered must match.

<br>

<p align="center">
  <img src="static/images/validations/same-email-valid.png">
</p>

<br>

- Usernames must be a minimum of 5 characters and a maximum of 150 characters.

<br>

<p align="center">
  <img src="static/images/validations/username-valid.png">
</p>

<br>

- Passwords must match.

<br>

<p align="center">
  <img src="static/images/validations/passwords-match-valid.png">
</p>

<br>

- Passwords must be a minimum of 8 characters. (MinimumLengthValidator)


<br>

<p align="center">
  <img src="static/images/validations/password-min.png">
</p>

<br>

- Passwords must not be one of 20,000 common passwords that Django checks it against. (CommonPasswordValidator)

<br>

<p align="center">
  <img src="static/images/validations/common-pass-valid.png">
</p>

<br>

- Passwords must not be purely numeric (NumericPasswordValidator)

<br>

<p align="center">
  <img src="static/images/validations/numeric-pass-valid.png">
</p>

<br>

- Passwords must not be too similar to user attributes. For example if your username is thisMightBeaGre8tPassword678 if you try and set that as your password, Django won't let you. (UserAttributeSimilarityValidator)

<br>

<p align="center">
  <img src="static/images/validations/user-attr-pass-valid.png">
</p>

<br>

3. Login Form Validations

- Your login details must match your registered account details. 
- Username OR Email 
- Password

Django won't tell you which one you have incorrect, to protect against the hacking of accounts. 

<br>

<p align="center">
  <img src="static/images/validations/login-valid.png">
</p>

<br>

4. Profile Form Validations

None of the profile form fields are required on the profile page, however for fields that are filled in, I have added a number of validations:
- The first_name field must not be longer than 40 characters.
- The last_name field must not be longer than 60 characters.

<br>

<p align="center">
  <img src="static/images/validations/profile-val-max-chars-names.png">
</p>

<br>

- The Last Name Field must be longer than 2 characters.

<br>

<p align="center">
  <img src="static/images/validations/profile-val-lastname-min.png">
</p>

<br>

- The Phone Number field must be a number.

<br>

<p align="">
  <img src="static/images/validations/num-val-notnum.png">
</p>

<br>

- The Phone Number field must be at least 5 numbers long:

<br>

<p align="">
  <img src="static/images/validations/num-val-5.png">
</p>

<br>

- The social media fields are not required, but *if* completed the twitter, instagram & facebook fields must all include the @ symbol.

<br>

<p align="">
  <img src="static/images/validations/sm-val.png">
</p>

<br>

5. Review Form Validations

- The Review Title & Review are both required fields.

<br>

<p align="">
  <img src="static/images/validations/review-req-fields.png">
</p>

<br>

- The review title cannot be longer than 120 characters.

- The review itself cannot be longer than 500 characters.

6. Checkout Form Validations

- Full Name, Email, Phone Number, Street Address 1, Town / City and Country are all required fields.

- Stripe takes care of the Payment validation - the credit card number entered must be valid.

<br>

<p align="">
  <img src="static/images/validations/payment-validation.png">
</p>

<br>

7. Admin: Add a new product Form

- The Name field must be a minimum of 2 characters long.
- The Friendly_name field must be a minimum of 2 characters long.
- The Description must be a minimum of 50 characters long.

<br>

<p align="">
  <img src="static/images/validations/50-chars-valid.png">
</p>

<br>

- The fields have the following max_length character limits attached to them:

    - Name: 254
    - Friendly Name: 254
    - Description: 500
    - Features: 1200
    - Price: 6 digits (with 2 decimal places)
    - ImageUrl: 1024

- The Price must be a decimal. The DecimalField field type will not allow users input a non numeric value.
- The image must be an image. The ImageField has its own validations to check that. Django validates the image uploaded using the Python Imaging Library and it will raise a validation error if the file the user is attempting to upload is not an image.

<br>

<p align="">
  <img src="static/images/validations/image-not.png">
</p>

<br>

8. Admin: Edit Product Form

- All of the above validations apply to the edit form as well. 

## 6. Email

__PASS__

Testing Process:

- Used the contact form to send an email to the dummy Lionize email account from my dummy user "Mariella" -- __PASS__

<br>

<p align="">
  <img src="static/images/functionality-testing/email-test-1.png">
</p>

<br>

- Verified its successful receipt by logging into the Lionize email account and reading the email. -- __PASS__

<br>

<p align="">
  <img src="static/images/functionality-testing/email-test-2.png">
</p>

<br>

## 7. Logout

__PASS__

Testing Process:

- Logged in with my dummy Mariella account and then clicked "Logout" and then manually ensured that Mariella did not have access to any of the logged in functionality. -- __PASS__

- Visually confirmed that the successful logout message was displayed to "Mariella". -- __PASS__

<br>

<p align="">
  <img src="static/images/functionality-testing/logout.png">
</p>

<br>

- Tried again to access one of the logged in only pages e.g. /products/ and confirmed that the application redirected the now guest user to the login page.-- __PASS__

- Checked in Chrome Dev Tools to ensure that Django flushes the session variable. The session variables does not disappear from Chrome Dev Tools, but it changes to reflect the new (non-logged in) session. -- __PASS__

## Advanced Functionality: Regular Users

## User Portal

### 1. Updating Profile

Testing Process:

- Navigate to the "Your Profile" page in the User Portal.
- Alter the profile form data in some way. 
- Click the "Update Information".
- Check that the profile form now displays the new information.

<br>

<div align="center">
    <img src="static/images/feature-gifs/profile.gif" width="600">
</div>

<br>

__PASS__

### 2. Viewing Order History & Viewing Individual Orders

Testing Process:

- Navigate to the "Your Orders" Page. 
- Click on any of the orders to see more details about that past order. 


<br>

<div align="center">
    <img src="static/images/feature-gifs/orders.gif" width="600">
</div>

<br>

__PASS__

### 3. Viewing "Your Reviews" and adding a new review

Testing Process:

- Navigate to and view, the "Your Reviews" Page.
- Click on the "Review" button under any of the "Products To Review".
- Add a review title. 
- Select a star rating from 1-5.
- Write the review.
- Click Submit. 
- Check that the review was added to the product details page.
- Check that the review is now in the "Your Reviews" list on the "Your Reviews" Page.
- Check that that product is no longer listed in the "Products to Review" list.

<br>

<div align="center">
    <img src="static/images/feature-gifs/reviews.gif" width="600">
</div>

<br>

__PASS__

## Shopping

### 1. Browsing & Filtering All Products

Testing Process:

- Navigated to the "All Products" Page in "Shop"
- Searched for "website content"
- Cleared the search field.
- Searched for "Social Media Strategy"

<br>

<div align="center">
    <img src="static/images/feature-gifs/all-products.gif" width="600">
</div>

<br>

__PASS__

### 2. Browsing Product Category Pages

Testing Process:

- Navigated to each of the 4 categories shop pages.
- Checked that all products were in the correct category.

<br>

<div align="center">
    <img src="static/images/feature-gifs/products-cats.gif" width="600">
</div>

<br>

__PASS__

### 3. Adding products to the shopping bag.

Testing Process:

- Navigated to the all products page.
- Added two items to the shopping bag.
- Viewed the shopping bag.
- Verified that those items were listed.

<br>

<div align="center">
    <img src="static/images/feature-gifs/addtobag.gif" width="600">
</div>

<br>

__PASS__

### 4. Updating the quantity of a product in the shopping bag.

Testing Process:

- Navigated to the shopping bag page.
- Added 1 to the quantity of an item.
- Verified that it was added and that the price increased correctly.

<br>

<div align="center">
    <img src="static/images/feature-gifs/addonetobag.gif" width="600">
</div>

<br>

__PASS__


### 5. Removing a product from the shopping bag.

Testing Process:

- Navigated to the shopping bag page.
- Removed a product from the shopping bag.
- Verified that it was removed and the total price changed to reflect that.

<br>

<div align="center">
    <img src="static/images/feature-gifs/removedfrombag.gif" width="600">
</div>

<br>

__PASS__

### 6. Checkout & Purchasing a Product. 

Testing Process:

- Navigated to the shopping bag.
- Clicked on "Secure Checkout".
- Verified that the Form Details were entered correctly.
- Entered the test credit card number. 
- Clicked "Complete Order"
- Viewed checkout successful order confirmation. 
- Clicked on "Your Orders" and verified that new order is now listed at the top.


<br>

<div align="center">
    <img src="static/images/feature-gifs/checkout.gif" width="600">
</div>

<br>


## Advanced Functionality: Admin (Staff & Superuser) Users

## Admin Product Dashboard

### 1. Search for Products

Testing Process:

- Navigated to the "Products" Page under Admin Portal
- Searched for "website content"
- Cleared the search field.
- Searched for "Social Media Strategy"

<br>

<div align="center">
    <img src="static/images/feature-gifs/adminprodsearch.gif" width="600">
</div>

<br>

__PASS__


### 2. Filter by Category

Testing Process:

- Navigated to the "Products" Page under Admin Portal
- Clicked on the various category buttons to ensure they are working correctly.

<br>

<div align="center">
    <img src="static/images/feature-gifs/adminprodfilter.gif" width="600">
</div>

<br>

__PASS__


### 3. Add a New Product

Testing Process:

- On the "Products" Page under Admin Portal, clicked the "Add Product Button".
- Completed the form & uploaded an illustration for the Product.
- Clicked "Add Product"
- Verified that the new product was present in the Shop and under the correct Category Page.

<br>

<div align="center">
    <img src="static/images/feature-gifs/adminaddproduct.gif" width="600">
</div>

<br>

__PASS__

### 4. Edit a Product

Testing Process:

- On the "Products" Page under Admin Portal, clicked on the "Edit" Button of a product.
- Altered some of the product info on the form & clicked "Update Product".
- Verified that the changes had been applied to the product in the Shop and on the Product Details Page.

<br>

<div align="center">
    <img src="static/images/feature-gifs/admineditproduct.gif" width="600">
</div>

<br>

__PASS__

### 5. Remove a Product from the Shop

Testing Process:

- On the "Products" Page under Admin Portal, clicked the "Remove from Shop" button on any product.
- Verified that that button was replaced with an "Add to Shop" button.
- Navigated to the Shop to ensure that that product was nowhere to be seen. 

<br>

<div align="center">
    <img src="static/images/feature-gifs/adminremovefromshop.gif" width="600">
</div>

<br>

__PASS__

### 6. Add a Product to the Shop

Testing Process:

- On the "Products" Page under Admin Portal, clicked the "Add to Shop" button on any product.
- Verified that that button was replaced with an "Remove from Shop" button.
- Navigated to the Shop to ensure that that product is now being displayed.

<br>

<div align="center">
    <img src="static/images/feature-gifs/adminaddtoshop.gif" width="600">
</div>

<br>

__PASS__

### 7. Attempt to Delete a Product

Testing Process:

- On the "Products" Page under Admin Portal, clicked the "Delete" button on the "To Be Deleted" Product.
- Verified that this staff admin user was not allowed to delete the product as that ability is reserved for superusers.

<br>

<div align="center">
    <img src="static/images/feature-gifs/admindeleteproductno2.gif" width="600">
</div>

<br>

__PASS__

### 8. Delete a Product (superusers only)

Testing Process:

- On the "Products" Page under Admin Portal, clicked the "Delete" button on the "To Be Deleted" Product.
- One the delete product page, clicked the "Yes, Delete it!" button.
- Verified that this superuser admin user was able to successfully delete the product.
- Verified that the product had been removed from the database by checking the Django backend.</s>

<br>

<div align="center">
    <img src="static/images/feature-gifs/admindeleteproduct1.gif" width="600">
</div>

<br>


__PASS__


## Admin User Dashboard

### 1. Search for Users

Testing Process:

- Navigated to the "Users" Page under Admin Portal.
- Entered "mariella" in the search bar and clicked search.
- Clicked to reset the search.

<br>

<div align="center">
    <img src="static/images/feature-gifs/adminusersearch.gif" width="600">
</div>

<br>

__PASS__

### 2. Browse Users

Testing Process:

- Navigated to the "Users" Page under Admin Portal.
- Scrolled and browsed users. 

<br>

<div align="center">
    <img src="static/images/feature-gifs/adminuserbrowse.gif" width="600">
</div>

<br>

__PASS__


## Admin Messages Dashboard

### 1. Browse Messages & Mark one message as resolved and re-open another one.

Testing Process:

- Navigated to the "Messages" Page under Admin Portal.
- Browsed the messages.
- Marked a message as "Resolved"
- "Re-Opened" another message.

<br>

<div align="center">
    <img src="static/images/feature-gifs/adminmessages.gif" width="600">
</div>

<br>

__PASS__

# Security Testing

## 1. Testing CSRF Protection

CSRF is hard to test without actively launching an attack, however I did undertake the following checks:

### Testing Process:

- Checked that no important functionality is served by GET requests. __PASS__
- No sensitive data is passed via GET requests. __PASS__
- All POST forms are embedded with Django's CSRF protection. __PASS__

__PASS__

## 2. Testing the Image Field Security

Any application that accepts file uploads instantly opens itself to potential threats. Django's ImageField comes equipped with an image verification protection.

### Testing Process:

- I attempted to upload a non-image file into the Add Product Form.
- Firstly it would not allow me to select any files with non-image suffixes for upload. __PASS__
- When I then re-named a non-image .doc file to a .jpg, Django correctly rejected the POST request and returned an error message, regardless of the fake suffix. __PASS__

__PASS__

## 3. Access Control Testing

One of the most important security checks is that user logins are secure and that other users cannot access sensitive user data that does not pertain to them. 

The way this application is structured is by its nature very secure. All data is returned based on the login credentials passed to Django's allauth. When the application retrieves user data it does so by referencing the user id passed in via the authetication process. 

No specific data is passed through or referenced via a URL, so without the user login details or admin login credentials it is effectively impossible to gain access to user data.

As detailed above during the status code testing, I also attempted to gain access to admin pages without being logged in as an admin user, and I confirmed this was impossible. 

Data altering actions on the application are: 

1. Purchasing a product. (regular user)
2. Altering profile details. (regular user)

3. Adding a new product. (staff user)
4. Editing a product. (staff user)
5. Adding and removing products from the Shop. (staff user)

6. Deleting a product. (superuser) * This *had* been included as a GET request until reaching this security testing process, at which point, I decided that it was safer to change the delete functionality to be a POST request. So now, clicking the delete button brings the superuser to a separate delete page, where they must confirm the deletion via a CSRF protected POST request. I also decided to only grant superusers the power to delete products completely, as it is an irreversible command and given that staff users can remove products from the shop, there is really no need for them to be able to delete products completely from the database. 

*Only for the __CRUD__ requirement in the FullStacks framework assessment guidelines, I would probably remove this functionality completely from the Front End, as it is not needed there. 

7. Marking a message as resolved or open. (staff user)

__PASS__

## 4. Chrome Dev Tools Security Check

- I checked the security summary using Chrome Dev Tools and it passed. __PASS__

<br>

<div align="center">
    <img src="static/images/security/chromedevsecurity.png">
</div>

<br>

<br>

<div align="center">
    <img src="static/images/security/chromedevtoolssecuritycert.png">
</div>

<br>

## 5. Content Security Policy

I tried to implement a CSP using django-csp with the following settings:

    # default source as self
    CSP_DEFAULT_SRC = ("'self'",
            "localhost:8000/",
            "amazonaws.com" )

    # style from our domain and bootstrapcdn
    CSP_STYLE_SRC = ("'self'",  
        "stackpath.bootstrapcdn.com",
        "cdn.jsdelivr.net",
        "https://s3.amazon.com",
        "lionize-ms4.s3-eu-west-1.amazonaws.com",
        "fonts.googleapis.com",
        "fonts.gstatic.com",
        "fontawesome.com",
        "amazonaws.com",
        "unsafe-inline",)

    # scripts from our domain and other domains
    CSP_SCRIPT_SRC = ("'self'",
        "cdn.jsdelivr.net",
        "code.jquery.com",
        "js.stripe.com",
        "https://s3.amazon.com",
        "lionize-ms4.s3-eu-west-1.amazonaws.com",
        "fonts.googleapis.com",
        "fonts.gstatic.com",
        "fontawesome.com",
        "unsafe-inline",)

    # images from our domain and other domains
    CSP_IMG_SRC = ("'self'", 
        "https://s3.amazon.com",
        "lionize-ms4.s3-eu-west-1.amazonaws.com",
        "fonts.googleapis.com",
        "fonts.gstatic.com",
        "fontawesome.com",
        "amazonaws.com")

    # loading manifest, workers, frames, etc
    CSP_FONT_SRC = ("'self'",
        "fonts.googleapis.com",
        "fonts.gstatic.com",
        "fontawesome.com" )
    CSP_CONNECT_SRC = ("'self'",)
    CSP_OBJECT_SRC = ("'self'", )
    CSP_BASE_URI = ("'self'", )
    CSP_FRAME_ANCESTORS = ("'self'", )
    CSP_FORM_ACTION = ("'self'", )
    CSP_INCLUDE_NONCE_IN = ('script-src', )
    CSP_MANIFEST_SRC = ("'self'", )
    CSP_WORKER_SRC = ("'self'", )
    CSP_MEDIA_SRC = ("'self'",
        "https://s3.amazon.com",
        "lionize-ms4.s3-eu-west-1.amazonaws.com",
        "fonts.googleapis.com",
        "fonts.gstatic.com",
        "fontawesome.com",
        "amazonaws.com", )

But no matter what combination of urls I implemented, it would not load static styles correctly.

Some resources online have referenced that newer versions of Bootstrap have become somewhat [harder to integrate into a CSP](https://github.com/twbs/bootstrap/issues/25394).

 There is definitely a way to implement this, but for now it will be added to future application improvements. The CSP was __a lot__ simpler to implement in a Flask application.

## 6. Mozilla Observatory Security Scanning

To check a range of other security concerns, I used the [Mozilla Observatory](https://observatory.mozilla.org/) a super useful free security scanning system.

The application received a B grade when the incomplete CSP was added, however once removed it reverted to a D grade based on the lack of a CSP.

<br>

<div align="center">
    <img src="static/images/security/security-ranking.png">
</div>

<br>

However looking at the breakdown of categories, the overall security profile remains strong. 

# Accessibility Testing

In addition to the accessibility user story testing outlined above, I also ran other manual & automated accessibility tests. 

## Lighthouse Accessibility Tests

### Mobile

### Desktop

## WAVE Web Accessibility Evaluation Tool

This is a great tool for getting a fast overview of a website's accessibility ranking and it highlights any areas that need improvement.