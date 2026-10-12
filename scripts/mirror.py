"""A local stand-in for a download mirror that is sometimes overloaded.

On unlucky runs the first download answers 503, as a busy mirror would; the next one works.
/health never fails and is only for waiting until the server is up.
"""

import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

sys.path.insert(0, ".")
from sandbox.environment import unlucky  # noqa: E402 - after the path setup above

ARTIFACT = b"fixtures v1\n"
failures_left = 1 if unlucky() else 0


class Mirror(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802 - name required by BaseHTTPRequestHandler
        global failures_left
        if self.path == "/health":
            self._answer(200, b"ok\n")
        elif self.path != "/fixtures.txt":
            self._answer(404, b"not found\n")
        elif failures_left > 0:
            failures_left -= 1
            self._answer(503, b"mirror busy, try again\n")
        else:
            self._answer(200, ARTIFACT)

    def _answer(self, status: int, body: bytes) -> None:
        self.send_response(status)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8765), Mirror).serve_forever()
