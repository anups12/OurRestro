let cart1 = document.getElementsByClassName("add-to-cart")
for (var i = 0; i < cart1.length; i++) {
    cart1[i].addEventListener('click', function (e) {
        e.preventDefault()
        productId = this.dataset.productid
        action = this.dataset.action
        if (user == 'AnonymousUser') {
            alert("you need to login to use this functionality")
        }
        else {
            if (confirm(" Confirm to modify  your order ") == true) {
                Add_to_cart(productId, action)
            }
        }
    })
}


function Add_to_cart(productId, action) {
    var url = '/add_to_cart/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })
        .then((response) => {
            return response.json()
        }).then((data) => {
            location.reload()
        })

}
