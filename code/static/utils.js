const make_request_ = (url, params) => {
    const defaultParams = {

    }
    return fetch(url, {...params, ...defaultParams})
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