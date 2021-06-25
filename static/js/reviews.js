
let ordersPresent = document.querySelector('.orders-to-review');
let ordersNotPresent = document.querySelector('.no-orders-to-review');

if (!ordersPresent){
    ordersNotPresent.innerHTML = `<p>You have no orders to review.</p>`
}
