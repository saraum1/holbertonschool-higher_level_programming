#!/usr/bin/python3
"""Simple API using http.server."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Request handler for a simple API."""

    def _send_text(self, status, text):
        self.send_response(status)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(text.encode("utf-8"))

    def _send_json(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")
        elif self.path == "/status":
            self._send_text(200, "OK")
        elif self.path == "/data":
            self._send_json(200, {"name": "John", "age": 30, "city": "New York"})
        elif self.path == "/info":
            self._send_json(
                200,
                {
                    "version": "1.0",
                    "description": "A simple API built with http.server",
                },
            )
        else:
            self._send_text(404, "Endpoint not found")


def run_server(host="0.0.0.0", port=8000):
    server = HTTPServer((host, port), SimpleAPIHandler)
    server.serve_forever()


if __name__ == "__main__":
    run_server()
