class Counter:
    def __init__(self):
        self.counter = 0
    
    def increase(self):
        self.counter += 1
    
    def result(self):
        return self.counter