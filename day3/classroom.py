class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def returnName(self):
        return self.firstname + ' ' + self.lastname

class Student(Person):
    def __init__(self, firstname, lastname, subject):
        Person.__init__(self, firstname, lastname)
        self.subject = subject
    def printNameSubject(self):
        print(self.returnName() + ', ' + self.subject)

class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        Person.__init__(self, firstname, lastname)
        self.course = course
    def printNameCourse(self):
        print(self.returnName() + ', ' + self.course)
