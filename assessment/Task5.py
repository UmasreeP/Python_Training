"""
Write 2 class-methods where one method to set company head name and another method to get company head name

Example:
EmployeeClass.set_company_head_name(‘head-1’)  print(EmployeeClass.get_company_head_name)     output  ‘head-1’

"""


class EmployeeClass:

    company_head_name = None

    @classmethod
    def set_company_head_name(cls, name):
        cls.company_head_name = name

    @classmethod
    def get_company_head_name(cls):
        return cls.company_head_name


EmployeeClass.set_company_head_name("head-1")
print("Head name is : ", EmployeeClass.get_company_head_name())
