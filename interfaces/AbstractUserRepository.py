from abc import abstractmethod


def AbstractUserRepository():

    @abstractmethod
    def create_user(self, user):
        pass

    @abstractmethod
    def get_user(self, id):
        pass

    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def update_user(self, id, newData):
        pass

    @abstractmethod
    def delete_user(self, id):
        pass

