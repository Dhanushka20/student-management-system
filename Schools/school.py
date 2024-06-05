from Person.person import Person
class School:
    def __init__(self):
        
        self.students = []
        self.teachers = []

    def add_students(self,student):
        self.students.append(student)

    def add_teacher(self,teacher):
        self.teachers.append(teacher) 

    def display_all_students(self):
        for student in self.students:
            print(student.display_info())
            
    def display_all_teachers(self):
        for teacher in self.teachers:
            print(teacher.display_info())

    def find_student_by_id(self,student_id):
        for student in self.students:
            if student.get_person_id()== student_id:
                return student.display_info()
        return None

    def find_teacher_by_id(self,teacher_id):
        for teacher in self.teachers:
            if teacher.get_person_id() == teacher_id:
                return teacher.display_info()
        return None
    
    
    #set student first name and last_name methods searching by ID
    
    def change_student_fname_by_id(self,student_id,first_name):
        for student in self.students:
            if student.get_person_id()== student_id:
                 return student.set_first_name(first_name)
            
    def change_student_lname_by_id(self,student_id,last_name):
        for student in self.students:
            if student.get_person_id()== student_id:
                 return student.set_last_name(last_name)      

    #set teachers first name and last_name methods searching by ID
    def change_teacher_fname_by_id(self,teacher_id,first_name):
        for teacher in self.teachers:
            if teacher.get_person_id()== teacher_id:
                 return teacher.set_first_name(first_name)    

    def change_teacher_lname_by_id(self,teacher_id,last_name):
        for teacher in self.teachers:
            if teacher.get_person_id()== teacher_id:
                 return teacher.set_last_name(last_name)               


                             

        
        


            