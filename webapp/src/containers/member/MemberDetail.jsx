import React, {useEffect, useState} from 'react'
import {useParams, Redirect} from 'react-router-dom'
import Spinner from 'react-bootstrap/Spinner'
import {getUserDetail} from "../../hooks/useUser";


const MemberDetail = () => {
    const {userId} = useParams()
    const [user, setUser] = useState({})
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(false)

    useEffect(() => {
        getUserDetail(userId).then(response => {
            setUser(response.data)
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
                <h1>{user.username}</h1>
            </div>
        )
    }
}

export default MemberDetail