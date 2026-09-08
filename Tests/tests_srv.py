import unittest
from Domain.student import Student
from Domain.validator import StudentValidator
from Services.servicestudenti import StudentService
from Repos.repostudent import StudentRepository
from Repos.reponotare import NotaRepository


class TestStudentServiceWhiteBox(unittest.TestCase):

    def setUp(self):
        # white-box: avem acces direct la dependintele interne
        self.student_repo = StudentRepository()
        self.nota_repo = NotaRepository()
        self.validator = StudentValidator()

        self.service = StudentService(
            self.student_repo,
            self.validator,
            self.nota_repo
        )


    def test_add_student_whitebox(self):
        student = self.service.add_student(1, "Ana")

        #  studentul a fost adaugat in repository (efect intern)
        self.assertEqual(len(self.student_repo), 1)

        #  repo contine exact studentul adaugat
        self.assertEqual(self.student_repo.find(1), student)

        #  datele studentului sunt corecte
        self.assertEqual(student.get_nume(), "Ana")

    def test_add_duplicate_student_raises_error_whitebox(self):
        self.service.add_student(1, "Ana")

        self.assertRaises(
            ValueError,
            self.service.add_student,
            1,
            "Maria"
        )

        # white-box: repo NU s-a modificat
        self.assertEqual(len(self.student_repo), 1)


    def test_delete_student_whitebox(self):
        self.service.add_student(2, "Mihai")

        deleted = self.service.delete_student(2)
        self.assertEqual(len(self.student_repo), 0)
        self.assertEqual(deleted.get_student_id(), 2)

    def test_delete_nonexistent_student_raises_error_whitebox(self):
        self.assertRaises(
            ValueError,
            self.service.delete_student,
            99
        )

        # white-box: repo ramane neschimbat
        self.assertEqual(len(self.student_repo), 0)


    def test_modify_student_whitebox(self):
        self.service.add_student(3, "Ioana")

        updated = self.service.modify_student(3, "Ioana Popescu")

        # modificarea s-a facut in repository
        student_repo = self.student_repo.find(3)
        self.assertEqual(student_repo.get_nume(), "Ioana Popescu")

        # obiectul returnat este cel din repo
        self.assertEqual(updated, student_repo)

    def test_modify_nonexistent_student_raises_error_whitebox(self):
        self.assertRaises(
            ValueError,
            self.service.modify_student,
            10,
            "Test"
        )

        # white-box: repo ramane gol
        self.assertEqual(len(self.student_repo), 0)


    def test_find_students_by_name_whitebox(self):
        self.service.add_student(1, "Ana Popescu")
        self.service.add_student(2, "Mihai Ionescu")
        self.service.add_student(3, "Ana Maria")

        rezultat = self.service.find_students_by_name("Ana")

        # rezultatul este corect
        self.assertEqual(len(rezultat), 2)

        # white-box: stim exact ce studenti sunt in repo
        nume_rezultat = [s.get_nume() for s in rezultat]
        self.assertIn("Ana Popescu", nume_rezultat)
        self.assertIn("Ana Maria", nume_rezultat)


    def test_get_all_students_whitebox(self):
        self.service.add_student(1, "Ana")
        self.service.add_student(2, "Mihai")

        studenti = self.service.get_all_students()

        # white-box: get_all_students este delegare directa catre repo
        self.assertEqual(len(studenti), len(self.student_repo))


import unittest
from Domain.disciplina import Disciplina
from Domain.validator import DisciplinaValidator
from Services.servicediscipline import DisciplinaService
from Repos.repodisciplina import DisciplinaRepository
from Repos.reponotare import NotaRepository
from Domain.notare import Nota


