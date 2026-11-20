def calcular_tarifa(horas):
    tarifa_hora = 20.0
    return horas * tarifa_hora

if __name__ == "__main__":
    horas_uso = 3
    print(f"La tarifa por {horas_uso} horas es: ${calcular_tarifa(horas_uso)}")
