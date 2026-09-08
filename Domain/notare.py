class Nota:
    def __init__(self, student_id, disciplina_id, valoare):
        self.__student_id = student_id
        self.__disciplina_id = disciplina_id
        self.__valoare = valoare

    def get_student_id(self):
        return self.__student_id

    def get_disciplina_id(self):
        return self.__disciplina_id

    def get_valoare(self):
        return self.__valoare

    def set_valoare(self, valoare):
        self.__valoare = valoare

    def __str__(self):
        return f"Student ID: {self.__student_id}, Disciplina ID: {self.__disciplina_id}, Nota: {self.__valoare}"

    def __eq__(self, other):
        if not isinstance(other, Nota):
            return False
        return self.__student_id == other.get_student_id() and self.__disciplina_id == other.get_disciplina_id()
