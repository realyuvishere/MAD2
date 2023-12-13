import { getUserTypes, signup } from "../methods.js"

export default {
    template: `
    <div class='d-flex justify-content-center' style="margin-top: 25vh">
        <div class="mb-3 p-5 bg-light">
            <div class="alert alert-danger" role="alert" v-if="error">{{error}}</div>
            
            <div class="form-floating mb-3">
                <input type="text" class="form-control" id="name" placeholder="Name" v-model="payload.name">
                <label for="name">Name</label>
            </div>

            <div class="form-floating mb-3">
                <input type="email" class="form-control" id="email" placeholder="name@example.com" v-model="payload.email">
                <label for="email">Email address</label>
            </div>

            <div class="form-floating mb-3">
                <input type="password" class="form-control" placeholder="Password" id="password" v-model="payload.password">
                <label for="password">Password</label>
            </div>

            
            <div class="form-floating my-3">
                <select class="form-select" id="role" v-model="payload.role">
                    <option v-for="role in roles" v-bind:value="role.id">{{ role.name }}</option>
                </select>
                <label for="role">Role</label>
            </div>

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
            roles: [],
            error: null,
        }
    },
    created() {
        getUserTypes().then((res) => {
            this.roles = [...res.data]
        })
    },
    methods: {
        signupMethod() {
            signup(this.payload)
            .then((res) => {
                localStorage.setItem('t', res.data.token)
                localStorage.setItem('role', res.data.role)

                this.$router.push({ path: '/' })
                
                // switch (res.data.role) {
                //     case 'user':
                //         this.$router.push({ path: '/' })
                //         break
                //     case 'admin':
                //         this.$router.push({ path: '/' })
                //         break
                //     case 'manager':
                //         this.$router.push({ path: '/' })
                //         break
                //     default:
                //         break
                // }
            })
        },
    },
}
