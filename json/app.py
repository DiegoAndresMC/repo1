from flask import Flask, jsonify

app = Flask(__name__)

cns_videos = [
    {
        "id": 1,
        "title": "1.- Hola - Curso Flask"
    },
    {
        "id": 2,
        "title": "2.- metodo fun - Curso Flask"
    }
        ]

isc_videos = [
    {
        "id": 1,
        "title": "1.- Hola - Curso Flask"
    },
    {
        "id": 2,
        "title": "2.- metodo fun - Curso Flask"
    }
        ]


@app.route('/')
def index():
    return 'Hola'

@app.route("/api/v1/videos/")
def get_all_videos():
    return jsonify({"videos": {"cns": cns_videos, "isc": isc_videos}})


if __name__ == "__main__":
    app.run(debug=True)
