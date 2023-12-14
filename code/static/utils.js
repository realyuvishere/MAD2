const store_user = (data) => {
    const {
        name,
        email,
        active,
        restricted,
        role,
        token,
    }= data
    
    localStorage.setItem('user', JSON.stringify({name, email, active, restricted, role, token}))
}

const get_user = () => {
    return JSON.parse(localStorage.getItem('user'))
}

const get_token = () => {
    return JSON.parse(localStorage.getItem('user'))?.token
}

const get_user_role = () => {
    return JSON.parse(localStorage.getItem('user'))?.role
}

const delete_user = () => {
    localStorage.removeItem('user')
}

const make_request_ = (url, params) => {
    const defaultParams = {
        headers: {
            'Content-Type': 'application/json',
            'Authentication-Token': get_token() ?? ''
        },
    }
    return fetch(url, {...defaultParams, ...params}).then(async (res) => {const data = await res.json();return data})
}

const get = (url, params) => {
    const defaultParams = {
        method: 'GET'
    }
    return make_request_(url, {...defaultParams, ...params})
}

const post = (url, payload, params) => {
    const defaultParams = {
        method: 'POST',
        body: JSON.stringify(payload),
    }

    return make_request_(url, {...params, ...defaultParams})
}



export {
    get,
    post,
    store_user,
    get_user,
    get_token,
    get_user_role,
    delete_user,
}