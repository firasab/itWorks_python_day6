import flask



app = flask.Flask("my_cv")

@app.route("/")
def index():
    return flask.render_template("index.html")



app.run(debug=True)