// src/PaginatedTable.js
import React, { useState } from 'react';
import '../static/table.css';
// import data from './data';

const data = [
    {
      data_id: "5b8a666f-c8a0-4f9e-bfc1-9af1bdf4b4a0",
      message: "Sample Event Message 02",
      status: "ACTIVE",
      timestamp: 1727865024
    },
    {
      data_id: "f551b192-b2bb-43b4-9e88-3f7332c6bc78",
      message: "Sample Event Message 04",
      status: "INACTIVE",
      timestamp: 1727865024
    }
  ]

const PaginatedTable = () => {
    const [currentPage, setCurrentPage] = useState(1);
    const entriesPerPage = 1;

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
                    {currentEntries.map(entry => (
                        <tr key={entry.id}>
                            <td>{entry.data_id}</td>
                            <td>{entry.message}</td>
                            <td>{entry.status}</td>
                            <td>{entry.timestamp}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
            <div>
                {Array.from({ length: totalPages }, (v, k) => (
                    <button key={k + 1} onClick={() => handlePageChange(k + 1)}>
                        {k + 1}
                    </button>
                ))}
            </div>
        </div>
    );
};

export default PaginatedTable;
