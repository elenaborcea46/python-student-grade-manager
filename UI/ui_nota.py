

def ui_add_nota(nota_srv):
    try:
        student_id = int(input("Introduceți ID-ul studentului: "))
        disciplina_id = int(input("Introduceți ID-ul disciplinei: "))
        valoare = float(input("Introduceți valoarea notei: "))
        n = nota_srv.add_nota(student_id, disciplina_id, valoare)
        print(f"Notă adăugată: {n}")
    except Exception as e:
        print("Eroare:", e)

def ui_list_note_student(nota_srv):
    student_id = int(input("Introduceți ID-ul studentului: "))
    note = nota_srv.get_note_student(student_id)
    if note:
        for n in note:
            print(n)
    else:
        print("Studentul nu are note.")

def ui_list_note_disciplina(nota_srv):
    disciplina_id = int(input("Introduceți ID-ul disciplinei: "))
    note = nota_srv.get_note_disciplina(disciplina_id)
    if note:
        for n in note:
            print(n)
    else:
        print("Nu există note pentru această disciplină.")


def ui_statistica_note_la_disciplina(nota_srv):
    try:
        disciplina_id = int(input("Introdu ID disciplina: "))
        rezultate = nota_srv.statistica_note_la_disciplina(disciplina_id)

        if not rezultate:
            print("Nu exista note la aceasta disciplina.")
            return

        print("\nStudenti + note la disciplina:")
        for nume, nota in rezultate:
            print(f"{nume} -> {nota}")

    except ValueError as ve:
        print("Eroare:", ve)

def ui_statistica_top_studenti_medii(nota_srv):
    top_studenti = nota_srv.statistica_top_studenti_medii()

    if not top_studenti:
        print("Nu exista studenti cu note.")
        return

    print("\nTop 20% studenti dupa medie:")
    for nume, medie in top_studenti:
        print(f"{nume} -> {medie:.2f}")

def ui_statistica_medii_disciplina_crescator(nota_srv):
    try:
        disciplina_id = int(input("Introdu ID disciplina: "))
        rezultate = nota_srv.statistica_medii_disciplina_crescator(disciplina_id)

        if not rezultate:
            print("Nu exista note la aceasta disciplina.")
            return

        print("\nStudenti ordonati crescator dupa media la disciplina:")
        for nume, medie in rezultate:
            print(f"{nume} -> {medie:.2f}")

    except ValueError as ve:
        print("Eroare:", ve)


def ui_note_sortate_dupa_nume_si_nota(nota_srv):
    try:
        disciplina_id = int(input("Introduceți ID-ul disciplinei: "))

        rezultate = nota_srv.note_sortate_dupa_nume_si_nota_la_disciplina(disciplina_id)

        if not rezultate:
            print("Nu există note pentru această disciplină.")
            return

        print("\nNote sortate după nume și notă:")
        for nume, valoare in rezultate:
            print(f"{nume} - {valoare}")

    except ValueError as ve:
        print("Eroare:", ve)

