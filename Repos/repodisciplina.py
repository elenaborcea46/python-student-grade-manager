from Domain.disciplina import Disciplina


class DisciplinaRepository:
    def __init__(self):
        self.__discipline = {}

    def add(self, disciplina):
        if disciplina.get_disciplina_id() in self.__discipline:
            raise ValueError(f"Disciplina cu ID-ul {disciplina.get_disciplina_id()} există deja!")
        self.__discipline[disciplina.get_disciplina_id()] = disciplina

    def remove(self, disciplina_id):
        if disciplina_id not in self.__discipline:
            raise ValueError(f"Nu există disciplină cu ID-ul {disciplina_id}!")
        return self.__discipline.pop(disciplina_id)

    def update(self, new_disciplina):
        if new_disciplina.get_disciplina_id() not in self.__discipline:
            raise ValueError(
                f"Nu există disciplină cu ID-ul {new_disciplina.get_disciplina_id()} pentru a fi modificată!")
        self.__discipline[new_disciplina.get_disciplina_id()] = new_disciplina

    def get_all(self):
        return list(self.__discipline.values())

    def find(self, disciplina_id):
        return self.__discipline.get(disciplina_id, None)

    def __len__(self):
        return len(self.__discipline)


class DisciplinaFileRepository(DisciplinaRepository):
    def __init__(self,filename):
        super().__init__()
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Incarca datele din fisier.
        :return: -;
        """
        with open(self.__filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    disciplina_id , nume , profesor = line.split(",")
                    disciplina_id = int(disciplina_id)
                    disciplina = Disciplina(disciplina_id, nume, profesor)
                    super().add(disciplina)

    def __save_to_file(self):
        """
        Salveaza datele in fisier
        :return: -;
        """
        discipline = super().get_all()
        with open(self.__filename, "w") as file:
            for disciplina in discipline:
                disciplina_line = str(disciplina.get_disciplina_id()) + "," + str(disciplina.get_nume()) + "," + str(disciplina.get_profesor()) + "\n"
                file.write(disciplina_line)

    def add(self, disciplina:Disciplina):
        super().add(disciplina)
        self.__save_to_file()

    def remove(self, disciplina_id:int):
        disciplina_stearsa = super().remove(disciplina_id)
        self.__save_to_file()
        return disciplina_stearsa

    def update(self, new_disciplina:Disciplina):
        super().update(new_disciplina)
        self.__save_to_file()

    def get_all(self):
        return super().get_all()
    def find(self, disciplina_id):
        return super().find(disciplina_id)
