import Cart from './Cart.js'

export default {
    template: `
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
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
                <ul class="navbar-nav" v-if="role=='user'">
                    <li class="nav-item">
                        <router-link class="nav-link" aria-current="page" to="/">Home</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/users">Users</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/create-resource">Create Resource</router-link>
                    </li>
                    <li class="nav-item" v-if="is_login">
                        <button class="nav-link" @click='logout'>logout</button>
                    </li>
                    <li class="nav-item" v-if="is_login">
                        <Cart />
                    </li>
                </ul>
                <ul class="navbar-nav" v-if="role=='admin'">
                    <li class="nav-item">
                        <router-link class="nav-link" aria-current="page" to="/">Home</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/users">Users</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/create-resource">Create Resource</router-link>
                    </li>
                    <li class="nav-item" v-if="is_login">
                        <button class="nav-link" @click='logout'>logout</button>
                    </li>
                </ul>
                <ul class="navbar-nav" v-if="role=='manager'">
                    <li class="nav-item">
                        <router-link class="nav-link" aria-current="page" to="/">Home</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/users">Users</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/create-resource">Create Resource</router-link>
                    </li>
                    <li class="nav-item" v-if="is_login">
                        <button class="nav-link" @click='logout'>logout</button>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    `,
    data() {
        return {
            role: localStorage.getItem('role'),
            is_login: localStorage.getItem('auth-token'),
        }
    },
    methods: {
        logout() {
            localStorage.removeItem('auth-token')
            localStorage.removeItem('role')
            this.$router.push({ path: '/login' })
        },
    },
    components: {
        Cart
    },
}
