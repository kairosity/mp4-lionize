/* Shows a message to user if they have no orders to review */

let ordersPresent = document.querySelector('.orders-to-review');
let ordersNotPresent = document.querySelector('.no-orders-to-review');

if (!ordersPresent){
    ordersNotPresent.innerHTML = `<p>You have no orders to review.</p>`;
}
