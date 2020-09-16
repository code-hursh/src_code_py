class Student:
    __q = 39
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    def show(self):
        print('the name of the student is %s and his roll no. is %d'%(self.name,self.roll_no))
# >>> from first import Student
# >>> a = Student()
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# TypeError: __init__() missing 2 required positional arguments: 'name' and 'roll_no'
# >>> a = Student('name',39)
# >>> a.__init__('sai',30)
# >>> a
# <first.Student object at 0x0000023ED0888940>
# >>> type(Student)
# <class 'type'>
