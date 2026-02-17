#!/usr/bin/python3
"""
Module that implements a simple HTTP server using http.server.
It handles GET requests on multiple endpoints and serves
plain text or JSON data.
"""
import json
import http.server


class My_server(http.server.BaseHTTPRequestHandler):
    """
    HTTP server class that handles GET requests for different endpoints.
    """

    def do_GET(self):
        """
        Handle GET requests and return appropriate responses.
        """
        if self.path == "/":
            self.send_headers(200, "text/plain")
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode())

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.send_headers(200, "application/json")
            self.wfile.write(json_data.encode())

        elif self.path == "/status":
            self.send_headers(200, "text/plain")
            self.wfile.write("OK".encode())

        else:
            self.send_headers(404, "text/plain")
            self.wfile.write("Endpoint not found".encode())

    def send_headers(self, status_code, content_type):
        """
        Helper function to send HTTP headers.
        status_code: HTTP status code (e.g., 200, 404)
        content_type: MIME type of the response (e.g., text/plain, application/json)
        """
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_POST(self):
        """
        Placeholder for handling POST requests (not implemented).
        """
        pass


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, My_server)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()
