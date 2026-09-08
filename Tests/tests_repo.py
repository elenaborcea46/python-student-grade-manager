

import unittest
from Domain.student import Student
from Repos.repostudent import StudentRepository


class TestStudentRepositoryWhiteBox(unittest.TestCase):

    def setUp(self):
        self.repo = StudentRepository()

    def test_add_student(self):
        s = Student(1, "Ana")
        self.repo.add(s)

        self.assertEqual(len(self.repo.get_all()), 1)
        self.assertEqual(self.repo.find(1), s)

    def test_add_duplicate_student_raises_error(self):
        s = Student(1, "Ana")
        self.repo.add(s)

        self.assertRaises(
            ValueError,
            self.repo.add,
            Student(1, "Maria")
        )

    def test_remove_student(self):
        s = Student(2, "Mihai")
        self.repo.add(s)

        removed = self.repo.remove(2)

        self.assertEqual(removed, s)
        self.assertEqual(len(self.repo.get_all()), 0)
        self.assertIsNone(self.repo.find(2))

    def test_remove_nonexistent_student_raises_error(self):
        self.assertRaises(
            ValueError,
            self.repo.remove,
            99
        )

    def test_update_student(self):
        s = Student(3, "Ioana")
        self.repo.add(s)

        updated = Student(3, "Ioana Popescu")
        self.repo.update(updated)

        self.assertEqual(self.repo.find(3).get_nume(), "Ioana Popescu")

    def test_update_nonexistent_student_raises_error(self):
        self.assertRaises(
            ValueError,
            self.repo.update,
            Student(10, "Test")
        )

    def test_get_all(self):
        s1 = Student(1, "Ana")
        s2 = Student(2, "Mihai")

        self.repo.add(s1)
        self.repo.add(s2)

        all_students = self.repo.get_all()

        self.assertEqual(len(all_students), 2)
        self.assertIn(s1, all_students)
        self.assertIn(s2, all_students)

    def test_find_returns_none_if_not_found(self):
        self.assertIsNone(self.repo.find(123))


from Repos.repostudent import StudentFileRepository


class TestStudentFileRepositoryWhiteBox(unittest.TestCase):

    def setUp(self):
        # cream fisierul de test (white-box: controlam datele)
        self.filename = "test_studenti.txt"
        with open(self.filename, "w") as f:
            f.write("1,Ana\n2,Mihai\n")

        self.repo = StudentFileRepository(self.filename)

    def tearDown(self):
        # stergem fisierul de test (presupunem ca exista)
        f = open(self.filename, "w")
        f.close()

    def test_load_from_file(self):
        students = self.repo.get_all()

        self.assertEqual(len(students), 2)
        self.assertEqual(self.repo.find(1).get_nume(), "Ana")
        self.assertEqual(self.repo.find(2).get_nume(), "Mihai")

    def test_add_student_saves_to_file(self):
        s = Student(3, "Ioana")
        self.repo.add(s)

        with open(self.filename, "r") as f:
            lines = f.readlines()

        self.assertEqual(len(lines), 3)
        self.assertIn("3,Ioana\n", lines)

    def test_remove_student_updates_file(self):
        self.repo.remove(1)

        with open(self.filename, "r") as f:
            content = f.read()

        self.assertNotIn("1,Ana", content)
        self.assertEqual(len(self.repo), 1)

    def test_update_student_updates_file(self):
        s_updated = Student(2, "Mihai Popescu")
        self.repo.update(s_updated)

        with open(self.filename, "r") as f:
            content = f.read()

        self.assertIn("2,Mihai Popescu", content)



from Domain.disciplina import Disciplina
from Repos.repodisciplina import DisciplinaRepository


class TestDisciplinaRepositoryWhiteBox(unittest.TestCase):

    def setUp(self):
        self.repo = DisciplinaRepository()

    def test_add_disciplina(self):
        d = Disciplina(1, "Matematica", "Popescu Ion")
        self.repo.add(d)

        self.assertEqual(len(self.repo), 1)
        self.assertEqual(self.repo.find(1), d)

    def test_add_duplicate_disciplina_raises_error(self):
        d = Disciplina(1, "Matematica", "Popescu Ion")
        self.repo.add(d)

        self.assertRaises(
            ValueError,
            self.repo.add,
            Disciplina(1, "Algebra", "Alt Profesor")
        )

    def test_remove_disciplina(self):
        d = Disciplina(2, "Informatica", "Ionescu Maria")
        self.repo.add(d)

        removed = self.repo.remove(2)

        self.assertEqual(removed, d)
        self.assertEqual(len(self.repo), 0)
        self.assertIsNone(self.repo.find(2))

    def test_remove_nonexistent_disciplina_raises_error(self):
        self.assertRaises(
            ValueError,
            self.repo.remove,
            99
        )

    def test_update_disciplina(self):
        d = Disciplina(3, "Fizica", "Popescu Ion")
        self.repo.add(d)

        updated = Disciplina(3, "Fizica Moderna", "Popescu Ion")
        self.repo.update(updated)

        self.assertEqual(self.repo.find(3).get_nume(), "Fizica Moderna")

    def test_update_nonexistent_disciplina_raises_error(self):
        self.assertRaises(
            ValueError,
            self.repo.update,
            Disciplina(10, "Test", "Test")
        )

    def test_get_all(self):
        d1 = Disciplina(1, "Matematica", "Popescu Ion")
        d2 = Disciplina(2, "Informatica", "Ionescu Maria")

        self.repo.add(d1)
        self.repo.add(d2)

        all_disc = self.repo.get_all()

        self.assertEqual(len(all_disc), 2)
        self.assertIn(d1, all_disc)
        self.assertIn(d2, all_disc)

    def test_find_returns_none_if_not_found(self):
        self.assertIsNone(self.repo.find(123))



