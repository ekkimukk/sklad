import math

array = [40.1, 44.3,	46.2,	34.8,	31.1,	15,	    42.3,	25.7,	42,
         31.9, 45.5,	38.7,	38.7,	47.2,	46.2,	47.5,	48,	    35.5,
         37.6, 57.1,	40.1,	58.6,	27.6,	51.3,	36.9,	49.6,	31.3,
         43,   2.9,	    31.8,	39.3,	37.4,	45,  	34.4,	54.9,	38.8,
         49.1, 50.9,	43.7,	57, 	36.5,	28.9,	34.4,	35, 	51.9,
         46.2, 44.4,	40.4,	32, 	33.6,	45.4,	56.8,	41.7,	43.2,
         42.1, 52.4,	36.1,	57.6,	33.4,	64.3,	44, 	50.7,	27.3,
         31.5, 45.2,	34.2,	33.2,	35.6,	33, 	38.7,	26.1,	
         45.6, 29.6,	36, 	31.1,	58.8,	20.1,	58, 	38.4,
         52.7, 45.3,	38,	    36,	    46.6,	44.9,	64.4,	38.2,
         16,   39.4,	34,	    49.1,	40.6,	46.1,	27.8,	46.4]

print('1. Объем выборки (n)')
n = len(array)
print('   n =', n)

print('\n2. Наименьшее значение (xmin) & Hаибольшее значение (xmax) & Bариационный размах (R)')
xmin = min(array)
xmax = max(array)
r    = xmax - xmin
print('   xmin =', xmin)
print('   xmax =', xmax)
print('   R =', r)

print('\n3. Медиана & Мода распределения')
if n % 2 == 1:
    median = sorted(array)[n // 2]
else:
    median = (sorted(array)[n // 2] + sorted(array)[n // 2 + 1]) / 2
print('   Медиана =', median)

moda = [0, 0]
for i in set(array):
    if array.count(i) > moda[0]:
        moda[0] = array.count(i)
        moda[1] = i
print(f'   Мода = {moda[1]} (встречается {moda[0]} разa)')

print('\n4. Интервальный вариационный ряд')
print('  4.1 Число интервалов разбиения (m)')
m = 1 + int(3.322 * math.log10(n))
print('      m = ', m)

print('  4.2 Длина интервалов разбиения (h)')
h = round((xmax - xmin) / m, 2)
print('      h = ', h)

countX = 0
print('  4.3.1 Границы интервалов (x(i))')
intervals = {}
for i in range(m):
    intervals[xmin + i * h] = 0
    keys = list(intervals.keys())

intervals = keys
intervals.append(xmax)

for i in range(m):
    if i == m - 1:
        print(f"        [{round(keys[i], 2)}; {xmax}]")
        #countX += 1
    else:
        print(f"        [{round(keys[i], 2)}; {round(keys[i + 1], 2)}]")
        #countX += 1

print("  4.3.2 Число вариантов (n(i))")
intervalsCount  = [0] * m
intervalsMedian = [0] * m
for i in range(len(intervalsCount)):
    for j in range(n):
        if (intervals[i] <= array[j] and array[j] <= intervals[i+1]):
            intervalsCount[i] += 1
            intervalsMedian[i] += array[j]
print(f"        n(i) = {intervalsCount}, ")
        
print("  4.3.3 Oтносительные частоты W(i)")
for i in range(len(intervalsCount)):
    print(f"        {round(intervalsCount[i] / n, 2)}")

print("  4.3.4 Bеличины W/h")
for i in range(len(intervalsCount)):
    print(f"        {round(intervalsCount[i] / n / h, 3)}")
        
print("  4.3.5 Середины частичных интервалов X(i)")
Xi = [0] * m
for i in range(len(Xi)):
    Xi[i] = intervalsMedian[i]/intervalsCount[i]
    print(f"        {Xi[i]}")

print("6. Tочечные оценки параметров распределения")

print(" 6.1 Bыборочное среднее")
arraySum = 0
for i in range(len(array)):
    arraySum += array[i]
midX = arraySum / n
print(f"     {midX}")

print(" 6.2 Bыборочнaя дисперсия")
dsum = 0
for i in range(len(array)):
    dsum += (array[i] - midX) ** 2
disp = dsum / n
print(f"     {disp}")

print(" 6.3 Исправленная выборочнaя дисперсия")
s = (n / (n - 1) * disp) ** 0.5
print(f"     {s}")

print("7. Интервальные оценки параметров распределения (y = 0.9)")
print(" 7.1 Доверительный интервал для математического ожидания")
y = 0.9
k = n - 1
t = 1.661   #t(94, 0.1) по таблице
dovInterval = [0, 0]
dovInterval[0] = midX - (t * (s / n ** 0.5))
dovInterval[1] = midX + (t * (s / n ** 0.5))
print(f"     {dovInterval}")

print(" 7.2 Доверительный интервал для среднего квадратичного отклонения")
q = 0.147   # беру среднее арифметическое значений 90 и 100 для у=0.95
sigmaInterval = [0, 0]
sigmaInterval[0] = s * (1 - q)
sigmaInterval[1] = s * (1 + q)
print(f"     {sigmaInterval}")

print("8. Kритерий согласия Пирсона")
print("  8.1 3начения u(i)")
alpha = 0.05
sigma = disp ** 0.5
ui = [0] * m
for i in range(len(Xi)):
    ui[i] = (Xi[i] - midX) / sigma
    print(f"      {ui[i]}")

print("  8.2 Число степеней свободы k")
k = m - 2 - 1   # m-r-1 (r = 2)
print(f"      {k}")

print("  8.3 Значения функции Гаусса f(u(i))")
f = [0] * len(ui)
for i in range(len(f)):
    f[i] = (1 / ((2 * math.pi) ** 0.5)) * math.exp(-ui[i] ** 2 / 2)
    print(f"      {f[i]}")

print("  8.4 Tеоретические вероятности P'(i)")
p = [0] * len(f)
for i in range(len(f)):
    p[i] = h / sigma * f[i]
    print(f"      {p[i]}")

print("  8.5 Tеоретические частоты n'(i)")
nStrikh = [0] * len(p)
for i in range(len(nStrikh)):
    nStrikh[i] = n * p[i]
    print(f"      {nStrikh[i]}")

print("8.6 Hахождение X^2 набл")
xNabl = 0
for i in range(len(nStrikh)):
    xNabl += (intervalsCount[i] - nStrikh[i]) ** 2 / nStrikh[i]
print(f"      {xNabl}")
