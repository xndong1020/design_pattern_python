class ProtectedResource:
    def __init__(self, user):
        self.user = user

    def secured_method(self):
        print(self.user.name)


class User:
    def __init__(self, name, auth_code):
        self.name = name
        self.auth_code = auth_code


class ProtectedResourceProxy:
    def __init__(self, user):
        self.user = user

    def secured_method(self):
        if self.user.auth_code != "my super secret auth code":
            print("Invalid auth code")
            return

        print(self.user.name)


if __name__ == "__main__":
    user = User("Jeremy", "my super secret auth code")

    # Instead of calling ProtectedResource directly,
    # now we call its proxy, which has added security logic
    # resource = ProtectedResource(user)
    resource = ProtectedResourceProxy(user)
    resource.secured_method()
