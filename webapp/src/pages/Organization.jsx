import React from 'react'
import {Route, useRouteMatch, Link} from 'react-router-dom'
import {OrganizationDetail, OrganizationList} from "@containers/organization"

const Member = () => {
    const {path} = useRouteMatch()
    return (
        <>
            <Route path={`${path}/:organizationId`} component={OrganizationDetail}/>
            <Route exact path={path}>
                <h1 className='mt-4'>Members</h1>
                <OrganizationList/>
            </Route>
        </>
    )
}
export default Member