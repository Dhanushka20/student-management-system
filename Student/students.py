from Person.person import Person

class Students(Person):
    def __init__(self,student_id,first_name,last_name,age,grade):
        super().__init__(student_id,first_name,last_name)
        self.__age = age
        self.__grade = grade

    def get_age(self):
        return self.__age

    def get_grade(self):
        return self.__grade

    def display_info(self):
        return f"Student {super().display_info()}, Age: {self.__age}, Grade: {self.__grade}."   
