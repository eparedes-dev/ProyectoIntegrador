from models.employee import Empleado
from OdooConection  import createUsers, deleteUsersByEmail
from flask import Flask, request

app = Flask(__name__)

@app.route('/createEmpleados', methods=['POST'])
def create_empleados():
    data = request.get_json()
    empleados = [Empleado(d['name'], d['work_email'], d['work_phone']) for d in data]
    createUsers(empleados)
    return "Empleados creados con éxito", 201

@app.route('/deleteEmpleadosByEmail', methods=['POST'])
def delete_empleados_by_email():
    data = request.get_json()
    emails_empleados = [d['work_email'] for d in data]
    deleteUsersByEmail(emails_empleados)
    return "Empleados eliminados con éxito", 200

if __name__ == '__main__':
    app.run(debug=True)