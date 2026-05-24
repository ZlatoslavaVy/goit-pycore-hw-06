from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    pass

class Phone(Field):
    # реалізація класу
	def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("The phone number must be a 10-digits long.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
		def add_record(self, record):
                        
        def find(self, name):
    
        def delete(self, name):
                
        