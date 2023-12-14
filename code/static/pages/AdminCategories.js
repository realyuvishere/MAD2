import { createCategoryForAdmin, getCategoriesForAdmin } from "../methods.js"

export default {
    template: `
    <div class="w-100">
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#createCategory">
            Create category
        </button>
        
        
        <div class="modal fade" id="createCategory" tabindex="-1" aria-labelledby="createCategoryLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="createCategoryLabel">Create category</h1>
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
                        <button type="button" class="btn btn-success" @click="createCategoryMethod">Create</button>
                    </div>
                </div>
            </div>
        </div>

        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Name</th>
                    <th scope="col">Description</th>
                    <th scope="col">Status</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="category in categories">
                    <th scope="row">{{ category.id }}</th>
                    <td>{{ category.name }}</td>
                    <td>{{ category.description }}</td>
                    <td>
                        <span class="badge text-bg-warning" v-if="category.isRequest">Request</span>
                        <span class="badge text-bg-success" v-if="category.active">Active</span>
                        <span class="badge text-bg-danger" v-if="!category.active">Inactive</span>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    `,
    data() {
        return {
            categories: [],
            payload: {
                name: '',
                description: '',
                active: false
            }
        }
    },
    created() {
        getCategoriesForAdmin()
        .then((res) => {
            this.categories = [...res.data]
        })
    },
    methods: {
        toggleActiveMethod() {
            this.payload.active = !this.payload.active
        },
        createCategoryMethod() {
            createCategoryForAdmin({...this.payload})
            .then((res) => {
                console.log(res)
            })
        }
    },
}
