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

export {
    login,
    logout,
    signup,
    createManagerProduct,
    getUserTypes,
    getAllInvoices,
    getInvoiceById,
}