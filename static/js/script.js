/* The following code takes data about the user from the request object and prefills the Contact form
with this data to save the user time and energy when requesting a consultation. */

let emailInput = document.querySelector('#id_email')
let subjectInput = document.querySelector('#id_subject')
let messageInput = document.querySelector('#id_message')

const scheduleConsultationBtn = document.querySelector('#schedule-consultation')
const userEmail = document.querySelector('#user-email').getAttribute('data-user-email')
const userFirstName = document.querySelector('#user-first-name').getAttribute('data-user-first-name')
const userLastName = document.querySelector('#user-last-name').getAttribute('data-user-last-name') 
const userPhone = document.querySelector('#user-phone').getAttribute('data-user-phone') 
const userInstagram = document.querySelector('#user-instagram').getAttribute('data-user-instagram') 
const userTwitter = document.querySelector('#user-twitter').getAttribute('data-user-twitter')
const userFacebook = document.querySelector('#user-facebook').getAttribute('data-user-facebook') 
const userLinkedIn = document.querySelector('#user-linkedin').getAttribute('data-user-linkedin')

emailInput.value = userEmail

/* Adds an event listener to the request consultation button and prefills the contact form with the variables collated above */
scheduleConsultationBtn.addEventListener('click', function(){
    emailInput.value = userEmail
    subjectInput.value = `Schedule free business consultation for ${userFirstName} ${userLastName}.`
    messageInput.value = `Dear Lionize,\n\nI would like to take this opportunity to schedule in my complimentary business consultation.\nThe best date & time for me would be ...... [Please edit HERE to suit your schedule].
    \nIn advance of our meeting here is my current business website: [Please enter website here if you have one, otherwise delete this line.]
    \nHere are my social media handles:\nInstagram: ${userInstagram}\nTwitter: ${userTwitter}\nFacebook: ${userFacebook}\nLinkedIn: ${userLinkedIn}
    \nMy phone number is: ${userPhone} should you need to contact me.\n\nThank You,\n${userFirstName}`
})