class TestDisciplinaServiceWhiteBox(unittest.TestCase):

    def setUp(self):
        # white-box: avem acces direct la dependintele interne
        self.disciplina_repo = DisciplinaRepository()
        self.nota_repo = NotaRepository()
        self.validator = DisciplinaValidator()

        self.service = DisciplinaService(
            self.disciplina_repo,
            self.validator,
            self.nota_repo
        )

    def test_add_disciplina_whitebox(self):
        disciplina = self.service.add_disciplina(1, "Matematica", "Popescu Ion")

        self.assertEqual(len(self.disciplina_repo), 1)
        self.assertEqual(self.disciplina_repo.find(1), disciplina)
        self.assertEqual(disciplina.get_nume(), "Matematica")
        self.assertEqual(disciplina.get_profesor(), "Popescu Ion")

    def test_add_duplicate_disciplina_raises_error_whitebox(self):
        self.service.add_disciplina(1, "Matematica", "Popescu Ion")

        self.assertRaises(
            ValueError,
            self.service.add_disciplina,
            1,
            "Algebra",
            "Alt Profesor"
        )

        # white-box: repo NU s-a modificat
        self.assertEqual(len(self.disciplina_repo), 1)

    def test_delete_disciplina_whitebox(self):
        self.service.add_disciplina(2, "Informatica", "Ionescu Maria")

        # adaugam note ca sa verificam efectul intern
        self.nota_repo.add_nota(Nota(1, 2, 9))
        self.nota_repo.add_nota(Nota(2, 2, 8))

        deleted = self.service.delete_disciplina(2)

        self.assertEqual(len(self.disciplina_repo), 0)
        self.assertEqual(deleted.get_disciplina_id(), 2)
        self.assertEqual(len(self.nota_repo), 0)

    def test_delete_nonexistent_disciplina_raises_error_whitebox(self):
        self.assertRaises(
            ValueError,
            self.service.delete_disciplina,
            99
        )

        # white-box: repo ramane gol
        self.assertEqual(len(self.disciplina_repo), 0)


    def test_modify_disciplina_whitebox(self):
        self.service.add_disciplina(3, "Fizica", "Popescu Ion")

        updated = self.service.modify_disciplina(
            3,
            "Fizica Moderna",
            "Popescu Ion"
        )

        # modificarea s-a facut in repository
        disciplina_repo = self.disciplina_repo.find(3)
        self.assertEqual(disciplina_repo.get_nume(), "Fizica Moderna")

        # obiectul returnat este cel din repo
        self.assertEqual(updated, disciplina_repo)

    def test_modify_nonexistent_disciplina_raises_error_whitebox(self):
        self.assertRaises(
            ValueError,
            self.service.modify_disciplina,
            10,
            "Test",
            "Test"
        )

        # white-box: repo ramane gol
        self.assertEqual(len(self.disciplina_repo), 0)


    def test_find_discipline_by_profesor_whitebox(self):
        self.service.add_disciplina(1, "Matematica", "Popescu Ion")
        self.service.add_disciplina(2, "Fizica", "Popescu Ion")
        self.service.add_disciplina(3, "Informatica", "Ionescu Maria")

        rezultat = self.service.find_discipline_by_profesor("Popescu")

        #  rezultatul este corect
        self.assertEqual(len(rezultat), 2)

        #  white-box: stim exact ce discipline sunt in repo
        nume_discipline = [d.get_nume() for d in rezultat]
        self.assertIn("Matematica", nume_discipline)
        self.assertIn("Fizica", nume_discipline)

    def test_get_all_discipline_whitebox(self):
        self.service.add_disciplina(1, "Matematica", "Popescu Ion")
        self.service.add_disciplina(2, "Informatica", "Ionescu Maria")

        discipline = self.service.get_all_discipline()

        # white-box: delegare directa catre repository
        self.assertEqual(len(discipline), len(self.disciplina_repo))

import unittest
from Domain.notare import Nota
from Domain.student import Student
from Domain.disciplina import Disciplina
from Domain.validator import NotaValidator
from Services.servicenotare import NotaService
from Repos.reponotare import NotaRepository
from Repos.repostudent import StudentRepository
from Repos.repodisciplina import DisciplinaRepository


