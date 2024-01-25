import { get_user_role } from "../utils.js"
import Marketplace from "../components/Marketplace.js"
import AdminHome from "../components/AdminHome.js"
import ManagerHome from "../components/ManagerHome.js"

export default {
    template: `

    <div class="w-75">
        
        <Marketplace v-if="role=='user'" />

        <AdminHome v-if="role=='admin'" />
    
        <ManagerHome v-if="role=='manager'" />
        
    </div>

    `,
    data() {
        return {
            role: get_user_role()
        }
    },
    components: {Marketplace, AdminHome, ManagerHome},
    methods: {
        
    },
}
