import { searchProduct, getMarketplace } from "../methods.js"

export default {
    template: `
    <div>
        <div class="form-floating input-group mb-3">
            <input class="form-control" id="search" name="search" type="text" placeholder="Search..." value="" />
            <button class="btn btn-outline-dark" type="submit">Search</button>
            <label for="search" class="form-label">Search...</label>
        </div>
    </div>
    `,
    data() {
        return {
            products: [],
            payload: {
                name: null,
                filter: null,
            },
            error: null,
        }
    },
    created() {
        getMarketplace().then((res) => {
            console.log(res)
            // this.products = [...res.data]
        })
    },
    methods: {
        searchMethod() {
            searchProduct(this.payload).then((res) => {})
        },
    },
}
