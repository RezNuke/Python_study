import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, msg):
        super(LoggableList, self).append(msg)
        self.log(msg)
    
        
z = list('qwe')
print(z)
x = LoggableList('qwe')  
print(x)
x.append('msg')