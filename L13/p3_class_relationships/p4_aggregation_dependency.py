class Employee:

    def __init__(self, name):
        self.name = name


class Department:

    def __init__(self, department_name):
        self.department_name = department_name
        self._employees = []

    def add_employee(self, employee: Employee):
        self._employees.append(employee)

    def get_all_employees(self):
        return self._employees


class DepartmentUIWidget:

    def __init__(self, department: Department):
        self._department = department

    def show_all_employees(self):
        print(f"Employees for '{self._department.department_name}' department:")
        for employee in self._department.get_all_employees():
            print(f"\t{employee.name}")
        print()


ui_test_department = Department("UI Test Department")
api_test_department = Department("API Test Department")

ui_test_department_ui = DepartmentUIWidget(ui_test_department)
api_test_department_ui = DepartmentUIWidget(api_test_department)

# creating employees' records when hire
john = Employee('John')
anna = Employee('Anna')
james = Employee('James')
olga = Employee('Olga')

# later decide what department each employee should be added
ui_test_department.add_employee(john)
ui_test_department.add_employee(anna)
api_test_department.add_employee(james)
api_test_department.add_employee(olga)

ui_test_department_ui.show_all_employees()
api_test_department_ui.show_all_employees()

# Unfortunately we don't have UI Test Department
del ui_test_department
# But we could move employees to other department
api_test_department.add_employee(john)
api_test_department.add_employee(anna)
api_test_department_ui.show_all_employees()
