export default {
    template: `
    <div>
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
            cred: {
                email: null,
                password: null,
            },
            error: null,
        }
    },
    created() {
        
    },
    methods: {
        
    },
}
