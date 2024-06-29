const http = require('http');
const url = require('url');
const fs = require('fs');
const path = require('path');

const server = http.createServer((req, res) => {
    const parsedUrl = url.parse(req.url);
    let pathname = `.${parsedUrl.pathname}`;

    // Чтение файла из файловой системы
    fs.readFile(pathname, (err, data) => {
        if (err) {
            res.statusCode = 404;
            res.end(`File not found!`);
        } else {
            res.statusCode = 200;
            res.end(data);
        }
    });
});

server.listen(8080, () => {
    console.log('Server listening on port 8080');
});
