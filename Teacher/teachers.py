from Person.person import Person

class Teachers(Person):
    def __init__(self,teacher_id,first_name,last_name,subject):
        super().__init__(teacher_id,first_name,last_name)
        self.__subject = subject

    def get_subject(self):
        return self.__subject

    def display_info(self):
        return f"Teacher {super().display_info()}, Subject: {self.__subject}"    