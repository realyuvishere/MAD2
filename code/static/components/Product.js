import { get_user_role } from "../utils.js"

export default {
    template: `
    <div>
        <div class="card" style="max-width: 20rem;">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
            </div>
            <ul class="list-group list-group-flush">
                <li class="list-group-item">An item</li>
                <li class="list-group-item">A second item</li>
                <li class="list-group-item">A third item</li>
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
                <div class="btn-group w-100" role="group">
                    <button type="button" class="btn btn-primary" @click="addToCartMethod" v-if="role=='user'">Add to cart</button>
                    <button type="button" class="btn btn-warning">Edit</button>
                    <button type="button" class="btn btn-danger">Delete</button>
                </div>
            </div>
        </div>
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
    methods: {
        addProductMethod() {
            this.payload.quantity += 1
        },
        subtractProductMethod() {
            if (this.payload.quantity > 0) this.payload.quantity -= 1
        },

        addToCartMethod() {
            
        },
    },
}
