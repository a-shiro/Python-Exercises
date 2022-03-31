from files_03_Multilevel_Inheritance.employee import Employee
from files_03_Multilevel_Inheritance.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'
