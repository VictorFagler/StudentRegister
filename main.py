
print("1. Lägg till student")
print("2. Lista alla studenter")
print("3. Sök student")
print("4. Ta bort student")
print("4. Beräkna snittåldern")
print("5. Avsluta")

GREEN = "\033[92m"
RESET = "\033[0m"

menu_active = True
students = [{"name":"Victor","age": 31}, {"name":"Kalle", "age": 35}]

while menu_active:
    user_choice = input("> Välj menyval 1-4: ")

    if user_choice == "1":
        print("\n > Lägg till student")
        name = input("Ange studentens namn: ")
        age = int(input("Ange ålder: "))
        students.append({"name": name, "age": age})
        print(f"{GREEN}{name, age}{RESET} har lagts till i listan.")

    elif user_choice == "2":
        print("\n > Listing all students")
        if students:
            for stud in students:
                print(f"- {stud['name']}, {stud['age']}")
        else:
            print("No students registered")
    
    elif user_choice == "3":
        search_name = input("Studentens namn: ").lower()
        found = False
        for stud in students:
         if stud["name"].lower() == search_name:
             print(f"- {stud['name']}, {stud['age']} år")
             found = True

        if not found:
            print("Studenten hittades inte.")

    elif user_choice == "4":
        name_to_delete = input("Ta bort student:")
        found = False

        for student in students:
            if student["name"].lower() == name_to_delete.lower():
                students.remove(student)
                print(f"{student['name']} har tagits bort.")
                found = True
                break
            if not found:
                print("Studenten hittades inte")

    elif user_choice == "5":
        print("> Beräkna snittålder")
        if students:
            total_age = 0
            for stud in students:
                total_age += stud["age"]
            average_age = total_age / len(students)
            print(f"Beräknad snittålder: {round(average_age)} år (Antal elever: {len(students)})")

        else:
            print("Inga studenter registrerade")

    elif user_choice == "6":
        print("\n > Programmet avslutas")
        menu_active = False

    else:
        print("Ogiltigt val")

