import myFormula1
import myFormula2
from myFormula3 import modulo

num1 = 10
num2 = 5

mySumCalculation = myFormula1.summation(num1, num2)
print(mySumCalculation)

mySubCalculation = myFormula1.subtraction(num1, num2)
print(mySubCalculation)

myMultiplicationCalculation = myFormula2.multiplication(num1, num2)
print(myMultiplicationCalculation)

myDivisionCalculation = myFormula2.division(num1, num2)
print(myDivisionCalculation)

myModuloCalculation = modulo(num1, num2)
print(myModuloCalculation)