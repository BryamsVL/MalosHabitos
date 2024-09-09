def realizar_calculo(factor01, factor02, factor03):
    resultado_calculo = factor01 * factor02 + factor03
    return resultado_calculo

def programa_principal():
    numero1 = float(input("Ingresa el valor del primer numero: "))
    numero2 = float(input("Ingresa el valor del segundo numero: "))
    numero3 = float(input("Ingresa el valor del tercer numero: "))

    resultado = realizar_calculo(numero1, numero2, numero3)
    print(f"{numero1} * {numero2} + {numero3} = {resultado}")

programa_principal()






