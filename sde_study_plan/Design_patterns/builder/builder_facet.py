class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"  

class PersonBuilder:
    def __init__(self, name):
        self.person = Person(name, 0)

    def age(self, age):
        self.person.age = age
        return self

    def build(self):
        return self.person

class PersonJobBuilder:
    def __init__(self, person):
        self.person = person

    def job(self, job_title):
        self.person.job_title = job_title
        return self

    def build(self):
        return self.person 

