import os


os.system('ls')
for a, b, c in os.walk("./"):
    print(a)
    print(b)
    print(c)
    print()
