class Student:
    def __init__(self, surname, name, group, year_of_birth, rating):
        self.surname = surname
        self.name = name
        self.group = group
        self.year_of_birth = year_of_birth
        self.rating = rating

    def __str__(self):
        return f"Surname: {self.surname}, name: {self.name}, group: {self.group}, " \
               f"year of birth: {self.year_of_birth}, rating: {self.rating} "
