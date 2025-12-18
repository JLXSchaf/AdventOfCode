a = [1,2,3]
b = [[i] for i in a]
c = a

a[1] = 7
print(a, b, c)