# Напишите программу, которая вычисляет стоимость введенного пользователем слова

dictionary = {1: 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ', 3: 'БГЁЬЯ',
              4: 'FHVWYЙЫ', 5: 'KЖЗХЦЧ', 8: 'JZШЭЮ', 10: 'QZФЩЪ'}
text = input().upper()
if (text):
    print(sum([i for j in text for i, k in dictionary.items() if j in k]))