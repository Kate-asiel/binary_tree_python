from student import Student
from node import Node


def main():
    yulia = Student("Shvets", "Yulia", "IR-12", 2004, 100)
    vadym = Student("Pavlyk", "Vadym", "IR-12", 2003, 90)
    pavlo = Student("Turchyniak", "Pavlo", "IR-11", 2004, 50)
    olha = Student("Rybenchuk", "Olha", "IR-14", 2003, 70)
    ihor = Student("Boklach", "Ihor", "IR-13", 2004, 80)

    root = Node(yulia)
    root.insert(vadym)
    root.insert(pavlo)
    root.insert(olha)
    root.insert(ihor)
    root.print_tree()
    print("\n")
    root.find(60)
    root.delete_by_group("IR-11")
    print("\n")
    root.print_tree()


if __name__ == '__main__':
    main()
