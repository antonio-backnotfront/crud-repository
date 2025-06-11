import json
from abc import ABC

from domain.User import User
from interfaces.AbstractUserRepository import AbstractUserRepository


class JsonUserRepository(AbstractUserRepository, ABC):
    def __init__(self, filepath):
        self.filepath = filepath

    def _load(self):
        with open(self.filepath, "r") as json_file:
            content = json_file.read().strip()
            if not content:
                return []
            return json.loads(content)

    def _save(self, data):
        with open(self.filepath, "w") as json_file:
            json.dump(data, json_file)

    def create_user(self, user: User):
        data = self._load()
        data.append(user.to_dict())
        self._save(data)

    def get_user(self, id):
        data = self._load()
        for user in data:
            if user["id"] == id:
                return User(user)
        return None

    def get_all_users(self):
        data = self._load()
        return [User(user_data) for user_data in data]
    #
    def update_user(self, userId, new_data):
        data = self._load()
        for user in data:
            if user["id"] == userId:
                for k, v in new_data.items():
                    user[k] = v
                self._save(data)
                return True
        return False

    def delete_user(self, userId):
        data = self._load()
        new_data = [user for user in data if user["id"] != userId]
        if (len(new_data) == len(data)):
            return False
        self._save(new_data)
        return True
