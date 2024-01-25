import { getInvoiceById } from "../methods.js"

export default {
    template: `
    <div v-bind="invoice">
        <span>{{ invoice.id }}</span>

    </div>
    `,
    props: ['i'],
    data() {
        return {
            invoice: {},
            error: null,
        }
    },
    created() {
        this.invoice = {...this.i}
    },
    methods: {
        downloadInvoiceMethod(id) {
            getInvoiceById(id)
            .then((res) => {})
        }
    },
}
