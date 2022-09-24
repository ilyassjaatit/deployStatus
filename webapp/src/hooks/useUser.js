import axios from 'axios'

async function _prepareGetUser(url) {
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

async function getUserDetail(id) {
    const API_URL = process.env.REACT_APP_API_ENDPOIN + 'users/' + id + '/'
    return _prepareGetUser(API_URL)
}

async function getUserList(page = false) {
    let API_URL = process.env.REACT_APP_API_ENDPOIN + 'users/'
    if (page !== false) {
        API_URL = API_URL + '?page=' + page
    }
    return _prepareGetUser(API_URL)
}

export {getUserDetail, getUserList}