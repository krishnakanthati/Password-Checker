import re


def checker(password):
    pattern = re.compile(
        r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[A-Z])[A-Za-z\d!@#$%&]{8,}$")
    return pattern.match(password)
