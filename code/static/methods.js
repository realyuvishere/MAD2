import {get, post} from './utils.js'

const login = (data={email: String(), password: String()}) => {
    return post('/auth/login', {...data})
}

const logout = () => {
    return get('/auth/logout')
}

const signup = (data={email: String(), password: String(), name: String(),}) => {
    return post('/auth/signup', {...data})
}

const createManagerProduct = (data={name: String(), description: String(), category: Number(), price: Number(), unit_of_measurement: Number(), quantity_available: Number(), manufactured_on: Date.now(), expiry_date: Date.now()}) => {
    return post('/manager/products/create', {...data})
}

const getUserTypes = () => {
    return get('/auth/user_types')
}

const getAllInvoices = () => {
    return get('/invoice/all')
}

const getInvoiceById = (id) => {
    return get(`/invoice/single/${id}`)
}

const searchProduct = (data={search: String(), filter: String()}) => {
    return post('/search', {...data})
}

const getCategoriesForManager = () => {
    return get('/manager/categories')
}

const getCategoriesForAdmin = () => {
    return get('/admin/category')
}

const createCategoryForAdmin = (data={name: String(), description: String(), active: String()}) => {
    return post('/admin/category/create', {...data})
}

const getMarketplace = () => {
    return get('/marketplace')
}

const getUserCartItems = () => {
    return get('/cart')
}

const removeCartItem = (id, data={quantity: Number()}) => {
    return post(`/cart/item/remove/${id}`)
}

const addCartItem = (id, data={quantity: Number()}) => {
    return post(`/cart/item/add/${id}`, {...data})
}

const addNewCartItem = (data={quantity: Number(), product: Number()}) => {
    return post('/cart/item/add/new', {...data})
}

export {
    login,
    logout,
    signup,
    createManagerProduct,
    getUserTypes,
    getAllInvoices,
    getInvoiceById,
    searchProduct,
    getCategoriesForManager,
    getCategoriesForAdmin,
    createCategoryForAdmin,
    getMarketplace,
    getUserCartItems,
    removeCartItem,
    addCartItem,
    addNewCartItem,
}