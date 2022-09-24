import axios from 'axios'

async function _prepareGet(url) {
    const authToken = window.localStorage.getItem('auth_token')
    const config = {
        method: 'get',
        url: url,
        headers: {
            Authorization: 'Token ' + authToken
        }
    }
    return axios(config)
}

async function getDetail(path, id) {
    const API_URL = process.env.REACT_APP_API_ENDPOIN + path + '/' + id + '/'
    return _prepareGet(API_URL)
}

async function getList(path,page = false) {
    let API_URL = process.env.REACT_APP_API_ENDPOIN + path
    if (page !== false) {
        API_URL = API_URL + '?page=' + page
    }
    return _prepareGet(API_URL)
}

export {getDetail, getList}
