from StudentNode import StudentNode


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class StudentList:
    def __init__(self):
        self.student_head = None
        self.courses = None

    def add_student(self, val):
        new_node = Node(val)

        if self.student_head is None:
            self.student_head = new_node

        else:
            last = self.student_head

            while last.next:
                last = last.next

            last.next = new_node

    def edit_student(self, uid, field, new_data):
        if self.find(uid):
            self.update(uid, field, new_data)
            return "Student Updated"

        return "Unable to edit student"

    def delete_student(self, uid):
        if self.find(uid):
            if self.student_head.val.get_stu_id() == uid:
                self.student_head = self.student_head.next
            else:
                student = self.student_head
                prev = None

                while student.val.get_stu_id() != uid:
                    prev = student
                    student = student.next

                prev.next = student.next

            return "Student Deleted"

        else:
            return "Unable to find student"

    def find(self, uid):
        if self.student_head is None:
            return False

        student = self.student_head
        print(student.val.get_stu_id())

        while student:
            if uid == student.val.get_stu_id():
                return True

            student = student.next

        return False

    def update(self, uid, field, data):
        student = self.student_head

        while student:
            if uid == student.get_stu_id():
                if field == "first_name":
                    student.val.set_first_name(data)
                elif field == "mid_name":
                    student.val.set_mid_name(data)
                elif field == "last_name":
                    student.val.set_last_name(data)
                elif field == "id_num":
                    student.val.set_id_num(data)
                elif field in ["street", "city", "state", "zip", "type"]:
                    mailing = student.val.get_mailing()
                    if field == 'street':
                        mailing.set_street(data)
                    elif field == "city":
                        mailing.set_city(data)
                    elif field == "state":
                        mailing.set_state(data)
                    elif field == 'zip':
                        mailing.set_zip(data)
                    elif field == 'type':
                        mailing.set_type(data)
                elif field == "email":
                    email = student.val.get_email()
                    email.set_email(data)
                elif field == "phone":
                    phone = student.val.get_phone()
                    phone.set_phone(data)
                elif field == "b_date":
                    b_date = student.val.get_b_date()
                    date = data.split()
                    b_date.set_month(date[0])
                    b_date.set_date(date[1])
                    b_date.set_year(date[2])
                elif field == "a_date":
                    a_date = student.val.get_a_date()
                    date = data.split()
                    a_date.set_month(date[0])
                    a_date.set_date(date[1])
                    a_date.set_year(date[2])
                elif field == "sem":
                    sem = student.val.get_sem()
                    sem_info = data.split()
                    sem.set_semester(sem_info[0])
                    sem.set_year(sem_info[1])
                elif field == "major":
                    student.val.set_major(data)
                elif field == "minor":
                    student.val.set_minor(data)
                elif field == "stats":
                    student.val.set_stats(data)

            student = student.next
