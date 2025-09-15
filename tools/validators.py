import re


def username_validator(username):
    if re.match(r"^[a-z0-9]{10,20}$", username):
        return username
    else:
        raise ValueError("Invalid Username!")


def password_validator(password):
    if re.match(r"^[a-z0-9$#@]{8,14}$", password):
        return password
    else:
        raise ValueError("Invalid Password!")


def nickname_validator(nickname):
    if re.match(r"^[a-zA-Z0-9\s]{8,14}$", nickname):
        return nickname
    else:
        raise ValueError("Invalid Nickname!")
