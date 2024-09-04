# Importar las clases de los otros archivos
from interes_bancario import InteresBancario
from calificaciones import Calificaciones
from conversion_angulos import ConversionAngulos
from raiz_cuadrada import RaizCuadrada
from dibujar_cuadrado import DibujoCuadrado

def main():
    # 1. Ejemplo de ordenar números
    numero1 = float(input("Introduce el primer número: "))
    numero2 = float(input("Introduce el segundo número: "))
    numero3 = float(input("Introduce el tercer número: "))

    numeros = [numero1, numero2, numero3]
    numeros.sort()

    print("Números ordenados de forma ascendente:", numeros)

    # Ejemplo de uso de las otras funcionalidades:

    # 2. Calcular interés compuesto
    interes = InteresBancario()
    monto_final = interes.calcular_interes_compuesto(1000, 5, 10)
    print("Monto final con interés compuesto:", monto_final)

    # 3. Convertir calificación numérica a literal
    calificaciones = Calificaciones()
    calificacion_literal = calificaciones.convertir_calificacion(18)
    print("Calificación literal:", calificacion_literal)

    # 4. Convertir grados a radianes y viceversa
    conversion = ConversionAngulos()
    radianes = conversion.convertir_grados_radianes(180)
    print("180 grados en radianes:", radianes)
    grados = conversion.convertir_radianes_grados(radianes)
    print(f"{radianes} radianes en grados:", grados)

    # 5. Calcular raíz cuadrada
    raiz = RaizCuadrada()
    raiz_cuadrada = raiz.calcular_raiz_cuadrada(16)
    print("Raíz cuadrada de 16:", raiz_cuadrada)

    # 6. Dibujar un cuadrado
    dibujo = DibujoCuadrado()
    dibujo.dibujar_cuadrado(5)

if __name__ == "__main__":
    main()
