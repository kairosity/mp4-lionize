console.log("connected")

// If there is no "orders-to-review" class in the document. 

let ordersPresent = document.querySelector('.orders-to-review');
let ordersNotPresent = document.querySelector('.no-orders-to-review');

if (!ordersPresent){
    ordersNotPresent.innerHTML = `<p>You have no orders to review.</p>`
}

// Add a p tag to the no-orders-to-review div with the textContent of  "You have no orders to review"