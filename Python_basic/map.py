# Cách 1
a = [1,2,3,4]
b = []
for i in range(len(a)):
    b.append(a[i]**2)
print(b)

#Cách 2: Dùng hàm map
# Định nghĩa hàm bình phương
def Square(x):
    return x**2
b = map(Square, a)
b = list(b)
print(b)

# Cách 3: Dùng hàm map + lambda
b = list(map(lambda x: x**2,a))
print(b)