class TestNotaServiceBlackBox(unittest.TestCase):

    def setUp(self):
        self.nota_repo = NotaRepository()
        self.student_repo = StudentRepository()
        self.disciplina_repo = DisciplinaRepository()
        self.validator = NotaValidator()

        self.service = NotaService(
            self.nota_repo,
            self.student_repo,
            self.disciplina_repo,
            self.validator
        )

        # date initiale (prin repo, NU verificate intern)
        self.student_repo.add(Student(1, "Ana"))
        self.student_repo.add(Student(2, "Mihai"))

        self.disciplina_repo.add(Disciplina(1, "Matematica", "Popescu Ion"))
        self.disciplina_repo.add(Disciplina(2, "Informatica", "Ionescu Maria"))



    def test_add_nota_blackbox(self):
        nota = self.service.add_nota(1, 1, 9)

        self.assertEqual(nota.get_student_id(), 1)
        self.assertEqual(nota.get_disciplina_id(), 1)
        self.assertEqual(nota.get_valoare(), 9)

        # verificam DOAR prin interfata publica
        self.assertEqual(len(self.service.get_all_note()), 1)

    def test_add_nota_student_inexistent_raises_error(self):
        self.assertRaises(
            ValueError,
            self.service.add_nota,
            99,
            1,
            8
        )

    def test_add_nota_disciplina_inexistenta_raises_error(self):
        self.assertRaises(
            ValueError,
            self.service.add_nota,
            1,
            99,
            8
        )

    def test_add_duplicate_nota_raises_error(self):
        self.service.add_nota(1, 1, 9)

        self.assertRaises(
            ValueError,
            self.service.add_nota,
            1,
            1,
            10
        )



    def test_statistica_note_la_disciplina_blackbox(self):
        self.service.add_nota(1, 1, 9)
        self.service.add_nota(2, 1, 7)

        rezultat = self.service.statistica_note_la_disciplina(1)

        self.assertEqual(len(rezultat), 2)
        self.assertEqual(rezultat[0][1], 9)  # nota cea mai mare prima

    def test_statistica_note_la_disciplina_inexistenta(self):
        self.assertRaises(
            ValueError,
            self.service.statistica_note_la_disciplina,
            99
        )


    def test_statistica_top_studenti_medii_blackbox(self):
        self.service.add_nota(1, 1, 10)
        self.service.add_nota(1, 2, 9)
        self.service.add_nota(2, 1, 6)

        rezultat = self.service.statistica_top_studenti_medii()

        self.assertEqual(len(rezultat), 1)   # top 20% => cel putin 1
        self.assertEqual(rezultat[0][0], "Ana")

    def test_statistica_top_studenti_fara_note(self):
        rezultat = self.service.statistica_top_studenti_medii()
        self.assertEqual(rezultat, [])

    def test_statistica_medii_disciplina_crescator_blackbox(self):
        self.service.add_nota(1, 1, 10)
        self.service.add_nota(1, 2, 8)  # ✔ altă disciplină
        self.service.add_nota(2, 1, 6)

        rezultat = self.service.statistica_medii_disciplina_crescator(1)

        self.assertEqual(len(rezultat), 2)
        self.assertLessEqual(rezultat[0][1], rezultat[1][1])

    def test_statistica_medii_disciplina_fara_note(self):
        rezultat = self.service.statistica_medii_disciplina_crescator(1)
        self.assertEqual(rezultat, [])


    def test_get_note_student_blackbox(self):
        self.service.add_nota(1, 1, 9)
        self.service.add_nota(1, 2, 10)

        note = self.service.get_note_student(1)

        self.assertEqual(len(note), 2)

    def test_get_note_disciplina_blackbox(self):
        self.service.add_nota(1, 1, 9)
        self.service.add_nota(2, 1, 7)

        note = self.service.get_note_disciplina(1)

        self.assertEqual(len(note), 2)

    def test_get_all_note_blackbox(self):
        self.service.add_nota(1, 1, 9)

        self.assertEqual(len(self.service.get_all_note()), 1)
