m1,m2,t1,t2 = input().split()

# m1 t1 / m1 t2 / m2 t1 / m2 t2

if m1 != m2 and t1 != t2:
    print("?")

elif m1 == m2 and t1 != t2:
    if m1 == "S" and (t1 == "R" or t2 == "R"):
        print("TK")
    elif m1 == "R" and (t1 == "P" or t2 == "P"):
        print("TK")
    elif m1 == "P" and (t1 == "S" or t2 == "S"):
        print("TK")
    else:
        print("?")

elif m1 != m2 and t1 == t2:
    if t1 == "S" and (m1 == "R" or m2 == "R"):
        print("MS")
    elif t1 == "R" and (m1 == "P" or m2 == "P"):
        print("MS")
    elif t1 == "P" and (m1 == "S" or m2 == "S"):
        print("MS")
    else:
        print("?")

else:
    if m1 == "R":
        if t1 == "S":
            print("MS")
        elif t1 == "P":
            print("TK")
        else:
            print("?")
    if m1 == "S":
        if t1 == "R":
            print("TK")
        elif t1 == "P":
            print("MS")
        else:
            print("?")
    if m1 == "P":
        if t1 == "R":
            print("MS")
        elif t1 == "S":
            print("TK")
        else:
            print("?")