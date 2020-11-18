"""Lesson 3 task 2"""


def user(first_name="Anonymous",
         last_name="Not defined",
         dob=0,
         city="R'lyeh",
         email="cthulhu@fhtagn.rlyeh",
         phone="664673"):
    print(f"User {last_name + ' ' + first_name}, "
          f"Year of Birth = {dob}, "
          f" is currently living in the {city}. "
          f"Contact Email is {email}, "
          f"phone number is {phone}")


user()


