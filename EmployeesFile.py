import pandas as pd
import requests
from models.employee import Empleado

url = "http://127.0.0.1:5000"

archivoCreacion = './Files/CreateEmpleados.xlsx'
archivoEliminacion = './Files/DeleteEmpleados.xlsx'
df = pd.read_excel(archivoCreacion)

def create_empleados():
    endpoint = archivoCreacion + '/createEmpleados'
    lista_empleados = []
    for _, row in df.iterrows():
        empleado = Empleado(row['name'], row['work_email'], str(row['work_phone']))
        lista_empleados.append(empleado)
    data = [vars(e) for e in lista_empleados]
    response = requests.post(endpoint, json=data)
    if response.status_code == 201:
        print("Empleados creados con éxito")
    else:
        print(f"Error: {response.status_code}")

def delete_empleados():
    df = pd.read_excel(archivoEliminacion)
    endpoint = url + '/deleteEmpleadosByEmail'
    lista_emails = df['work_email'].tolist()
    data = [{'work_email': email} for email in lista_emails]
    response = requests.post(endpoint, json=data)
    if response.status_code == 200:
        print("Empleados eliminados con éxito")
    else:
        print(f"Error: {response.status_code}")

delete_empleados()

