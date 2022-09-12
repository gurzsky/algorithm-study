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


