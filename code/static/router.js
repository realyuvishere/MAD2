import Home from './pages/Home.js'
import Login from './pages/Login.js'
import Signup from './pages/Signup.js'

const routes = [
    { path: '/', component: Home, name: 'Home' },
    { path: '/login', component: Login, name: 'Login' },
    { path: '/signup', component: Signup, name: 'Sign up' },
]

const router = new VueRouter({routes})

export default router