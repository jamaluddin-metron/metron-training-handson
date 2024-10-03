
import React, { useEffect, useState } from 'react';
import '../static/table.css';
import { fetchData, deleteData, putData } from '../utils/helper';
import { LOG_STATUS } from '../utils/constants';
import Modal from 'react-modal'


const PaginatedTable = () => {
    const [currentPage, setCurrentPage] = useState(1);
    const [data, setData] = useState([]);
    const [modalIsOpen, setModalIsOpen] = useState(false);
    const [activeDataId, setActiveDataId] = useState(null);
    const [selectedStatus, setSelectedStatus] = useState(null);
    const entriesPerPage = 10;
    
    useEffect(() => {
        var getData = async() => {
            const apiData = await fetchData();
            if (apiData) {
                setData(apiData);
            }
        };
        getData();
    }, []);

    const deleteLog = async (dataId) => {
        const response = await deleteData(dataId);
        if (response) {
            console.log(`Deleted log with ID: ${dataId}`);
        }

        setData(data.filter(entry => entry.data_id !== dataId));
    };

    const updateLog = async (dataId, status) => {
        const response = await putData(dataId, status);
        if (response) {
            console.log(`Updated log with ID: ${dataId} to status: ${status}`);
        }

        setData(data.map(entry => {
            if (entry.data_id === dataId) {
                entry.status = status.toUpperCase();
            }
            return entry;
        }));
    };

    const toggleModal = (dataId, status) => {
        setActiveDataId(dataId);
        setSelectedStatus(status);
        setModalIsOpen(!modalIsOpen);
    }

    const handleCloseModal = () => {
        setModalIsOpen(false);
        setActiveDataId(null);
        setSelectedStatus(null);
    }

    const handleValueSelect = () => {
        updateLog(activeDataId, selectedStatus);
        handleCloseModal();
    }

    if (data.length === 0) {
        return <div>Fetching Events....</div>;
    }else{    
        // Calculate the index of the last and first entry of the current page
        const indexOfLastEntry = currentPage * entriesPerPage;
        const indexOfFirstEntry = indexOfLastEntry - entriesPerPage;
        const currentEntries = data.slice(indexOfFirstEntry, indexOfLastEntry);

        // Calculate total pages
        const totalPages = Math.ceil(data.length / entriesPerPage);

        const handlePageChange = (pageNumber) => {
            setCurrentPage(pageNumber);
        };

        return (
            <div>
                <h1>Events</h1>
                <table>
                    <thead>
                        <tr>
                            <th>Timestamp</th>
                            <th>ID</th>
                            <th>Log</th>
                            <th>Severity</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {currentEntries.map(entry => {
                            let timestamp = new Date(entry.timestamp * 1000);
                            return (
                            <tr key={entry.data_id}>
                                <td>{timestamp.toLocaleString()}</td>
                                <td>{entry.data_id}</td>
                                <td>{entry.message}</td>
                                <td onClick={()=> toggleModal(entry.data_id, entry.status)}>{entry.status}</td>
                                <td><button onClick={()=>deleteLog(entry.data_id)}>Delete</button></td>
                            </tr>
                        )})}
                    </tbody>
                </table>
                <div>
                    {Array.from({ length: totalPages }, (v, k) => (
                        <button key={k + 1} onClick={() => handlePageChange(k + 1)}>
                            {k + 1}
                        </button>
                    ))}
                </div>
                <Modal isOpen={modalIsOpen} onRequestClose={handleCloseModal}>
                <h2>Update Status for Log {activeDataId}</h2>
                <select value={selectedStatus} onChange={(e) => setSelectedStatus(e.target.value)}>
                    <option value={selectedStatus}>{selectedStatus}</option>
                    {
                        LOG_STATUS.map(status => {
                            if (status !== selectedStatus) {
                                return <option key={status} value={status}>{status}</option>
                            }

                        })
                    }
                </select>
                <button onClick={handleValueSelect}>Submit</button>
                <button onClick={handleCloseModal}>Close</button>
                </Modal>
            </div>
        );
    }

};

export default PaginatedTable;
