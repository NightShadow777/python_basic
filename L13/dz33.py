'''
1) Создайте класс, описывающий человека (создайте метод, выводящий информацию о человеке).

2) На его основе создайте класс Студент (переопределите метод вывода информации).

3) Создайте класс Группа, экземпляр которого, состоит из объектов класса Студент. Реализуйте методы добавления,
удаления студента и метод поиска студента по фамилии.

Метод поиска студента должен возвращать именно экземпляр класса Студент, если студент есть в группе,
 в противном случае - None.

Определите для Группы метод __str__() для возвращения списка студентов в виде строки.

Ниже представленны заготовки, которые необходимо дополнить.
'''

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

    def delete_student(self, last_name):
        res = self.find_student(last_name)
        pass

    def find_student(self, last_name):
        pass

    def __str__(self):
        all_students = ''
        for i, st in enumerate(self.group):
            all_students += "{0}) First name: {1} \n" \
                            "   Last name: {2}\n" \
                            "   Gender: {3}\n" \
                            "   Age: {4}\n" \
                            "   Record book:{5}\n" \
                            "".format(i+1, st.first_name, st.last_name, st.gender, st.age, st.record_book)
        return f'Number:{self.number}\n{all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
gr.find_student('Jobs')
gr.find_student('Jobs2')  # None

gr.delete_student('Taylor')
print(gr) # Only one student