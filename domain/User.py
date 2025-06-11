class User:
    def __init__(self, data):
        self.username = data['username']
        self.email = data['email']
        self.name = data['name']
        self.phone = data['phone']
        self.age = data['age']
