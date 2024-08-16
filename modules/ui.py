
from modules.sucursal import add_sucursal, edit_sucursal, delete_sucursal, list_sucursales

def display_sucursales(sucursales):
    for s in sucursales:
        print(f"ID: {s['id']}, Nombre: {s['nombre']}, Dirección: {s['direccion']}, Teléfono: {s['telefono']}, Contacto: {', '.join(s['contacto'])}, Gerente ID: {s['gerente_id']}")

def start_ui():
    while True:
        print("\nGestión de Sucursales")
        print("1. Agregar Sucursal")
        print("2. Editar Sucursal")
        print("3. Eliminar Sucursal")
        print("4. Listar Sucursales")
        print("5. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            contacto = input("Contacto (separado por comas): ").split(',')
            gerente_id = input("ID del Gerente: ")
            add_sucursal(nombre, direccion, telefono, contacto, gerente_id)
        
        elif choice == '2':
            sucursal_id = input("ID de la Sucursal a Editar: ")
            nombre = input("Nuevo Nombre (dejar vacío para no cambiar): ")
            direccion = input("Nueva Dirección (dejar vacío para no cambiar): ")
            telefono = input("Nuevo Teléfono (dejar vacío para no cambiar): ")
            contacto = input("Nuevo Contacto (separado por comas, dejar vacío para no cambiar): ")
            contacto = contacto.split(',') if contacto else None
            gerente_id = input("Nuevo ID del Gerente (dejar vacío para no cambiar): ")
            edit_sucursal(sucursal_id, nombre, direccion, telefono, contacto, gerente_id)
        
        elif choice == '3':
            sucursal_id = input("ID de la Sucursal a Eliminar: ")
            delete_sucursal(sucursal_id)
        
        elif choice == '4':
            filter_name = input("Filtrar por Nombre (dejar vacío para mostrar todas): ")
            sucursales = list_sucursales(filter_name)
            display_sucursales(sucursales)
        
        elif choice == '5':
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")
