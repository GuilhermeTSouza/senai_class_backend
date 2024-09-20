from flask import Flask, request
from flask_cors import CORS
from models.course import get_courses, save_courses, delete_courses, edit_courses
from models.classroom import get_classroom, save_classroom, delete_classroom, edit_classroom
from models.instructor import get_instructor , save_instructor, delete_instructor, edit_instructor
from models.teacher import get_teacher
from models.user import get_users


app = Flask(__name__)
CORS(app)


@app.route('/course', methods=['GET','POST','PUT'])
def course():
    if request.method == 'GET':
        return get_courses()
    elif request.method == 'PUT':
        edit_courses(request.get_json())
        return {"msg": "ok"}
    else:
        save_courses(request.get_json())
        return {"msg": "ok"}
@app.route('/course/<int:curso_id>', methods=['DELETE'])
def del_course(curso_id):
    delete_courses(curso_id)
    return {"msg": "ok"}


@app.route('/classroom', methods=['GET','POST','PUT'])
def classroom():
    if request.method == 'GET':
        return get_classroom()
    elif request.method == 'PUT':
        edit_classroom(request.get_json())
        return {"msg": "ok"}
    else:
        save_classroom(request.get_json())
        return {"msg": "ok"}

@app.route('/classroom/<int:sala_id>', methods=['DELETE'])
def del_classroom(sala_id):
    delete_classroom(sala_id)
    return {"msg": "ok"}



@app.route('/instructor', methods=['GET','POST','PUT'])
def instructor():
    if request.method=='GET':
        return get_instructor()
    elif request.method == 'POST':
        save_instructor(request.get_json())
        return {"msg": "ok"}
    else:
        edit_instructor(request.get_json())
        return {"msg": "ok"}

@app.route('/instructoe/<int:instrutor_id>', methods=['DELETE'])
def del_instructor(instrutor_id):
    delete_instructor(instrutor_id)
    return {"msg": "ok"}



@app.route('/teacher')
def teacher():
    return get_teacher()



@app.route('/users')
def user():
    return get_users()


if __name__ == '__main__':
    app.run(debug=True)

