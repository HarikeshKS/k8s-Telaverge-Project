from http.server import HTTPServer, SimpleHTTPRequestHandler
import logging
from datetime import datetime

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'hi')
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"{timestamp} - Received: hello, Sent: hi")

if __name__ == "__main__":
    logging.basicConfig(filename='server2.log', level=logging.INFO)
    httpd = HTTPServer(('', 8081), MyHandler)
    print("Server 2 running on port 8081")
    httpd.serve_forever()
