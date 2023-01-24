class AgeExeptionMaker(Exception):
    pass

class Voter:
    def __init__(self, age):
        self.age = age
        
    def validateAge(self):
        if self.age < 18:
            raise AgeExeptionMaker(" Not eligible to vote.")
        else:
            print("Eligible to vote.")

age = int(input("Enter voter's age: "))
voter = Voter(age)
try:
    voter.validateAge()
except AgeExeptionMaker as e:
    print(e)
