class Employee():
   #Employee class here
   def __init__(self, name, age, salary, employment_years):
    self.name = name
    self.age = age
    self.salary = salary
    self.employment_years = employment_years
    
    print("Welcome to HR Pro")
    Employee.count += 1
    
    Employee = []
    for Employee in Employees:
        if show_Employee:
            print(f"Options {show_Employee["Employee"]}:)
            
    Employee1 = int(input("Enter the employees information:"))
    Employee2 = int(input("Enter the managers information:"))
    Employee3 = int(input("allow the HR employee:"))
    user_Employee = [Employee1, Employee2, Employee3]

    print("What would you like to do?")


    print(user_Employee)
    return user_Employee



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
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.employment_years}, Bonus: {self.bonus_percentage")

    def get_bonus():
        bonus_percentage["Manager"] = salary
        return bonus_percentage * salary
    


        
 def main():
 	# main code here

 if __name__ == '__main__':
 	main()
