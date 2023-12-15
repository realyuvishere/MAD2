// import Admin from './pages/Admin.js'
// import ManagerHome from './pages/ManagerHome.js'
import Home from './pages/Home.js'
import Login from './pages/Login.js'
import Signup from './pages/Signup.js'
import AdminUsers from './pages/AdminUsers.js'
import AdminCategories from './pages/AdminCategories.js'
import ManagerProducts from './pages/ManagerProducts.js'
import Invoices from './pages/Invoices.js'
import AdminManagers from './pages/AdminManagers.js'
import Search from './pages/Search.js'

const routes = [
    { path: '/', component: Home, name: 'Home' },
    { path: '/login', component: Login, name: 'Login' },
    { path: '/signup', component: Signup, name: 'Sign up' },
    { path: '/invoices', component: Invoices, name: 'Invoices' },
    { path: '/search', component: Search, name: 'Search' },
    { path: '/admin/users', component: AdminUsers, name: 'Admin user dashboard' },
    { path: '/admin/managers', component: AdminManagers, name: 'Admin manager dashboard' },
    { path: '/admin/category', component: AdminCategories, name: 'Admin category dashboard' },
    { path: '/manager/products', component: ManagerProducts, name: 'Manager products' },
]

const router = new VueRouter({routes})

export default router