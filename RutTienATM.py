# Bài toán rút tiền ATM

#Lặp lại nhập số tiền đến khi thỏa điều kiện
while True:
    m = int(input("Nhap so tien rut:"))
    if m <= 0 or m % 5 != 0:
        print ("Số tiền không thỏa mãn.")
    else : break
n =m
# a - Tìm phương án tốt nhất
# Các làm: ưu tiên rút mệnh giá cao trước
soTo100 = m //100
m = m % 100
soTo20 = m //20
m = m % 20
soTo5 = m //5
print ("Phương án rút tiền tốt nhất là: ")
print ("{} tờ 100 + {} tờ 20 + {} tờ 5." .format(soTo100,soTo20,soTo5))
soCach =0
for soTo100 in range(n//100+1):
    for soTo20 in range(n//20+1):
        for soTo5 in range(n//5+1):
            if soTo100*100 + soTo20*20 + soTo5*5 == n : 
                soCach +=1
                print ("{}: {} tờ 100 + {} tờ 20 + {} tờ 5." .format(soCach,soTo100,soTo20,soTo5))
print("Có tất cả {} cách rút".format(soCach))