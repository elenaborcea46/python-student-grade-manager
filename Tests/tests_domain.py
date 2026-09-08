

import unittest
from Domain.student import Student


class TestStudentWhiteBox(unittest.TestCase):

    def test_getters(self):
        s = Student(1, "Ana")

        # white-box: verificăm starea internă prin getters
        self.assertEqual(s.get_student_id(), 1)
        self.assertEqual(s.get_nume(), "Ana")

    def test_set_id(self):
        s = Student(1, "Ana")
        s.set_id(10)

        # white-box: știm că __student_id se modifică
        self.assertEqual(s.get_student_id(), 10)

    def test_set_nume(self):
        s = Student(1, "Ana")
        s.set_nume("Maria")

        # white-box: știm că __nume se modifică
        self.assertEqual(s.get_nume(), "Maria")

    def test_eq(self):
        s1 = Student(1, "Ana")
        s2 = Student(1, "Maria")  # nume diferit

        # white-box: știm că __eq__ compară doar ID-ul
        self.assertEqual(s1, s2)

        s1 = Student(1, "Ana")
        s2 = Student(2, "Ana")

        self.assertNotEqual(s1, s2)

        s = Student(1, "Ana")
        self.assertNotEqual(s, "nu e student")


    def test_str_format(self):
        s = Student(3, "Ioana")

        # white-box: știm formatul exact al stringului
        self.assertEqual(str(s), "ID: 3, Nume: Ioana")


from Domain.disciplina import Disciplina

class TestDisciplinaWhiteBox(unittest.TestCase):

    def test_getters_disciplina(self):
        d = Disciplina(1, "Matematica", "Popescu Ion")

        # white-box: verificăm starea internă prin getters
        self.assertEqual(d.get_disciplina_id(), 1)
        self.assertEqual(d.get_nume(), "Matematica")
        self.assertEqual(d.get_profesor(), "Popescu Ion")

    def test_set_disciplina_id(self):
        d = Disciplina(1, "Matematica", "Popescu Ion")
        d.set_disciplina_id(10)

        # white-box: știm că __disciplina_id se modifică
        self.assertEqual(d.get_disciplina_id(), 10)

    def test_set_nume(self):
        d = Disciplina(1, "Matematica", "Popescu Ion")
        d.set_nume("Algebra")

        # white-box: știm că __nume se modifică
        self.assertEqual(d.get_nume(), "Algebra")

    def test_set_profesor(self):
        d = Disciplina(1, "Matematica", "Popescu Ion")
        d.set_profesor("Ionescu Maria")

        # white-box: știm că __profesor se modifică
        self.assertEqual(d.get_profesor(), "Ionescu Maria")

    def test_eq_compares_only_id(self):
        d1 = Disciplina(1, "Matematica", "Popescu Ion")
        d2 = Disciplina(1, "Algebra", "Alt Profesor")

        # white-box: știm că __eq__ compară doar ID-ul
        self.assertEqual(d1, d2)

    def test_eq_different_ids(self):
        d1 = Disciplina(1, "Matematica", "Popescu Ion")
        d2 = Disciplina(2, "Matematica", "Popescu Ion")

        self.assertNotEqual(d1, d2)

    def test_eq_with_non_disciplina(self):
        d = Disciplina(1, "Matematica", "Popescu Ion")

        self.assertNotEqual(d, "nu e disciplina")

    def test_str_format(self):
        d = Disciplina(3, "Informatica", "Ionescu Maria")

        # white-box: verificăm formatul exact
        self.assertEqual(
            str(d),
            "ID: 3, Nume: Informatica, Profesor: Ionescu Maria"
        )



from Domain.notare import Nota

class TestNotaWhiteBox(unittest.TestCase):

    def test_constructor_sets_fields(self):
        n = Nota(1, 2, 9)

        # white-box: verificăm starea internă prin getters
        self.assertEqual(n.get_student_id(), 1)
        self.assertEqual(n.get_disciplina_id(), 2)
        self.assertEqual(n.get_valoare(), 9)

    def test_set_valoare_modifies_internal_state(self):
        n = Nota(1, 2, 9)
        n.set_valoare(10)

        # white-box: știm că __valoare se modifică
        self.assertEqual(n.get_valoare(), 10)

    def test_eq_same_student_and_disciplina(self):
        n1 = Nota(1, 2, 9)
        n2 = Nota(1, 2, 5)  # valoare diferită

        # white-box: __eq__ ignoră valoarea, compară doar student + disciplină
        self.assertEqual(n1, n2)

    def test_eq_different_student(self):
        n1 = Nota(1, 2, 9)
        n2 = Nota(2, 2, 9)

        self.assertNotEqual(n1, n2)

    def test_eq_different_disciplina(self):
        n1 = Nota(1, 2, 9)
        n2 = Nota(1, 3, 9)

        self.assertNotEqual(n1, n2)

    def test_eq_with_non_nota(self):
        n = Nota(1, 2, 9)

        self.assertNotEqual(n, "nu e nota")

    def test_str_format(self):
        n = Nota(3, 4, 8)

        # white-box: verificăm formatul exact al stringului
        self.assertEqual(
            str(n),
            "Student ID: 3, Disciplina ID: 4, Nota: 8"
        )


