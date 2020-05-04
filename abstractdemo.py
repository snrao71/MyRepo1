from abc import ABC, abstractmethod

class Sample(ABC):          # abstract class
    def __init__(this, val):
        this.value = val
        super().__init__()
    @abstractmethod
    def method1(this):      # abstract method
        pass

#obj = Sample(10)       # error

class Example(Sample):      # abstract class must be inherited
    def method1(this):      # abstract methods must be implemented
        return this.value * 2

obj = Example(10)
print(obj.method1())
