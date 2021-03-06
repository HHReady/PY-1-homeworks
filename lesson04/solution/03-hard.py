# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]

# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку
matrix_t = list(map(list, zip(*matrix)))
print('---------', *[f'\n{line}' for line in matrix_t], '\n---------')

# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:
number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370482345699890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

number_str = number.replace('\n', '')
number = list(map(int, number_str))
# slices -> [12345], [56789]

start, end = -1, -1
current_item, next_item = 0, 0

multiplications = []


def multiply(*numbers):
    result = 1

    for x in numbers:
        result *= x

    return result


for idx, num in enumerate(number):
    start = idx if start is -1 else start

    if current_item is not 0 and next_item is not 0:
        if num is next_item:
            end = idx
        else:
            start, end = idx, -1
            current_item = num
    else:
        start = idx
        current_item = num

    next_item = num + 1

    # если нашли группу (индексы с нуля)
    if end - start == 4:
        collection = number_str[start:end + 1]
        multiplication = multiply(*number[start:end + 1])
        current_item, next_item = -1, -1

        print(f'collection: [{collection}], start - {start}, end - {end}, multiplication - {multiplication}')


# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

count = 8  # кол-во ферзей
x = []  # положения по X
y = []  # положения по Y

"""
Ферзь может ходить 
как по диагонали, 
так и по прямой 
(горизонтали и вертикали)
"""

''' YES
3 4
8 5
4 1
7 3
6 6
1 7
5 8
2 2
'''

''' NO
1 7
2 4
3 2
4 8
5 6
6 1
7 3
8 5
'''

# берем координаты в виде строки "X Y"
for _ in range(count):
    new_x, new_y = [int(s) for s in input("Type position [x y]: ").split()]
    x.append(new_x)
    y.append(new_y)

# статус проверки по умолчанию
correct = True

# проверяем положения всех ферзей (с дополнительным перебором на каждого - slow)
for first in range(count):
    for second in range(first + 1, count):
        # проверка X, Y и диагонали
        if x[first] == x[second] \
                or y[first] == y[second] \
                or abs(x[first] - x[second]) == abs(y[first] - y[second]):
            correct = False

if correct:
    print('NO')
else:
    print('YES')
