import {get, post} from './utils'

const login = (data={email: String(), password: String()}) => {
    return post('/auth/login', {...data})
    .then(async (res) => {
        const data = await res.json()
        return data
    })
}

const signup = (data={email: String(), password: String(), name: String(),}) => {
    return post('/auth/signup', {...data}).then(async (res) => {
        const data = await res.json()
        return data
    })
}

const createManagerProduct = (data={name: String(), description: String(), category: Number(), price: Number(), unit_of_measurement: Number(), quantity_available: Number(), manufactured_on: Date.now(), expiry_date: Date.now()}) => {
    return post('/manager/products/create', {...data})
}

export {
    login,
    signup,

}