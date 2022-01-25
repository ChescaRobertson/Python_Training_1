class TrainingCourse:

    def __init__(self, title, duration, pricePerPerson, delegates=[]):
        self.title = title
        self.duration = duration
        self.pricePerPerson = pricePerPerson
        self.delegates = delegates

    def __str__(self): #  Overrides the default  __str__ dunder method, so when call print(course1) it will use this method instead
        return (f"Course Title: {self.title}, Course Duration: {self.duration}, Price Per Person: {self.pricePerPerson}, Delegate List: {self.delegates}")

    def addDelegates(self, name):
        self.delegates.append(name)
    
    def getTotalRevenue(self):
        totalRevenue = len(self.delegates) * self.pricePerPerson
        return totalRevenue

course1 = TrainingCourse('Python Programming 1', 4, 1600)
course1.addDelegates('Jim')
course1.addDelegates('Dave')
course1.addDelegates('Sarah')
course1.addDelegates('Sam')
course1.addDelegates('Kyle')

print(course1.getTotalRevenue())
print(course1)