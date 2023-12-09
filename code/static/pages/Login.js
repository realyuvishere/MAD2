import { login } from '../methods.js'

export default {
    template: `
    <div class='d-flex justify-content-center'>
        <div class="mb-3 p-5 bg-light">
            <label for="email" class="form-label">
                Email address
            </label>
            <input type="email" class="form-control" id="email" placeholder="name@example.com" v-model="payload.email">
            <label for="password" class="form-label">
                Password
            </label>
            <input type="password" class="form-control" id="password" v-model="payload.password">
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
            login(this.cred)
            .then((res) => {
                console.log(res)
            })
        },
    },
}
