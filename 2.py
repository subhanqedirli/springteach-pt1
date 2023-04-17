while True:
    a=list(str(int(input())))
    print(a)
    c=0 ; h=1
    for i in a:
        i = int(i)
        c+=i
        h*=i
    print("Cəm: ",c,"\nHasil: ",h)
