def hallow(n,m):
    for i in range(n+1):
        for j in range(m+1):
            if (i>1) and (j>1) and (j<19):
                print(end=" ")
            else:
                print("*", end =" ")
        print()

hallow(6, 20)