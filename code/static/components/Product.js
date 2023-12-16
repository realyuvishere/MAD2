import { get_user_role } from "../utils.js"
import EditProduct from "./EditProduct.js"
import DeleteProduct from "./DeleteProduct.js"
import { restrictManagerProduct, unrestrictManagerProduct } from "../methods.js"

export default {
    template: `
    <div>
        <div class="card" style="min-width: 20rem; width: 100%;max-width: 20rem;">
            <div class="card-body">
                <h5 class="card-title">{{ product.name }}</h5>
                <p class="card-text">{{ product.description }}</p>
            </div>
            <ul class="list-group list-group-flush">
                <li class="list-group-item"><i class="bi bi-currency-rupee"></i>{{ product.price }} / {{ product.unit_of_measurement }}</li>
                <li class="list-group-item">Available quantity: {{ product.quantity_available }} {{ product.unit_of_measurement }}</li>
                <li class="list-group-item">Manufacturing date: {{ product.manufactured_on.replace('T', ' ') }}</li>
                <li class="list-group-item">Best before: {{ product.expiry_date.replace('T', ' ') }}</li>
            </ul>

            <div class="card-body" v-if="role=='user'">
                <div class="input-group">
                    <button class="btn btn-link" type="button" @click="subtractProductMethod">
                        <i class="bi bi-arrow-down-circle"></i>
                    </button>
                    <input class="form-control" type="number" placeholder="0 units" v-model="payload.quantity">
                    <button class="btn btn-link" type="button" @click="addProductMethod">
                        <i class="bi bi-arrow-up-circle"></i>
                    </button>
                </div>
            </div>
            <div class="card-footer">
                <button type="button" class="btn btn-primary" @click="addToCartMethod" v-if="role=='user'">Add to cart</button>
                <div class="btn-group w-100" role="group" v-if="role=='manager'">
                    <button type="button" class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#editProduct">Edit</button>
                    <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#deleteProductConfirm">Delete</button>
                    <button type="button" class="btn btn-info" v-if="product.active" @click="deactivateProductMethod">Make unavailable</button>
                    <button type="button" class="btn btn-info" v-if="!product.active" @click="activateProductMethod">Make available</button>
                </div>
            </div>
        </div>
        
        <EditProduct v-if="role=='manager'" :p="product" />
        <DeleteProduct v-if="role='manager'" :p="product.id" />
    </div>
    `,
    props: ['p'],
    data() {
        return {
            product: {
            },
            payload: {
                quantity: 0,
            },
            error: null,
            role: get_user_role()
        }
    },
    created() {
        this.product = {...this.p}
    },
    components: {
        EditProduct,
        DeleteProduct,
    },
    methods: {
        addProductMethod() {
            this.payload.quantity += 1
        },
        subtractProductMethod() {
            if (this.payload.quantity > 0) this.payload.quantity -= 1
        },
        activateProductMethod() {
            unrestrictManagerProduct(this.product.id)
            .then((res ) => {})
        },
        deactivateProductMethod() {
            restrictManagerProduct(this.product.id)
            .then((res ) => {})
        },
        addToCartMethod() {
            
        },
    },
}
