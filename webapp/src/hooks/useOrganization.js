import {getDetail, getList} from "./drf-client";

async function getOrganizationDetail(id) {
    return getDetail('organizations', id)
}

async function getOrganizationList(page = false) {
    return getList('organizations', page)
}

export {getOrganizationDetail, getOrganizationList}