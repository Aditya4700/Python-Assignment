import statistics

class Arithmetic:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data)

    def average(self):
        return self.mean()

    def mode(self):
        return statistics.mode(self.data)

    def stdev(self):
        return statistics.stdev(self.data)

# Usage
data = [1, 2, 3, 4, 5]
arith = Arithmetic(data)
print("Mean: ", arith.mean())
print("Average: ", arith.average())
print("Mode: ", arith.mode())
print("Standard Deviation: ", arith.stdev())
