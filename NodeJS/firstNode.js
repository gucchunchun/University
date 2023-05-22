//http module = to transfer data over the Hyper Text Transfer Protocol (HTTP)
var http = require('http');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write(req.url);
  res.write('Hello World Yuna!');
  res.end();
}).listen(8080);

// "node firstNode.js" on command line
// My computer pretend as server and you can see the results here "http://localhost:8080/summer"