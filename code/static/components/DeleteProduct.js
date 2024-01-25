import { deleteManagerProduct } from '../methods.js'

export default {
    template: `
    <div>

        <div class="modal fade" id="deleteProductConfirm" tabindex="-1" aria-labelledby="deleteProductConfirmLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="deleteProductConfirmLabel">Delete product</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        Are you sure about this? It can't be reversed.
                    </div>

                    <div class="modal-footer">
                        <button type="button" class="btn btn-danger" @click="deleteProductConfirmMethod" data-bs-dismiss="modal">Yes, do it</button>
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">No, forget it</button>
                    </div>
                </div>
            </div>
        </div>
        
    </div>
    `,
    props: ['p'],
    data() {
        return {
            deleteId: Number(),
            categories: [],
        }
    },
    created() {
        this.deleteId = this.p
    },
    methods: {
        deleteProductConfirmMethod() {
            deleteManagerProduct(this.deleteId)
            .then((res) => {
                console.log(res)
                window.alert('Product deleted.')
            })
        },
    },
}
