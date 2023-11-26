import {post} from '../utils.js'

export default {
    template: `
    <div class='d-flex justify-content-center' style="margin-top: 25vh">
        <div class="mb-3 p-5 bg-light">
            <div class='text-danger'>{{error}}</div>
            <label for="user-email" class="form-label">Email address</label>
            <input type="email" class="form-control" id="user-email" placeholder="name@example.com" v-model="cred.email">
            <label for="user-password" class="form-label">Password</label>
            <input type="password" class="form-control" id="user-password" v-model="cred.password">
            <button class="btn btn-primary mt-2" @click='login'>Login</button>
        </div> 
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
    methods: {
        login() {
            post('/auth/login', this.cred)
            .then(async (res) => {
                const data = await res.json()
                console.log(data)
                console.log(res)
            })
            // .then((data) => {
            //     console.log(data)
            //     // localStorage.setItem('auth-token', data.token)
            //     // localStorage.setItem('role', data.role)
            //     // this.$router.push({ path: '/' })
                
            // })
            .catch((err) => {
                this.error = err
            })
        },
    },
}
