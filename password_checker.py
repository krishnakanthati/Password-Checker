from validate_password import checker

username = input('Enter your username: ')
password = input('Enter your password: ')
if checker(password) != None:
    hidden_password = len(password) * '*'
    print(f'{ username }, your passowrd is { hidden_password }.')
else:
    print('Incorrect password format.')
