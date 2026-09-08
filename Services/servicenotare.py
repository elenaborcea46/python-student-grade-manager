from Domain.validator import NotaValidator
from Domain.notare import Nota

from Utils.utils_sort import generic_sort

class NotaService:
    def __init__(self, nota_repo, student_repo, disciplina_repo, nota_validator: NotaValidator):
        self.__nota_repo = nota_repo
        self.__student_repo = student_repo
        self.__disciplina_repo = disciplina_repo
        self.__validator = nota_validator

    def add_nota(self, student_id, disciplina_id, valoare):
        """
            Atribuie și salvează o notă unui student la o anumită disciplină.

            :param student_id: ID-ul studentului căruia i se atribuie nota
            :param disciplina_id: ID-ul disciplinei la care se acordă nota
            :param valoare: valoarea numerică a notei
            :return: obiectul Nota creat
            :raises ValueError: dacă studentul sau disciplina nu există
                                sau dacă nota nu este validă
        """
        student = self.__student_repo.find(student_id)
        if student is None:
            raise ValueError(f"Nu există student cu ID-ul {student_id}")


        disciplina = self.__disciplina_repo.find(disciplina_id)
        if disciplina is None:
            raise ValueError(f"Nu există disciplină cu ID-ul {disciplina_id}")


        nota = Nota(student_id, disciplina_id, valoare)
        self.__validator.validate(nota)


        self.__nota_repo.add_nota(nota)
        return nota

    def statistica_note_la_disciplina(self, disciplina_id):
        """
        Returnează lista de tuple (nume_student, nota) pentru
        o disciplină dată, ordonată:
           1. descrescător după nota
           2. alfabetic după nume
        :param disciplina_id: ID-ul disciplinei
        :return: Returneaza lista de studenți și notele lor la o disciplină dată, ordonat: alfabetic după nume, după notă
        """

        disciplina = self.__disciplina_repo.find(disciplina_id)
        if disciplina is None:
            raise ValueError(f"Nu există disciplină cu ID-ul {disciplina_id}")

        rezultate = []

        for nota in self.__nota_repo.get_all():
            if nota.get_disciplina_id() == disciplina_id:
                student = self.__student_repo.find(nota.get_student_id())
                rezultate.append((student.get_nume(), nota.get_valoare()))

        # ordonare: întâi alfabetic, apoi după nota descrescător
        rezultate = generic_sort(rezultate, key=lambda x: x[1], reverse=True, method = "bubble")
        rezultate = generic_sort(rezultate, key=lambda x: x[0].lower(), reverse=False, method="bubble")

        return rezultate



    def statistica_top_studenti_medii(self):
        """
        Creeaza o lista cu primii 20% din studenți ordonata dupa media notelor la toate disciplinele (nume și notă)
        :return: Returneaza lista
        """

        toate_notele = self.__nota_repo.get_all()
        studenti = self.__student_repo.get_all()

        if not studenti:
            return []

        # student_id -> listă de note
        map_note = {}
        for n in toate_notele:
            map_note.setdefault(n.get_student_id(), []).append(n.get_valoare())

        rezultate = []

        for student in studenti:
            sid = student.get_student_id()
            if sid not in map_note:
                continue

            medie = sum(map_note[sid]) / len(map_note[sid])
            rezultate.append((student.get_nume(), medie))

        # sortare descrescător după medie
        rezultate = generic_sort(rezultate, key=lambda x: x[1], reverse=True, method = "shell")

        if not rezultate:
            return []

        # top 20%
        k = max(1, len(rezultate) * 20 // 100)

        return rezultate[:k]

    def statistica_medii_disciplina_crescator(self, disciplina_id):
        """
        Creeaza o lista de tupluri cu toti studentii care au note la disciplina data, ordonati crescator dupa medie.
        :param disciplina_id: ID-ul disciplinei
        :return: Returneaza lista de tuple (nume_student, medie) pentru toti studentii
        care au note la disciplina data, ordonati crescator dupa medie.
        """
        # obținem toate notele
        toate_notele = self.__nota_repo.get_all()

        # filtrăm notele pentru disciplina cerută
        note_filtrate = [n for n in toate_notele if n.get_disciplina_id() == disciplina_id]

        if not note_filtrate:
            return []  # nu există note pentru disciplina respectivă

        # grupăm notele după student_id: map student_id -> [note...]
        note_pe_student = {}
        for n in note_filtrate:
            sid = n.get_student_id()
            note_pe_student.setdefault(sid, []).append(n.get_valoare())

        # calculăm media pentru fiecare student și obținem numele studentului din repo
        rezultate = []
        for sid, lista_note in note_pe_student.items():
            student = self.__student_repo.find(sid)
            # dacă nu găsim studentul (sau a fost șters), îl sărim
            if student is None:
                continue
            medie = sum(lista_note) / len(lista_note)
            rezultate.append((student.get_nume(), medie))

        # sortăm crescător după medie
        rezultate = generic_sort(rezultate, key=lambda x: x[1], reverse=False, method = "shell")

        return rezultate



    #Lab12
    def note_sortate_dupa_nume_si_nota_la_disciplina(self, disciplina_id):
            """
            Construiește lista de note pentru disciplina dată și o sortează:
                - crescător după numele studentului
                - pentru nume egale, descrescător după valoarea notei
            :param disciplina_id:id-ul disciplinei
            :return: lista de note sortata
            """

            # verificăm disciplina
            disciplina = self.__disciplina_repo.find(disciplina_id)
            if disciplina is None:
                raise ValueError(f"Nu există disciplină cu ID-ul {disciplina_id}")

            # construim lista de obiecte Nota pentru disciplina dată
            note = []
            for nota in self.__nota_repo.get_all():
                if nota.get_disciplina_id() == disciplina_id:
                    note.append(nota)

            if not note:
                return []

            # sortare secundară: după valoarea notei (descrescător)

            note = generic_sort(note,key= lambda n: (-n.get_valoare(),self.__student_repo.find(n.get_student_id()).get_nume()),method="bubble")
            # sortare principală: după numele studentului (alfabetic)


            # transformăm pentru afișare
            rezultat = []
            for nota in note:
                student = self.__student_repo.find(nota.get_student_id())
                rezultat.append((student.get_nume(), nota.get_valoare()))

            return rezultat

    def get_note_student(self, student_id):
        return [n for n in self.__nota_repo.get_all() if n.get_student_id() == student_id]

    def get_note_student_recursiv(self, student_id, note=None, index=0):
        if note is None:
            note = self.__nota_repo.get_all()

        if index == len(note):
            return []

        rest = self.get_note_student_recursiv(student_id, note, index + 1)

        if note[index].get_student_id() == student_id:
            return [note[index]] + rest
        return rest

    def get_note_disciplina(self, disciplina_id):
        return [n for n in self.__nota_repo.get_all() if n.get_disciplina_id() == disciplina_id]

    def get_all_note(self):
        return self.__nota_repo.get_all()
