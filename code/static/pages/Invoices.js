import { getAllInvoices } from "../methods.js"
import Invoice from '../components/Invoice.js'

export default {
    template: `
    <div class="row w-100">
        <div class="col-md-6">
            <div class="table-responsive">

                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">#</th>
                            <th scope="col">Purchase date</th>
                            <th scope="col">Items purchased</th>
                            <th scope="col">Total amount</th>
                            <td></td>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-if="invoices.length == 0">
                            <td colspan="4" class="text-center text-muted p-5">
                                No invoices.
                            </td>
                        </tr>
                        <tr v-for="inv in invoices">
                            <th scope="row">{{ inv.id }}</th>
                            <td>{{ inv.purchase_date }}</td>
                            <td>{{ inv.purchased_items.length }}</td>
                            <td>{{ inv.purchased_items.reduce((accumulator, item) => accumulator + (item.purchased_quantity * item.purchased_price), 0) }}</td>
                            <td>
                                <div class="dropdown">
                                    <button class="btn btn-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                        <i class="bi bi-gear"></i>
                                    </button>

                                    <ul class="dropdown-menu">
                                        <li>
                                            <button class="dropdown-item" @click="activateinvoiceMethod(inv)">View details</button>
                                        </li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="col-md-6">
            <div v-if="invoice.id">
                <div class="d-flex w-100 justify-content-between align-items-center mb-5">
                    <h2 class="m-0">Invoice #{{ invoice.id }}</h2>
                    <button type="button" class="btn btn-outline-danger" @click="activateinvoiceMethod({})"><i class="bi bi-x-lg"></i></button>
                </div>
                <div class="table-responsive">
                    <table class="table table-hover table-borderless">
                        <tbody>
                            <tr>
                                <th>Purchase date & time</th>
                                <td>{{ invoice.purchase_date }}</td>
                            </tr>
                            <tr>
                                <th># of items bought</th>
                                <td>{{ invoice.purchased_items.length }}</td>
                            </tr>
                            <tr>
                                <th>Total amount paid</th>
                                <td>&#8377; {{ invoice.purchased_items.reduce((accumulator, item) => accumulator + (item.purchased_quantity * item.purchased_price), 0) }}</td>
                            </tr>
                        </tbody>
                    </table>
                    <table class="table table-hover table-light">
                        <thead>
                            <tr>
                                <th>
                                    Item
                                </th>
                                <th>
                                    Price
                                </th>
                                <th>
                                    Quantity
                                </th>
                                <th>
                                    Total
                                </th>
                            </tr>
                        </thead>
                        <tbody>

                            <tr v-for="item in invoice.purchased_items">
                                <td>
                                    {{ item.item_name }}
                                </td>
                                <td>
                                    &#8377; {{ item.purchased_price }}
                                </td>
                                <td>
                                    x {{ item.purchased_quantity }}
                                </td>
                                <td>
                                    &#8377; {{ item.purchased_price * item.purchased_quantity }}
                                </td>
                            </tr>

                            <tr>
                                <th colspan="3">Grand Total</th>
                                <td>&#8377; {{ invoice.purchased_items.reduce((accumulator, item) => accumulator + (item.purchased_quantity * item.purchased_price), 0) }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
    `,
    data() {
        return {
            invoices: [],
            invoice: {}
        }
    },
    created() {
        this.fetchInvoicesMethod();
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
        activateinvoiceMethod(i) {
            console.log(i)
            this.invoice = {...i}
        },
    },
}
