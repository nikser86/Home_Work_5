import datetime
import statistics

now = datetime.datetime.now()


def second_value(line=[3, 3, 2, 1]):
    """ return second value  """
    line.sort()
    for item in line:
        if line[0] < item:
            res = item
            break
    return res


l = [0, 1, 2, 3, 4, 5, 6, 87, 8]
print('Second value is ', second_value(l))
print()


class Person:
    """ class Person  """

    def __init__(self, fullname='Ivan Ivanenko', year_b=2000):
        assert type(fullname) is str
        self.fullname = fullname
        if (year_b >= now.year) or (year_b <= 1900):
            raise Exception('wrong year ')
        self.year_b = year_b

    def name(self):
        """ return name  """
        name = self.fullname.split()
        return name[0]

    def surname(self):
        """ return surname  """
        name = self.fullname.split()
        return name[1]

    def age_in(self, ag=2021):
        """ calculate the age  """

        return ag - self.year_b

    def __str__(self):
        return f'Person {self.fullname} year of birth {self.year_b}'


pp = Person(fullname='12 sdfgsdfg', year_b=1985)
# fn = ''
# while len(fn.split()) <= 1:
#     fn = input('Enter name and surname ')
#     pp = Person(fullname=fn, year_b=1600)

print(f'Name {pp.name()} surname {pp.surname()} is {pp.age_in(2020)} years old this year ')
print(pp)


class Employee(Person):
    """ Class Employee """

    def __init__(self, fullname='Ivanenko Ivan', year_b=1990, pos='programmer', work_exp=7, salary=1000):
        Person.__init__(self, fullname, year_b)
        self.work_exp = work_exp
        self.pos = pos
        self.salary = salary

    def income(self, m):
        """ to increase salary """
        self.salary += m

    def pos_up(self):
        if self.work_exp < 3:
            return ' Junior ' + self.pos
        if 3 <= self.work_exp <= 6:
            return ' Middle ' + self.pos
        if self.work_exp > 6:
            return ' Senior ' + self.pos

    def __str__(self):
        return f'Employee {self.fullname} {self.age_in()} {self.pos_up()} {self.salary}'


print()
ee = Employee()
ee.income(500)
print(ee)
print()


class ITEmployee(Employee):
    """ Class ITEmployee """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skills = []

    def add_skill(self, new_skill):
        """Add new skill"""
        self.skills.append(new_skill)

    def __str__(self):
        return f'ITEmployee {self.fullname} {self.age_in()} {self.pos_up()} {self.salary} {self.skills}'


it = ITEmployee()
it.add_skill('Teamwork skills')
it.add_skill('Effective decision making ')

print(it)


class Room:
    """ class rectangular area   """

    def __init__(self, sideA=5, sideB=2):
        self.sideA = sideA
        self.sideB = sideB

    def area(self):
        """ return area  """
        return self.sideA * self.sideB

    def perimeter(self):
        """ return perimeter  """
        return self.sideA * 2 + self.sideB * 2

    def __str__(self):
        return f'Room sideA = {self.sideA} sideb = {self.sideB}, area =  {self.area()} perimeter is {self.perimeter()}'


print()
rr = Room()
print(rr)


class Student:
    """ class student   """

    def __init__(self, fullName="Ivav Ivanov", specialty='plasterer', year_begin=2015, list_of_grades=[2, 5, 3, 6]):
        self.fullName = fullName
        self.specialty = specialty
        self.year_begin = year_begin
        self.list_of_grades = list_of_grades

    def add_list_of_grades(self, new):
        """Add new grades"""
        self.list_of_grades.append(new)

    def average_mark(self):
        """calculate average_mark """
        return statistics.mean(self.list_of_grades)

    def years_of_study(self):
        """return years of study"""
        return now.year - self.year_begin

    def __str__(self):
        return f'Student Name is {self.fullName} specialty is {self.specialty}, year begin =  {self.year_begin}, ' \
               f'list_of_grades ={self.list_of_grades}, \n average mark {self.average_mark()} years_of_study {self.years_of_study()}'


print()
st = Student()
st.add_list_of_grades(7)
print(st)

print()


class Tochka:
    def __init__(self, x1=4, x2=3):
        self.x1 = x1
        self.x2 = x2

    def origin(self):
        """return distance from self to 0"""
        return ((self.x1 ** 2) + (self.x2 ** 2)) ** 0.5

    def distance(self, t2):
        """return distance from self to t2"""
        return (((self.x2 - self.x1) ** 2) + ((t2.x2 - t2.x1) ** 2)) ** 0.5

    def __str__(self):
        return f'to begin {self.origin()} '


t = Tochka(5, 7)
print(t)
y = Tochka(4, -2)
print(t.distance(y))
