class User:
    def __init__(self, data):
        self.username = data['username']
        self.email = data['email']
        self.name = data['name']
        self.phone = data['phone']
        self.age = data['age']
        self.id = data.get('id')



    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'name': self.name,
            'phone': self.phone,
            'age': self.age,
        }