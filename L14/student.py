import human as hum
class Student(hum.Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book
    def __str__(self):
        return f"Human: {super().__str__()}, record_book: {self.record_book}"