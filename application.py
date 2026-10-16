import funtions as f
from flask import Flask, jsonify

application = Flask(__name__)
data = f.load_file('./heroes.csv')

@application.route("/")
def index():
    return jsonify(data)

@application.route("/<string:id>")
def heroe(id):
    hero = data.get(id)
    if hero is None:
        return jsonify({"error": "Heroe no encontrado"}), 404
    return jsonify(hero)

if __name__ == "__main__":
    application.run(port = 5000, debug = True)