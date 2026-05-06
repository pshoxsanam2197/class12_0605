# 14-m
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def work(self):
        print("Working...")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self._team_size = team_size

    def manage(self):
        print("Managing team...")

    def increase_salary(self, x):
        self._salary += x
        print(f"Salary:{self._salary}")

m = Manager("Ali", 1000, 5)
m.work()
m.manage()
m.increase_salary(500)
