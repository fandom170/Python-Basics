"""Homework 2 task 6"""

decision = input("Would you like to enter goods? Print 'Y' if you want to. \n").lower()
counter = 1
goods = []
if decision == 'y':
    # goods data entering
    while True:
        name = input(f"Please enter name of item {counter} or enter 'STOP' to finish process: \n")
        if name.lower() == "stop":
            break
        if name is None:
            print("Name was not entered, please try again")
            continue
        price = input(f"Please enter price of {name}: \n")
        if price is None or not price.isdigit:
            print("Incorrect value was entered. Please try again")
            continue
        amount = input(f"Please enter available amount of {name}: \n")
        if amount is None or not amount.isdigit:
            print("Incorrect value was entered. Please try again")
            continue
        unit = input(f"Please enter measurement unit if {name} \n")
        if unit is None:
            print("Incorrect unit was entered. Pcs will be set")
            unit = 'pcs'

        # Tuple creation
        params = {'name': name, 'price': price, 'amount': amount, 'unit': unit}
        goods_data = (counter, params)
        goods.append(goods_data)
        counter += 1

    # creation of dictionary with statistic
    stats = {}

    for elem in goods:
        tmp_dict = elem[1]
        print(tmp_dict)
        for key, value in tmp_dict.items():
            if key not in stats:
                stats[key] = set(value)
            else:

                stats[key].add(value)
    print(stats)
else:
    print("Work of program has been completed.")



