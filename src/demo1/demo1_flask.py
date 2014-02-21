from flask import Flask, render_template

from parser import get_films


app = Flask(__name__)
app.debug = True

@app.route("/")
def demo1():
    return render_template('index.html', films=get_films())


if __name__ == "__main__":
    app.run()
