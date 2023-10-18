n = int(input("Nhập số cần kiểm tra: "))
k=0
S=0
if n%2==0:
    k=0
else:
    k=1
if k==0:
    for i in range (1,n+1):
        S=S+i
    print ("Tong: ",S)
else:
    S=1
    for i in range (1,n+1):
        S=S*i
    print ("Tich: ",S)

        