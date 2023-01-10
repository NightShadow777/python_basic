import mcustom_exception as mce
class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise mce.MCustomException("You discover more than 10 students")
        self.group.add(student)

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