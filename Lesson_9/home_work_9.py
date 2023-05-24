class Dron:
    def __init__(self, model, num_of_engine, camera_type):
        self.model = model
        self.num_of_engine = num_of_engine
        self.camera_type = camera_type

    def rise(self):
        print("Взлітаю")

    def landing(self):
        print("йду на посадку")

class User:
    def __init__(self, username, email='any', age='any', user_type='any', data_access='any'):
        self.username = username
        self.__email = email
        self.__age = age
        self.__user_type = user_type
        self.__data_access = data_access

    def get_email(self):
        print(self.__email)

    def set_email(self, value):
        self.__email = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

    def get_user_type(self):
        return self.__user_type

    def set_user_type(self, value):
        self.__user_type = value

    @property
    def data_access(self):
        return self.__data_access

    @data_access.setter
    def data_access(self, value):
        self.__data_access = value


    def valid_age(self):
        ag = int(self.__age)
        if ag > 0 and ag <= 12:
            return 'дитина'
        if ag > 12 and ag <= 18:
            return 'юнак'
        if ag > 18 and ag <=25:
            return 'молода людина'
        if ag > 25 and ag <= 40:
            return 'дорослий'
        if ag > 40 and ag <= 55:
            return 'зрілий'
        if ag > 55:
            return 'старий'

    def acc(self):
        ut = self.__user_type
        if ut == 'superuser' or ut == 'moderator':
            return 'access granted'
        else:
            return 'access denied'




oleksiy = User('oleksiy')
# print(oleksiy.data_access)
oleksiy.set_age(34)
print(oleksiy.get_age())
print(oleksiy.valid_age())
print(oleksiy.acc())
oleksiy.set_user_type('superuser')
print(oleksiy.acc())
