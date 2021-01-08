# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is canadian address program


def address(Addressee_str, Street_number_str, Street_name_str,
            City_str, Province_str, Postal_Code,
            Apt_Number_str=None):
    # this function checks the inputs

    if Apt_Number_str is not None:
        address = Addressee_str + "\n" + Street_number_str + \
                  " " + Street_name_str + \
                  " " + City_str + " " + Province_str + \
                  " " + Postal_Code + " " + Apt_Number_str
        # more than 89 characters
        # \n
        # flow chart

    else:
        address = Addressee_str + "\n" + Street_number_str + \
                  " " + Street_name_str + " " + City_str + \
                  " " + Province_str + " " + Postal_Code
    return address


def main():
    # input
    Apt_Number_str = None

    Addressee_str = input("Enter addressee name:")
    question = input("Do you have an Apt.Number? (y/n):")
    if question == "Y" or question == "Yes":
        Apt_Number_str = input("Enter the Apt. Number: ")
    Street_number_str = input("Enter the street number:")
    Street_name_str = input("Enter the street name:")
    City_str = input("Enter the city:")
    Province_str = input("Enter the province:")
    Postal_Code = input("Enter the postal code: ")

    if Apt_Number_str is not None:
        address_titels = address(Addressee_str, Street_number_str,
                                 Street_name_str, City_str, Province_str,
                                 Postal_Code, Apt_Number_str)
    else:
        address_titels = address(Addressee_str, Street_number_str,
                                 Street_name_str, City_str, Province_str,
                                 Postal_Code)

    print("{0}.".format(address_titels))


if __name__ == "__main__":
    main()
