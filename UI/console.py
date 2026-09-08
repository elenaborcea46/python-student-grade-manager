
from Services.servicestudenti import StudentService
from Services.servicediscipline import DisciplinaService
from Services.servicenotare import NotaService

from Repos.repostudent import StudentRepository,StudentFileRepository
from Repos.repodisciplina import DisciplinaRepository,DisciplinaFileRepository
from Repos.reponotare import NotaRepository,NotaFileRepository

from Domain.validator import StudentValidator, DisciplinaValidator, NotaValidator

from UI.ui_student import *
from UI.ui_disciplina import *
from UI.ui_nota import *


def print_menu():
    print("\n=== MENIU PRINCIPAL ===")
    print("1. Adaugă student")
    print("2. Modifică student")
    print("3. Șterge student")
    print("4. Listează studenți")
    print("5. Caută student după nume")
    print("6. Adaugă disciplină")
    print("7. Modifică disciplină")
    print("8. Șterge disciplină")
    print("9. Listează discipline")
    print("10. Caută disciplină după profesor")
    print("11. Adaugă notă")
    print("12. Listează note student")
    print("13. Listează note disciplină")
    print("14. Generare random studenti")
    print("15. Lista de studenți și notele lor la o disciplină dată, ordonat: alfabetic după nume, după notă")
    print("16. Primii 20% din studenți ordonat dupa media notelor la toate disciplinele (nume și notă)")
    print("17. Lista de studenti si notele lor la o disciplina data,ordonat: dupa media de la disciplina,crescator")
    print("18. Lista de note sortate după nume și valoarea notei (pentru o disciplină)")
    print("0. Ieșire")


def run():

    student_repo = StudentFileRepository("data/studenti.txt")
    disciplina_repo = DisciplinaFileRepository("data/discipline.txt")
    nota_repo = NotaFileRepository("data/note.txt")


    student_validator = StudentValidator()
    disciplina_validator = DisciplinaValidator()
    nota_validator = NotaValidator()


    student_srv = StudentService(student_repo, student_validator, nota_repo)
    disciplina_srv = DisciplinaService(disciplina_repo, disciplina_validator, nota_repo)
    nota_srv = NotaService(nota_repo, student_repo, disciplina_repo, nota_validator)

    while True:
        print_menu()
        cmd = input(">>> ")

        if cmd == "1":
            ui_add_student(student_srv)
        elif cmd == "2":
            ui_modify_student(student_srv)
        elif cmd == "3":
            ui_delete_student(student_srv)
        elif cmd == "4":
            ui_list_students(student_srv)
        elif cmd == "5":
            ui_find_students_by_name(student_srv)

        elif cmd == "6":
            ui_add_disciplina(disciplina_srv)
        elif cmd == "7":
            ui_modify_disciplina(disciplina_srv)
        elif cmd == "8":
            ui_delete_disciplina(disciplina_srv)
        elif cmd == "9":
            ui_list_discipline(disciplina_srv)
        elif cmd == "10":
            ui_find_discipline_by_profesor(disciplina_srv)
        elif cmd == "11":
            ui_add_nota(nota_srv)
        elif cmd == "12":
            ui_list_note_student(nota_srv)
        elif cmd == "13":
            ui_list_note_disciplina(nota_srv)
        elif cmd == "14":
            ui_generare_random_studenti(student_srv)
        elif cmd == "15":
            ui_statistica_note_la_disciplina(nota_srv)
        elif cmd == "16":
            ui_statistica_top_studenti_medii(nota_srv)
        elif cmd == "17":
            ui_statistica_medii_disciplina_crescator(nota_srv)
        elif cmd == "18":
            ui_note_sortate_dupa_nume_si_nota(nota_srv)
        elif cmd == "0":
            break

        else:
            print("Comandă invalidă!")

