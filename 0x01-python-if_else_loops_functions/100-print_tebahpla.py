for i in range(122, 96, -1):
    print("{}".format(chr(i) if (122 - i) % 2 == 0 else chr(i - 32)), end="")
