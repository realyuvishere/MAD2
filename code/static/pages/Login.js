import {post} from '../utils.js'

export default {
    template: `
    <div class='d-flex justify-content-center'>
        <div class="mb-3 p-5 bg-light">
            <label for="email" class="form-label">
                Email address
            </label>
            <input type="email" class="form-control" id="email" placeholder="name@example.com" v-model="cred.email">
            <label for="password" class="form-label">
                Password
            </label>
            <input type="password" class="form-control" id="password" v-model="cred.password">
            <button class="btn btn-primary mt-2" @click='login'>Login</button>
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
            cred: {
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
        login() {
            post('/auth/login', this.cred)
            .then(async (res) => {
                const data = await res.json()

                switch (res.status) {
                    case 200:
                        window.alert(data.message)
                        break;
                    case 400:
                        this.error = data.message
                        break
                    default:
                        break;
                }

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
                
            })
        },
    },
}
