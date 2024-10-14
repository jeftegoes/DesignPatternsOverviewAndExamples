from combination_lock import CombinationLock

combination_lock = CombinationLock([1, 2, 3, 4, 5])
print(combination_lock.status)
combination_lock.enter_digit(1)
print(combination_lock.status)
combination_lock.enter_digit(2)
print(combination_lock.status)
combination_lock.enter_digit(3)
print(combination_lock.status)
combination_lock.enter_digit(4)
print(combination_lock.status)
combination_lock.enter_digit(5)
print(combination_lock.status)
