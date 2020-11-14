"""Lesson 2 task 3"""

month_list = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
month_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
              7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
seasons = ['Winter', 'Spring', 'Summer', 'Autumn']

month_dict_extended = {"Winter": ("December", "January", "February"),
                       "Spring": ("March", "April", "May"),
                       "Summer": ("June", "July", "August"),
                       "Autumn": ("September", "October", "November")}

month = input("Please enter desired number of month: \n")

if month.isdigit() and 1 <= int(month) <= 12:
    month = int(month)
    # solution with list
    print("Entered month is {}. \nThis is {}.".format(month_list[month - 1],
                                                     seasons[month // 3] if month // 3 != 4
                                                     else seasons[0]))
    # solution with dictionary v1
    print("Entered month is {}. \nThis is {}.".format(month_dict[month], seasons[month // 3] if month // 3 != 4
                                                     else seasons[0]))

    # solution with dictionary v2
    season = month//3 if month != 12 else 0
    month_number = month % 3
    for enum, elem in enumerate(month_dict_extended.items(), 0):
        if enum == season:
            print("Entered month is {}. \nThis is {}.".format(elem[1][month_number], elem[0]))
            break
else:
    print("Wrong value has been entered.")
