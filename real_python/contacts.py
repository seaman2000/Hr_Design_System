class AddressBook:
    def __init__(self):
        self._employee_addresses = {
            1: Address('San Stefano 60A','Burgas','Burgas',8000),
            2: Address('San Stefano 60B', 'Burgas', 'Burgas', 8000),
            3: Address('Fotinov 65', 'Aitos', 'Burgas', 2001),
            4: Address('Gladstoun 23A', 'Stara Zagora', 'Burgas', 3320),
            5: Address('Slavqnska 69', 'Plovdiv', 'Plovdiv', 4002)
        }
    def get_employee_address(self, id):
        employee_address = self._employee_addresses.get(id)
        if not employee_address:
            raise ValueError('Invalid employee_id')
        return employee_address

class Address:
    def __init__(self, street, city, state, zipcode, street2=None):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state}, {self.zipcode}')
        return '\n'.join(lines)

