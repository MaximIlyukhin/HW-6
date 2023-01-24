a = [10, 20, 30, 40]
b = ['a', 'b', 'c', 'd', 'e']
for i, j in zip(a, b):
    print(i, j)

b = "Geekbrains"
for i in enumerate(b):
    print(i)

my_list = [11, 22, 33, 44, 55, 66]
result = list(filter(lambda x: (x % 3 == 0), my_list)) 
print(result)     