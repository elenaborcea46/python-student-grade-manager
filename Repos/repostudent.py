
from Domain.student import Student


class StudentRepository:
    def __init__(self):
        self.__students = {}

    def add(self, student):
        if student.get_student_id() in self.__students:
            raise ValueError(f"Student cu ID-ul {student.get_student_id()} există deja!")
        self.__students[student.get_student_id()] = student

    def remove(self, student_id):
        if student_id not in self.__students:
            raise ValueError(f"Nu există student cu ID-ul {student_id}!")
        return self.__students.pop(student_id)

    def update(self, new_student):
        if new_student.get_student_id() not in self.__students:
            raise ValueError(f"Nu există student cu ID-ul {new_student.get_student_id()} pentru a fi modificat!")
        self.__students[new_student.get_student_id()] = new_student

    def get_all(self):
        return list(self.__students.values())

    def find(self, student_id):
        #return self.__students.get(student_id, None)
        for student in self.__students.values():
            if student.get_student_id() == student_id:
                return student
        return None

    def __len__(self):
        return len(self.__students)


class StudentFileRepository(StudentRepository):
    def __init__(self, filename):
        super().__init__()
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Incaraca datele din fisier
        :return: -;
        """
        with open(self.__filename,"r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                   student_id , nume = line.split(",")
                   student_id = int(student_id)
                   student = Student(student_id, nume)
                   super().add(student)

    def __save_to_file(self):
        """
        Salveaza datele in fisier
        :return: -;
        """
        students = super().get_all()
        with open(self.__filename, "w") as file:
            for student in students:
                student_line = str(student.get_student_id()) + "," + str(student.get_nume()) + "\n"
                file.write(student_line)

    def add(self, student:Student):
        super().add(student)
        self.__save_to_file()

    def remove(self, student_id:int):
        student_sters = super().remove(student_id)
        self.__save_to_file()
        return student_sters

    def update(self, new_student:Student):
        super().update(new_student)
        self.__save_to_file()

    def get_all(self):
        return super().get_all()
    def find(self, student_id:int):
        return super().find(student_id)




