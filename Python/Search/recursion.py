def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        value = list.pop(0)
        return value + sum(list)

print(sum([1, 3, 5, 7, 9]))

def countItens(list, count):
    if (len(list) == 0):
        return count
    else:
        list.pop(0)
        return countItens(list, (count + 1))

print(countItens([1, 3, 5, 7, 9], 0))

def higherValue(list, value):
    if (len(list) == 0):
        return value
    else:
        higher = list.pop(0)
        if (value < higher):
            value = higher
        return higherValue(list, value)

print(higherValue([1, 3, 5, 7, 9, 2, 4], 0))



