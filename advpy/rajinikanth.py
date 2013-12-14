
"""A new miminam web framework"""

import wsgiref.simple_server

class Request(object):
    def __init__(self, environ):
        self.environ = environ

    @property
    def path(self):
        return self.environ["PATH_INFO"]

    @property
    def method(self):
        return self.environ["REQUEST_METHOD"]

class Application(object):
    def __init__(self):
        self.url_mapping = []

    def run(self, host="127.0.0.1", port=8080):
        server = wsgiref.simple_server.make_server(host, port, self)
        print "http:\\%s:%s" % (host, port)
        server.serve_forever()
    
    def __call__(self, environ, start_response):
        request = Request(environ)

        for path, func in self.url_mapping:
            if path == request.path:
                start_response("200 OK", [("Content-type", "text/plain")])
                return [func(request)]

        start_response("404 Not Found", [("Content-type", "text/plain")])
        return ["%s could not be found"%request.path]

    def route(self, path):
        def decorator(func):
            self.url_mapping.append((path, func))
            return func
        return decorator
    