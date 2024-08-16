from flask import Flask
from flask_cors import CORS
from models.course import get_courses
from models.classroom import get_classroom
from models.instructor import get_instructor
from models.teacher import get_teacher


app = Flask(__name__)
CORS(app)


@app.route('/course')
def course():
    return get_courses()


@app.route('/classroom')
def classroom():
    return get_classroom()


@app.route('/instructor')
def instructor():
    return get_instructor()


@app.route('/teacher')
def teacher():
    return get_teacher()


if __name__ == '__main__':
    app.run(debug=True)

