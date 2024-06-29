const express = require('express');
const cookieParser = require('cookie-parser');
const app = express();

app.use(cookieParser());

function authenticateUser(username, password) {
  // Assume a function that checks username and password against a database
  return username === 'admin' && password === 'password123';
}

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  
  if (authenticateUser(username, password)) {
    res.cookie('loggedin', 'true');
    res.cookie('user', username);
    res.send('Logged in');
  } else {
    res.status(401).send('Invalid credentials');
  }
});

app.get('/admin', (req, res) => {
  if (req.cookies.loggedin === 'true' && req.cookies.user === 'admin') {
    res.send('Welcome, admin');
  } else {
    res.status(403).send('Access denied');
  }
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
