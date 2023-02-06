# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].

N = int(input())
list_1 = [i for i in range(1, N + 1)]
print(*list_1)
x = int(input())
count = 0           # или print('->', list_1.count(x))
for i in list_1:
    if x == i:
        count += 1
print('->', count)