# By Jake Reddock
class ClassData:
    """
    Class Data object containing attributes
    Author: Jake

    >>> ClassData("TestClass",1,1).class_name
    'TestClass'
    >>> ClassData("TestClass",1,1).attribute_count
    1
    >>> ClassData("TestClass",1,1).method_count
    1
    """

    def __init__(self, class_name, attribute_count, method_count):
        self.class_name = class_name
        self.attribute_count = attribute_count
        self.method_count = method_count

    def get_attribute_count(self):
        return self.attribute_count

    def get_method_count(self):
        return self.method_count

    def get_name(self):
        return self.class_name
