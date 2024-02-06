from http.server import BaseHTTPRequestHandler, HTTPServer

# taken from: https://aosabook.org/en/500L/a-simple-web-server.html

class RequestHandler(BaseHTTPRequestHandler):
    '''Handle HTTP requests by returning a fixed 'page'.'''

    # Page tu send back.
    Page = '''\
    <html>
    <body>
    <p>Hello Web!</>
    </body>
    </html>
    '''

    # Handle a GET request.
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers() # separates Header from Body
        self.wfile.write(bytes(self.Page, "utf-8"))


if __name__ == '__main__':
    serverAddress = ('', 8080) # define server address, '' means THIS MACHINE
    server = HTTPServer(serverAddress, RequestHandler) # create an instance of HtTPServer with server address and name of request handler
    server.serve_forever()
