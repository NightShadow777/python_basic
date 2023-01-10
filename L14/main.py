import mcustom_exception as mce
import student
import group

def main():

    st1 = student.Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = student.Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    st3 = student.Student('Male', 30, 'Jon', 'Ivar', 'AN141')
    st4 = student.Student('Female', 30, 'Eva', 'Test2', 'AN141')
    st5 = student.Student('Female', 30, 'Alice', 'Test', 'AN141')
    st6 = student.Student('Female', 30, 'Hellga', 'Test', 'AN141')
    st7 = student.Student('Male', 30, 'Markus3', 'Ivar3', 'AN141')
    st8 = student.Student('Male', 30, 'Markus1', 'Ivar1', 'AN141')
    st9 = student.Student('Male', 30, 'Markus2', 'Ivar2', 'AN141')
    st10 = student.Student('Male', 30, 'Markus22', 'Ivar3', 'AN141')
    st11 = student.Student('Male', 30, 'Markus11', 'Ivar11', 'AN141')

    gr = group.Group('PD1')
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)

    print(gr)

    try:
        gr.add_student(st11)
    except mce.MCustomException as err:
        print("-" * 34)
        print(err.get_exception_message())
        print("-" * 34)

    print()
    print(gr.find_student('Jobs'))
    print(gr.find_student('Jobs2'))# None
    print()

    gr.delete_student('Taylor')
    gr.delete_student('Ivar')

    print(gr) # Only one student

if __name__ == "__main__":
    main()