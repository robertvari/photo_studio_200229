class User:
    def __init__(self):
        self.name = "Robert"

    @classmethod
    def my_class_method(cls):
        cls.name = "Tamas"

    @staticmethod
    def get_all_users():
        print("Hello, i'm a static method here is your class:")


if __name__ == '__main__':
    MyClass.my_class_method()