class StudentNode:
    def __init__(self, first_name=None, mid_name=None, last_name=None, stu_id=None, id_num=None, mailing=None, email=None, phone=None, b_date=None, a_date=None, sem=None, major=None, minor=None, stats=None):
        if all(i is None for i in [first_name, mid_name, last_name, stu_id, id_num, mailing, email, phone, b_date, a_date, sem, major, minor, stats]):
            self.first_name = ""
            self.mid_name = ""
            self.last_name = ""
            self.stu_id = 0
            self.id_num = 0
            self.mailing = None
            self.email = None
            self.phone = None
            self.b_date = None
            self.a_date = None
            self.sem = None
            self.major = None
            self.minor = None
            self.stats = None
        else:
            self.first_name = first_name
            self.mid_name = mid_name
            self.last_name = last_name
            self.stu_id = stu_id
            self.id_num = id_num
            self.mailing = mailing
            self.email = email
            self.phone = phone
            self.b_date = b_date
            self.a_date = a_date
            self.sem = sem
            self.major = major
            self.minor = minor
            self.stats = stats

    def set_first_name(self, val):
        self.first_name = val

    def get_first_name(self):
        return self.first_name

    def set_mid_name(self, val):
        self.mid_name = val

    def get_mid_name(self):
        return self.mid_name

    def set_last_name(self, val):
        self.last_name = val

    def get_last_name(self):
        return self.last_name

    def set_stu_id(self, val):
        self.stu_id = val

    def get_stu_id(self):
        return self.stu_id

    def set_id_num(self, val):
        self.id_num = val

    def get_id_num(self):
        return self.id_num

    def set_mailing(self, val):
        self.mailing = val

    def get_mailing(self):
        return self.mailing

    def set_email(self, val):
        self.email = val

    def get_email(self):
        return self.email

    def set_phone(self, val):
        self.phone = val

    def get_phone(self):
        return self.phone

    def set_b_date(self, val):
        self.b_date = val

    def get_b_date(self):
        return self.b_date

    def set_a_date(self, val):
        self.a_date = val

    def get_a_date(self):
        return self.a_date

    def set_sem(self, val):
        self.sem = val

    def get_sem(self):
        return self.sem

    def set_major(self, val):
        self.major = val

    def get_major(self):
        return self.major

    def set_minor(self, val):
        self.minor = val

    def get_minor(self,):
        return self.minor

    def set_stats(self, val):
        self.stats = val

    def get_stats(self):
        return self.stats
