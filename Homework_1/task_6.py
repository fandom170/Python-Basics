
result = float(input("Please enter initial result by numbers: \n"))
distance = float(input("Please enter required distance: \n"))
counter = 1

while result < distance:
    counter += 1
    result *= 1.1
    # print(f"{result:.2f}")

print("Expected result is reachable on {} day.".format(counter))

