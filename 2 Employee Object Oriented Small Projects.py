### Omar Cooper
### 2 Employee Object Oriented Small Projects






#### Small Project 1
#### This program will use class objects to take employee info in and display it uniformly. Extra objects/employee info can simply be added without changing  the source code

class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title
    def set_name(self,name):
        self.__name = name
    def set_id_number(self, id_number):
        self.__id_number = id_number
    def set_department(self, department):
        self.__department = department
    def set_job_title(self, job_title):
        self.__job_title = job_title
    def get_name(self):
        return self.__name
    def get_id_number(self):
        return self.__id_number
    def get_department(self):
        return self.__department
    def get_job_title(self):
        return self.__job_title
    
def main():
    employee1 = Employee("Susan Meyers", "47899", "Accounting", "Vice President")
    employee2 = Employee("Mark Jones", "39119", "IT", "Programmer")
    employee3 = Employee("Joy Rogers", "81774", "Manufacturing", "Engineer")

    print ("EMPLOYEE INFO")

    print (f" Name: {employee1.get_name()}\n  ID Number: {employee1.get_id_number()}\n  Department: {employee1.get_department()}\n  Job Title: {employee1.get_job_title()}\n")

    print (f" Name: {employee2.get_name()}\n  ID Number: {employee2.get_id_number()}\n  Department: {employee2.get_department()}\n  Job Title: {employee2.get_job_title()}\n")
    
    print (f" Name: {employee3.get_name()}\n  ID Number: {employee3.get_id_number()}\n  Department: {employee3.get_department()}\n  Job Title: {employee3.get_job_title()}\n")

if __name__ == "__main__":
    main()









######## Small Project 2
### This program will prompt the user for employee info the display it uniformly and correctly adjusted if necessary

class Employee:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
    def set_name(self,name):
        self.__name = name
    def set_id(self, id):
        self.__id = id
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id

# To create a subclass, place main class in parameter
class ProductionWorker(Employee):
    def __init__(self, name, id, shift, hourly_pay_rate):       ### You have to manually bring over parent class values
        super().__init__(name, id)
        self.__shift = shift
        self.__hourly_pay_rate = hourly_pay_rate
        self.pay_multiplier()

    def set_shift(self, shift):
        self.__shift = shift
    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate
    def get_shift(self):
        return self.__shift
    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate
    def pay_multiplier(self):
        if self.__shift == 2:
            self.__hourly_pay_rate *= 1.5
    
    
def main():
    name = input("Enter the employee's name: ")
    id = input("Enter the employee's ID number: ")

    shift = int(input("Enter a 1 for day shift or enter 2 for night shift: "))
    while shift not in [1,2]:
        print ("Enter a 1 for day shift or enter 2 for night shift: ")
        shift = int(input())

    hourly_pay_rate = int(input("Enter the rate of pay: $"))
    while hourly_pay_rate <= 0:
        hourly_pay_rate = int(input("Enter a value greater than 0: "))

    employee1 = ProductionWorker(name, id, shift, hourly_pay_rate)

    print ("EMPLOYEE INFO")
    print(f" Name: {employee1.get_name()}")
    print(f"  ID: {employee1.get_id()}")
    if employee1.get_shift() == 1:
        print("  Daytime Shift")
    else:
        print("  Nighttime shift")
    print(f"  Hourly Pay Rate : ${employee1.get_hourly_pay_rate():.2f}")


if __name__ == "__main__":
    main()

       
    
