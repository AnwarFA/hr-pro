class Employee():
   #Employee class here
   def __init__(self, name, age, salary, employment_years):
    self.name = name
    self.age = age
    self.salary = salary
    self.employment_years = employment_years
    
    print("Welcome to HR Pro")
    Employee.count += 1
    
    employee_list = []

    print("What would you like to do?")



    def __str__(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.employment_years}")

    def get_annual_salary(self, Employee):
        salary["Employee"] = salary
        return salary * 12



 class Manager(Employee):
     #Manager class here
     def __init__(self, name, age, salary, employment_years, bonus_percentage):
        super().__init__(self, name, age, salary, employment_years)
        self.bonus_percentage = bonus_percentage
    
    def __str__(self):
        return (f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.employment_years}, Bonus: {self.bonus_percentage")

    def get_bonus(self):
        self.bonus_percentage = salary
        return bonus_percentage * salary
    


        
 def main():
 	# main code here
    employee1 = input("Show the employee information:")
    employee2 = input("Show the maneger information:")
    employee3 = input("Show the HR employee:")
    user_employee = [employee1, employee2, employee3]

    for employee_list in user_employee:
    if employee_list == 0
    print(user_employee)
    return user_employee

 if __name__ == '__main__':
 	main()
