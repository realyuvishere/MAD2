import { signup } from "../methods"

export default {
    template: `
    <div class='d-flex justify-content-center' style="margin-top: 25vh">
        <div class="mb-3 p-5 bg-light">
            <div class="alert alert-danger" role="alert" v-if="error">{{error}}</div>
            <label for="name" class="form-label">Email address</label>
            <input type="email" class="form-control" id="name" placeholder="name@example.com" v-model="payload.name">
            <label for="email" class="form-label">Email address</label>
            <input type="email" class="form-control" id="email" placeholder="name@example.com" v-model="payload.email">
            <label for="password" class="form-label">Password</label>
            <input type="password" class="form-control" id="password" v-model="payload.password">
            <button class="btn btn-primary mt-2" @click='signupMethod'>Sign up</button>
        </div> 
    </div>
    `,
    data() {
        return {
            payload: {
                name: null,
                email: null,
                password: null,
                role: null,
            },
            error: null,
        }
    },
    methods: {
        signupMethod() {
            signup(this.payload)
        },
    },
}
