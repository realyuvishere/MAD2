export default {
    template: `
    <div class='d-flex justify-content-center'>
        
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
