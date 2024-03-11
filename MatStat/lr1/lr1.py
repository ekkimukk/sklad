import math

array = [40.1, 44.3,	46.2,	34.8,	31.1,	15,	  42.3,	25.7,	42,
               31.9, 45.5,	38.7,	38.7,	47.2,	46.2,	47.5,	48,	  35.5,
               37.6, 57.1,	40.1,	58.6,	27.6,	51.3,	36.9,	49.6,	31.3,
               43,	 2.9,	  31.8,	39.3,	37.4,	45,  	34.4,	54.9,	38.8,
               49.1, 50.9,	43.7,	57, 	36.5,	28.9,	34.4,	35, 	51.9,
               46.2, 44.4,	40.4,	32, 	33.6,	45.4,	56.8,	41.7,	43.2,
               42.1, 52.4,	36.1,	57.6,	33.4,	64.3,	44, 	50.7,	27.3,
               31.5, 45.2,	34.2,	33.2,	35.6,	33, 	38.7,	26.1,	
               45.6, 29.6,	36, 	31.1,	58.8,	20.1,	58, 	38.4,
               52.7, 45.3,	38,	  36,	  46.6,	44.9,	64.4,	38.2,
               16,   39.4,	34,	  49.1,	40.6,	46.1,	27.8,	46.4]

after_dot = 2

print("\n1 .ОБЪЕМ ВЫБОРКИ (n)")
n_1_1 = len(array)
print("n_1_1 =", n_1_1)

print("\n2.1 MAX/MIN (Xmax/Xmin)")
x_min_1_2 = min(array)
x_max_1_2 = max(array)
print("x_max_1_2 =", x_max_1_2, "x_min_1_2 =", x_min_1_2)

print("\n2.2 РАЗМАХ ВАРЬИРОВАНИЯ (R)")
r_1_3 = x_max_1_2 - x_min_1_2
print("r_1_3 =", r_1_3)

