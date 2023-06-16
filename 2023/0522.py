key = "keys"
key2 = f"hello {key}"
print(key)
print(key2)

key3 = "new world {}".format("good")
key4 = "new world %s %s" % ("21", "43")
print(key3, end="--")
print(key4)
