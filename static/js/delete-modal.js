var removeProductModal = document.getElementById('removeProductModal')
removeProductModal.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    // Extract info from data-bs-* attributes
    var productId = button.getAttribute('data-bs-product-id')
    var productName = button.getAttribute('data-bs-product-name')
    
    // Update the modal's content.
    var modalTitle = removeProductModal.querySelector('.modal-title')
    var modalBody = removeProductModal.querySelector('.modal-body')
    var deletionHref = removeProductModal.querySelector('.product-delete-button')

    modalTitle.textContent = `REMOVAL CONFIRMATION`
    modalBody.textContent = `Are you sure you want to remove the product "${productName}"? from the shop? You can reinstate this product using the Django admin login.`
    deletionHref.setAttribute('href', `/products/remove/${productId}/`)
});