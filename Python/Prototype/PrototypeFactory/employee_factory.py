import copy

from address import Address
from employee import Employee


class EmployeeFactory:
    main_office_employee = Employee(
        "", Address("Av. Sete", "Brazil", "Salvador"))

    aux_office_employee = Employee(
        "", Address("Av. Sete", "Brazil", "Salvador"))

    @staticmethod
    def __new_employee(prototype, name: str, suite: str):
        result = copy.deepcopy(prototype)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name: str, suite: str):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee, name, suite
        )

    @staticmethod
    def new_aux_office_employee(name: str, suite: str):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee, name, suite
        )
