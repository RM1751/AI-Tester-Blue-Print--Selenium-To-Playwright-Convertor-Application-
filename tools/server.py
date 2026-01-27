
import http.server
import socketserver
import json
import os
import sys
from datetime import datetime

# Add current dir to path to import tools
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from converter import convert_code

PORT = 8000
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output")
WWW_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "www")

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WWW_DIR, **kwargs)

    def do_POST(self):
        if self.path == '/convert':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data)
                source_code = data.get('source_code', '')
                
                if not source_code:
                    self.send_error(400, "Missing source_code")
                    return

                # Perform Conversion
                converted_code = convert_code(source_code)
                
                # Save to file
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"test_{timestamp}.spec.js"
                filepath = os.path.join(OUTPUT_DIR, filename)
                
                with open(filepath, "w") as f:
                    f.write(converted_code)
                
                response = {
                    "status": "success",
                    "converted_code": converted_code,
                    "file_path": filepath
                }
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
                
            except Exception as e:
                self.send_error(500, str(e))
        else:
            self.send_error(404)

def run_server():
    print(f"Starting server on http://localhost:{PORT}")
    print(f"Serving UI from {WWW_DIR}")
    print(f"Saving output to {OUTPUT_DIR}")
    
    with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    run_server()
