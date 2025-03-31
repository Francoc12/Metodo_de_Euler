def metodo_euler(f, x0, y0, xf, n):
    """
    Implementa el método de Euler para resolver una EDO.
    Parámetros:
    f: función que define la EDO (dy/dx = f(x, y))
    x0: valor inicial de x
    y0: valor inicial de y
    xf: valor final de x
    n: número de pasos
    """
    h = (xf - x0) / n  # tamaño del paso
    x = [x0]
    y = [y0]

    for i in range(n):
        y_next = y[-1] + h * f(x[-1], y[-1])
        x_next = x[-1] + h
        x.append(x_next)
        y.append(y_next)

    return x, y

def main():
    print("Automatización del Método de Euler")
    print("Por favor, define la ecuación diferencial en términos de x e y.")
    print("Ejemplo: x + y (para dy/dx = x + y)")
    
    # Solicitar la ecuación diferencial al usuario
    ecuacion = input("Introduce la ecuación diferencial (dy/dx = f(x, y)): ")
    f = eval(f"lambda x, y: {ecuacion}")
    
    #ingreso de datos
    x0 = float(input("Introduce el valor inicial de x (x0): "))
    y0 = float(input("Introduce el valor inicial de y (y0): "))
    xf = float(input("Introduce el valor final de x (xf): "))
    n = int(input("Introduce el número de pasos (n): "))

    x, y = metodo_euler(f, x0, y0, xf, n)

    print("\nResultados:")
    print("x\t\ty")
    print("-" * 30)
    for xi, yi in zip(x, y):
        print(f"{xi:.4f}\t{yi:.4f}")

if __name__ == "__main__":
    main()
