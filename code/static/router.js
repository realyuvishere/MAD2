import Admin from './pages/Admin.js'
import Home from './pages/Home.js'
import Login from './pages/Login.js'
import Signup from './pages/Signup.js'
import Marketplace from './pages/Marketplace.js'
import AdminUsers from './pages/AdminUsers.js'
import ManagerHome from './pages/ManagerHome.js'
import ManagerProducts from './pages/ManagerProducts.js'

const routes = [
    { path: '/', component: Home, name: 'Home' },
    { path: '/login', component: Login, name: 'Login' },
    { path: '/signup', component: Signup, name: 'Sign up' },
    { path: '/admin', component: Admin, name: 'Admin home' },
    { path: '/market', component: Marketplace, name: 'Marketplace' },
    { path: '/admin/users', component: AdminUsers, name: 'Admin user dashboard' },
    { path: '/manager', component: ManagerHome, name: 'Manager home' },
    { path: '/manager/products', component: ManagerProducts, name: 'Manager products' },
    { path: '/' }
]

const router = new VueRouter({routes})

export default router