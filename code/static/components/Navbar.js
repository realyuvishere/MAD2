import { logout, getManagerCSV } from '../methods.js'
import { delete_user, get_token, get_user_role, get_user } from '../utils.js'
import Cart from './Cart.js'

export default {
    template: `
    <nav class="navbar navbar-expand-lg bg-body-tertiary shadow-sm hover hover-shadow">
        <div class="container-fluid">
            <router-link class="navbar-brand" to="/">Grocery Store</router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse justify-content-end" id="navbarNav">

                <ul class="navbar-nav" v-if="!role">
                    <li class="nav-item">
                        <router-link class="nav-link" aria-current="page" to="/login">Login</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/signup">Sign up</router-link>
                    </li>
                </ul>

                <ul class="navbar-nav" v-if="role=='user' && !is_restricted">
                    <li class="nav-item">
                        <router-link class="nav-link" aria-current="page" to="/">Home</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/invoices">Invoices</router-link>
                    </li>
                    <li class="nav-item">
                        <Cart />
                    </li>
                    <li class="nav-item" v-if="is_login">
                        <button class="btn btn-outline-danger" @click='logoutMethod'><i class="bi bi-power"></i></button>
                    </li>
                </ul>

                <ul class="navbar-nav" v-if="role=='admin'">
                    <li class="nav-item">
                        <router-link class="nav-link" aria-current="page" to="/">Home</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/admin/managers">Managers</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/admin/users">Users</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/admin/category">Categories</router-link>
                    </li>
                    <li class="nav-item" v-if="is_login">
                        <button class="btn btn-outline-danger" @click='logoutMethod'><i class="bi bi-power"></i></button>
                    </li>
                </ul>

                <ul class="navbar-nav" v-if="role=='manager' && !is_restricted">
                    <li class="nav-item">
                        <router-link class="nav-link" aria-current="page" to="/">Home</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/manager/products">Manage products</router-link>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" @click="downloadCSVMethod">Download CSV</a>
                    </li>
                    <li class="nav-item" v-if="is_login">
                        <button class="btn btn-outline-danger" @click='logoutMethod'><i class="bi bi-power"></i></button>
                    </li>
                </ul>

            </div>
        </div>
    </nav>
    `,
    data() {
        return {
            role: get_user_role(),
            is_login: get_token(),
            is_restricted: get_user()?.restricted

        }
    },
    components: {
        Cart
    },
    methods: {
        logoutMethod() {
            delete_user()
            logout().then((res) => this.$router.push({ path: '/login' }))
        },
        downloadCSVMethod() {
            getManagerCSV()
            .then((res) => {
                if (res.ok) {
                    console.log(res.body)
                }
            })
        },
    },
}
