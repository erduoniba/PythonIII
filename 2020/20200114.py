# -*- coding: utf-8 -*-

"""
用户身份验证
"""

from math import sqrt
import random
import math
username = "harrydeng"
password = "123456"
if username == "hd" and password == "123456":
    print("用户名或密码不正确")
else:
    print("用户名密码正确")


"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""

x = 20
y = 0
if x > 1:
    y = 3 * x - 5
    print("3x-5")
elif x < -1:
    y = 5 * x + 3
    print("5x+3")
else:
    y = x + 2
    print("x+2")
print("x:%d y:%d" % (x, y))


"""
要求：如果输入的成绩在90分以上（含90分）输出A；
80分-90分（不含90分）输出B；
70分-80分（不含80分）输出C；
60分-70分（不含70分）输出D；
60分以下输出E。
"""
grade = 90
value = ""
if grade >= 90:
    value = "A"
elif grade >= 80:
    value = "B"
elif grade >= 70:
    value = "C"
elif grade >= 60:
    value = "D"
else:
    value = "E"
print("%0.1f分数是：%s" % (grade, value))


"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积
** 即 math.sqrt
"""

a = 30
b = 40
c = 50
if (a + b > c) or (a + c > b) or (b + c > a):
    p = (a + b + c) / 2
    v = p * (p - a) * (p - b) * (p - c)

    area = v ** 0.5
    print("周长是:%0.1f 面积是:%0.3f" % (p, area))

    v = math.sqrt((p * (p - a) * (p - b) * (p - c)))
    print("周长是:%0.1f 面积是:%0.3f" % (p, area))
else:
    print("不是三角形")


"""
用for循环实现1~100求和

用for循环实现1~100之间的偶数求和

"""
sum = 0
for i in range(101):
    sum += i
print(sum)

sum = 0
for i in range(2, 101, 2):
    sum += i
print(sum)


sum = 0
for i in range(101):
    if i % 2 == 0:
        sum += i
print(sum)


"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

random = random.randint(1, 100)
count = 0
number = 50
while True:
    count += 1
    # number = int(input("请输入:"))
    if number > random:
        print("大了点")
        number -= 1
    elif number < random:
        print("小了点")
        number += 1
    else:
        print("猜对了，正确的是：%d" % random)
        break
print("总共猜了 %d 次" % count)
if count > 7:
    print("你的智商明显不足")


"""
输出乘法口诀表(九九表)
"""
# for x in range(1, 10):
# 	for y in range(1, 10):
# 		print("%d*%d=%d" % (x, y, x * y), end="\t")
# 	print()


"""
输入一个正整数判断它是不是素数
素数指的是只能被1和自身整除的大于1的整数。
"""


whileCount = 0
num = 21
while True:
    whileCount += 1
    # num = int(input("num:"))
    count = 0
    for x in range(1, num):
        if num % x == 0:
            count += 1

    if count > 2:
        print("%d 不是素数" % num)
    else:
        print("%d 是素数" % num)

    if whileCount > 10:
        break


"""
输入两个正整数计算它们的最大公约数和最小公倍数
"""
x = int(input("x = "))
y = int(input("y = "))

# 如果x大于y就交换x和y的值
if x > y:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    x, y = y, x

# 从两个数中较的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
    print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
    break

print('xxx')
