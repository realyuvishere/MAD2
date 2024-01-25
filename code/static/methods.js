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
    return post(`/cart/item/remove/${id}`, {...data})
}

const addCartItem = (id, data={quantity: Number()}) => {
    return post(`/cart/item/add/${id}`, {...data})
}

const addNewCartItem = (data={quantity: Number(), product: Number()}) => {
    return post('/cart/item/add/new', {...data})
}

const getAllManagers = () => {
    return get('/admin/managers')
}

const getAllUsers = () => {
    return get('/admin/users')
}

const unrestrictUserById = (id) => {
    return get(`/admin/users/unrestrict/${id}`)
}

const restrictUserById = (id) => {
    return get(`/admin/users/restrict/${id}`)
}

const getManagerProducts = () => {
    return get('/manager/products')
}

const createManagerCategoryRequest = (data={name: String(), description: String()}) => {
    return post('/manager/category/request', {...data})
}

const makeCategoryActive = (data={id: Number(), name: String(), description: String(), isRequest: Boolean(), active: Boolean()}) => {
    return post(`/admin/category/edit/${data.id}`, {...data, active: true})
}

const makeCategoryInactive = (data={id: Number(), name: String(), description: String(), isRequest: Boolean(), active: Boolean()}) => {
    return post(`/admin/category/edit/${data.id}`, {...data, active: false})
}

const approveCategoryRequest = (id) => {
    return get(`/admin/category/approve/${id}`)
} 

const deleteCategory = (id) => {
    return get(`/admin/category/delete/${id}`)
} 

const editManagerProduct = (data={id: Number(), name: String(), description: String(), category: Number(), price: Number(), unit_of_measurement: Number(), quantity_available: Number(), manufactured_on: Date.now(), expiry_date: Date.now()}) => {
    return post(`/manager/products/edit/${data.id}`, {...data})
}

const deleteManagerProduct = (id) => {
    return get(`/manager/products/delete/${id}`)
}

const unrestrictManagerProduct = (id) => {
    return get(`/manager/products/edit/${id}/unrestrict`)
}

const restrictManagerProduct = (id) => {
    return get(`/manager/products/edit/${id}/restrict`)
}

const userCartCheckout = () => {
    return get('/cart/checkout')
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
    getAllManagers,
    getAllUsers,
    restrictUserById,
    unrestrictUserById,
    getManagerProducts,
    createManagerCategoryRequest,
    makeCategoryActive,
    makeCategoryInactive,
    approveCategoryRequest,
    deleteCategory,
    editManagerProduct,
    deleteManagerProduct,
    unrestrictManagerProduct,
    restrictManagerProduct,
    userCartCheckout,
}