from Repos.repodisciplina import DisciplinaFileRepository


class TestDisciplinaFileRepositoryWhiteBox(unittest.TestCase):

    def setUp(self):
        self.filename = "test_discipline.txt"
        with open(self.filename, "w") as f:
            f.write("1,Matematica,Popescu Ion\n")
            f.write("2,Informatica,Ionescu Maria\n")

        self.repo = DisciplinaFileRepository(self.filename)

    def tearDown(self):
        # golim fisierul (presupunem ca exista)
        f = open(self.filename, "w")
        f.close()

    def test_load_from_file(self):
        self.assertEqual(len(self.repo), 2)
        self.assertEqual(self.repo.find(1).get_nume(), "Matematica")
        self.assertEqual(self.repo.find(2).get_profesor(), "Ionescu Maria")

    def test_add_disciplina_updates_file(self):
        d = Disciplina(3, "Fizica", "Georgescu Andrei")
        self.repo.add(d)

        with open(self.filename, "r") as f:
            content = f.read()

        self.assertIn("3,Fizica,Georgescu Andrei", content)

    def test_remove_disciplina_updates_file(self):
        self.repo.remove(1)

        with open(self.filename, "r") as f:
            content = f.read()

        self.assertNotIn("1,Matematica", content)
        self.assertEqual(len(self.repo), 1)

    def test_update_disciplina_updates_file(self):
        updated = Disciplina(2, "Informatica Aplicata", "Ionescu Maria")
        self.repo.update(updated)

        with open(self.filename, "r") as f:
            content = f.read()

        self.assertIn("2,Informatica Aplicata,Ionescu Maria", content)



from Domain.notare import Nota
from Repos.reponotare import NotaRepository


class TestNotaRepositoryWhiteBox(unittest.TestCase):

    def setUp(self):
        self.repo = NotaRepository()

    def test_add_nota(self):
        n = Nota(1, 2, 9)
        self.repo.add_nota(n)

        self.assertEqual(len(self.repo), 1)
        self.assertEqual(self.repo.find_note_by_student_and_disciplina(1, 2), n)

    def test_add_duplicate_nota_raises_error(self):
        n = Nota(1, 2, 9)
        self.repo.add_nota(n)

        self.assertRaises(
            ValueError,
            self.repo.add_nota,
            Nota(1, 2, 10)
        )

    def test_delete_by_student_id(self):
        n1 = Nota(1, 1, 9)
        n2 = Nota(1, 2, 8)
        n3 = Nota(2, 1, 7)

        self.repo.add_nota(n1)
        self.repo.add_nota(n2)
        self.repo.add_nota(n3)

        self.repo.delete_by_student_id(1)

        self.assertEqual(len(self.repo), 1)
        self.assertEqual(self.repo.find_note_by_student_and_disciplina(2, 1), n3)

    def test_delete_by_disciplina_id(self):
        n1 = Nota(1, 1, 9)
        n2 = Nota(2, 1, 8)
        n3 = Nota(1, 2, 7)

        self.repo.add_nota(n1)
        self.repo.add_nota(n2)
        self.repo.add_nota(n3)

        self.repo.delete_by_disciplina_id(1)

        self.assertEqual(len(self.repo), 1)
        self.assertEqual(self.repo.find_note_by_student_and_disciplina(1, 2), n3)

    def test_find_note_returns_none_if_not_found(self):
        self.assertIsNone(
            self.repo.find_note_by_student_and_disciplina(1, 1)
        )

    def test_get_all(self):
        n1 = Nota(1, 1, 9)
        n2 = Nota(2, 2, 8)

        self.repo.add_nota(n1)
        self.repo.add_nota(n2)

        all_notes = self.repo.get_all()

        self.assertEqual(len(all_notes), 2)
        self.assertIn(n1, all_notes)
        self.assertIn(n2, all_notes)


from Repos.reponotare import NotaFileRepository

class TestNotaFileRepositoryWhiteBox(unittest.TestCase):

    def setUp(self):
        self.filename = "test_note.txt"
        with open(self.filename, "w") as f:
            f.write("1,1,9\n")
            f.write("2,1,8\n")

        self.repo = NotaFileRepository(self.filename)

    def tearDown(self):
        # golim fisierul (stim ca exista)
        f = open(self.filename, "w")
        f.close()

    def test_load_from_file(self):
        self.assertEqual(len(self.repo), 2)
        self.assertEqual(
            self.repo.find_note_by_student_and_disciplina(1, 1).get_valoare(),
            9
        )

    def test_add_nota_updates_file(self):
        n = Nota(3, 2, 10)
        self.repo.add_nota(n)

        f = open(self.filename, "r")
        content = f.read()
        f.close()

        self.assertIn("3,2,10", content)

    def test_delete_by_student_id_updates_file(self):
        self.repo.delete_by_student_id(1)

        f = open(self.filename, "r")
        content = f.read()
        f.close()

        self.assertNotIn("1,1,9", content)
        self.assertEqual(len(self.repo), 1)

    def test_delete_by_disciplina_id_updates_file(self):
        self.repo.delete_by_disciplina_id(1)

        f = open(self.filename, "r")
        content = f.read()
        f.close()

        self.assertEqual(len(self.repo), 0)
