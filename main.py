# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Test:

    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def test_func(self):
        print(f"test{self.var1}")


class Test2(Test):



    def test_func2(self):
        print(f"testing{self.var2}")
