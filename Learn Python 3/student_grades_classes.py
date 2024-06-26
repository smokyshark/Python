class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)
  def get_average(self):
    sum = 0
    for grade in self.grades:
      sum += grade.score
    return sum / len(self.grades)

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score
  def is_passing(self):
    return self.score >= minimum_passing

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter_grade = Grade(100)
pieter.add_grade(pieter_grade)
print(pieter.get_average())