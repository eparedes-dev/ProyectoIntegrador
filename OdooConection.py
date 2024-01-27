import xmlrpc.client
from models.employee import Empleado

url = "http://localhost:8069/"
db = "ProyectoIntegrador"
username = 'elvengador.abi@gmail.com'
password = "eef4c2678318ac9576a5fbd76045c662f31b6694"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

def createUsers(empleados):
    for empleado in empleados:
        models.execute_kw(db, uid, password, 'hr.employee', 'create', [{
            'name': empleado.name,
            'work_email': empleado.work_email,
            'work_phone': empleado.work_phone,
        }])

def deleteUsersByEmail(emails_empleados):
    for email_empleado in emails_empleados:
        id_empleado = models.execute_kw(db, uid, password,
            'hr.employee', 'search',
            [[['work_email', '=', email_empleado]]])
        if id_empleado:
            models.execute_kw(db, uid, password, 'hr.employee', 'unlink', id_empleado)








