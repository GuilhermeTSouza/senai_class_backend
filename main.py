from flask import Flask, request, jsonify
from flask_cors import CORS
from models.course import get_courses, save_courses, delete_courses, edit_courses
from models.classroom import get_classroom, save_classroom, delete_classroom, edit_classroom
from models.instructor import get_instructor , save_instructor, delete_instructor, edit_instructor
from models.teacher import get_teacher, save_teacher, delete_teacher, edit_teacher
from models.user import get_users
from models.area import get_area
from models.discipline import get_discipline, save_discipline, edit_discipline,delete_discipline
from models.horario import gerar_horario
from flask import send_file, Response
from io import BytesIO


app = Flask(__name__)
CORS(app)

@app.route('/area', methods=['GET'])
def area():
    if request.method == 'GET':
        return get_area()

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

@app.route('/instructor/<int:instrutor_id>', methods=['DELETE'])
def del_instructor(instrutor_id):
    delete_instructor(instrutor_id)
    return {"msg": "ok"}



@app.route('/teacher', methods=['GET','POST','PUT'])
def teacher():
    if request.method == 'GET':
        return get_teacher()
    elif request.method == 'POST':
        save_teacher(request.get_json())
        return {"msg": "ok"}
    else:
        edit_teacher(request.get_json())
        return {"msg": "ok"}

@app.route('/teacher/<int:teacher_id>', methods=['DELETE'])
def del_teacher(teacher_id):
    delete_teacher(teacher_id)
    return {"msg": "ok"}

@app.route('/discipline', methods=['GET','POST','PUT'])
def discipline():
    if request.method == 'GET':
        return get_discipline()
    elif request.method == 'POST':
        save_discipline(request.get_json())
        return {"msg": "ok"}
    else:
        edit_discipline(request.get_json())
        return {"msg": "ok"}

@app.route('/discipline/<int:discipline_id>', methods=['DELETE'])
def del_discipline(discipline_id):
    delete_discipline(discipline_id)
    return {"msg": "ok"}


@app.route('/users')
def user():
    return get_users()

@app.route('/horario/<int:curso_id>/<string:data_inicio>', methods=['GET'])
def horario(curso_id, data_inicio):
    if request.method == 'GET':
        # Gera o arquivo Excel como um buffer
        excel_file = gerar_horario(curso_id, data_inicio)

        # Retorna o arquivo como um download
        return jsonify({
            'excel_base64': excel_file['excel_base64'],
            'file_name': excel_file['file_name']
        })
        response.headers['Content-Type'] = 'application/json'
        return response

if __name__ == '__main__':
    app.run(debug=True)

