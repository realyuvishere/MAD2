import { login } from '../methods.js'

export default {
    template: `
    <div>
        <div class="mb-3 p-5 bg-light">

            <div class="form-floating mb-3">
                <input type="email" class="form-control" id="email" placeholder="name@example.com" v-model="payload.email">
                <label for="email">Email address</label>
            </div>

            <div class="form-floating mb-3">
                <input type="password" class="form-control" placeholder="Password" id="password" v-model="payload.password">
                <label for="password">Password</label>
            </div>

            <button class="btn btn-primary mt-2" @click='loginMethod'>Login</button>
            
            <div class="alert alert-danger alert-dismissible fade show mt-5" role="alert" v-if="error">
                <h6>An error occurred</h6>
                <div>{{error}}</div>
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" @click='clearError'></button>
            </div>
            
        </div> 
    </div>
    `,
    data() {
        return {
            payload: {
                email: null,
                password: null,
            },
            error: null,
        }
    },
    methods: {
        clearError() {
            this.error = ''
        },
        loginMethod() {
            login(this.payload)
            .then((res) => {
                localStorage.setItem('t', res.data.token)
                localStorage.setItem('role', res.data.role)

                this.$router.push({ path: '/' })
            })
        },
    },
}
