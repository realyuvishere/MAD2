import { getAllInvoices } from "../methods.js"
import Invoice from '../components/Invoice.js'

export default {
    template: `
    <div>
        <div class="table-responsive">

            <table class="table table-hover">
                <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Purchase date</th>
                        <th scope="col">Total amount</th>
                        <td></td>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th scope="row">{{ invoice.id }}</th>
                        <td>{{ invoice.purchase_date }}</td>
                        <td>{{ invoice.purchased_items.reduce((accumulator, item) => accumulator + (item.purchased_quantity * item.purchased_price), 0) }}</td>
                        <td>
                            <div class="dropdown">
                                <button class="btn btn-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    <i class="bi bi-gear"></i>
                                </button>

                                <ul class="dropdown-menu">
                                    <li>
                                        <button class="dropdown-item">View details</button>
                                    </li>
                                    <li v-if="!invoice.active">
                                        <button class="dropdown-item" @click="activateinvoiceMethod(invoice)">Download file</button>
                                    </li>
                                </ul>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <Invoice :i="invoice" /> 
    </div>
    `,
    data() {
        return {
            invoices: [],
            invoice: {},
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
