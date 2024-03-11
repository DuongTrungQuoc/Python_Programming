# Tính tổng bình phương các số nguyên liên tiếp <= n
def Square(n):
    return n**2
#Chương trình chính
if __name__ == '__main__':
    n=5
    #Cách 1
    s=0
    for i in range(n+1):
        s +=i**2
    #in kết quả
    print("S = {}".format(s))
    #Cách 2
    s=0
    for i in range(n+1):
        s+= Square(i)
    print("S = {}".format(s))
    #Cách 3
    s=0
    for i in range(n+1):
        x = lambda i: i*i
        s += x(i)
    print("S = {}".format(s))