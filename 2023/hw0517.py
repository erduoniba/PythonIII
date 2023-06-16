name = "John"
print("Hello, %s!" % name)

age = 23
print("%s is %d years old." % (name, age))


txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)

print(txt1)
print(txt2)
print(txt3)


name = ['Pete', 'John', 'Elizabeth']
age = [6, 23, 44]
for n, a in zip(name, age):
    print('%s is %d years old' % (n, a))
