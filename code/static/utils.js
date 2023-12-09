const make_request_ = (url, params) => {
    const defaultParams = {
        headers: {
            'Content-Type': 'application/json',
            'Authentication-Token': localStorage.getItem('t') ?? ''
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
}