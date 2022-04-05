class User:
    # this is the function used to create the user
    def __init__(self):
        self.user_type = 'guest'
        self.uname = None
        self.pwd = None
        self.emailID = None

    def register(self, name, pwd, emailID):
        self.uname = name
        self.pwd = pwd
        self.emailID = emailID

    def __repr__(self):
        s = "Name: {0}, Email: {1}, type: {2}\n"
        s = s.format(self.uname, self.emailID, self.user_type)
        return s


class FrequentTraveller(User):
    def __init__(self):
        super().__init__()
        self.user_type = 'Frequent Traveller'

    def register(self, name, pwd, emailID, travellerID):
        self.travellerID = travellerID
        super().register(name, pwd, emailID)

    def __repr__(self):
        s = "Name: {0}, Email: {1}, Traveller: {2}, type: {3}\n"
        s = s.format(self.uname, self.emailID,
                     self.travellerID, self.user_type)
        return s
