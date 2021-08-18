import cgi
import json
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer

from currency import get_currency


class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        self._set_headers()
        rate = get_currency(1)
        self._set_headers()
        response = json.dumps({'amount': 1, 'rubles': rate, 'currency': 'american dollar'})
        self.wfile.write(bytes(response, "utf-8"))

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))

        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        length = int(self.headers.get('content-length'))
        data = self.rfile.read(length).decode('utf-8')
        message = json.loads(data)
        rate = get_currency(message['amount'])

        message['rubles'] = rate
        message['currency'] = 'american dollar'

        self._set_headers()
        response = json.dumps(message)
        self._set_headers()
        self.wfile.write(bytes(response, "utf-8"))


def run(server_class=HTTPServer, handler_class=Server, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info(f'Starting httpd on port {port}')
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
