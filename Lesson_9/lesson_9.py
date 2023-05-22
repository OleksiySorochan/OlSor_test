class Users:
    def __init__(self, user_name, password, e_mail, age, name='no_name', s_name='no_s_name'):
        self.user_name = user_name
        self.e_mail = e_mail
        self.age = age
        self.name = name
        self.s_name = s_name

    def username_info(self):
        return f'My user, is {self.user_name}'

    @staticmethod
    def summa(a, b):
        return a + b


class Admin:
    def __init__(self, permissions=None):
        self.permissions = permissions

    def i_am_admin(self):
        print("I am administrator!")


class AdminUser(Users, Admin):

    def username_info(self):
        return f'My ADMIN, is {self.user_name}'


admin_dmytro = AdminUser('dmytro', 'Password', 'dmytro@mail.com', 30)
# print(admin_dmytro.username_info())
# admin_dmytro.i_am_admin()
print(admin_dmytro.username_info())