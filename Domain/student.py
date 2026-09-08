class Student:
    def __init__(self, student_id, nume):
        self.__student_id = student_id
        self.__nume = nume

    def get_student_id(self):
        return self.__student_id

    def get_nume(self):
        return self.__nume

    def set_id(self, new_student_id):
        self.__student_id = new_student_id

    def set_nume(self, new_nume):
        self.__nume = new_nume

    def __str__(self):
        return f"ID: {self.get_student_id()}, Nume: {self.get_nume()}"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.get_student_id() == other.get_student_id()