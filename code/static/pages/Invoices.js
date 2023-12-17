import { getAllInvoices } from "../methods.js"
import Invoice from '../components/Invoice.js'

export default {
    template: `
    <div>
       <Invoice v-for="invoice in invoices" :i="invoice" /> 
    </div>
    `,
    data() {
        return {
            invoices: [],
            error: null,
        }
    },
    components: {
        Invoice
    },
    methods: {
        fetchInvoicesMethod() {
            getAllInvoices()
            .then((res) => {
                this.invoices = [...res.data]
            })
        },
    },
}
