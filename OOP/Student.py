class Student:
    # ham thiet lap (constructor)
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade
    #ham in thong tin
    def print_info(self):
        print("ID: " + self.id)
        print("Name: " + self.name)
        print("Grade: " + str(self.grade))
# Khoi tao 1 doi tuong sinh vien
sv1 = Student("53134212","Le Van Tam",8.33)
sv1.print_info()
print(sv1.id)
print(sv1.name)
print(sv1.grade)