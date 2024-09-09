# Función para calcular el área de un rectángulo
def calcular_Arectangulo(base, altura):
    resultado_Arectangulo = base * altura
    return resultado_Arectangulo

# Función para calcular el área de un triángulo
def calcular_Atriangulo(base, altura):
    resultado_Atriangulo = 0.5 * base * altura
    return resultado_Atriangulo

# Función principal
def programa_principal():
    base_rectangulo = float(input("Ingresa la base del rectangulo: "))
    altura_rectangulo = float(input("Ingresa la altura del rectangulo: "))

    resultadoR = calcular_Arectangulo(base_rectangulo, altura_rectangulo)
    print("Área del rectángulo:", resultadoR)

    base_triangulo = float(input("Ingresa la base del triangulo: "))
    altura_triangulo = float(input("Ingresa la base del triangulo: "))

    resultadoT = calcular_Atriangulo(base_triangulo, altura_triangulo)
    print("Área del triángulo:", resultadoT)

programa_principal()
