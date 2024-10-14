from ceo import CEO
from cfo import CFO

ceo1 = CEO()
print(ceo1)

ceo1.age = 66

ceo2 = CEO()
ceo2.age = 77
print(ceo1)
print(ceo2)

ceo2.name = 'Tim'

ceo3 = CEO()
print(ceo1, ceo2, ceo3)

cfo1 = CFO()
cfo1.name = 'Sheryl'
cfo1.money_managed = 1

print(cfo1)

cfo2 = CFO()
cfo2.name = 'Ruth'
cfo2.money_managed = 10
print(cfo1, cfo2, sep='\n')
