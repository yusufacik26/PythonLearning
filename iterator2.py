
class Counter():
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self


    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x 
        else:
            raise StopIteration 
        
iterator = iter(Counter(1,20))

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

    

