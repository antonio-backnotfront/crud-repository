import re


class UserValidators:
    @staticmethod
    def validate_email(email):
        email_regex = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(email and re.match(email_regex, email))

    @staticmethod
    def validate_age(age):
        return bool(age.isdigit() and int(age) >= 0)

    @staticmethod
    def validate_name(name):
        return name is not None

    @staticmethod
    def validate_phone(phone):
        phone_regex = r"^\+[0-9]{7,15}$"
        return bool(phone and re.match(phone_regex, phone))

