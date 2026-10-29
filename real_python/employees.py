from productivity import ProductivitySystem
from hr import PayrollSystem
from contacts import AddressBook
from representations import AsDictionaryMixin

class EmployeeDatabase:
    def __init__(self):
        self._employees = [
            {
                'id': 1,
                'name': 'George Angelov',
                'role': 'manager'
            },
            {
                'id': 2,
                'name': 'Mariq Georgieva',
                'role': 'secretary'

            },
            {
                'id': 3,
                'name': 'Kaloqn Nikolov',
                'role': 'sales'
            },
            {
                'id': 4,
                'name': 'Todor Nikolaev',
                'role': 'factory'
            },
            {
                'id': 5,
                'name': 'Kristiqn Kirilov',
                'role': 'secretary'
            }
        ]
        self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self.employee_addresses = AddressBook()

    def employees(self):
        return [self._create_employee(**data) for data in self._employees]

    def _create_employee(self,id, name, role):
        address = self.employee_addresses.get_employee_address(id)
        employee_role = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, payroll_policy)

class Employee(AsDictionaryMixin):
    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address
        self._role = role
        self._payroll = payroll

    def work(self, hours):
        duties = self._role.work(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {duties}')
        print('')
        self._payroll.track_work(hours)

    def calculate_payroll(self):
        return self._payroll.calculate_payroll()

