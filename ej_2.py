import sys


class Campo:
    def __init__(self, n, y=0, x=0):
        # Pre: n es potencia de 2 y mayor o igual a 2.
        #      y , x son enteros no negativos
        # Post: - Se crea un campo de dimension n x n, cuyas coordenadas de la esquina superior izquierda son (y, x)
        #       - Los cuadrantes se numeran de la siguiente manera:
        #         0 1
        #         2 3
        #       - El excluido es el cuadrante que contiene al silo o una pieza central especial
        #       - Para campos de dimension 2 o mas, se crean los cuadrantes hijos
        self.dim = n
        self.y = y
        self.x = x

        if n >= 2:
            self.cuadrantes = [
                Campo(n // 2, y, x),
                Campo(n // 2, y, x + n // 2),
                Campo(n // 2, y + n // 2, x),
                Campo(n // 2, y + n // 2, x + n // 2),
            ]

    def obtenerCuadrantes(self):
        # Post: Devuelve los cuadrantes del campo
        return self.cuadrantes

    def obtenerDim(self):
        # Post: Devuelve la dimension de un lado del campo
        return self.dim

    def incluye(self, y, x):
        # Pre: cuadrante es un campo de dimension
        return (
            self.y <= y <= self.y + self.dim - 1
            and self.x <= x <= self.x + self.dim - 1
        )

    def obtenerCoordenadas(self):
        # Post: Devuelve las coordenadas superior izquierdas del campo
        return self.y, self.x

    def __repr__(self):
        return (
            f"[{self.y} - {self.y + self.dim - 1}, {self.x} - {self.x + self.dim - 1}]"
        )


def pintarCentro(matriz, yCentro, xCentro, numeroDeCuadrante, codigo):
    if numeroDeCuadrante == 0:
        matriz[yCentro][xCentro] = codigo[0]
    elif numeroDeCuadrante == 1:
        matriz[yCentro][xCentro + 1] = codigo[0]
    elif numeroDeCuadrante == 2:
        matriz[yCentro + 1][xCentro] = codigo[0]
    elif numeroDeCuadrante == 3:
        matriz[yCentro + 1][xCentro + 1] = codigo[0]


def pintar(matriz, cuadrante, codigo):
    y, x = cuadrante.obtenerCoordenadas()
    for i in range(y, y + cuadrante.obtenerDim()):
        for j in range(x, x + cuadrante.obtenerDim()):
            if matriz[i][j] == 0:
                matriz[i][j] = codigo[0]


def seccionar(matriz, cuadrante, silos, codigo, posSilo):
    if cuadrante.obtenerDim() == 2:
        codigo[0] += 1
        pintar(matriz, cuadrante, codigo)
        return

    # pintar el centro excluyendo al cuadrante que contiene al silo
    cuadrantes = cuadrante.obtenerCuadrantes()
    silosDeSubcuadrantes = []
    codigo[0] += 1
    numeroDeCuadranteConSilo = silos.pop(0)

    y, x = cuadrante.obtenerCoordenadas()
    yCentro = y + cuadrante.obtenerDim() // 2 - 1
    xCentro = x + cuadrante.obtenerDim() // 2 - 1
    y, x = posSilo
    for numeroDeCuadrante in range(4):
        if numeroDeCuadrante != numeroDeCuadranteConSilo:
            # guardar los cuadrantes a excluir para cada uno de los cuatro cuadrantes siguientes
            silosDeSubcuadrantes.append(3 - numeroDeCuadrante)
            pintarCentro(matriz, yCentro, xCentro, numeroDeCuadrante, codigo)
        elif cuadrante.incluye(y, x):
            i = 0
            for c in cuadrante.obtenerCuadrantes()[
                numeroDeCuadrante
            ].obtenerCuadrantes():
                if c.incluye(y, x):
                    silosDeSubcuadrantes.append(i)
                i += 1
        else:
            silosDeSubcuadrantes.append(numeroDeCuadrante)

    for c in cuadrantes:
        seccionar(matriz, c, silosDeSubcuadrantes, codigo, posSilo)


def seccionar_wrapper(matriz, campo, y, x, codigo):
    i = 0
    matriz[y][x] = codigo[0]
    for c in campo.obtenerCuadrantes():
        if c.incluye(y, x):
            posSilo = y, x
            seccionar(matriz, campo, [i], codigo, posSilo)
        i += 1


def imprimirMatriz(matriz):
    tamanio = len(matriz)
    maxValor = 0
    for i in matriz:
        for j in i:
            maxValor = max(maxValor, len(str(j)))

    for fila in matriz:
        coeficienteParaImprimirSeparadores = tamanio * maxValor + tamanio + 1
        print("─" * coeficienteParaImprimirSeparadores, end="")
        print()
        print("│", end="")
        for valor in fila:
            longitud_valor = len(str(valor))
            espacio_extra = " " * (
                maxValor - longitud_valor
            )  # Calcula el espacio extra necesario
            print(f"{espacio_extra}{valor}│", end="")
        print()
    print("─" * coeficienteParaImprimirSeparadores, end="")


def main(n, y, x):
    # Pre: n es potencia de 2 y mayor o igual a 2.
    #      y , x son enteros no negativos
    # Post: Se muestra la matriz que representa el campo de dimension n x n
    #       con las secciones pintadas de acuerdo a las reglas del problema
    campo = Campo(n)
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    seccionar_wrapper(matriz, campo, y, x, [1])
    imprimirMatriz(matriz)


if __name__ == "__main__":
    n = int(sys.argv[1])
    x = int(sys.argv[2])
    y = int(sys.argv[3])
    main(n, x, y)
