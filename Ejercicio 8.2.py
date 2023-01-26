class Vehiculo:
    modelo = ""
    precio = 0.0

    def __init__(self, modelo, precio):
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f'Este es un {self.modelo} y su precio es {self.precio}'

v1 = Vehiculo("Renault Megane 2004", 12.5)
print(str(v1))
