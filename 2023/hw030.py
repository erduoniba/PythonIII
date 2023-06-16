print("   左侧不留白".lstrip())

print("右侧不留白   ".rstrip())

print("     右侧不留白   ".strip())

print("www.harry.home.com".lstrip("w."))

print("www.harry.home.com".strip("w.com"))


print("www.harry.home.com".partition("."))

print("------------------")
print("www.harry.home.com".split("."))
print("www.harry.home.com".split(".", 1))
print("www.harry.home.com".split(".", 2))

print("------------------")
x = ".".join(["www", "harry", "com"])
print(x)
x = "\n".join(["www", "harry", "com"])
print(x)

# 从上图的比对数据我们不难看出，当拼接的数据比较少的时候，两者差别不大，但随着数据的增加，两者的性能差距越来越大……
# 由此可以看出，使用加号拼接的方式，一旦碰到大数据处理的时候，性能是非常非常缓慢的。
