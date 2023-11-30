#zad 1
class Human:
    
    # zmienna klasowa - 'globalna'
    Number_of_humans = 0
    
    def __init__(self, name, age):
        
        # pola zmiennych instacji klasy
        self.name = name
        self.age = age
        
        Human.Number_of_humans += 1
    
    def introduce(self):
        print(f'Hi, nazywam się {self.name} i mam {self.age} lata')

class Student(Human):
    
    def __init__(self, name, age, program):
        
        super().__init__(name, age)
        
        self.program = program
        self.grades = []
        
    def introduce(self):
        print(f'Hi, nazywam się {self.name}, studjuję {self.program} i mam {self.age} lata')
    
    def recive_grade(self, grade):
        self.grades.append(grade)

    def srednia(self):
        self.srednia = sum(self.grades)/len(self.grades)
        
    def __lt__(self, other):
       return self.srednia < other.srednia

x = Student("ania", 22, "cos")
x.recive_grade(1)
x.recive_grade(1)
x.recive_grade(5)
x.srednia()

y = Student("monia",21,"kk")
y.recive_grade(3)
y.recive_grade(3)
y.recive_grade(3)
y.recive_grade(5)
y.srednia()

z = Student("michal",23,"ancs")
z.recive_grade(6)
z.recive_grade(6)
z.srednia()

lista_studentow = [x,y,z]
posortowani_studenci = sorted(lista_studentow)

for student in posortowani_studenci:
    print(f'{student.name}, srednia = {student.srednia}')

