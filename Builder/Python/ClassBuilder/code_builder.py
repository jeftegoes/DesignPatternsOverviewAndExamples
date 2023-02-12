from class_structure import ClassStructure
from field import Field


class CodeBuilder:
    def __init__(self, root_name):
        self.__class = ClassStructure(root_name)

    def add_field(self, type, name):
        self.__class.fields.append(Field(type, name))
        return self

    def __str__(self):
        return self.__class.__str__()
