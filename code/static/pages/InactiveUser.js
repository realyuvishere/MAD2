export default {
    template: `
    <div class="w-75 vh-100 d-flex justify-content-center align-items-center">
        <div>
            <h1>You are restricted from accessing the site for now. Admin will activate your account.</h1>
            <div>Get in touch with admin for this</div>
            <button class="btn btn-outline-danger" @click='logoutMethod'><i class="bi bi-power"></i> Log out and try again</button>
        </div>
    </div>
    `,
    data() {
        return {}
    },
    methods: {
        logoutMethod() {
            delete_user()
            logout().then((res) => this.$router.push({ path: '/login' }))
        },
    },
}
