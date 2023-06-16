x = "我爱Python"
print(x.startswith("我"))
print(x.startswith("1"))

print(x.endswith("Python"))
print(x.endswith("python"))

print(x.startswith("爱", 1))
print(x.endswith("Py", 0, 4))


print(x.startswith(("你", "我", "她")))

y = "I Love Python"
print(y.istitle())

print("============")
print(y.upper().isupper())
