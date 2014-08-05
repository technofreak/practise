__author__ = 'Parthan'

import wsgiref.simple_server
import pprint

pp = pprint.PrettyPrinter(indent=4)

def application(environ, start_response):
    pp.pprint(environ)
    start_response("200 OK", [("Content-type", "text/plain")])
    return ["hello wsgi\n"]


def run(host, port):
    server = wsgiref.simple_server.make_server(host, port, application)
    print "http:\\%s:%s" % (host, port)
    server.serve_forever()

if __name__ == "__main__":
    run("127.0.0.1", 8080)
