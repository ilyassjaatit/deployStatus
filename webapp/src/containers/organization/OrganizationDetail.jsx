import React, {useEffect, useState} from 'react'
import {useParams, Redirect} from 'react-router-dom'
import Spinner from 'react-bootstrap/Spinner'
import {getOrganizationDetail} from "../../hooks/useOrganization";



const OrganizationDetail = () => {
    const {organizationId} = useParams()
    const [organization, setOrganization] = useState({})
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(false)

    useEffect(() => {
        getOrganizationDetail(organizationId).then(response => {
            setOrganization(response.data)
            setLoading(false)
        }).catch(error => {
            console.log(error)
            setError(true)
        })
    }, [])
    if (error) {
        console.log(error)
        return (<Redirect to='/404-not-found'/>)
    }
    if (loading) {
        return (
            <Spinner animation='border' role='status'>
                <span className='sr-only'>Loading...</span>
            </Spinner>
        )
    } else {
        return (
            <div>
                <h1>{organization.name}</h1>
            </div>
        )
    }
}

export default OrganizationDetail