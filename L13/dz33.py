class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
    def __str__(self):
        return f"gender: self.gender, age: self.age, first_name: self.first_name, last_name: self.last_name"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book
    def __str__(self):
        return f"Human: {super().__str__()}, record_book: {self.record_book}"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()
    def add_student(self, student):
        self.group.add(student)

    #ох чет с удалением голову сломал, пришло такое решение. Но наверняка есть более элегантное)
    def delete_student(self, last_name):
        res = self.find_student(last_name)
        self.group.discard(res)

    def find_student(self, last_name):
        for stud in self.group:
            if last_name == stud.last_name:
                return stud

    def __str__(self):
        all_students = ''
        delim = " "* 2
        for i, st in enumerate(self.group):
            all_students += "{0}) First name: {1}{6}" \
                            "Last name: {2}{6}" \
                            "Gender: {3}{6}" \
                            "Age: {4}{6}" \
                            "Record book: {5}\n" \
                            "".format(i+1, st.first_name, st.last_name, st.gender, st.age, st.record_book, delim)
        return f'Number:{self.number}\n{all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 30, 'Markus', 'Ivar', 'AN141')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
print(gr)

gr.find_student('Jobs')
gr.find_student('Jobs2')# None

gr.delete_student('Taylor')
gr.delete_student('Ivar')
print(gr) # Only one student