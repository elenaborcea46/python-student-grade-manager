

class StudentValidator:
    def validate(self, student):
        errors = []

        if student.get_student_id() <= 0:
            errors.append("ID-ul studentului trebuie să fie un număr pozitiv!")
        if student.get_nume() == "":
            errors.append("Numele studentului nu poate fi vid!")

        if len(errors) > 0:
            raise ValueError('\n'.join(errors))


class DisciplinaValidator:
    def validate(self, disciplina):
        errors = []

        if disciplina.get_disciplina_id() <= 0:
            errors.append("ID-ul disciplinei trebuie să fie un număr pozitiv!")
        if disciplina.get_nume() == "":
            errors.append("Numele disciplinei nu poate fi vid!")
        if disciplina.get_profesor() == "":
            errors.append("Numele profesorului nu poate fi vid!")

        if len(errors) > 0:
            raise ValueError('\n'.join(errors))


class NotaValidator:
    def validate(self, nota):
        errors = []
        if nota.get_valoare() < 1 or nota.get_valoare() > 10:
            errors.append("Nota trebuie să fie între 1 și 10!")
        if len(errors) > 0:
            raise ValueError('\n'.join(errors))
