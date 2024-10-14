from expression_processor import ExpressionProcessor

ep = ExpressionProcessor()
ep.variables['x'] = 5
print(ep.calculate('1'))
print(ep.calculate('1+2'))
print(ep.calculate('1+x'))
print(ep.calculate('1+xy'))
