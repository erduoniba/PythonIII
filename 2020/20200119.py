# -*- coding: utf-8 -*-

"""
寻找水仙花数
说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
// ： 整除
% ： 取余
"""

for x in range(100,1000):
	i = x // 100
	j = x // 10 % 10
	k = x % 10
	if x == i*i*i + j*j*j + k*k*k:
		print("水仙花数：%d" % x)

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)



"""
正整数的反转
例如：将12345变成54321
"""
num = 98657
reversed_num = 0
while num > 0:
	reversed_num = reversed_num * 10 + num % 10
	num //= 10
	print("reversed_num : %d num : %d" % (reversed_num, num))
print("reversed_num : %d" % reversed_num)



"""
百钱百鸡问题
说明：百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
翻译成现代文是：
公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
"""
for gj in range(1,20):
	for mj in range(1,33):
		for xj in range(1,100):
			if (gj + mj + xj == 100) and (gj * 5 + mj * 3 + xj / 3 == 100):
				print("🐓: %d 🐔: %d 🐤:%d" % (gj, mj, xj))

print()

for gj in range(1,20):
	for mj in range(1,33):
		xj = 100 - mj - gj;
		if gj * 5 + mj * 3 + xj / 3 == 100:
			print("🐓: %d 🐔: %d 🐤:%d" % (gj, mj, xj))
			



"""
CRAPS赌博游戏
说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负。
"""

import random

totalCount = 10000
rrr = 0
success = 0
for x in range(1,totalCount):
	print("第%d把 结果：" % x)

	count = 0
	firstNum = 0
	result = False
	while True:
		randomX = random.randint(1, 6)
		randomY = random.randint(1, 6)
		count += 1
		if count == 1:
			firstNum = randomX + randomY
			print("第一次玩家摇出了 %d 点" % firstNum)
			if (firstNum == 7) or (firstNum == 11):
				result = True
				rrr += 1
				success += 1
				print("第%d次就摇出了 %d 点，玩家赢" % (count, firstNum))
				break
			elif (firstNum == 2) or (firstNum == 3) or (firstNum == 12):
				result = False
				rrr -= 1
				print("第%d次就摇出了 %d 点，玩家输" % (count, firstNum))
				break
			else:
				continue
		else:
			otherNum = randomX + randomY
			if firstNum == otherNum:
				result = True
				rrr += 1
				success += 1
				print("第%d次就摇出了 %d 点，玩家赢" % (count, otherNum))
				break
			elif otherNum == 7:
				result = False
				rrr -= 1
				print("第%d次就摇出了 %d 点，玩家输" % (count, otherNum))
				break
			else:
				continue

# 我只玩10000把, 胜利把数：4889,胜率为 48.89 %
print("我只玩%d把, 胜利把数：%d,胜率为 %0.2f %%" % (totalCount, success, float(success) / float(totalCount) * 100))



"""
生成斐波那契数列的前20个数。
说明：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）在《计算之书》
中提出一个在理想假设条件下兔子成长率的问题而引入的数列，
所以这个数列也被戏称为"兔子数列"。
斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，
形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。
斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。
"""

num1 = 1
num2 = 1
array = [1, 1]
while True:
	num = num1 + num2
	num1 = num2
	num2 = num
	array.append(num)
	
	if len(array) > 19:
		break

print("Fibonacci 前20个数为", array)



"""
找出10000以内的完美数。

说明：完美数又称为完全数或完备数，
它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。
完美数有很多神奇的特性，有兴趣的可以自行了解。
"""

array = []
count = 10000
for x in range(1,count):
	total = 0
	for j in range(1, x - 1):
		if x % j == 0:
			total += j
	if total == x:
		array.append(x)
print("%d 内的完美数为:" % count, array)



"""
输出100以内所有的素数。
说明：素数指的是只能被1和自身整除的正整数（不包括1）。
"""

array = []
count = 100
for x in range(1,count):
	total = 0
	for j in range(2, x - 1):
		if x % j == 0:
			total += 1
	if total == 0:
		array.append(x)
print("%d 内的素数为:" % count, array)






















