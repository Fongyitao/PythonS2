# _date_:2017/11/2 21:38

def method_name():
    i = 1
    j = 1
    while i <= 9:
        while j <= 9:
            print(i, "x", j, "= %d" % (i * j), end="\t")
            j += 1
        i += 1
        j = i
        print()


# method_name()

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(j, "x", i, "= %d" % (i * j), end="\t")
        j += 1
    i += 1
    print()
