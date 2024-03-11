def LaSNT(n):
    # Nếu n<2 thì không phải SNT
    if n < 2: return False
    # Nếu n>=2: nếu trong đoạn [2,n//2] có 1 ước số của n
    # thì n không phải SNT
    for i in range(2, n//2+1):
        if n % i == 0: return False
    # Nếu không phải 2 trường hợp trên thì n là SNT
    return True

def InSNT(n):
    for i in range(2,n+1):
        if LaSNT(i): print (i,end='\n')
def TimSNT(n):
    i=n+1
    while not LaSNT(i):
        i=i+1
    return i
# Chương trình chính
if __name__ == '__main__':
    n= 100
    print ("Số {} có phải là số nguyên tố không ? {}".format(n,LaSNT(n)))
    print('Các số nguyên tố <= %d là' % (n))
    InSNT(n)
    
    print ("Số Nguyên tố nhỏ nhất > {} là {}".format(n,TimSNT(n)))