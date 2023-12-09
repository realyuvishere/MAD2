import Admin from './pages/Admin.js'
import Cart from './pages/Cart.js'
import Home from './pages/Home.js'
import Login from './pages/Login.js'
import Signup from './pages/Signup.js'
import Marketplace from './pages/Marketplace.js'

const routes = [
    { path: '/', component: Home, name: 'Home' },
    { path: '/login', component: Login, name: 'Login' },
    { path: '/signup', component: Signup, name: 'Sign up' },
    { path: '/cart', component: Cart, name: 'Cart' },
    { path: '/admin', component: Admin, name: 'Admin home' },
    { path: '/market', component: Marketplace, name: 'Marketplace' },
    // {  }
]

const router = new VueRouter({routes})

export default router