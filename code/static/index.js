import router from './router.js'
import Navbar from './components/Navbar.js'
import { get_token } from './utils.js'

router.beforeEach((to, from, next) => {
    if (!get_token()) {

        switch (to.name) {
            case 'Login':
                next()
                break
            case 'Sign up':
                next()
                break
            default:
                next({name: 'Login'})
                break
        }

    } else {
        switch (to.name) {
            case 'Login':
                next({name: 'Home'})
                break
            case 'Sign up':
                next({name: 'Home'})
                break
            default:
                next()
                break
        }
    }
})

new Vue({
    el: '#app',
    template: `
    <div>
        <Navbar :key='has_changed' />
        <div class='d-flex justify-content-center w-100' style="margin-top: 56px">
            <router-view />
        </div>
    </div>
    `,
    router,
    components: {
        Navbar,
    },
    data: {
        has_changed: true,
    },
    watch: {
        $route(to, from) {
            this.has_changed = !this.has_changed
        },
    },
})
