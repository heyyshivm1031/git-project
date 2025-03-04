class Auth:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            return "User already exists!"
        self.users[username] = password
        return "User registered successfully!"

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return "Login successful!"
        return "Invalid credentials!"
