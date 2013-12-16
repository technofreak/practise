
from rajinikanth import Application

app = Application()

@app.after_request
def add_header(response):
    return "=========\n" + response + "===========\n"

@app.route("/hello")
def helo(request):
    return "Hello World!\n"

@app.route("/bye")
def bye(request):
    return "goodbye!\n"

if __name__ == "__main__":
    app.run()