n = int(input("Nhap so can kiem tra "))
k=0
if n<0:
    print ("Loi")
if n==1:
    print (n," La so nguyen to")
else:
    for i in range (2,n):
        if n%i == 0:
            k=1
            break
if k==1:
    print (n, " Khong phai la so nguyen to")
elif k==0:
    print (n, " La so nguyen to")