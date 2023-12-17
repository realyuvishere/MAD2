import { getInvoiceById } from "../methods.js"

export default {
    template: `
    <div>

        <div class="modal fade" id="invoiceDetails" tabindex="-1" aria-labelledby="invoiceDetailsLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="invoiceDetailsLabel">Create category</h1>
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

                        <div class="form-check form-switch">
                            <input class="form-check-input" type="checkbox" role="switch" id="activeBool" v-bind:checked="payload.active" @click="toggleActiveMethod">
                            <label class="form-check-label" for="activeBool">Display on / off</label>
                        </div>

                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-success" @click="invoiceDetailsMethod">Create</button>
                    </div>
                </div>
            </div>
        </div>

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
