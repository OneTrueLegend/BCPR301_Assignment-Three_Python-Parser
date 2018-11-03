from src.Statistics.ClassData import ClassData


class ClassAdapter(ClassData):
    def __init__(self, class_node):
        self.class_adapt = class_node

    def get_name(self):
        return self.class_adapt.get_name()

    def get_attribute_count(self):
        return len(self.class_adapt.get_attributes())

    def get_method_count(self):
        return len(self.class_adapt.get_methods())
