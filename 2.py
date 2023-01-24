# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

def fun_sum(a):
    if len(a) % 2 == 0:
        return [a[i] * (a[len(a) - i - 1]) for i in range(len(a) // 2)]
    else:
        return [a[i] * (a[len(a) - i - 1]) for i in range(len(a) // 2 + 1)]

c = list(map(int, input().split()))
print(fun_sum(c))
