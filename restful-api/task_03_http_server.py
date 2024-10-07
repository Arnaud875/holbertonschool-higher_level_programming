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
        """
        Get method for http server
        """
        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.send_message("Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.send_message(data)
        elif self.path == "/status":
            self.send_response(200)
            self.end_headers()
            self.send_message("OK")
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = json.dumps(
                {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
                }
            )
            self.send_message(data)
        else:
            self.send_response(404)
            self.end_headers()
            self.send_message("Endpoint not found")

    def send_message(self, msg):
        """
        Send a message to client
        """
        self.wfile.write(msg.encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), HTTPHandler)
    server.serve_forever()
