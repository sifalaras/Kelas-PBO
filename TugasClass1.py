class student:
    """A class representing a student"""
    def __init__ (self,n,a,b,c,d,e):
        self.full_name = n
        self.age = a
        self.gender = b
        self.address = c
        self.telephone_number = d
        self.parent_name = e
    def get_name(self):
        return self.full_name
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def get_address(self):
        return self.address
    def get_telephone(self):
        return self.telephone_number
    def get_parent(self):
        return self.parent_name
