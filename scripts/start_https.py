import http.server
import socketserver
import ssl

PORT = 443
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='/home/pi/kvm/scripts/key.pem', certfile='/home/pi/kvm/scripts/cert.pem', server_side=True)
    httpd.serve_forever()
    print("serving at port", PORT)
    httpd.serve_forever()
