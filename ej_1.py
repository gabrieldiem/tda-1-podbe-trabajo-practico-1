import csv
import sys


def crearListaDeInfluencers(filename):
    listaDeInfluencers = []
    contadorInfluencers = 0

    with open(filename, "r") as file:
        lector = csv.reader(file)
        for fila in lector:
            contadorInfluencers = contadorInfluencers + 1
            influencerId = int(fila[0])
            nombreInfluencer = fila[1]
            valor = int(fila[2])
            listaIncompatibilidades = []
            for i in fila[3:]:
                listaIncompatibilidades.append(int(i))

            influencer = {
                "id": influencerId,
                "nombre": nombreInfluencer,
                "valor": valor,
                "incompatibilidades": listaIncompatibilidades,
            }

            listaDeInfluencers.append(influencer)
    return listaDeInfluencers, contadorInfluencers


listaInicial = []
n = 0
listaActual = []
valorListaActual = 0
mejorLista = []
valorMejorLista = 0
posInfluencerActual = -1


INFLUENCER_VACIO = {
    "id": -1,
    "nombre": "INFLUENCER_VACIO",
    "valor": 0,
    "incompatibilidades": [],
}


def getValor(influencer):
    return influencer["valor"]


def armarNodo(posActual, listaActual, valorListaActual):
    global listaInicial
    posSiguiente = posActual + 1
    influencerActual = INFLUENCER_VACIO if posActual == -1 else listaInicial[posActual]
    influencerSiguiente = listaInicial[posSiguiente]

    listaIzq = listaActual + [influencerSiguiente]
    valorListaIzq = valorListaActual + influencerSiguiente["valor"]
    listaDer = listaActual
    valorListaDer = valorListaActual

    nodo = {
        "posActual": posActual,
        "listaActual": listaActual,
        "valorListaActual": valorListaActual,
        "influencerActual": influencerActual,
        "influencerSiguiente": influencerSiguiente,
        "listaIzq": listaIzq,
        "valorListaIzq": valorListaIzq,
        "listaDer": listaDer,
        "valorListaDer": valorListaDer,
    }

    return nodo


def esCompatible(influencerAVerificar, listaInfluencers):
    esCompatible = True
    for influencer in listaInfluencers:
        for idInfluencerIncompatible in influencer["incompatibilidades"]:
            if influencerAVerificar["id"] == idInfluencerIncompatible:
                esCompatible = False

    return esCompatible


def costo(posActual, valorListaActual, valorInfluencerSiguiente):
    return valorListaActual + (n - posActual) * valorInfluencerSiguiente


def navegoIzquierda(nodo):
    costoIzq = costo(
        nodo["posActual"],
        nodo["valorListaActual"],
        nodo["influencerSiguiente"]["valor"],
    )
    if (
        esCompatible(nodo["influencerSiguiente"], nodo["listaIzq"])
        and costoIzq > valorMejorLista
    ):
        return True
    else:
        return False


def navegoDerecha(nodo):
    costoDer = costo(
        nodo["posActual"],
        nodo["valorListaActual"],
        nodo["influencerSiguiente"]["valor"],
    )
    if costoDer > valorMejorLista:
        return True
    else:
        return False


def DepthFirstBranchAndBound(listaActual, valorListaActual, posActual):
    global mejorLista
    global valorMejorLista
    if valorListaActual > valorMejorLista:
        mejorLista = listaActual
        valorMejorLista = valorListaActual

    if posActual == (n - 1):
        return
    else:
        nodoActual = armarNodo(posActual, listaActual, valorListaActual)

        if navegoIzquierda(nodoActual) == True:
            DepthFirstBranchAndBound(
                nodoActual["listaIzq"], nodoActual["valorListaIzq"], posActual + 1
            )

        if navegoDerecha(nodoActual) == True:
            DepthFirstBranchAndBound(
                nodoActual["listaDer"], nodoActual["valorListaDer"], posActual + 1
            )

    return


def resetGlobals():
    global listaInicial
    global n
    global listaActual
    global valorListaActual
    global mejorLista
    global valorMejorLista
    global posInfluencerActual

    listaInicial = []
    n = 0
    listaActual = []
    valorListaActual = 0
    mejorLista = []
    valorMejorLista = 0
    posInfluencerActual = -1


def main(filename):
    resetGlobals()
    if filename is None:
        filename = input("Ingrese la ubicación del archivo: ")

    global listaInicial
    global n

    listaInicial, n = crearListaDeInfluencers(filename)
    print(f"Leidos {n} influencers" + "\n")

    if n <= 0:
        print("No se pudo leer ningún influencer")
        return mejorLista, valorMejorLista

    # Ordenamiento inplace. Se usa Timsort O(n*logn) para python hasta 3.10 y usa Powersort O(n*logn) para python desde 3.11
    listaInicial.sort(key=getValor, reverse=True)
    DepthFirstBranchAndBound(listaActual, valorListaActual, posInfluencerActual)

    return mejorLista, valorMejorLista


if __name__ == "__main__":
    argc = len(sys.argv)

    if argc < 2:
        mejorListaReturn, valorMejorListaReturn = main(None)
    else:
        mejorListaReturn, valorMejorListaReturn = main(sys.argv[1])

    print(f"Maximo valor obtenido: {valorMejorListaReturn}" + "\n")
    print("Lista resultado de influencers:" + "\n")
    for influencer in mejorListaReturn:
        print(influencer["nombre"])
