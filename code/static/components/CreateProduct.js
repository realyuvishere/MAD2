import {getCategoriesForManager} from '../methods.js'

export default {
    template: `
    <div>

        <div class="form-floating mb-3">
            <input type="text" class="form-control" id="name" placeholder="Name" v-model="payload.name">
            <label for="name">Name</label>
        </div>

        <div class="form-floating mb-3">
            <input type="text" class="form-control" id="description" placeholder="Description" v-model="payload.description">
            <label for="description">Description</label>
        </div>

        <div class="form-floating mb-3">
            <input type="text" class="form-control" id="unit_of_measurement" placeholder="Unit of Measurement" v-model="payload.unit_of_measurement">
            <label for="unit_of_measurement">Unit of Measurement</label>
        </div>
        
        <div class="form-floating mb-3">
            <input type="number" class="form-control" id="quantity_available" placeholder="Quantity Available" v-model="payload.quantity_available">
            <label for="quantity_available">Quantity Available</label>
        </div>

        <div class="form-floating mb-3">
            <input type="datetime-local" class="form-control" id="manufactured" name="manufactured" placeholder="Manufactured on" v-model="payload.manufactured_on">
            <label for="manufactured">Manufactured on</label>
        </div>

        <div class="form-floating mb-3">
            <input type="datetime-local" class="form-control" id="expiry" name="expiry" placeholder="Expires on" v-model="payload.expiry_date">
            <label for="expiry">Expires on</label>
        </div>
    </div>
    `,
    data() {
        return {
            payload: {

            },
            categories: [],
        }
    },
    created(){
        
        getCategoriesForManager()
        .then((res) => {
            this.categories = [...res.data]
        })

    },
    methods: {
        createProductMethod() {
            
        },
    },
}
