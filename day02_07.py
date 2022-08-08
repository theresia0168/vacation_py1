price = int(input("Type the price : "))
num = int(input("Type the E/A : "))
sum = price*num
print("Total price is",sum,"dollar")

num1 = int(input("Type the E/A : "))
sum = int(input("Type the total price : "))
price1 = sum/num1
print("Each of the goods price is",price1,"dollar")
print(type(price1))

num2 = int(input('Type the number of books : '))
price2 = int(input('Type the each of the books price : '))
sum = price2*num2
print("Total price is",sum,"dollar")

age = int(input("Type your age : "))
totalMonth = 12*age
print("Total",totalMonth,"months lived")

str = "200"
str1 = "300"
str2 = str + str1

print(str2)     #연산자의 오버로딩이 일어나 200+300의 결과가 문자열 이어붙이기가 된다
print(str2*3)
