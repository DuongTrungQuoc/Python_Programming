#Lọc các phần tử chẵn 
ds = [1,2,3,4,5,6,7,8,9,10,11,12]

nl = list(filter(lambda i: i % 2 ==0,ds))

print (nl)
