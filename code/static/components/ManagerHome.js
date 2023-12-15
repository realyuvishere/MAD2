export default {
    template: `
    <div>
        
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
            fetch('/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(this.cred),
            })
            .then((res) => res.json())
            .then((data) => {
                console.log(data)
                // localStorage.setItem('auth-token', data.token)
                // localStorage.setItem('role', data.role)
                // this.$router.push({ path: '/' })
                
            })
            .catch((err) => {
                const data = err.response.data
                this.error = data.message
            })
        },
    },
}
