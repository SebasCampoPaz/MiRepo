##Sebastian Campo Paz 8972728## 

import math

#############
## Punto 1 ##
#############
def verificarDiagonales(matriz):
    indiceI = 0
    indiceD = -1
    while indiceI < len(matriz):
        if matriz[indiceI][indiceI] != matriz[indiceI][indiceD]:
            return False
        indiceI += 1
        indiceD -= 1
    return True


#############
## Punto 2 ##
#############

def esCapicua(lista):
    listaInvertida = lista[::-1]
    if listaInvertida != lista:
        return False
    else:
        return True

#############
## Punto 3 ##
#############

def verificarRepetidos(diccionario, numero, indice):
    bandera = 0
    if numero not in diccionario:
        diccionario[numero] = [indice]
        bandera = 1
    else:
        if indice not in diccionario[numero]:
            diccionario[numero].append(indice)
            bandera = 1
    return bandera

def diferenciaListas(listaA, listaB):
    listaNoRepetidos = []
    noRepetidos = {}
    i = 0
    while i < len(listaA):
        bandera = 0
        j = 0
        while j < len(listaB) and bandera == 0:
            if listaA[i] == listaB[j]:
                if verificarRepetidos(noRepetidos, listaB[j], j) == 1:
                    bandera = 1
            j += 1
        if bandera == 0:
            listaNoRepetidos.append(listaA[i])
        i += 1

    return listaNoRepetidos

def leerDatos():
    i = 0
    numeroIntentos = int(input())
    while i < numeroIntentos:
        listaA = [int(x) for x in input().split()]
        listaB = [int(x) for x in input().split()]
        del listaA[0]
        del listaB[0]
        print(diferenciaListas(listaA, listaB))
        i += 1
            

#############
## Punto 4 ##
#############

def esPrimo(num):
    limite = math.sqrt(num)
    bandera = 0
    i = 2
    while i <= limite and bandera == 0:
        if num % i == 0:
            bandera = 1
        i += 1
    return bandera

def sumaCifras(numero_dos_cifras):
    n1 = numero_dos_cifras // 10
    n2 =( n1 % 10) + (numero_dos_cifras % 10)
    while n1 >= 10:
        n1 /= 10
        n2 += n1 % 10
    return n2

def mostrarPrimos(numero):
    i = 3
    j = 0
    listaDosCifras = [2]
    ultimoPrimo = 2
    print("Numeros primos entre el 1 y %d:" %numero)
    while i <= numero:
        if esPrimo(i) == 0:
            print("--> %d," %ultimoPrimo)
            ultimoPrimo = i
            verificar_numero = sumaCifras(i)
            if esPrimo(verificar_numero) == 0:
                listaDosCifras.append(i)
        i += 1
    print("--> %d\n" %ultimoPrimo)
    print("Números entre 1 y %d con suma de dígitos con valor primo:" %numero)
    while j < len(listaDosCifras) - 1:
        print("%d" %listaDosCifras[j], end = ", ")
        j += 1
    print(listaDosCifras[-1])

#############
## Punto 5 ##
#############

def sumaValoresMatriz(mat, par):
    sumaValores = 0 
    i = 0
    while i < len(par):
        if par[i][0] in mat:
            j = 0
            bandera = 0
            while j < len(mat[par[i][0]]) and bandera == 0:
                if mat[par[i][0]][j][0] == par[i][1]:
                    sumaValores += mat[par[i][0]][j][1]
                    bandera = 1
                j += 1
        i += 1
    return sumaValores
