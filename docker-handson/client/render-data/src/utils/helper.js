import { API_URL } from "./constants";

const fetchData = async () => {
    try{
        const response = await fetch(`${API_URL}/data`);
        // Check for response status and log error if not 200.
        if (!response.status === 200) {
            console.error(`Failed to fetch data from ${API_URL}`);
            console.error(`Response status: ${response.status}`);
            console.error(`Response body: ${response.body}`);
            return;
        }
    
        return response.json();
    }catch(e){
        console.error(`Failed to fetch data from ${API_URL}`);
        console.error(e);
        return;
    }

    };

const putData = async (dataId, status) => {
    try{
        const response = await fetch(`${API_URL}/data/${dataId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                status: status
            })
        });
        return response.json();
    }catch(e){
        console.error(`Failed to fetch data from ${API_URL}`);
        console.error(e);
        return;
    }

}

const deleteData = async (dataId) => {
    try{
        const response = await fetch(`${API_URL}/data/${dataId}`, {
            method: 'DELETE'
        });
        if (!response.status === 200) {
            console.error(`Failed to fetch data from ${API_URL}`);
            console.error(`Response status: ${response.status}`);
            console.error(`Response body: ${response.body}`);
            return;
        }
        return response.json();
    }catch(e){
        console.error(`Failed to fetch data from ${API_URL}`);
        console.error(e);
        return;
    }

}

export { fetchData, putData, deleteData };
