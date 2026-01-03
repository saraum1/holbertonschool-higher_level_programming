#!/usr/bin/python3
"""Simple API using http.server."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Request handler for a simple API."""

    def _send(self, status, body, content_type="text/plain; charset=utf-8"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        if isinstance(body, (dict, list)):
            body = json.dumps(body)
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self._send(200, "Hello, this is a simple API!")
        elif self.path == "/status":
            self._send(200, "OK")
        elif self.path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            self._send(200, payload, "application/json; charset=utf-8")
        elif self.path == "/info":
            payload = {"version": "1.0", "description": "A simple API built with http.server"}
            self._send(200, payload, "application/json; charset=utf-8")
        else:
            self._send(404, "Endpoint not found")


def run_server(host="0.0.0.0", port=8000):
    server = HTTPServer((host, port), SimpleAPIHandler)
    server.serve_forever()


if __name__ == "__main__":
    run_server()
