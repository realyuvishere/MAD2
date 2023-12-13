export default {
    template: `
    <div class="form-floating mb-3">
        <input type="datetime-local" class="form-control" id="manufactured" name="manufactured" placeholder="Manufactured on">
        <label for="manufactured">Manufactured on</label>
    </div>
    <div class="form-floating mb-3">
        <input type="datetime-local" class="form-control" id="expiry" name="expiry" placeholder="Expires on">
        <label for="expiry">Expires on</label>
    </div>
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
}
