def main():  # defining the function that executes the whole program
    # declare variables
    import time
    chances = 3  # error pin, only have 3 chances
    user_pin = 4323
    pin_input = 0
    withdrawl_amounts = [10, 20, 40, 60, 80, 100]
    print("")
    print("Welcome to Humber Bank ATM")
    print("")

    # the input is not equal to the 4 digit pin and chances is less than or equal to the default chances given
    while pin_input != user_pin and chances <= chances:
        balance = 100.0  # current balance when program starts
        # Asking the User
        pin_input = int(input("Please Enter Your 4 Digit Pin:"))
        # if the input is equal to the pin
        if pin_input == user_pin:
            print("")
            print("You entered your pin Correctly")
            print("")
            while (True):  # while the loop is true
                print("")
                print("")
                print("----------------------------------------")
                print("Please Press 1 For Your Balance")
                print("")
                print("Please Press 2 To Make a Withdrawl")
                print("")
                print("Please Press 3 To Pay in")
                print("")
                print("Please Press 4 To Return Card")
                print("----------------------------------------")
                print("")
                # Ask the User
                option = int(input("What Would you like to choose?"))
                print("")
                print("")
                # if the option is 1
                if option == 1:
                    print("Your Balance is $", str(balance))  # outputs balance in string format
                    print("")
                    # Ask the User
                    menu = input("Would You like to go back? yes or no")
                    if menu in ('yes', 'no'):  # in menu input, only yes and no is allocated
                        if menu == 'yes':
                            continue  # continues from menu options
                        else:
                            print("")
                            print("Thank you")
                            return main()  # return to the main function at the beginning of the program

                    else:  # else user dont put yes or no
                        print("")
                        print("Please put a proper response")

                # if option is 2
                elif option == 2:
                    print("How Much Would you like to withdraw?")
                    print("$10")
                    print("$20")
                    print("$40")
                    print("$60")
                    print("$80")
                    print("$100")
                    # Ask the User
                    withdraw = float(input("For other enter 1:"))
                    if withdraw in withdrawl_amounts:  # if assoicated values are in the list
                        balance = balance - withdraw  # substracts the amount inputed by user
                        print("Your Balance is now $", str(balance))  # outputs balance in string format
                        print("")
                        # Ask the User
                        menu = input("Would You like to go back? yes or no")
                        if menu in ('yes', 'no'):  # in menu input, only yes and no is allocated
                            if menu == 'yes':
                                continue  # continues from menu options
                            else:
                                print("")
                                print("Thank you")
                                return main()  # return to the main function at the beginning

                        else:  # else user dont put yes or no
                            print("")
                            print("Please put a proper response")

                    if withdraw == 1:  # if user enters 1, prompts them for their desired amount
                        # Ask the User
                        desired_amount = float(input("Please Enter Desired amount:"))
                        balance = balance - desired_amount  # substracts the amount inputed by user
                        print("Your Balance is now $", str(balance))  # outputs balance in string format
                        print("")
                        # Ask the User
                        menu = input(
                            "Would You like to go back? yes or no")  # in menu input, only yes and no is allocated
                        if menu in ('yes', 'no'):
                            if menu == 'yes':
                                continue  # continues from menu options
                            else:
                                print("")
                                print("Thank you")
                                return main()  # return to the main function at the beginning

                        else:  # else user dont put yes or no
                            print("")
                            print("Please put a proper response")



                    elif withdraw != withdrawl_amounts:  # if the input does not match the values given in the list
                        print("")
                        print("Invalid Amount, Please Re-try")
                        continue



                elif option == 3:  # if User chooses 3
                    # Ask the User
                    deposit = float(input("How Much Would You Like To Deposit?"))
                    balance = balance + deposit  # Add to the amount the User choose
                    print("Your Balance is now $", str(balance))  # outputs balance in string format
                    menu = input("Would You like to go back? yes or no")
                    if menu in ('yes', 'no'):  # same method used explained above
                        if menu == 'yes':
                            continue
                        else:
                            print("")
                            print("Thank you")
                            return main()

                    else:
                        print("")
                        print("Please put a proper response")

                elif option == 4:  # if User picks 4
                    print("Please wait whilst your card is Returned...")
                    for i in range(1):  # process of this statment appear once
                        print("")
                        time.sleep(3)  # process of this statment taking three seconds too appear
                        print("Thank you for you service")
                    return main()  # returns to main


                elif (option > 7 or option < 1):  # if option is not valid
                    print("Not an option please try again!")



        elif pin_input != user_pin:  # if the input is not equal to the digit pin
            print("Incorrect Password")
            chances -= 1  # decrements 1 from the chances variable

        if chances < 1:  # if chances are below 1
            print("No more tries")
            break  # break the loop and end the program


# start of the program in the main() function
main()
