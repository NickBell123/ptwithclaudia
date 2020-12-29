// $(document).ready(function() {
//     $('.update-cart').click(function () {
//         let productId = this.dataset.product
//         console.log(productId)
//         let action = this.dataset.action
//         console.log(action)

//         if (user === 'AnonymousUser'){
//             console.log('Not logged in...')
//         }else{
//             updateUserCart(productId, action)
//         }
//     })

//     function updateUserCart(productId, action) {
//         let url = 'update_item/'

//         fetch(url, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//                 'X-CSRFToken': csrftoken
//             },
//             body:JSON.stringify({'productID': productId, 'action': action})
//         })
        
//         .then((response) =>{
//             return response.json()
//         })

//         .then((data) =>{
//            console.log('Data:', data)
//            location.reload()
//         })
//     }
// })




