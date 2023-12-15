import { searchProduct, getMarketplace } from "../methods.js"

export default {
    template: `
    <div class="w-100">
        <div class="row">
            <div class="col-md-4">
                <div class="form-floating">
                    <select class="form-select" id="filter" v-model="payload.filter">
                        <option value="product">Product name</option>
                        <option value="category">Category name</option>
                    </select>
                    <label for="filter">Filter by</label>
                </div>
            </div>
            <div class="col-md-8">
                <div class="form-floating input-group">
                    <input class="form-control" id="search" name="search" type="text" placeholder="Search..." value="" v-model="payload.search" />
                    <button class="btn btn-outline-dark" type="submit">Search</button>
                    <label for="search" class="form-label">Search...</label>
                </div>
            </div>
        </div>

    </div>
    `,
    data() {
        return {
            products: [],
            payload: {
                search: null,
                filter: 'product',
            },
            error: null,
        }
    },
    created() {
        getMarketplace().then((res) => {
            this.products = [...res.data]
        })
    },
    methods: {
        searchMethod() {
            searchProduct(this.payload).then((res) => {
                console.log(res)
            })
        },
    },
}
