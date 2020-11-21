import re


def checker(password):
    pattern = re.compile(r"^[A-Za-z0-9_-!@#$%&]{8,}$")
    return print(pattern.match(password))


checker(input("Enter password: "))
