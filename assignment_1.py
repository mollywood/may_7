class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.num_greeted = 0
        self.already_greeted = []

    def num_unique_people_greeted(self):
            self.num_greeted += 1

    def greet(self, other_person):
        print(f"Hello {other_person.name}, I am {self.name}!")
        self.greeting_count += 1
        already_greeted = []
        if other_person not in already_greeted:
            other_person.already_greeted.append(self)
            num_unique_people_greeted()

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")

    def add_friend(self, other_person):
        self.friends.append(other_person)

    def num_friends(self):
        print(len(self.friends))

    def __repr__(self):
        return (f"{self.name}, {self.email}, {self.phone}")



sonny = Person("Sonny", "sonny@hotmail.com", "438-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
sonny.greet(jordan)
jordan.greet(sonny)
jordan.greet(sonny)
jordan.greet(sonny)

print(jordan.num_greeted)

jordan.add_friend(sonny)
#jordan.friends.append(sonny)
jordan.num_friends()

print(sonny.email, sonny.phone)
print(jordan.email, jordan.phone)

sonny.print_contact_info()
print(jordan.greeting_count)
print(sonny.greeting_count)

jordan.__repr__()

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.make, self.model, self.year)

car = Vehicle("Ford", "Escape", 2014)

car.print_info()
