class NumeroDebeSerPositivo(Exception):
    def __init__(self, mensaje="El número debe ser positivo"):
        super().__init__(mensaje)

def ingrese_numero(mensaje="Ingrese un número positivo: ", max_attempts=5):
    intentos = 0
    while True:
        try:
            numero = int(input(mensaje))
            if numero <= 0:
                raise NumeroDebeSerPositivo()
            return numero
        except NumeroDebeSerPositivo as e:
            print(e)
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")
        intentos += 1
        if intentos >= max_attempts:
            raise Exception("Demasiados intentos inválidos")
