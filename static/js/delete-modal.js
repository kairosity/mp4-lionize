var deleteProductModal = document.getElementById('deleteProductModal')
deleteProductModal.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    // Extract info from data-bs-* attributes
    var productId = button.getAttribute('data-bs-product-id')
    var productName = button.getAttribute('data-bs-product-name')
    
    // Update the modal's content.
    var modalTitle = deleteProductModal.querySelector('.modal-title')
    var modalBody = deleteProductModal.querySelector('.modal-body')
    var deletionHref = deleteProductModal.querySelector('.product-delete-button')

    modalTitle.textContent = `DELETION CONFIRMATION`
    modalBody.textContent = `Are you certain you want to delete the product "${productName}"? This is an irreversible action.`
    deletionHref.setAttribute('href', `/products/delete/${productId}/`)

})