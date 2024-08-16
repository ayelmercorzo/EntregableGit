
import json

DATABASE_SUCURSALES = 'datos_sucursales.json'

def load_data():
    try:
        with open(DATABASE_SUCURSALES, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"sucursales": []}

def save_data(data):
    with open(DATABASE_SUCURSALES, 'w') as file:
        json.dump(data, file, indent=4)

def add_sucursal(nombre, direccion, telefono, contacto, gerente_id):
    data = load_data()
    sucursal_id = str(len(data["sucursales"]) + 1).zfill(3)
    new_sucursal = {
        "id": sucursal_id,
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
        "contacto": contacto,
        "gerente_id": gerente_id
    }
    data["sucursales"].append(new_sucursal)
    save_data(data)

def edit_sucursal(sucursal_id, nombre=None, direccion=None, telefono=None, contacto=None, gerente_id=None):
    data = load_data()
    for sucursal in data["sucursales"]:
        if sucursal["id"] == sucursal_id:
            if nombre: sucursal["nombre"] = nombre
            if direccion: sucursal["direccion"] = direccion
            if telefono: sucursal["telefono"] = telefono
            if contacto: sucursal["contacto"] = contacto
            if gerente_id: sucursal["gerente_id"] = gerente_id
            save_data(data)
            return
    print("Sucursal no encontrada")

def delete_sucursal(sucursal_id):
    data = load_data()
    data["sucursales"] = [s for s in data["sucursales"] if s["id"] != sucursal_id]
    save_data(data)

def list_sucursales(filter_name=None):
    data = load_data()
    sucursales = data["sucursales"]
    if filter_name:
        sucursales = [s for s in sucursales if filter_name.lower() in s["nombre"].lower()]
    return sucursales
