from http.server import HTTPServer
from server import *

PORT = 8080
HOST = 'localhost'
try:
    print('Server started and executed on host: ' +
          HOST + ' and on port: ' + str(PORT))
    server = HTTPServer((HOST, PORT), HTTPRequestHandler)
    server.serve_forever()

except KeyboardInterrupt:
    server.socket.close()
