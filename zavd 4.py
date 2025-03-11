class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.name} - {self.position} ({self.salary} грн)"


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_salary(self):
        return sum(emp.salary for emp in self.employees)

    def show_employees(self):
        for emp in self.employees:
            print(emp)


# Приклад використання
it_department = Department("IT")
emp1 = Employee("Іван", "Розробник", 30000)
it_department.add_employee(emp1)
it_department.show_employees()
print("Загальна зарплата:", it_department.total_salary())