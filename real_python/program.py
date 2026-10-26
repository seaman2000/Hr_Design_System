import hr
import employees
import productivity
import contacts

manager = employees.Manager(1, 'John Smith', 1500)
manager.address = contacts.Address(
    'San Stefano 60',
    'Burgas',
    'Burgas',
    8000
)
secretary = employees.Secretary(2, 'Jane Doe', 1200)
secretary.address = contacts.Address(
    'boul. Bulgaria 25',
    'Plovdiv',
    'Plovdiv',
    4002
)
sales_guy = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employees.FactoryWorker(4, "Pete Peterson", 40, 15)
temporary_secretary = employees.TemporarySecretary(5, "Nana Peterson", 40, 9)

employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary
]

productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)