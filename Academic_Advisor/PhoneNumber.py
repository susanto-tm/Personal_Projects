class PhoneNumber:
    def __init__(self, phones):
        self.types, self.phone = phones

    def set_phone(self, new_data):
        phone = new_data[0]
        p_type = new_data[1]

        if phone not in self.phone:
            self.phone.append(phone)
            self.types.append(p_type)
        elif phone in self.phone or p_type in self.types:
            idx = self.phone.index(phone)
            self.phone[idx] = phone
            self.types[idx] = p_type

    def get_number(self, p_type):
        for i in range(len(self.types)):
            if self.types[i].lower() == p_type.lower():
                return self.phone[i]
