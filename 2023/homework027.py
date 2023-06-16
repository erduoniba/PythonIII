# https: // fishc.com.cn/thread-185046-1-1.html

x = input("请输入一个数字，用于判断是非是回文：")
if x == x[::-1]:
    print("%s 是回文" % x)
else:
    print("%s 不是回文" % x)


y = "I love FishC"
print(y.capitalize())
print(y.title())

print(y.casefold())
print(y.lower())

# lower()相关比较弱，只对 ASCII 也就是 'A-Z'有效。
# casefold() 比较全强，不仅能转ASCII，也可以转一小语种的大小写如德文
# 总结来说，汉语 & 英语环境下面，继续用 lower()没问题；要处理其它语言且存在大小写情况的时候再用casefold()。


z = "省省卡自动触达系统"
print(z.center(15))
print(z.ljust(15))
print(z.rjust(20))

print(z.center(20, "#"))
