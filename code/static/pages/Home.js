import { get_user_role } from "../utils.js"
import Marketplace from "../components/Marketplace.js"

export default {
    template: `

    <div class="w-75">
        
        <Marketplace v-if="role=='user'" />

        <div v-if="role=='admin'">
            Welcome admin
        </div>
    
        <div v-if="role=='manager'">
            <div>
                
            </div>
        </div>
    </div>

    `,
    data() {
        return {
            role: get_user_role()
        }
    },
    components: {Marketplace},
    methods: {
        
    },
}
