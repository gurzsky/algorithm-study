def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x - 1)

print (fat(5))

#fat 1
#fat 2 x 1 = 2
#fat 3 x 2 = 6
#fat 4 x 6 = 24
#fat 5 x 24 = 120