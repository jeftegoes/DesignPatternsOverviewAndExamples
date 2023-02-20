from many_values import ManyValues
from single_value import SingleValue

single_value = SingleValue(11)
other_values = ManyValues()
other_values.append(22)
other_values.append(33)
# make a list of all values
all_values = ManyValues()
all_values.append(single_value)
all_values.append(other_values)
print(all_values.sum)
