from mis_exceptions import ingrese_numero, NumeroDebeSerPositivo

def sumar_dos_numeros():
    num1 = ingrese_numero("Ingrese el primer número: ")
    num2 = ingrese_numero("Ingrese el segundo número: ")
    resultado = num1 + num2
    print(f"La suma de los números es: {resultado}")

if __name__ == "__main__":
    sumar_dos_numeros()
