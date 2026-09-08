
class NotaRepository:
    def __init__(self):
        self.__note = []

    def add_nota(self, nota):
        """
            Adaugă o notă în listă.

            :param nota: obiect de tip Nota ce urmează să fie adăugat
            :return: None
            :raises ValueError: dacă există deja o notă pentru același student și aceeași disciplină
        """
        for n in self.__note:
            if n == nota:
                raise ValueError(f"Nota pentru studentul {nota.get_student_id()} la disciplina {nota.get_disciplina_id()} există deja!")
        self.__note.append(nota)

    def delete_by_student_id(self, student_id):
        """
            Șterge toate notele unui student.

            :param student_id: ID-ul studentului ale cărui note sunt eliminate
            :return: None
        """
        self.__note = [n for n in self.__note if n.get_student_id() != student_id]

    def delete_by_disciplina_id(self, disciplina_id):
        """
            Șterge toate notele unei discipline.

            :param disciplina_id: ID-ul disciplinei pentru care se elimină notele
            :return: None
        """
        self.__note = [n for n in self.__note if n.get_disciplina_id() != disciplina_id]

    def get_all(self):
        return list(self.__note)

    def find_note_by_student_and_disciplina(self, student_id, disciplina_id):
        """
           Caută o notă a unui student la o anumită disciplină.

           :param student_id: ID-ul studentului
           :param disciplina_id: ID-ul disciplinei
           :return: obiect Nota dacă există, altfel None
        """
        for n in self.__note:
            if n.get_student_id() == student_id and n.get_disciplina_id() == disciplina_id:
                return n
        return None

    def __len__(self):
        return len(self.__note)


from Domain.notare import Nota


class NotaFileRepository(NotaRepository):
    def __init__(self, filename):
        super().__init__()
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        with open(self.__filename, "r") as file:
            for line in file:
                line = line.strip()
                if line != "":
                    student_id, disciplina_id, valoare = line.split(",")
                    nota = Nota(int(student_id), int(disciplina_id), float(valoare))
                    super().add_nota(nota)

    def __save_to_file(self):
        with open(self.__filename, "w") as file:
            for nota in super().get_all():
                nota_line = str(nota.get_student_id()) + "," + str(nota.get_disciplina_id()) + "," + str(nota.get_valoare()) + "\n"
                file.write(nota_line)

    def add_nota(self, nota):
        super().add_nota(nota)
        self.__save_to_file()

    def delete_by_student_id(self, student_id):
        super().delete_by_student_id(student_id)
        self.__save_to_file()

    def delete_by_disciplina_id(self, disciplina_id):
        super().delete_by_disciplina_id(disciplina_id)
        self.__save_to_file()

    def get_all(self):
        return super().get_all()