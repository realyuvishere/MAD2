import { getUserCartItems } from "../methods.js"

export default {
    template: `
    <div>
        <button type="button" class="btn btn-primary position-relative">
            Cart
            <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
                {{  }}
                <span class="visually-hidden">items in cart</span>
            </span>
        </button>
    </div>
    `,
    data() {
        return {
            cart_items: []
        }
    },
    created() {
        getUserCartItems
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
