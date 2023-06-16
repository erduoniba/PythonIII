# -*- coding: utf-8 -*-

"""
first project
hello,world
"""

import math
import this
print("hello, world")


"""
import turtle
turtle.pensize(4)
turtle.pencolor('red')

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.mainloop()
"""

"""
second project
"""

a = 100
b = 200
print(a+b)
print(a-b)
print(a/float(b))
print(a*b)


a = 100
b = 1.235
c = 1 + 5j
d = "hello,world"
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print("\n")


"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串
"""

ax = 20
bx = 90
print('%d + %d = %d' % (ax, bx, ax+bx))

ax *= bx + 200
print('ax : ', ax)


"""
华氏温度转换为摄氏温度。
华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。
"""

f = 210
c = (f - 32)/1.8
print("%0.3f华氏温度，对应的摄氏温度为:%0.3f" % (f, c))


"""
输入半径计算圆的周长和面积
"""


radius = 100
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print("%0.3f半径的周长是:%0.3f, 面积是:%0.3f" % (radius, perimeter, area))


"""
输入年份 如果是闰年输出True 否则输出False
闰年是公历中的名词。闰年分为普通闰年和世纪闰年。
普通闰年:公历年份是4的倍数的，且不是100的倍数，为闰年。（如2004年就是闰年）；
世纪闰年:公历年份是整百数的，必须是400的倍数才是世纪闰年（如1900年不是世纪闰年，2000年是世纪闰年）；
"""
year = 2021
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
ll = "否"
if is_leap:
    ll = "是"
    pass
print("%d年是不是闰年:%s" % (year, ll))
