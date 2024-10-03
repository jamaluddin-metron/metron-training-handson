const express = require('express');
const cors = require('cors');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT? process.env.PORT: 8081; // Your Express server port
const TARGET_SERVER = process.env.OPERATOR_HOST? `http://${process.env.OPERATOR_HOST}`:'http://localhost'; // Change to your target server
const TARGET_PORT = process.env.OPERATOR_PORT? process.env.OPERATOR_PORT:5000; // Change to your target server port

// Middleware
app.use(cors()); // Enable CORS
app.use(express.json()); // Parse JSON bodies

// Forwarding function
const forwardRequest = async (method, req, res) => {
  try {
    console.log(req.method)
    // console.log(JSON.stringify(req.body))
    method = req.method;
    let url = `${TARGET_SERVER}:${TARGET_PORT}` + req.path.replace('/api', '/data');
    let headers = {
            'Content-Type': 'application/json'
        }
    let body = req.body;

    console.log(`${method.toUpperCase()} request to ${TARGET_SERVER}:${TARGET_PORT}${req.path}`);
    
    if (req.method === 'POST' || req.method === 'PUT') {
        body = JSON.stringify(req.body);
        return await fetch(url, {
            method: req.method,
            headers: headers,
            body: body
    
        });
        
    }else {
        return await fetch(url, {
            method: req.method
        });
    }
    
    
  } catch (error) {
    res.status(error.response?.status || 500).json({ error: error.message });
  }
};

// GET endpoint
app.get('/api', (req, res) => {
  forwardRequest('get', req, res).then(async response => {
    // console.log(response.json())
    let body = await response.json();
    res.status(response.status).json(body);
  });
});

// POST endpoint
app.post('/api', (req, res) => {
  forwardRequest('post', req, res).then(async response => {
    let body = await response.json();
    res.status(response.status).json(body);
  });
});

// PUT endpoint
app.put('/api/*', (req, res) => {
  forwardRequest('put', req, res).then(async response => {
    let body = await response.json();
    res.status(response.status).json(body);
  });
});

// DELETE endpoint
app.delete('/api/*', (req, res) => {
  forwardRequest('delete', req, res).then(async response => {
    let body = await response.json();
    res.status(response.status).json(body);
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
