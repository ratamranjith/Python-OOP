import re
class Calculator:
    def __init__(self):
        self.num1 = None
        self.num2 = None
        
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Division by zero is not allowed"
    
    def modulus(self):
        if self.num2 != 0:
            return self.num1 % self.num2
        else:
            return "Error: Division by zero is not allowed"

    def operations(self, operations):
        
            match operations:
                case "+":
                    return self.add()
                case "-":
                    return self.subtract()
                case "*":
                    return self.multiply()
                case "/":
                    return self.division()
                case "%":
                    return self.modulus()

print("Basic Calculator - Simple Class")
print("Operations")
print("+" , end="\n")
print("-" , end="\n")
print("*" , end="\n")
print("/" , end="\n")
print("%" , end="\n")
calc = Calculator()
cache = 0
while(input != 'exit'):
    value = input()
    if value == 'clear':
        cache = 0
    else:
        splittedValue = re.split(r'([+\-*/%])', value)
        print(f"{int(splittedValue[0])} {splittedValue[1]} {int(splittedValue[2])} = ")  
        calc.num1 = int(splittedValue[0])
        calc.num2 = int(splittedValue[2])
        output = calc.operations(splittedValue[1])
        print(output)
        cache += output