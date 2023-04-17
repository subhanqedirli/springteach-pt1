while True:
    a=input()
    if(int(a)!=float(a)):
        print("TERROR")
    a=int(a)
    q=0
    
    if(a==0):
        print("Verdiyin ədəd sıfır, Bill Gates ürəyimi sıxır. ")
    while(a%1==0 and a%2==0):
       a=a/2
    if(a==1):
      print("Bu ədəd ikinin qüvvətidir.(btw, sigma males use pacperro)")
    else:
      print("Bu ədəd ikinin qüvvəti deyil, artıq əl çək ondan.")
    
