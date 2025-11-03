print(">>>>>>>>>>>>>>>STUDENT GRADE TRACKER<<<<<<<<<<<<<<")

students = ["John", "Jess", "Pedro", "Mike", "Red", "Bjorn", "Rosita", "Michelle", "Veronica"]
grades = [80, 93, 75, 82, 91, 86, 90, 85, 72]

while True:
    print("""\n\n===========================GRADE TRACKER MENU===========================
    
            1. Add Student & Grade
            2. Remove Student
            3. Show All Students
            4. Show Average Grade
            5. Search for Student
            6. Highest Honor Student
            7. Quit 
    """)

    try:
        select = int(input("\t\tSelect: "))

        # ADD STUDENT
        if select == 1:
            add_stu = input("\nEnter The Student Name: ").strip().title()
            add_grade = int(input(f"\nEnter {add_stu}'s Grade: "))
            students.append(add_stu)
            grades.append(add_grade)
            print(f"\n✅ {add_stu} successfully added with grade {add_grade}.")

        # REMOVE STUDENT
        elif select == 2:
            print(f'\n{"="*15} Student List {"="*15}\n')
            print(f'{"No.":<3} | {"Student":<15} | {"Grade"}')
            print('—' * 37)
            
            for i in range(len(students)):
                print(f'{i+1:<3} | {students[i]:<15} | {grades[i]} ')
            
            del_stu = input("\nType the name or number of the student you want to remove: ").strip()

            if del_stu.isdigit():
                index = int(del_stu)
                if 0 < index <= len(students):
                    rmv_name = students.pop(index - 1)
                    rmv_grade = grades.pop(index - 1)
                    print(f"✅ Removed '{rmv_name}' (Grade: {rmv_grade}).")
                else:
                    print("❌ Invalid number.")
            else:
                del_stu = del_stu.title()
                if del_stu in students:
                    index = students.index(del_stu)
                    rmv_name = students.pop(index)
                    rmv_grade = grades.pop(index)
                    print(f"✅ Removed '{rmv_name}' (Grade: {rmv_grade}).")
                else:
                    print(f"❌ No student named '{del_stu}' found.")

        # SHOW ALL
        elif select == 3:
            print(f'\n{"="*15} Student List {"="*15}\n')
            print(f'{"No.":<3} | {"Student":<15} | {"Grade"}')
            print('—' * 37)
            for i in range(len(students)):
                print(f'{i+1:<3} | {students[i]:<15} | {grades[i]} ')
            print(f'\n{"="*43}\n')

        #  AVERAGE
        elif select == 4:
            average = round(sum(grades) / len(grades), 2)
            print(f'\n{"="*15} Average Grade {"="*15}\n')
            print(f'{"No.":<3} | {"Student":<15} | {"Grade"}')
            print('—' * 37)
            for i in range(len(students)):
                print(f'{i+1:<3} | {students[i]:<15} | {grades[i]} ')
            print('—' * 37)
            print(f"📊 Class Average: {average}")
            print(f'\n{"="*43}\n')

        #  SEARCH
        elif select == 5:
            search_name = input("Type the student name: ").strip().title()
            if search_name in students:
                idx = students.index(search_name)
                print(f"\n✅ {search_name} found with grade {grades[idx]}.")
            else:
                print(f"❌ No student named '{search_name}' found.")

        # HIGHEST HONOR
        elif select == 6:
            highest_grade = max(grades)
            idx = grades.index(highest_grade)
            print(f"🏆 Highest Honor: {students[idx]} with grade {highest_grade}")

        #  QUIT
        elif select == 7:
            print("\t\tGoodbye 👋")
            break

        else:
            print("\t\t⚠️ Invalid option, try again.")

    except ValueError:
        print("\n❌ Invalid input! Please enter a number.")
