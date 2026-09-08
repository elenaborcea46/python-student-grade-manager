from Domain.disciplina import Disciplina
from Domain.validator import DisciplinaValidator
from Repos.repodisciplina import DisciplinaRepository,DisciplinaFileRepository
from Repos.reponotare import NotaRepository


class DisciplinaService:
    def __init__(self, repo, validator: DisciplinaValidator, nota_repo: NotaRepository):
        self.__repo = repo
        self.__validator = validator
        self.__nota_repo = nota_repo

    def add_disciplina(self, disciplina_id, nume, profesor):
        disciplina = Disciplina(disciplina_id, nume, profesor)
        self.__validator.validate(disciplina)
        self.__repo.add(disciplina)
        return disciplina

    def get_all_discipline(self):
        return self.__repo.get_all()

    def delete_disciplina(self, disciplina_id):
        disciplina_stearsa = self.__repo.remove(disciplina_id)  # Ridică ValueError
        self.__nota_repo.delete_by_disciplina_id(disciplina_id)
        return disciplina_stearsa

    def modify_disciplina(self, disciplina_id, new_nume, new_profesor):
        temp_disciplina = Disciplina(disciplina_id, new_nume, new_profesor)
        self.__validator.validate(temp_disciplina)  # Ridică ValueError

        disciplina = self.__repo.find(disciplina_id)
        if disciplina is None:
            raise ValueError(f"Nu există disciplină cu ID-ul {disciplina_id} pentru a fi modificată!")

        disciplina.set_nume(new_nume)
        disciplina.set_profesor(new_profesor)

        self.__repo.update(disciplina)  # Ridică ValueError
        return disciplina

    def find_discipline_by_profesor(self, profesor_cautat):
        """
        Caută discipline a căror profesor conține textul dat
        Folosește buclă for normală
        """
        rezultat = []
        for disciplina in self.__repo.get_all():
            if profesor_cautat.lower() in disciplina.get_profesor().lower():
                rezultat.append(disciplina)
        return rezultat


