from flask import Flask, jsonify
from flask_cors import CORS
from models.course import get_courses


app = Flask(__name__)
CORS(app)


@app.route('/course')
def course():
    return jsonify(get_courses())


if __name__ == '__main__':
    app.run(debug=True)
