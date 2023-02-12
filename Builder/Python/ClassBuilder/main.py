from code_builder import CodeBuilder

code_builder = CodeBuilder("Person")
code_builder.add_field("str", "name")
code_builder.add_field("int", "age")
code_builder.add_field("str", "city")
print(code_builder)