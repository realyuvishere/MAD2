import Home from './pages/Home.js'
import Login from './pages/Login.js'

const routes = [
    { path: '/', component: Home, name: 'Home' },
    { path: '/login', component: Login, name: 'Login' },
]

const router = new VueRouter({
    routes,
})

export default router