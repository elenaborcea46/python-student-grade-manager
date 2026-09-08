

def ui_add_disciplina(disciplina_srv):
    try:
        disciplina_id = int(input("Introduceți ID-ul disciplinei: "))
        nume = input("Introduceți numele disciplinei: ")
        profesor = input("Introduceți profesorul: ")
        d = disciplina_srv.add_disciplina(disciplina_id, nume, profesor)
        print(f"Disciplină adăugată: {d}")
    except Exception as e:
        print("Eroare:", e)

def ui_modify_disciplina(disciplina_srv):
    try:
        disciplina_id = int(input("Introduceți ID-ul disciplinei de modificat: "))
        nume = input("Introduceți noul nume: ")
        profesor = input("Introduceți noul profesor: ")
        d = disciplina_srv.modify_disciplina(disciplina_id, nume, profesor)
        print(f"Disciplină modificată: {d}")
    except Exception as e:
        print("Eroare:", e)

def ui_delete_disciplina(disciplina_srv):
    try:
        disciplina_id = int(input("Introduceți ID-ul disciplinei de șters: "))
        d = disciplina_srv.delete_disciplina(disciplina_id)
        print(f"Disciplină ștearsă: {d}")
    except Exception as e:
        print("Eroare:", e)

def ui_list_discipline(disciplina_srv):
    discipline = disciplina_srv.get_all_discipline()
    if discipline:
        for d in discipline:
            print(d)
    else:
        print("Nu există discipline.")

def ui_find_discipline_by_profesor(disciplina_srv):
    profesor = input("Introduceți profesorul căutat: ")
    gasite = disciplina_srv.find_discipline_by_profesor(profesor)
    if gasite:
        for d in gasite:
            print(d)
    else:
        print("Nicio disciplină găsită.")
