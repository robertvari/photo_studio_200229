from unittest import TestCase


class MyTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.name = "Tamás"

    @staticmethod
    def i_am_a_static():
        print("I am a static method. I can't see inside the class")

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_add_numbers(self):
        result = 2 + 2
        self.assertEqual(result, 4)

    def test_say_hello(self):
        pass

    def test_do_nothing(self):
        pass


if __name__ == '__main__':
    MyTests.i_am_a_static()