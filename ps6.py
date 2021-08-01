list=[]
print("Enter W for win and L for lose the fight")
p=0;q=0;
for i in range(10):
    print("Enter the result of {} fight".format(i+1))
    n=input()
    list.append(n)
    if(n=='w'):
        a=a+1
    else:
        b=b+1
p=a/10
q=b/10
print(a)
print(b)
    