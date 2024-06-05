from Student.students import Students
from Schools.school import School
from Teacher.teachers import Teachers

school = School()

while True:
    print("\n ======Student Management System=======")
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. Display a list of all students.")
    print("4. Display a list of all teachers. ")
    print("5. Find a student by their ID and display their information. ")
    print("6. Find a teacher by their ID and display their information. ")
    print("7. Exit")

    choice = input("\nEnter number your choice:(1 to 7) ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        first_name = input("Enter First Name: ").capitalize()
        last_name = input("Enter Last name: ").capitalize()
        age = int(input("Enter Age: "))
        grade = int(input("Enter Grade: "))
        student = Students(student_id,first_name,last_name,age,grade)
        school.add_students(student)
        print(f"Student {student_id} is added.")
        
    elif choice == "2":
        teacher_id = input("Enter Teacher ID: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        subject = input("Enter Subject: ")
        teacher = Teachers(teacher_id,first_name,last_name,subject)
        school.add_teacher(teacher)
        print(f"Teacher {teacher_id} is added.")

    elif choice == "3":
        print("\nList of all students: ")
        #set student first name and last_name methods searching by ID
        choice_2 = input("Do you want to set another first name or last name for student (Y/N) ").lower()

        if choice_2 == "y":
            choice_3 = input("First name or Last name: (F/L)? ").lower()
            if choice_3 == "f":
                student_id = input("Enter student ID: ")
                first_name = input("Enter another first name: ")
                school.change_student_fname_by_id(student_id,first_name)
                school.display_all_students()

            elif choice_3 == "l":
                student_id = input("Enter student ID: ")
                last_name = input("Enter another last name: ")
                school.change_student_lname_by_id(student_id,last_name)
                school.display_all_students()

            else:
                print("Invalid name")   

        elif choice_2 == "n":
            school.display_all_students()  

        else:
            print("Invalid input. Please enter 'y' or 'n'")   
                   
        
    elif choice == "4":
        print("\nlist of all teachers: ")
        #set teachers first name and last_name methods searching by ID
        choice_2 = input("Do you want to set another first name or last name for teachers(Y/N) ").lower()

        if choice_2 == "y":
            choice_3 = input("First name or Last name: (F/L)? ").lower()
            if choice_3 == "f":
                teacher_id= input("Enter teacher ID: ")
                first_name = input("Enter another first name: ")
                school.change_teacher_fname_by_id(teacher_id,first_name)
                school.display_all_teachers()

            elif choice_3 == "l":
                teacher_id = input("Enter teacher ID: ")
                last_name= input("Enter another last name: ")
                school.change_teacher_lname_by_id(teacher_id,last_name)
                school.display_all_teachers()

            else:
                print("Invalid name")   

        elif choice_2 == "n":
            school.display_all_teachers()  

        else:
            print("Invalid input. Please enter 'y' or 'n'")   
               

    elif choice == "5":
        print("\nFind a student their ID and display their information: ")
        student_id = input("Enter student ID: ")
        print(school.find_student_by_id(student_id))
        
    elif choice == "6":
        print("\nFind a teacher their ID and display their information: ")
        teacher_id = input("Enter teacher ID: ")
        print(school.find_teacher_by_id(teacher_id))
        
    elif choice == "7":
        print('You successfully to used student management system.Thank you!')
        quit()

    else:
        print("Invalid choice")
       
