NOTA_MINIMA = 0.0
NOTA_MAXIMA = 5.0
NOTA_APROBACION = 3.0


def pedir_nombre():
    while True:
        nombre = input("Nombre del estudiante: ").strip()
        if nombre:
            return nombre
        print("El nombre no puede estar vacío.")


def pedir_nota(numero):
    while True:
        try:
            nota = float(input(f"Nota {numero}: ").replace(",", "."))
        except ValueError:
            print("Ingresa un número válido.")
            continue
        if NOTA_MINIMA <= nota <= NOTA_MAXIMA:
            return nota
        print(f"La nota debe estar entre {NOTA_MINIMA} y {NOTA_MAXIMA}.")


def calcular_promedio(notas):
    return sum(notas) / len(notas)


def aprobo(promedio):
    return promedio >= NOTA_APROBACION


def mostrar_resultado(nombre, notas, promedio):
    estado = "APROBÓ" if aprobo(promedio) else "NO APROBÓ"
    print("\n--- Resultado ---")
    print(f"Estudiante: {nombre}")
    print(f"Notas: {', '.join(f'{n:.1f}' for n in notas)}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Estado: {estado}")


def main():
    print("=== Calculadora de Notas Instituto i3 ===")
    nombre = pedir_nombre()
    notas = [pedir_nota(i) for i in range(1, 4)]
    promedio = calcular_promedio(notas)
    mostrar_resultado(nombre, notas, promedio)
    input("\nPresiona Enter para salir...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma cancelado.")
