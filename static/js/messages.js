let resolvedElements = document.querySelectorAll('.resolved-msg');
let openElements = document.querySelectorAll('.open-msg')

resolvedElements.forEach(el => {

    let parentTd = el.parentElement.parentElement;
    parentTd.classList.add('resolved-dim')

});

openElements.forEach(el => {

    let parentTd = el.parentElement.parentElement;
    parentTd.classList.add('open-message-style')

});