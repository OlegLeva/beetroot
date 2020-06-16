class Person():

    def __init__(self, name, hours_visited, number_of_lectures, practical_lessons):
        self.name = name
        self.hours_visited = hours_visited
        self.number_of_lectures = number_of_lectures
        self.practical_lessons = practical_lessons

    def fire_alarm(self):
        return "Всі на вихід 'БІГОМ'"


class Student(Person):
    course = 5

    def missed(self):
        if self.hours_visited == 0:
            return f"{self.name} на тобі N-ку в журнал"


student = Student("Sheldon", 0, 0, 0)


class Teacher(Person):
    wage = 1000000

    def missed(self):
        if self.number_of_lectures == 0:
            return f"{self.name} Фіг тобі, а не '1000000'"


snejanna_denisovna = Teacher("Snejka", 0, 0, 0)

print(snejanna_denisovna.missed())
print(student.missed())
print(snejanna_denisovna.fire_alarm())
print(student.fire_alarm())
