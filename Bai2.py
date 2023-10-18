m = int(input("Nhap thang can kiem tra: "))
y = int(input("Nhap nam can kiem tra: "))
k=0
if m > 12 or m < 1:
    print("Loi")

if y%400 == 0:
    k=1
elif y%4 == 0 and y%100 !=0:
    k=1
if k == 1 and m == 2:
    print ("Thang ", m ," co 29 ngay")

if m == 2 and k != 1:
    print ("Thang ",m," co 28 ngay")

if m == 1 or m == 3 or m==5 or m==7 or m==8 or m==10 or m== 12:
    print ("Thang ",m," co 31 ngay")
if m == 4 or m == 6 or m==9 or m==11:
    print ("Thang ",m," co 30 ngay")