import math
class gaussian():
    def __init__(self, mu=0, sigma=1, data=[]):
        self.mean = mu
        self.stdev = sigma
        self.data = data
    def calculate_mean(self):
        mu = sum(self.data) / len(self.data)
        self.mean = mu
        return self.mean
    def calculate_stdev(self, sample=True):
        var=((2-self.mean)**2*sum(self.data))/len(self.data)-1
        self.stdev=math.sqrt(var)
        return self.stdev

