import random

from Domain.student import Student
from Domain.validator import StudentValidator
from Repos.repostudent import StudentRepository,StudentFileRepository
from Repos.reponotare import NotaRepository


class StudentService:
    def __init__(self, repo, validator: StudentValidator, nota_repo: NotaRepository):
        self.__repo = repo
        self.__validator = validator
        self.__nota_repo = nota_repo

    def add_student(self, student_id, nume):
        student = Student(student_id, nume)
        self.__validator.validate(student)
        self.__repo.add(student)
        return student

    def get_all_students(self):
        return self.__repo.get_all()

    def delete_student(self, student_id):
        student_sters = self.__repo.remove(student_id)
        self.__nota_repo.delete_by_student_id(student_id)
        return student_sters

    def modify_student(self, student_id, new_nume):
        temp_student = Student(student_id, new_nume)
        self.__validator.validate(temp_student)  # Ridică ValueError

        student = self.__repo.find(student_id)
        if student is None:
            raise ValueError(f"Nu există student cu ID-ul {student_id} pentru a fi modificat!")

        student.set_nume(new_nume)

        self.__repo.update(student)  # Ridică ValueError
        return student

    def find_students_by_name(self, nume_cautat):
        """
        Caută studenți a căror nume conține textul dat
        """
        rezultat = []
        for student in self.__repo.get_all():
            if nume_cautat.lower() in student.get_nume().lower():
                rezultat.append(student)
        return rezultat

    def find_students_by_name_rec(self, nume_cautat, studenti=None, index=0):
        if studenti is None:
            studenti = self.__repo.get_all()

        if index == len(studenti):
            return []

        rest = self.find_students_by_name_rec(nume_cautat, studenti, index + 1)

        if nume_cautat.lower() in studenti[index].get_nume().lower():
            return [studenti[index]] + rest
        return rest

    def generare_random_studenti(self, n):
        """
        Genereaza n studenti random si ii adauga in repository.
        :param n: n numarul de studenti de generat
        :return: Lista cu studenti generati random.
        """
        nume_posibile = ["Ana", "Mihai", "Ioana", "Paul", "Maria", "Vlad"]

        generati = []

        for _ in range(n):

            while True:
                student_id = random.randint(1, 9999)
                if self.__repo.find(student_id) is None:
                    break

            nume = random.choice(nume_posibile)

            student = Student(student_id, nume)
            self.__repo.add(student)

            generati.append(student)

        return generati