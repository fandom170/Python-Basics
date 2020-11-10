"""Lesson 1 Task 5"""

earned = float(input("Please enter amount of earned: \n"))

wasted = float(input("Please enter amount spent: \n"))

if earned < wasted:
    print("You have worked without profit!")
elif earned == wasted:
    print("Hey dude! Why are you working for?")
else:
    profitability = (earned - wasted)/earned
    print(f"Your current profitability is {profitability:.2f} or {profitability:.2%}")
    employees = int(input("Please enter quantity of employees: \n"))
    print("Your current profitability is about {:.2f} units per one employee".format((earned - wasted)/employees))


