import random


def guessNum(randomeNum):
    temp = input("请输入一个数字：")
    guess = int(temp)

    if guess == randomeNum:
        print("恭喜你猜对了")
        return True
    else:
        if guess > randomeNum:
            print("太大了，往下面猜猜")
        else:
            print("太小了，往上面猜猜")
    return False


count = 0
randomeNum = random.randint(1, 100)
# print(randomeNum)
while(count < 8):
    count += 1
    print("这是你第%d次猜数噢， 还有%d次机会，加油" % (count, 9 - count))
    if guessNum(randomeNum):
        break
print("游戏结束")
