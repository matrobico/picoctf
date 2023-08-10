flag = "thisIsMyFlag"
key = 1010101010

result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))

print("Result: {}".format(result))
