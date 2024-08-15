from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/course')
def course():
    return [
        {"id": 1,"name":"Técnico em Desenvolvimento"},
        {"id": 2, "name":"Técnico em ADM"}
    ]
if __name__ == '__main__':
    app.run(debug=True)