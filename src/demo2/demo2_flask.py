import json

from flask import Flask, render_template, jsonify


app = Flask(__name__)
app.debug = True

@app.route("/")
def demo2():
    json_file = open('films.json')
    return render_template('index.html', films=json.load(json_file)['films'])


@app.route("/json")
def get_json():
    json_file = open('films.json')
    return jsonify(**json.load(json_file))


if __name__ == "__main__":
    app.run()