print("\n3.1 МЕДИАНА")
if n_1_1 % 2 == 1:
    med = sorted(array)[n_1_1 // 2]
else:
    med = (sorted(array)[n_1_1 // 2] + sorted(array)[n_1_1 // 2 + 1]) / 2
print("med =", med)

print("\n3.2 МОДА")
moda = [0, 0]
for i in set(array):
    if array.count(i) > moda[0]:
        moda[0] = array.count(i)
        moda[1] = i
print(f"moda = {moda[1]} встречается {moda[0]} раз")

print("\n4. ИНТЕРВАЛЬНЫЙ РЯД РАСПРЕДЕЛЕНИЯ ЧАСТОТ")

print("\n4.1 Количество частичных интервалов (m)")
m_1_4 = int(1 + 3.322 * math.log10(n_1_1))
print("m_1_4 =", m_1_4)

print("\n4.2 Длина (шаг) частичного интервала (h)")
h_1_5 = round((x_max_1_2 - x_min_1_2) / m_1_4, 2)
print("h_1_5 =", h_1_5, 2)

print("\n4.3.1 Границы всех частичных интервалов (Xi-Xi+1)")
intervals = {}
for i in range(m_1_4):
    intervals[x_min_1_2 + i * h_1_5] = 0
    keeys = list(intervals.keys())

for i in range(m_1_4):
    if i == m_1_4 - 1:
        print(f"[{round(keeys[i], after_dot)}-{x_max_1_2}]")
    else:
        print(f"[{round(keeys[i], after_dot)}-{round(keeys[i + 1], after_dot)}]", end=', ')

print("\n4.3.2 Частоты интервалов (ni)")
for el in array:
    for key, value in intervals.items():
        if key == keeys[-1]:
            if key <= el <= x_max_1_2:
                intervals[key] = intervals[key] + 1
            elif key <= el <= key + h_1_5:
                intervals[key] = intervals[key] + 1
    chastoty = list(intervals.values())
print(chastoty)
print(sum(chastoty), n_1_1)

print("\n4.3.3 Серединыы частичных интервалов (Xi)")
sered_intervals = [(keeys[i] + keeys[i + 1]) / 2 for i in range(m_1_4 - 1)] + [(keeys[-1] + x_max_1_2) / 2]
print(sered_intervals)

print("\n4.3.4 Относительные частоты интервалов (wi)")
otnos_chast = [i / n_1_1 for i in chastoty]
print(otnos_chast)

print("\n4.3.5 Значения для гистограммы (wi/h)")
znach_gist = [i / h_1_5 for i in otnos_chast]
print(znach_gist)

print("\n----------------------------------\n")
print("6. ТОЧЕЧНЫЕ ОЦЕНКИ ПАРАМЕТРОВ РАСПРЕДЕЛЕНИЯ F*(x)")

print("\n6.1 Выборочная средняя (Xv)")
x_v_sred = 0
for i in range(n_1_1):
x_v_sred += array[i] #
x_v_sred /= n_1_1
print("x_v_sred =", x_v_sred)

print("\n6.2 Выборочная дисперсия (D)")
d_v = 0
for i in range(n_1_1):
d_v += (array[i] - x_v_sred) ** 2
d_v = d_v / n_1_1
print("d_v =", d_v)

print("\n6.3 Иправленная выборочная дисперсия (s)")
s_2 = n_1_1 / (n_1_1 - 1) * d_v
print("s_2 =", s_2, "s =", s_2**0.5,)

print("\n----------------------------------\n")
print("7. ИНТЕРВАЛЬНЫЕ ОЦЕНКИ ПАРАМЕТРОВ РАСПРЕДЕЛЕНИЯ (y = 0.9)")
a = x_v_sred
s_v = d_v ** 0.5
print("s_v =", s_v)
print("a =", x_v_sred)

y = 0.9
alfa = 1 - y
k = n_1_1 - 1
t = 1.6588241874019427

print("\n7.1 Доверительный интервал для математического ожидания")
dov_a = [0, 0]
dov_a[0] = x_v_sred - t * s_v / n_1_1 ** 0.5
dov_a[1] = x_v_sred + t * s_v / n_1_1 ** 0.5
print("dov_a =", dov_a)

print("\n7.2 Доверительный интервал для среднего квадратичного отклонения")
q = 1.65895
dov_sigma = [0, 0]
# dov_sigma[0] = s_2**0.5 * (1 - q)
dov_sigma[1] = (s_2 ** 0.5) * (1 + q)
print("dov_sigma =", dov_sigma)


print("\n----------------------------------\n")
print("8. КРИТЕРИЙ СОГЛАСИЯ ПИРСОНА (a = 0.05)")
a = 0.05

print("\n8.1 Ui и число степеней свободы")
k = m_1_4 - r_1_3 - 1
u_i = [(sered_intervals[i] - x_v_sred) / s_v for i in range(m_1_4)]
print(u_i)

print("\n8.2 Значение функции Гаусса")
fi_u_i = [1 / ((2 * math.pi) ** 0.5) * math.exp(-u_i[i] ** 2 / 2) for i in range(m_1_4)]
print(fi_u_i)

print("\n8.3 Теоретические вероятности попадания в интервал")
teor_ver = [h_1_5 / s_v * fi_u_i[i] for i in range(m_1_4)]
print(teor_ver)
print(sum(teor_ver))

print("\n8.4 Теоретические частоты")
teor_chast = [n_1_1 * teor_ver[i] for i in range(m_1_4)]
print(teor_chast)
print("sum =", sum(teor_chast))

print("\n8.5 Объединение (1 и 2) и нахождение X^2 набл")
teor_chast_ob = [teor_chast[0] + teor_chast[1]] + [i for i in teor_chast[2:]]
chastoty_ob = [chastoty[0] + chastoty[1]] + [i for i in chastoty[2:]]
x_nabl_2 = [(chastoty_ob[i] - teor_chast_ob[i]) ** 2/ teor_chast_ob[i] for i in range(m_1_4 - 1)]
print(x_nabl_2)
print("x_nabl_2 =", sum(x_nabl_2))
