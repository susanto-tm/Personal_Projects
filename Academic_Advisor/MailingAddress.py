class MailingAddress:
    def __init__(self, address):
        self.street, self.city, self.state, self.zip, self.type = ' '.join([address[0], address[1]]), address[2], address[3], address[4], address[5]

    def set_street(self, val):
        self.street = val

    def get_street(self):
        return self.street

    def set_city(self, val):
        self.city = val

    def get_city(self):
        return self.city

    def set_state(self, val):
        self.state = val

    def get_state(self):
        return self.state

    def set_zip(self, val):
        self.zip = val

    def get_zip(self):
        return self.zip

    def set_type(self, val):
        self.type = val

    def get_type(self):
        return self.type

