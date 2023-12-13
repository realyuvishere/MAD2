import { searchProduct } from "../methods.js"

export default {
    template: `
    <div>
        
    </div>
    `,
    data() {
        return {
            payload: {
                name: null,
                filter: null,
            },
            error: null,
        }
    },
    methods: {
        searchMethod() {
            searchProduct(this.payload).then((res) => {})
        },
    },
}
