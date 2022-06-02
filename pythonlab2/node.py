from student import Student


class Node:
    def __init__(self, student: Student):
        self.left = None
        self.right = None
        self.student = student

    def insert(self, student: Student):
        if self.student:
            if student.rating < self.student.rating:
                if self.left is None:
                    self.left = Node(student)
                else:
                    self.left.insert(student)
            elif student.rating > self.student.rating:
                if self.right is None:
                    self.right = Node(student)
                else:
                    self.right.insert(student)
        else:
            self.student.rating = student.rating
        return self

    def find(self, rating):
        if self.left:
            self.left.find(rating)
        if self.student.rating > rating:
            print(self.student)
        if self.right:
            self.right.find(rating)

    def delete_by_group(self, value):
        if value < self.student.group:
            if self.left is None:
                return " not found"
            self.left.delete_by_group(value)
        elif value > self.student.group:
            if self.right is None:
                return " not found"
            self.right.delete_by_group(value)
        else:
            self.student = self.right
            if self.left is not None:
                self.left.delete_by_group(value)
            if self.right is not None:
                self.right.delete_by_group(value)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.student),
        if self.right:
            self.right.print_tree()

    def traverse_preorder(self):
        print(self.student, end=' ')
        if self.left:
            self.left.traverse_preorder()
        if self.right:
            self.right.traverse_preorder()

    def __str__(self):
        return "_"
