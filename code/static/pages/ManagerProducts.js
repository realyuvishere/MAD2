import { createManagerCategoryRequest, getManagerProducts } from "../methods.js"
import CreateProduct from "../components/CreateProduct.js"
import Product from "../components/Product.js"

export default {
    template: `
    <div class="w-100 p-5 mt-3">
        <div class="d-flex justify-content-around">
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#requestCategory">
                Request new category
            </button>

            <CreateProduct />
        </div>

        <div class="modal fade" id="requestCategory" tabindex="-1" aria-labelledby="requestCategoryLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="requestCategoryLabel">Create category</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        
                        <div class="form-floating mb-3">
                            <input type="text" class="form-control" id="name" placeholder="Name" v-model="payload.name">
                            <label for="name">Name</label>
                        </div>
                        
                        <div class="form-floating mb-3">
                            <input type="text" class="form-control" id="description" placeholder="Description" v-model="payload.description">
                            <label for="description">Description</label>
                        </div>

                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-success" @click="requestCategoryMethod">Create</button>
                    </div>
                </div>
            </div>
        </div>

        <div>
            <div class="my-4 d-flex flex-wrap justify-content-around">
                <Product v-for="product in products" :p="product" />
            </div>
        </div>
    </div>
    `,
    data() {
        return {
            products: [],
            payload: {
                name: '',
                description: '',
            }
        }
    },
    created() {
        this.getManagerProductsMethod()
    },
    components: {
        CreateProduct,
        Product,
    },
    methods: {
        getManagerProductsMethod() {
            getManagerProducts().then((res) => {this.products = [...res.data]})
        },
        requestCategoryMethod() {
            createManagerCategoryRequest(this.payload)
            .then((res) => {
                console.log(res);
            })
        },
    },
}
