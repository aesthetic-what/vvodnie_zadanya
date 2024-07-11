# '1st programm'
x1 = 9
sum = 9 ** 0.5 * 5
print("первое задание, ответ: ", sum)

# '2st programm'
x2 = 9.99
y2 = 9.98
z2 = 1000
c2 = 1000.1
print("второе задание, ответ: ", x2 > y2 and z2 != c2)

# "3rd programm"
num1 = 1234
num2 = 5678
midnum1 = num1 % 1000
midnum11 = midnum1 // 10
midnum2 = num2 % 1000
midnum22 = midnum2 // 10
midsum = midnum11 + midnum22
print(f"третье задание, ответ: сумма серединных чисел равна: {midsum}")

# "4rd programm"
dr_num1 = 13.42
dr_num2 = 42.13

mid_dr1 = dr_num1 * 100
mid_dr2 = dr_num2 * 100

eq_mid_dr = (mid_dr1 // 100 == mid_dr2 % 100) and (mid_dr1 % 100 == mid_dr2 // 100)
print(f"Четвертое задание, ответ: {eq_mid_dr}")
