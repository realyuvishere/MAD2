import { searchProduct, getMarketplace } from "../methods.js"

export default {
    template: `
    <div>
        
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
