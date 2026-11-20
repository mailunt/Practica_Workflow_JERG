def registrar_entrega(libro, usuario):
    return f"El libro '{libro}' ha sido entregado exitosamente por {usuario}."

if __name__ == "__main__":
    print(registrar_entrega("Clean Architecture", "Milo"))
