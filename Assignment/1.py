def get_name_and_age():
    """ function gets name and age"""
    name = input("Enter name")
    age = int(input("Enter Age"))
    return name, age


name, age = get_name_and_age()
print(name)


def get_decades_lived(years):
    """Gets the year  how many years the person has lived"""
    return years//10


print(get_decades_lived(23))
