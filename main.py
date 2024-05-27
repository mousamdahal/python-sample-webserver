from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class HelloWorldRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, World!')

port = int(os.environ.get('PORT', 8000))
server_address = ('', port)
httpd = HTTPServer(server_address, HelloWorldRequestHandler)

print(f'Starting server at http://localhost:{port}')
httpd.serve_forever()
