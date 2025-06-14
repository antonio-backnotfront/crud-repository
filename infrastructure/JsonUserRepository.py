import json
from abc import ABC

from domain.User import User
from interfaces.AbstractUserRepository import AbstractUserRepository


class JsonUserRepository(AbstractUserRepository, ABC):
    def __init__(self, filepath):
        self.filepath = filepath
        try:
            with open(filepath, "x") as json_file:
                json.dump([], json_file)
        except FileExistsError:
            pass

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
        if data:
            next_id = max(u["id"] for u in data) + 1
        else:
            next_id = 1
        user.id = next_id
        data.append(user.to_dict())

        self._save(data)

    def get_user(self, user_id):
        data = self._load()
        for user in data:
            if int(user["id"]) == int(user_id):
                return User(user)
        return None

    def get_user_by_username(self, user_username):
        data = self._load()
        for user in data:
            if user["username"] == user_username:
                return User(user)
        return None

    def get_all_users(self):
        data = self._load()
        return [User(user_data) for user_data in data]
    #
    def update_user(self, user_id, new_data):
        data = self._load()
        for user in data:
            if int(user["id"]) == int(user_id):
                for k, v in new_data.items():
                    user[k] = v
                self._save(data)
                return True
        return False

    def delete_user(self, user_id):
        data = self._load()
        new_data = [user for user in data if int(user["id"]) != int(user_id)]
        if len(new_data) == len(data):
            return False
        self._save(new_data)
        return True
