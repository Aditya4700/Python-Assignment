class Person:
    def __init__(self, salary):
        self.salary = salary

class EligibilityChecker:
    def check_ifeligible(self, person):
        if person.salary < 10000:
            raise ValueError("Not eligible for loan.Salary less than 10k/Month")
        else:
            print("Eligible for loan.")

try:
    p = Person(18000)
    checker = EligibilityChecker()
    checker.check_ifeligible(p)
except ValueError as e:
    print(e)
