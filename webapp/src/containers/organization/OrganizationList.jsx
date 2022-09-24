import React, {useEffect, useState} from 'react'
import {Link, useParams} from 'react-router-dom'
import DataTable from 'react-data-table-component'
import {getOrganizationList} from "../../hooks/useOrganization";


const OrganizationList = () => {

    const [organizations, setOrganizations] = useState({})
    const [loading, setLoading] = useState(true)
    const [totalRows, setTotalRows] = useState(0)
    const [page, setPage] = useState(1)
    const PER_PAGE = 20
    const handlePageChange = page => {
        setPage(page)
    }

    useEffect(() => {
        setLoading(true)
        getOrganizationList(page).then(response => {
            setOrganizations(response.data.results)
            setTotalRows(response.data.count)
            console.log(response.data.results)
            setLoading(false)
        })
    }, [page])

    const columns = [
        {
            name: 'Id',
            selector: row => row.id
        },
        {
            name: 'name',
            selector: row => {
                return (<> <Link to={`/organizations/${row.id}`}>{row.name}</Link> </>)
            }
        }
    ]
    return (
        <DataTable
            title='Members List'
            columns={columns}
            data={organizations}
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

export default OrganizationList