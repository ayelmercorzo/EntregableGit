
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
