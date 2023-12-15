import { getAllManagers, restrictUserById, unrestrictUserById } from "../methods.js"

export default {
    template: `
    <div class="w-100 p-3">
        <h2 class="my-4">Manage store managers</h2>
        <div class="table-responsive">
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col" class="w-50">Name</th>
                        <th scope="col" class="w-50">Email</th>
                        <th scope="col">Status</th>
                        <th scope="col"></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="manager in managers">
                        <th scope="row">{{ manager.id }}</th>
                        <td>{{ manager.name }}</td>
                        <td>{{ manager.email }}</td>
                        <td>
                            <span class="badge text-bg-success" v-if="manager.active">Active</span>
                            <span class="badge text-bg-danger" v-if="!manager.active">Inactive</span>
                            <span class="badge text-bg-danger" v-if="manager.restricted">Restricted</span>
                        </td>
                        <td>
                            <div class="dropdown">

                                <button class="btn btn-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    <i class="bi bi-gear"></i>
                                </button>

                                <ul class="dropdown-menu">
                                    <li v-if="manager.restricted">
                                        <button class="dropdown-item" @click="unrestrictManagerMethod(manager.id)">Unrestrict this manager</button>
                                    </li>
                                    <li v-if="!manager.restricted">
                                        <button class="dropdown-item" @click="restrictManagerMethod(manager.id)">Restrict this manager</button>
                                    </li>
                                </ul>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    `,
    data() {
        return {
            managers: [],
        }
    },
    created() {
        this.fetchManagersMethod()
    },
    methods: {
        fetchManagersMethod() {
            getAllManagers().then((res) => {this.managers = [...res.data];console.log(res)})
        },
        restrictManagerMethod(id) {
            restrictUserById(id).then((res) => {
                console.log(res);
                this.fetchManagersMethod();
            })
        },
        unrestrictManagerMethod(id) {
            unrestrictUserById(id).then((res) => {
                console.log(res);
                this.fetchManagersMethod();
            })
        }
    },
}
