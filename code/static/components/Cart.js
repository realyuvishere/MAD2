import { getUserCartItems, removeCartItem, addCartItem, userCartCheckout } from "../methods.js"

export default {
    template: `
    <div>

        <button type="button" class="btn btn-primary position-relative me-3 mb-sm-3 mb-lg-0" data-bs-toggle="modal" data-bs-target="#userCart" @click="getCartItemsMethod">
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
                        <div class="table-responsive">

                            <table class="table table-hover">
                                <thead>
                                    <tr>
                                        <td></td>
                                        <th scope="col" class="w-75">Product</th>
                                        <th scope="col" class="text-center">Quantity</th>
                                        <th scope="col" style="width: 10%">Price</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-if="cart_items.length == 0">
                                        <td colspan="4" class="text-center text-muted p-5">
                                            No items in the cart yet.
                                        </td>
                                    </tr>
                                    <tr v-for="item in cart_items">
                                        <th scope="row">
                                            <button @click="deleteItemMethod(item)" class="btn btn-outline-danger">
                                                <i class="bi bi-trash"></i>
                                            </button>
                                        </th>
                                        <td>{{ item.product_details.name }}</td>
                                        <td>
                                            <div class="input-group">
                                                <button class="btn btn-link" type="button" @click="removeItemMethod(item)">
                                                    <i class="bi bi-dash-circle"></i>
                                                </button>
                                                <input class="form-control" readonly type="number" placeholder="0 units" v-model="item.quantity">
                                                <button class="btn btn-link" type="button" @click="addItemMethod(item)">
                                                    <i class="bi bi-plus-circle"></i>
                                                </button>
                                            </div>
                                        </td>
                                        <td><i class="bi bi-currency-rupee"></i>{{ item.product_details.price }}</td>
                                    </tr>
                                    <tr>
                                        <td></td>
                                        <th colspan="2">Total amount</th>
                                        <td>
                                            <i class="bi bi-currency-rupee"></i>{{ cart_items.reduce((accumulator, item) => accumulator + (item.quantity * item.product_details.price), 0) }}
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
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
        this.getCartItemsMethod()
    },
    methods: {
        getCartItemsMethod() {
            getUserCartItems().then((res) => {this.cart_items = [...res.data.cart_items]})
        },
        checkoutMethod() {
            userCartCheckout()
            .then((res) => {
                alert(res.message)
            })
            .finally(() => {this.getCartItemsMethod()})
        },
        removeItemMethod(item) {
            removeCartItem(item.id, {quantity: 1})
            .then((res) => {})
            .finally(() => {this.getCartItemsMethod()})
        },
        addItemMethod(item) {
            addCartItem(item.id, {quantity: 1})
            .then((res) => {})
            .finally(() => {this.getCartItemsMethod()})
        },
        deleteItemMethod(item) {
            removeCartItem(item.id, {quantity: item.quantity})
            .then((res) => {})
            .finally(() => {this.getCartItemsMethod()})
        }
    },
}
