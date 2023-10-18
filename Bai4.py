n = int(input("Nhap so can tinh: "))
k = [0,1]
if n == 0: 
    print (0)
else:
    for i in range (n+1):
        c = k[i]+k[i+1]
        k.append(c)
for i in range (n+1):
    print (k [i],end="")