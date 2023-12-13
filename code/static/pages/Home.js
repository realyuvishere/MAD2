export default {
    template: `
    <div>
        <div v-if="role=='manager'">
            <div>
                
            </div>
        </div>
    </div>
    `,
    data() {
        return {
            role: localStorage.getItem('role')
        }
    },
    methods: {
        
    },
}
