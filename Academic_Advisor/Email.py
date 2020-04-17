class Email:
    def __init__(self, emails):
        self.types, self.email = emails

    def set_email(self, new_data):
        email = new_data[0]
        e_type = new_data[1]

        if email not in self.email:
            self.email.append(email)
            self.types.append(e_type)
        elif email in self.email or e_type in self.types:
            idx = self.email.index(email)
            self.email[idx] = email
            self.types[idx] = e_type

    def get_email(self, e_type):
        for i in range(len(self.types)):
            if self.types[i].lower() == e_type.lower():
                return self.email[i]

        return "Unable to find email"
