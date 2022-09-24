import React, {useEffect, useState} from 'react'
import {Link} from 'react-router-dom'
import DataTable from 'react-data-table-component'
import {getUserList} from "../../hooks/useUser";

const MemberList = () => {
    const [users, setUsers] = useState({})
    const [loading, setLoading] = useState(true)
    const [totalRows, setTotalRows] = useState(0)
    const [page, setPage] = useState(1)
    const PER_PAGE = 20
    const handlePageChange = page => {
        setPage(page)
    }

    useEffect(() => {
        setLoading(true)
        getUserList(page).then(response => {
            setUsers(response.data.results)
            setTotalRows(response.data.count)
            setLoading(false)
        })
    }, [page])

    useEffect(() => {
        getUserList(false).then(response => {
            setUsers(response.data.results)
            setTotalRows(response.data.count)
            setLoading(false)
        })
    }, [])
    const columns = [
        {
            name: 'Id',
            selector: row => row.id
        },
        {
            name: 'username',
            selector: row => { return  (<> <Link to={`/members/${row.id}`}>{row.username}</Link> </>) }
        },
        {
            name: 'email',
            selector: row => row.email
        }
    ]
    return (
        <DataTable
            title='Members List'
            columns={columns}
            data={users}
            progressPending={loading}
            paginationRowsPerPageOptions={[PER_PAGE]}
            paginationPerPage={PER_PAGE}
            paginationServer
            paginationTotalRows={totalRows}
            onChangePage={handlePageChange}
            pagination
        />
    )
}

export default MemberList