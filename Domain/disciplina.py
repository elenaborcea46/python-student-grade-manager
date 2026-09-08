class Disciplina:
    def __init__(self, disciplina_id, nume, profesor):
        self.__disciplina_id = disciplina_id
        self.__nume = nume
        self.__profesor = profesor

    def get_disciplina_id(self):
        return self.__disciplina_id

    def get_nume(self):
        return self.__nume

    def get_profesor(self):
        return self.__profesor

    def set_disciplina_id(self, new_disciplina_id):
        self.__disciplina_id = new_disciplina_id

    def set_nume(self, new_nume):
        self.__nume = new_nume

    def set_profesor(self, new_profesor):
        self.__profesor = new_profesor

    def __str__(self):
        return f"ID: {self.get_disciplina_id()}, Nume: {self.get_nume()}, Profesor: {self.get_profesor()}"

    def __eq__(self, other):
        if not isinstance(other, Disciplina):
            return False
        return self.get_disciplina_id() == other.get_disciplina_id()