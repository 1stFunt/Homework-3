# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.

N = int(input())
list_1 = [i for i in range(1, N + 1)]
print(*list_1)
x = int(input())
minraz = (x - list_1[0])**2
i = 0
j = 0
while i < len(list_1):
    if x == 1:
        j = i + 1
        break
    if (x-list_1[i])**2 <= 0:
        j = i - 1
        break
    if (x - list_1[i])**2 <= minraz:
        minraz = (x-list_1[i])**2
        j = i
        i += 1
print('->', list_1[j])
