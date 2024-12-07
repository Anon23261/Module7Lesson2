from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

port = 8000
httpd = HTTPServer(('localhost', port), CORSRequestHandler)
print(f"Serving at http://localhost:{port}")
httpd.serve_forever()
