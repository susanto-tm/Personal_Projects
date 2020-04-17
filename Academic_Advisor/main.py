from Student import StudentList
from StudentNode import StudentNode
from MailingAddress import MailingAddress
from Email import Email
from PhoneNumber import PhoneNumber
from Date import Date
from Semester import Semester


def get_multiple(data, delimiter):
    count = i = 0
    out = ""
    while count != 2:
        if data[i] == delimiter or data[i+1] == delimiter:
            count += 1
        else:
           out += data[i]
        i += 1

    return out, i


def parse(f):
    parsed_data = []

    data = f.split("\n")[1:]
    data = data[0].split("|")
    in_progress = []

    # get name
    for i in range(3):
        in_progress.append(data[i])

    parsed_data.append(in_progress)
    temp = data[3].split()
    id_num, uid, sem_year, major = [temp[0]], [temp[1]], [temp[2], temp[3]], [' '.join(temp[4:])]
    minor = data[4]
    status = data[5]
    b_date, a_date = data[6].split()[:3], data[6].split()[3:]

    data = '|'.join(data[7:])

    emails, i = get_multiple(data, "!")
    data = data[i:]

    e_types, emails = emails.split("|")[1::2], emails.split("|")[0::2]
    phone, i = get_multiple(data, "!")

    data = data[i:]
    p_types, phones = phone.split("|")[1::2], phone.split("|")[0::2]

    address, i = get_multiple(data, "!")

    street, road, city, state, m_zip, m_type = address.split("|")

    for info in [uid, id_num, [street, road, city, state, m_zip, m_type], [e_types, emails],  [p_types, phones], b_date, a_date, sem_year, major, minor, status]:
        parsed_data.append(info)

    return parsed_data


def show_message(message):
    inp = input(message)

    return str(inp)


def enter_students():
    first_name = input("Enter first name: ")
    middle_name = input("Enter middle name: ")
    last_name = input("Enter last name: ")
    uid = input("Enter student ID: ")
    id_num = input("Enter ID number: ")
    street = input("Enter street address")
    city = input("Enter city: ")
    state = input("Enter state: ")
    a_zip = input("Enter zip: ")
    a_type = input("Enter type: ")
    emails = []
    e_types = []
    while (c:=show_message("Menu Email:\n1. Add new email\n2. Exit")) != 2:
        if c == "1":
            emails.append(input("Enter email: "))
            e_types.append(input("Enter email type: "))
        else:
            break

    phones = []
    p_types = []
    while (c:=show_message("Menu Phone:\n1. Add new phone number\n2. Exit")) != 2:
        if c == "1":
            phones.append(input("Enter phone number: "))
            p_types.append(input("Enter phone number type: "))
        else:
            break

    b_date = input("Enter birth date (month day year): ")
    a_date = input("Enter acceptance date (month day year): ")
    sem = input("Enter semester and semester standing: ")
    major = input("Enter major: ")
    minor = input("Enter minor: ")
    stats = input("Enter status: ")

    return StudentNode(first_name, middle_name, last_name, uid, id_num,
                       MailingAddress([street.split(), city, state, a_zip, a_type]),
                       Email([emails, e_types]), PhoneNumber([phones, p_types]),
                       Date(b_date.split()), Date(a_date.split()), Semester(sem.split()), major,
                       minor, stats)


def edit_student_information():
    uid = input("Enter student ID: ")
    field = ""
    c = show_message("What information to change:\n1. First name\n2. Middle Name\n3. Last Name\n4. ID Number"
                     "\n5. Mailing Address\n6. Email\n7. Phone Number\n8. Birthdate\n9. Acceptance Date\n10. Semester"
                     "\n11. Major\n12. Minor\n13. Status")



def menu():
    students = StudentList()
    while True:
        c = show_message(f'1. Enter new student\n2. Edit a student\n3. Delete a student\n4. Display Student\n'
                     f'5. Display Students\n6. Write students to file\n7. Read students from file\n8. Exit application')
        if c == "1":
            students.add_student(enter_students())
        # elif c == "2":
        #     uid, field, new_data = edit_student_information()
        #     students.edit_student(uid, field, new_data)
        elif c == "8":
            return False








def main():
    students = menu()
    with open("test.txt", 'r') as f:
        info = parse(f.read())
        students = StudentList()
        students.add_student(StudentNode(info[0][0], info[0][1], info[0][2],
                                         info[1][0],
                                         info[2][0],
                                         MailingAddress(info[3]),
                                         Email(info[4]),
                                         PhoneNumber(info[5]),
                                         Date(info[6]),
                                         Date(info[7]),
                                         info[8][0],
                                         info[9][0],
                                         info[10][0],
                                         info[11][0]))

        print(students.find("stu1567"))