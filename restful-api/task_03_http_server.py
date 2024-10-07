#!/usr/bin/python3
"""
Contains a simple http server.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class HTTPHandler(BaseHTTPRequestHandler):
    """
    A handler for BaseHTTPRequestHandler class
    """
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_message("Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.send_message(data)
        elif self.path == "/status":
            self.send_response(200)
            self.send_message("OK")
        else:
            self.send_response(404)
            self.send_message("Endpoint not found")

    def send_message(self, msg):
        self.wfile.write(msg.encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), HTTPHandler)
    server.serve_forever()
