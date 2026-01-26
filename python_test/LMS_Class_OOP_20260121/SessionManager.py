class SessionManager:
    def __init__(self):
        self.current_user = None   # Member 객체

    def login(self, member):
        self.current_user = member

    def logout(self):
        self.current_user = None

    def is_logged_in(self):
        return self.current_user is not None

    def get_user(self):
        return self.current_user

    def get_role(self):
        if not self.current_user:
            return None
        return self.current_user.role
