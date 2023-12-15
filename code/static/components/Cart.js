import { getUserCartItems } from "../methods.js"

export default {
    template: `
    <div>
        <button type="button" class="btn btn-primary position-relative mx-3" data-bs-toggle="modal" data-bs-target="#userCart">
            <i class="bi bi-handbag"></i>
            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
                {{ cart_items.length }}
                <span class="visually-hidden">items in cart</span>
            </span>
        </button>
        
        <div class="modal fade" id="userCart" tabindex="-1" aria-labelledby="userCartLabel" aria-hidden="true">
            <div class="modal-dialog modal-fullscreen">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="userCartLabel">Your shopping cart</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        
                        

                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-success" @click="checkoutMethod">Checkout</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    `,
    data() {
        return {
            cart_items: []
        }
    },
    created() {
        getUserCartItems().then((res) => console.log(res))
    },
    methods: {
        checkoutMethod() {

        },
        removeItemMethod() {

        },
        addItemMethod() {

        },
        deleteItemMethod(q) {

        }
    },
}
