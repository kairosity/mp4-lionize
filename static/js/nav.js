/* Selects the path and splits it and then selects all the navigation
links on the website. Uses 2 for loops to first remove all .active-page classes 
and all .active-page-side-nav classes on page load. Then proceeds to add them back 
to the appropriate pages using very specific splitPath array selectors encompassed
within a long if/else statement.

Then it also adds an event listener to the cart link so that when clicked it changes 
the title to "Shopping Cart".

Finally it adds an event listener to show and hide the shopping cart if the shopping cart
variables are present in the document (i.e. if the user is logged in).
*/
$(function(){

    let path = window.location.href;
    let splitPath = path.split('/').slice(3);
    
    let homeLink = document.querySelector('#home-link');
    let contactLink = document.querySelector('#contact-link');
    let servicesLink = document.querySelector('.services-link');
    let webdesignInfoLink = document.querySelector('#webdesign-info-link');
    let seoInfoLink = document.querySelector('#seo-info-link');
    let smmInfoLink = document.querySelector('#smm-info-link');
    let contentCreationInfoLink = document.querySelector('#content-creation-info-link');

    let userPortalLink = document.querySelector('#user-portal-link');
    let userPortalLinkMob = document.querySelector('.user-portal-link-mob');
    let profilePageLink = document.querySelector('#profile-page-link');
    let profilePageLinkMob = document.querySelector('#profile-page-link-mob');
    let bagLink = document.querySelector('#bag-link');
    let bagLinkMob = document.querySelector('#bag-link-mob');
    let ordersLink = document.querySelector('#orders-link');
    let ordersLinkMob = document.querySelector('#orders-link-mob');
    let reviewsLink = document.querySelector('#reviews-link');
    let reviewsLinkMob = document.querySelector('#reviews-link-mob');

    let shopLink = document.querySelector('#shop-link');
    let shopLinkMob = document.querySelector('#navbarDropdownMenuLink3');
    let shopAllProductsLink = document.querySelector('#shop-all-products-link');
    let shopAllProductsLinkMob = document.querySelector('#shop-all-products-link-mob');
    let shopWebdesignLink = document.querySelector('#shop-webdesign-link');
    let shopWebdesignLinkMob = document.querySelector('#shop-webdesign-link-mob');
    let shopSeoLink = document.querySelector('#shop-seo-link');
    let shopSeoLinkMob = document.querySelector('#shop-seo-link-mob');
    let shopSmmLink = document.querySelector('#shop-smm-link');
    let shopSmmLinkMob = document.querySelector('#shop-smm-link-mob');
    let shopContentCreationLink = document.querySelector('#shop-content-creation-link');
    let shopContentCreationLinkMob = document.querySelector('#shop-content-creation-link-mob');

    let adminLink = document.querySelector('#admin-link');
    let adminLinkMob = document.querySelector('#navbarDropdownMenuLink4');
    let adminProductsLink = document.querySelector('#admin-products-link');
    let adminProductsLinkMob = document.querySelector('#admin-products-link-mob');
    let adminUsersLink = document.querySelector('#admin-users-link');
    let adminUsersLinkMob = document.querySelector('#admin-users-link-mob');
    let adminMessagesLink = document.querySelector('#admin-messages-link');
    let adminMessagesLinkMob = document.querySelector('#admin-messages-link-mob');

    let registerLink = document.querySelector('#register-link');
    let logoutLink = document.querySelector('#logout-link');
    
    let currentActiveElements = document.getElementsByClassName('active-page');
    let currentActiveSideNavElements = document.getElementsByClassName('active-page-side-nav');

    for (let i=0; i<currentActiveElements.length; i++){
        currentActiveElements[i].classList.remove('active-page');
    }
    for (let i=0; i<currentActiveSideNavElements.length; i++){
        currentActiveSideNavElements[i].classList.remove('active-page-side-nav');
    }
    
    if (splitPath == ""){
        homeLink.classList.add('active-page');
    } else if (splitPath == "#contact-us"){
        contactLink.classList.add('active-page');
    } else if (splitPath == 'webdesign' || splitPath == 'seo' || splitPath == 'social-media-management' || splitPath == 'content-creation'){
        servicesLink.classList.add('active-page');
        if (splitPath == 'webdesign'){
            webdesignInfoLink.classList.add('active-page-side-nav');
        } else if (splitPath == 'seo'){
            seoInfoLink.classList.add('active-page-side-nav');
        } else if (splitPath == 'social-media-management'){
            smmInfoLink.classList.add('active-page-side-nav');
        } else if (splitPath == 'content-creation'){
            contentCreationInfoLink.classList.add('active-page-side-nav');
        }
    } else if (splitPath[0] == 'user-portal' || splitPath[0] == 'bag' || splitPath[0] == 'products' && splitPath[1] == 'delete-review' || splitPath[0] == 'products' && splitPath[1] == 'edit-review'){
        userPortalLink.classList.add('active-page');
        userPortalLinkMob.classList.add('active-page');

        if (splitPath[1] == 'profile'){
            profilePageLink.classList.add('active-page-side-nav');
            profilePageLinkMob.classList.add('active-page-side-nav');
        } else if (splitPath[1] == 'orders' || splitPath[1] == 'order_history'){
            ordersLink.classList.add('active-page-side-nav');
            ordersLinkMob.classList.add('active-page-side-nav');
        } else if (splitPath[0] == 'bag'){
            bagLink.classList.add('active-page-side-nav');
            bagLinkMob.classList.add('active-page-side-nav');
        } else if (splitPath[1] == 'reviews' || splitPath[1] == 'edit-review' || splitPath[1] == 'delete-review'){
            reviewsLink.classList.add('active-page-side-nav');
            reviewsLinkMob.classList.add('active-page-side-nav');
        }
    } else if (splitPath[0] == 'checkout' && splitPath[1] == 'checkout_success'){
        userPortalLink.classList.add('active-page');
        userPortalLinkMob.classList.add('active-page');
        ordersLink.classList.add('active-page-side-nav');
        ordersLinkMob.classList.add('active-page-side-nav');

    } else if (splitPath[0] == 'products' && splitPath[1] !== 'add' && splitPath[1] !== 'edit' && splitPath[1] !== 'delete' && splitPath[1] !== 'edit-review' && splitPath[1] !== 'delete-review'){
        shopLink.classList.add('active-page');
        shopLinkMob.classList.add('active-page');

        if (splitPath[1] == ""){
            shopAllProductsLink.classList.add('active-page-side-nav');
            shopAllProductsLinkMob.classList.add('active-page-side-nav');
        } else if (splitPath[1] == 'web-design-products'){
            shopWebdesignLink.classList.add('active-page-side-nav');
            shopWebdesignLinkMob.classList.add('active-page-side-nav');
        } else if (splitPath[1] == 'seo-products'){
            shopSeoLink.classList.add('active-page-side-nav');
            shopSeoLinkMob.classList.add('active-page-side-nav');
        } else if (splitPath[1] == 'social-media-management'){
            shopSmmLink.classList.add('active-page-side-nav');
            shopSmmLinkMob.classList.add('active-page-side-nav');
        } else if (splitPath[1] == 'content-creation-products'){
            shopContentCreationLink.classList.add('active-page-side-nav');
            shopContentCreationLinkMob.classList.add('active-page-side-nav');
        }
    } else if (splitPath[0].includes('admin-product-dashboard') || splitPath[0].includes('admin-user-dashboard') || splitPath[0].includes('admin-messages-dashboard') || splitPath[1] == 'add' || splitPath[1] == 'edit' || splitPath[1] == 'delete') {
        adminLink.classList.add('active-page');
        adminLinkMob.classList.add('active-page');
        if (splitPath[0].includes('admin-product-dashboard') || splitPath[1] == 'add' || splitPath[1] == 'edit' || splitPath[1] == 'delete'){
            adminProductsLink.classList.add('active-page-side-nav');
            adminProductsLinkMob.classList.add('active-page-side-nav');
        } else if (splitPath[0].includes('admin-user-dashboard')){
            adminUsersLink.classList.add('active-page-side-nav');
            adminUsersLinkMob.classList.add('active-page-side-nav');
        } else if (splitPath[0].includes('admin-messages-dashboard')){
            adminMessagesLink.classList.add('active-page-side-nav');
            adminMessagesLinkMob.classList.add('active-page-side-nav');
        }
    } else if (splitPath[1] == 'signup'){
        registerLink.classList.add('active-page');
    } else if (splitPath[1] == 'logout'){
        logoutLink.classList.add('active-page');
    }
    // If there is a desktop cart menu link in the document, then listen for clicks on it. 
    if(document.querySelector('#navbarDropdownMenuLinkCart')){
        let cartLink = document.querySelector('#navbarDropdownMenuLinkCart');
        let cartTitle = document.querySelector('#cart-title');
        
        cartLink.addEventListener('click', function(){
            cartTitle.textContent = 'Shopping Cart:';
        });
    }
    // If the mobile dropdown cart element is present, then listen for clicks on it.
    if (document.querySelector('#dropdown-mob-cart')) {
        let dropdownMobCart = document.querySelector('#dropdown-mob-cart');
        let secondCartUl = document.querySelector('#cart-ul');

        dropdownMobCart.onclick = function(){
        secondCartUl.classList.toggle('show');
        }
    }    
});
