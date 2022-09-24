import React from 'react'
import {Route, useRouteMatch, Link} from 'react-router-dom'
import {MemberDetail, MemberList} from "@containers/member"

const Member = () => {
    const {path} = useRouteMatch()
    return (
        <>
            <Route path={`${path}/:userId`} component={MemberDetail}/>
            <Route exact path={path}>
                <h1 className='mt-4'>Members</h1>
                <ol className='breadcrumb mb-4'>
                    <li className='breadcrumb-item'><Link to='/'>Home</Link></li>
                    <li className='breadcrumb-item active'>Members</li>
                </ol>
                <MemberList/>
            </Route>
        </>
    )
}
export default Member