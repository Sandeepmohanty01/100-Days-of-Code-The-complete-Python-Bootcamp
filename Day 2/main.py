two_digit_number = input("Type a two digit number: ")
first_number = two_digit_number[0]
second_number = two_digit_number[1]
sum = int(first_number) + int(second_number)
print(sum)

Calculate the BMI

height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
bmi = (weight)/(height*height)
print(bmi)

age = int(input("What is your current age? "))
years = 90-age
days = years * 365
weeks = years * 52
months = years * 12

print(f"you have {days} days, {weeks} weeks and {months} months remaining")


print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_bill = bill + (bill * (tip/100))
split = input("How many people to split the bill? ")
each_split = total_bill/float(split)
print("Each person should pay: ", round(each_split,2))


