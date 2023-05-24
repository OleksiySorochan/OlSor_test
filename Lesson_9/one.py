
class Users:
    def __init__(self, user_name, password, e_mail, age, name='noname', s_name='nos_name'):
        self.user_name = user_name
        self.password = password
        self.e_mail = e_mail
        self.age = age
        self.__name = name
        self.__s_name = s_name

    def get_name(self):
        return f"Імя користувача - {self.__name}"

    def set_name(self, value):
        self.__name = f"{value} - новий користувач"

    # @property
    # def name(self):
    #     return self.__name

    @property
    def s_name(self):
        return self.__s_name

    # @name.setter
    # def name(self, value):
    #     self.__name = value

    @s_name.setter
    def s_name(self, value):
        self.__s_name = value


    def username_info(self):
        return f'My user name is: {self.user_name}'

    @staticmethod
    def summa(a, b):
        return a + b

class Admin:
    def __init__(self, permissions=None):
        self.permissions = permissions

    def i_am_admin(self):
        print('I am adinistrator')


class AdminUsers(Users, Admin):
    def username_info(self):
        return f'My ADMIN name is: {self.user_name}'





vasya = Users('vasya', 'passwOrd', 'vasya@mail.com', 32)
mykola = Users('mykola', 'passwOrd', 'mykola@mail.com', 32)
viktor = Users('viktor', 'passwOrd', 'viktor@mail.com', 32)
ivan = Users('ivan', 'passwOrd', 'ivan@mail.com', 32, 'Ivan')



admin_dmytro = AdminUsers('dmytro', 'PASSWORD', 'dmytro@mail.com', 30)

# print(admin_dmytro.username_info())
# admin_dmytro.i_am_admin()

# print(vasya.password)
# print(vasya.username_info())
# print(ivan.username_info())
# print(Users.summa(4, 6))


# print(ivan.get_name())
# # ivan.name = 'Ivan Ivanovich'
# # print(ivan.name)
# ivan.set_name('Ivan Ivanovich')
# print(ivan.get_name())

print(admin_dmytro.username_info())
print(ivan.username_info())
