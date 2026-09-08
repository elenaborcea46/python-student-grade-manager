

def ui_add_student(student_srv):
    try:
        student_id = int(input("Introduceți ID-ul studentului: "))
        nume = input("Introduceți numele studentului: ")
        student = student_srv.add_student(student_id, nume)
        print(f"Student adăugat: {student}")
    except Exception as e:
        print("Eroare:", e)

def ui_modify_student(student_srv):
    try:
        student_id = int(input("Introduceți ID-ul studentului de modificat: "))
        nume = input("Introduceți noul nume: ")
        student = student_srv.modify_student(student_id, nume)
        print(f"Student modificat: {student}")
    except Exception as e:
        print("Eroare:", e)

def ui_delete_student(student_srv):
    try:
        student_id = int(input("Introduceți ID-ul studentului de șters: "))
        student = student_srv.delete_student(student_id)
        print(f"Student șters: {student}")
    except Exception as e:
        print("Eroare:", e)

def ui_list_students(student_srv):
    studenti = student_srv.get_all_students()
    if studenti:
        for s in studenti:
            print(s)
    else:
        print("Nu există studenți.")

def ui_find_students_by_name(student_srv):
    nume = input("Introduceți numele căutat: ")
    gasiti = student_srv.find_students_by_name(nume)
    if gasiti:
        for s in gasiti:
            print(s)
    else:
        print("Niciun student găsit.")

def ui_generare_random_studenti(student_srv):
    try:
        n = int(input("Câți studenți random doriți să generați? "))
        lista = student_srv.generare_random_studenti(n)
        print(f"{n} studenți generați:")
        for s in lista:
            print(s)
    except Exception as e:
        print("Eroare:", e)
