import secrets

class Password:
    def __init__(self, set_symbols):
        self.set_symbols = set_symbols
        self.required_symbols = [secrets.choice(symbol) for symbol in self.set_symbols]

    def generate_password(self, length):
        chars = "".join(self.set_symbols)
        password = "".join(secrets.choice(chars)
                        for _ in range(length - len(self.required_symbols)))
        password = "".join(secrets.choice(password + "".join(self.required_symbols))
                        for _ in range(len(password + "".join(self.required_symbols))))
        return password

set_symbols = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
               '0123456789', '!@#$%^&*"№;:?']
password_generator = Password(set_symbols)
for i in range(10):
    password = password_generator.generate_password(length=20)
    print(password)