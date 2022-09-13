def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        value = list.pop(0)
        return value + sum(list)

print(sum([1, 3, 5, 7, 9]))

#book solution
def soma(lista):
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:])

print(soma([1, 3, 5, 7, 9]))

def countItens(list, count):
    if (len(list) == 0):
        return count
    else:
        list.pop(0)
        return countItens(list, (count + 1))

print(countItens([1, 3, 5, 7, 9], 0))

#book solution
def conta(lista):
    if lista == []:
        return 0
    return 1 + conta(lista[1:])

print(conta([1, 3, 5, 7, 9]))

def higherValue(list, value):
    if (len(list) == 0):
        return value
    else:
        higher = list.pop(0)
        if (value < higher):
            value = higher
        return higherValue(list, value)

print(higherValue([1, 3, 5, 7, 9, 2, 4], 0))

#book solution
def maximo(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maximo(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max

print(maximo([1, 3, 5, 7, 9, 2, 4]))



