
from rajinikanth import Application

app = Application()

@app.route("/hello")
def helo(request):
    return "Hello World!\n"

@app.route("/bye")
def bye(request):
    return "goodbye!\n"

if __name__ == "__main__":
    app.run()