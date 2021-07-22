# Python Assignment (Super Car Rental System)
# Chan Ming Li TP060774
# Goh Jiun Sen TP059875

# Main menu of the car rental system
def menu():
    while True:  # An infinite loop
        print("-" * 15, "Welcome to Super Car Rental Service", "-" * 15)
        print("Please Choose Your Option: ")
        print("1. Admin Login")
        print("2. Registered Member Login")
        print("3. Register as a New Member")
        print("4. View All Cars Available to Rent")
        print("5. Exit")
        try:  # try and except block to prevent alphabetic input
            option = int(input("\nPlease Enter Your Option: "))
            print()
            if option == 1:  # admin_login() function will be called when option is 1
                admin_login()
            elif option == 2:  # member_login() function will be called when option is 2
                member_login()
            elif option == 3:  # save_memberDetails() function will be called when option is 3
                save_memberDetails()
            elif option == 4:  # display_carsAvailability("Available") function will be called when option is 4
                display_carsAvailability("Available")
                print()
                print("Reminder: Please Register As Our Member for Car Rental.")
                ctn = input("Do You Want to Register As Member [R] OR Back to Home Menu [B]?: ")  # ctn = continue
                print()
                if ctn == "R" or ctn == "r":  # save_memberDetails() function will be called when ctn is "R" or "r"
                    save_memberDetails()
            elif option == 5:  # break the loop if option is 5
                print("Thank you. Have a nice day!")
                print("Bye!")
                break
            else:  # only runs if option has other numeric values except 1 to 5
                print("Invalid Input. Please try again. \n")

        except:
            print("\nInvalid Input. This Option Only Accept Numeric Values.")
            print("Please try again.\n")


# admin menu that shows after admin login successfully and provide a variety of functions
def admin_menu():
    state = True  # assign state = True
    while state:  # the loop continue when state is True
        print()
        print("-" * 15, "Welcome Back to Admin Homepage!", "-" * 15)
        print("Actions Can be Made:")
        print("1. Add Cars to be Rented Out")
        print("2. Modify Car Details")
        print("3. Display Records")
        print("4. Search Record")
        print("5. Return a Rented Car")
        print("6. Log Out")
        print()
        try:  # try and except block to prevent alphabetic input
            opt = int(input("Please Enter Your Option: "))
            if opt == 1:
                save_carDetails()
            elif opt == 2:
                modify_carDetails()
            elif opt == 3:
                admin_displayMenu()
            elif opt == 4:
                admin_searchMenu()
            elif opt == 5:
                return_car()
            elif opt == 6:  # assign state as False when opt is 6
                print("Logging Out and Returning to Home Menu...\n")
                state = False
            else:  # only runs if opt has other numeric values except 1 to 6
                print("Invalid Input. Please Try Again.")

        except:
            print("\nInvalid Input. This Option Only Accept Numeric Values.")
            print("Please try again.")


# menu that has all display functions for admin
def admin_displayMenu():
    while True:         # An infinite loop
        print()
        print("-" * 15, "Welcome Back to Display Menu!", "-" * 15)
        print("Choose Your Option:")
        print("1. Cars Rented Out")
        print("2. Car Available for Rent")
        print("3. Customer Bookings")
        print("4. Customer Payment for a Specific Time Duration")
        print("5. Back")
        try:            # try and except block to prevent alphabetic input
            choice = int(input("\nPlease Enter Your Option: "))
            print()
            if choice == 1:
                display_carsAvailability("Unavailable")
                go = input("Enter Any Button to Continue: ")
            elif choice == 2:
                display_carsAvailability("Available")
                cot = input("Please Press Any Button to Continue: ")
            elif choice == 3:
                display_bookPayInfo("Booking")
            elif choice == 4:
                display_bookPayInfo("Payment")
            elif choice == 5:       # break the loop if choice is 5
                print("Returning to Admin Homepage...")
                break
            else:           # only runs if choice has other numeric values except 1 to 5
                print("Invalid Input. Please Try Again.")

        except:
            print("\nInvalid Input. This Option Only Accept Numeric Values.")
            print("Please try again.")


# admin_searchMenu() allows admin to search customer records
def admin_searchMenu():
    while True:         # An infinite loop
        print()
        print("-" * 15, "Welcome Back to Search Menu!", "-" * 15)
        print("Choose Your Option:")
        print("1. Search Customer Bookings")
        print("2. Search Customer Payments")
        print("3. Back")
        try:            # try and except block to prevent alphabetic input
            option = int(input("\nPlease Enter Your Option: "))
            print()
            if option == 1:
                search_memBookings()
            elif option == 2:
                search_memPayments()
            elif option == 3:          # break the loop if option is 3
                print("Returning to Admin Homepage...")
                break
            else:           # only runs if option has other numeric values except 1 to 3
                print()
                print("Invalid Input. Please Try Again.\n")
        except:
            print("\nInvalid Input. This Option Only Accept Numeric Values.")
            print("Please try again.")


# member menu that shows when members login successfully, username and password is required for this function
def member_menu(username, password):
    while True:  # Infinite loop
        try:  # try and except block to prevent alphabetic input
            print()
            print("-" * 15, "Welcome Back to Member Homepage!", "-" * 15)
            print("Options: ")
            print("1. Modify Personal Details")
            print("2. View Personal Rental History")
            print("3. View Details of Car to be Rented Out")
            print("4. Car Booking")
            print("5. Log Out")
            member_choice = int(input("\nPlease Enter Your Choice: "))
            print()

            if member_choice == 1:
                modify_memberDetails(username, password)  # modify_memberDetails() required username and password to run
            elif member_choice == 2:
                view_rentalHistory(username)  # view_rentalHistory() required username to run
            elif member_choice == 3:
                display_carsAvailability("Available")
                go = input("Please Press Any Button to Continue: ")     # input that asks users to continue
            elif member_choice == 4:
                save_bookingList(username)      # save_bookingList() required username to run
            elif member_choice == 5:        # break the loop if member_choice is 5
                print("Logging Out and Returning to Home Menu...\n")
                break
            else:           # only runs if member_choice has other numeric values except 1 to 5
                print("Invalid Input. Please Try Again.")

        except:
            print("\nInvalid Input. This Option Only Accept Numeric Values.")
            print("Please try again.")


# admin_login() function allows admin to login if credentials are matched
def admin_login():
    print("-" * 15, "Welcome to Admin Login Page!", "-" * 15)
    print("Please Login Into Admin Homepage:")
    admin_username = "ADMIN1314"        # assign a value for admin_username
    admin_password = "admin@handsome"   # assign a value for admin_password
    state = True
    while state:
        admin_usernameEntered = input("Please Enter Admin Username: ")
        admin_passwordEntered = input("Please Enter Admin Password: ")
        if admin_username == admin_usernameEntered:     # check if the username is same as the username assigned earlier
            if admin_password == admin_passwordEntered: # check if the password is same as the password assigned earlier
                print("Login Successfully. Welcome Back Admin!")
                admin_menu()                # call admin_menu() if all condition matched
                state = False               # assign state as False
            else:                       # only runs if password users entered does not match the admin password
                print("Incorrect Password. Please Try Again.")
        else:                # only runs if username users entered does not match the admin username
            print("Incorrect Username. Please Try Again")


# member_login() allows members to login if credentials are matched
def member_login():
    print("-" * 15, "Welcome to Member Login Page", "-" * 15)
    print("Please Login to Member Homepage")
    flag = True
    while flag:
        username = input("Please Enter Your Username: ")
        password = input("Please Enter Your Password: ")
        try:            # try and except block to prevent file error
            file = open('registered_member.txt', 'r')       # open the file in a read mode

        except:
            print("Something Went Wrong. File Cannot be Opened")

        for line in file:         # for loop of every line in the file
            login_info = line.split()   # split every line in the file
            if username == login_info[0] and password == login_info[1]:
                verify = 1
                break
            verify = 0
        file.close()
        if verify == 1:
            print("Login Successfully! Welcome Back Member!")
            member_menu(username, password)        # call function with username and password
            flag = False

        else:
            print("Oops, Your Username or/and Password Does Not Match. Please Try Again.")
            cont = input("Do you want to try again? [Y/N]: ")
            print()
            if cont == "N" or cont == "n":
                print("Returning to Main Menu...")
                print()
                flag = False


# save member details into a text file
def save_memberDetails():
    try:
        fHand = open('registered_member.txt', 'a')      # open file to append information
        member_info = member_details()
    except:
        print("Something Went Wrong. File Cannot Be Opened")
        print("Please Try Again.")
        exit()

    for line in member_info:          # append all information in the list into the text file
        fHand.write(line)
        fHand.write("\t")
    if not member_info == []:
        fHand.write("\n")

    fHand.close()


# ask new customer for member details before registration
def member_details():
    print("-" * 15, "Member's Personal Details Page", "-" * 15)
    print("Hi! Thanks for Joining Super Car Rental Membership.")
    print("Before Going to Registration Homepage, Please Enter Your Personal Details Below.\n")
    while True:
        mem_details = []
        print("-" * 15, "Personal Details", "-" * 15)
        mem_name = input("Please Enter Your Name: ").replace(" ", "_")  # ensure input has no space
        try:
            mem_age = int(input("Please Enter Your Age: "))
            if mem_age < 18:        # check if the customer age is over 18
                print()
                print("Sorry, You are not qualified to register as our member.")
                print("Member's age must be 18 or above.")
                cont = input("Do you want to try again? [Y/N]: ")
                print()
                if cont == 'Y' or cont == 'y':
                    continue
                else:
                    print("Returning to Home Menu...\n")
                    break
        except:
            print()
            print("Invalid Input. Your Age Should be Numeric Input.")
            print("Please Re-enter Your Personal Details.\n")
            continue
        mem_city = input("Please Enter City You Lived In: ").replace(" ", "_")
        mem_email = input("Please Enter Your Email: ").replace(" ", "")
        try:
            mem_phoneNumber = int(input("Please Enter Your Phone Number: "))
        except:
            print()
            print("Invalid Input. Your Phone Number Should be Numeric Input.")
            print("Please Re-enter Your Personal Details.\n")
            continue
        mem_unPw = registration_member()
        mem_details.append(mem_unPw[0])         # member new username
        mem_details.append(mem_unPw[1])         # member new password
        mem_details.append(mem_name.upper())
        mem_details.append(str(mem_age))        # convert the type of variable into string
        mem_details.append(mem_city.upper())
        mem_details.append(mem_email)
        mem_details.append(str(mem_phoneNumber))
        print("Returning to Main Menu...\n")
        break
    return mem_details  # return member details if function is called


# registration_member() allows new customer to register as member in this function
def registration_member():
    print()
    print("-" * 15, "Welcome to the Registration Homepage!", "-" * 15)
    while True:
        try:
            fileH = open('registered_member.txt', 'r')
        except:
            print("Something Went Wrong. File Cannot Be Opened")
            exit()
        newMemInfo = []
        found = 0
        print("Reminder: Blank Spaces Are Not Allowed For Username and Password.")
        newMemUsername = input("Please Enter Your New Username: ").replace(" ", "")  # ensure input has a value
        if newMemUsername == "":
            print("Sorry, username cannot be null value. Please Try Again.\n")
            continue
        for line in fileH:
            if line.startswith(newMemUsername):     # check if there is a same username in text file
                print("\nSorry, this username has been used. Please use another username\n")
                found = 1                       # if there is a same username, found = 1
        if found == 0:                 # if the username does not same as usernames in text file
            newMemPassword = input("Please Enter Your New Password: ").replace(" ", "")
            if newMemPassword == "":
                print("Sorry, password cannot be null value. Please Try Again.\n")
                continue
            comfirmPassword = input("Please Confirm Your Password: ").replace(" ", "")
            if newMemPassword == comfirmPassword:
                print("Congrats! Registered Successfully!\n")
                print("Your Username:", newMemUsername)
                print("Your Password:", newMemPassword)
                break
            else:
                print()
                print("Your Password Does Not Match. Please Try Again\n")
        fileH.close()
    newMemInfo.append(newMemUsername)   # append information into a list
    newMemInfo.append(newMemPassword)
    return newMemInfo       # return list which stores username and password when the function is called


# save car details into a text file
def save_carDetails():
    try:
        fHand = open('car_details.txt', 'a')        # open file to append information
        carDetails = add_carsAvailable()
    except:
        print("Something Went Wrong. File Cannot Be Opened.")
        print("Please Try Again")
        exit()

    for ls in carDetails:
        for i in ls:
            fHand.write(i)
            fHand.write("\t")
        fHand.write("\n")

    fHand.close()


# admin can add cars which are available to rent in this function
def add_carsAvailable():
    print("-" * 10, "Admin, Welcome to Cars Available Adding Page!", "-" * 10)
    print("Please Enter the Details of Car Accurately:")
    car_available = []
    while True:
        car_details = []
        car_model = input("Please Enter Car Model: ")
        car_plateNum = input("Please Enter Car Plate Number: ")
        try:
            car_year = int(input("Please Enter Manufactured Year of the Car: "))
        except:
            print()
            print("Invalid Input. Manufactured Year Only Allows Numeric Input.")
            print("\nPlease Re-enter Car Details")
            continue
        car_type = input("Please Enter the Type of the Car: ").replace(" ", "")
        try:
            car_rentalPrice = int(input("Please Enter Car Rental Price per day [RM]: "))
        except:
            print()
            print("Invalid Input. Car Rental Price Only Allows Numeric Input.")
            print("\nPlease Re-enter Car Details")
            continue
        pickup_location = input("Please Enter a Pickup Location: ").replace(" ", "")
        cars_availability = input("Please Enter Car Availability For Rent [Available/Unavailable]: ").upper()
        if cars_availability == "AVAILABLE" or cars_availability == "UNAVAILABLE":
            car_details.append(car_model.upper())       # ensure the string is all upper case
            car_details.append(car_plateNum.upper())
            car_details.append(str(car_year))
            car_details.append(car_type.upper())
            car_details.append(str(car_rentalPrice))
            car_details.append(pickup_location.upper())
            car_details.append(cars_availability)
            car_available.append(car_details)
            print()
            print(car_model.upper(), "Added Successfully.")
            cont = input("Do you want to add another car? [Y/N]: ")
            if cont == "N" or cont == "n":
                print("\nReturning to Admin Homepage...")
                break
        else:
            print("Invalid Input. Only [AVAILABLE] or [UNAVAILABLE] is acceptable.")
    return car_available        # return car available when the function is called


# admin modify cars' details by using this function
def modify_carDetails():
    print("-" * 15, "Welcome to Car Modification Page!", "-" * 15)
    while True:     # the loop will keep running until users requested
        try:
            print()
            display_carsAvailability("Available")
            file = open('car_details.txt', 'r+')    # open file to read and write information

        except:
            print("Something Went Wrong. File Cannot Be Opened.")
            print("Please Try Again")
            exit()

        print()
        temp = input("Press [M] to Modify or [E] to Exit: ")
        if temp == "M" or temp == "m":
            car_info = []
            for info in file:           # append information from file into a list line by line
                x = info.split()
                car_info.append(x)

            car_data = input("Choose a Car to Modify By Entering Car Plate Number: ")
            line_matched = None
            for line in car_info:                       # check if the input is same as car plate number in the list
                if car_data.upper() == line[1]:         # all car plate number locates in line[1]
                    line_matched = line                 # if successful, the line is assigned to the variable

            if line_matched == None:
                print("Car Number Plate Cannot be Found!")
                continue

            print(line_matched)
            try:
                change_data = input("Please Enter Data To Be Replace For This Car: ").upper()
                new_data = input("Please Enter New Data: ").upper()
                position = line_matched.index(change_data)      # find the index of data to change
                data_replace = line_matched.remove(change_data)       # remove data to change from the list
                # insert the new data into the list in the same index as data to change
                data_replaced = line_matched.insert(position, new_data)
                print(line_matched)

                file.seek(0)         # set the reference point in file to the beginning of the file
                file.truncate()        # resize the file into 0
                for lines in car_info:      # rewrite all cars information include the modified one into the file
                    for n in lines:
                        file.write(n)
                        file.write("\t")
                    file.write("\n")
                file.close()
                # car information modified successfully if all information rewrites into the text file
                print("Data Modified Successfully!")
                cont = input("Do you wish to continue? [Y/N]: ")
                if cont != "Y" or cont != "y":
                    print("Returning to Admin Homepage...")
                    break       # break the loop if admin does not want to continue
            except:
                print("Data Entered Cannot Be Found. Please Try Again.")
        else:
            print()         # break the loop if admin is not willing to continue
            print("Returning to Admin Homepage...")
            break


# display the cars based on their availability (Available/Unavailable)
def display_carsAvailability(keyword):
    try:
        fileH = open('car_details.txt', 'r')        # open text file in read mode
    except:
        print("Something Went Wrong. File Cannot Be Opened.")
        print("Please Try Again")
        exit()
    if keyword == "Unavailable":
        print("-" * 15, "Cars Rented Out", "-" * 15)
        print("CarModel / CarPlateNumber / ManufacturedYear / CarType / Price / PickupLocation / Availability")
        for ls in fileH:
            cars = ls.split()
            if cars[6] == "AVAILABLE":  # check the availability of car
                continue
            print(ls, end="")

    elif keyword == "Available":
        print("-" * 10, "Cars Available for Rent", "-" * 10)
        print("CarModel / CarPlateNumber / ManufacturedYear / CarType / PickupLocation / Availability")
        for ls in fileH:
            cars = ls.split()
            if cars[6] != "AVAILABLE":  # cars[6] stores the availability of cars
                continue  # if the car is not available, it returns to the top of the loop
            print(ls, end="")

    fileH.close()
    print()


# display booking or payment information based on the keyword entered
def display_bookPayInfo(keyword):
    try:
        file_handler = open('booking_list.txt', 'r')        # open text file in read mode
    except:
        print("Something Went Wrong. File Cannot Be Opened.")
        print("Please Try Again")
        exit()
    if keyword == "Booking":
        print("-" * 15, "All Members Booking Details", "-" * 15)
        print("Username / CarModel / CarPlateNumber / CarType / PickupDate / ReturnDate / BookingDays / TotalPrice(RM)")
        for info in file_handler:
            book_info = info.split()
            for element in book_info[:8]:  # only shows information related booking details
                print(element, end="    ")
            print()

    elif keyword == "Payment":
        print("-" * 15, "All Members Payment Details", "-" * 15)
        print("Username / TotalPrice(RM) / AccountNumber / AccountName / Bank / PaymentDate")
        for info in file_handler:
            pay_info = info.split()
            print(pay_info[0], end="    ")
            for element in pay_info[7:]:  # only shows information related payment details
                print(element, end="    ")
            print()
    print()
    go = input("Enter Any Key to Continue: ")
    file_handler.close()


# members bookings can be searched with this function
def search_memBookings():
    print("-" * 10, "Search Customer Bookings", "-" * 10)
    while True:             # infinite loop
        try:
            file_hand = open('booking_list.txt', 'r')       # open text file in read mode
        except:
            print("Something Went Wrong. File Cannot Be Opened")
            exit()

        go = input("Please Enter Any Button to Continue or [E] to Exit: ")
        if go == "E" or go == "e":
            print()
            print("Returning to Admin Search Menu...")
            break           # break the loop if admin wants to exit
        searchInput = input("Enter Username To Search Customer Booking Details: ")
        if searchInput == "":           # check if the search input has blank space or null values
            print("Blank Space is Not Acceptable For Searching\n")
            continue
        print()
        print("Username /  CarModel / CarPlateNumber / PickupLocation / PickupDate "
              "/ ReturnDate / BookingDays / TotalPrice(RM)")
        state = True
        for line in file_hand:
            data = line.split()
            if searchInput in data[0]:      # search the username entered in text file
                for element in data[:8]:        # shows only the booking details
                    print(element, end="    ")
                print()
                state = False           # if username can be found in text file, state is False
        if state:                       # if username cannot be found in text file, state remains True
            print('Username Not found')
        print()
        file_hand.close()


# members payments details can be searched with this function
def search_memPayments():
    print("-" * 10, "Search Customer Payments", "-" * 10)
    while True:             # infinite loop
        try:
            file_hand = open('booking_list.txt', 'r')       # open text file in read mode
        except:
            print("Something Went Wrong. File Cannot Be Opened")
            exit()

        go = input("Please Enter Any Button to Continue or [E] to Exit: ")
        if go == "E" or go == "e":
            print()
            print("Returning to Admin Search Menu...")
            break               # break the loop if admin wants to exit
        searchInput = input("Enter Username To Search Customer Booking Details: ")
        if searchInput == "":           # check if the search input has blank space or null values
            print("Blank Space is Not Acceptable For Searching\n")
            continue
        print()
        print("Username / TotalPrice(RM) / AccountNumber / AccountName / Bank / PaymentDate")
        state = True
        for line in file_hand:
            data = line.split()
            if searchInput in data[0]:              # search the username entered in text file
                print(data[0], end="    ")             # shows the username
                for element in data[7:]:            # shows only the payment details
                    print(element, end="    ")
                print()
                state = False                 # if username can be found in text file, state is False
        if state == True:                   # if username cannot be found in text file, state remains True
            print('Username Not found')
        file_hand.close()
        print()


# return_car() is used to return car by admin
def return_car():
    print()
    print("-" * 15, "Welcome to Return Car Page!", "-" * 15)
    print("Note: Please Ensure Car Is Returned Before Entering.")
    print()
    while True:
        try:
            display_carsAvailability("Unavailable")         # display all cars which is rented out
            file = open('car_details.txt', 'r')        # open text file with read mode
        except:
            print("Something Went Wrong. File Cannot Be Opened.")
            print("Please Try Again")
            exit()

        go = input("Please Enter Any Button to Continue or [E] to Exit: ")
        if go == "E" or go == "e":
            print("Returning to Admin Menu...")
            break           # break the loop if admin wants to exit
        car_return = input("Please Enter Car Plate Number of Car Returned: ").upper()
        found = 0
        for x in file:
            cars_list = x.split()
            if car_return == cars_list[1]:          # find the car plate number of the car return in text file
                car_matched = cars_list
                modify_carAvailability(car_matched)     # call function to change the car to available
                print("Car Returned Successfully!")
                print(car_matched)
                print()
                found = 1           # if car plate number can be found in text file, found is 1
        if found == 0:            # if car plate number cannot be found in text file, found is 0
            print("Car Cannot Be Found. Please Try Again.")
            print()
        file.close()


# modifying car availability with a car matched list and key word that defines the availability of car
def modify_carAvailability(car_matched, key="return"):
    try:
        file_handler = open('car_details.txt', 'r+')        # open text file in read and write mode
    except:
        print("Something Went Wrong. File Cannot Be Opened.")
        print("Please Try Again")
        exit()

    cars_info = []
    for ls in file_handler:
        cars = ls.split()
        if cars != car_matched:     # find the car matched list text file
            cars_info.append(cars)
            continue                # return to the top of the loop if does not match
        # only car matched list runs
        elif key == "booking":        # if the key is booking, it will turns unavailable to available
            changed_availability = car_matched.insert(-1, "UNAVAILABLE")
            change_availability = car_matched.remove("AVAILABLE")
            cars_info.append(car_matched)       # append the car matched list into the master list
        elif key == "return":       # if the key is booking, it will turns available to unavailable
            changed_availability = car_matched.insert(-1, "AVAILABLE")
            change_availability = car_matched.remove("UNAVAILABLE")
            cars_info.append(car_matched)       # append the changed car matched list into the master list

    file_handler.seek(0)        # set the reference point in file to the beginning of the file
    file_handler.truncate()     # resize the file into 0
    for info in cars_info:      # rewrite master list into the text file
        for l in info:
            file_handler.write(l)
            file_handler.write("\t")
        file_handler.write("\n")

    file_handler.close()


# modify member's personal details with username and password from member menu
def modify_memberDetails(username, password):
    print("-" * 10, "Welcome to Personal Details Modification Page!", "-" * 10)
    print("Note: You are able to modify your personal details here.")
    while True:
        try:
            my_file = open('registered_member.txt', 'r+')   # open text file in read and write mode

        except:
            print("Something Went Wrong. File Cannot Be Opened.")
            print("Please Try Again")
            exit()

        temp = input("Press [M] to Modify or Any Button to Exit: ")
        if temp == "M" or temp == "m":          # check if the user want to continue or exit
            print()
            membersInfo = []
            for i in my_file:                   # saves all information in txt file into a list line by line
                memberInfo = i.split()
                membersInfo.append(memberInfo)

            for ls in membersInfo:          # find the line that contain information of the username
                if username == ls[0] and password == ls[1]:
                    username_matched = ls       # assign the line which matched the username into a variable

            print("This is your personal information in our system: ")
            print("Username / Password / Name / Age / City / Email / ContactNumber")
            print(username_matched)
            print()
            try:
                old_info = input("Please Enter Information To Be Modified: ")
                new_info = input("Please Enter Your New Information: ")
                location = username_matched.index(old_info)     # find the index of old info
                modify_info = username_matched.remove(old_info)     # remove the old info from the list
                # insert new info into the list in the same index as old info
                modified_info = username_matched.insert(location, new_info)
                print(username_matched)

                my_file.seek(0)         # set the reference point in file to the beginning of the file
                my_file.truncate()          # resize the file into 0
                for line in membersInfo:    # rewrite all member information include the modified one into the file
                    for l in line:
                        my_file.write(l)
                        my_file.write("\t")
                    my_file.write("\n")
                my_file.close()
                # member's information modified successfully if all information rewrites into the text file
                print("Data Modified Successfully!")
                cont = input("Do you wish to continue? [Y/N]: ")
                print()
                if cont == "N" or cont == "n":
                    print("Returning to Member Homepage...")
                    break           # break the loop if user does not want to continue
            except:
                print("Data Entered Cannot Be Found. Please Try Again.")
        else:
            print()
            print("Returning to Member Homepage...")
            break               # break the loop if user is not willing to continue


# view rental_History provide a view of personal rental history to members
def view_rentalHistory(username):
    try:
        fileH = open('booking_list.txt', 'r')       # open text file in read mode

    except:
        print("Something Went Wrong. File Cannot Be Opened")
        exit()
    print("-" * 10, "Your Personal Rental History", "-" * 10)
    print("CarModel / CarPlateNumber / PickupLocation / PickupDate / ReturnDate / "
          "BookingDays / TotalPrice(RM) / AccountNumber / AccountName / Bank / PaymentDate")
    found = 0
    for detail in fileH:
        temp = detail.split()
        if username == temp[0]:     # find the username that matches username of the member login
            for data in temp[1:]:   # shows all information except username
                print(data, end="    ")
            print()
            found = 1               # if personal history is found, found is 1
    print()
    if found == 0:          # found is 0 means there is no history found in the text file
        print("No Rental History Can be Found.")
    go = input("Please Enter Any Button to Continue: ")
    fileH.close()


# save booking list into a text file
def save_bookingList(username):
    try:
        my_file = open('booking_list.txt', 'a')         # open file in append mode
        booking_list = members_booking(username)
    except:
        print("Something Went Wrong. File Cannot Be Opened.")
        print("Please Try Again")
        exit()

    if booking_list != None:
        for line in booking_list:
            my_file.write(line)
            my_file.write("\t")
        my_file.write("\n")

    my_file.close()


# car booking can be done by members with username from member menu in this function
def members_booking(username):
    from datetime import date       # date is imported from datetime
    print("-" * 15, "Welcome to Cars Booking Page!", "-" * 15)
    while True:
        try:
            display_carsAvailability("Available")         # call this function to display all cars available
            file = open('car_details.txt', 'r')         # open file in read mode
        except:
            print("Something Went Wrong. File Cannot Be Opened.")
            print("Please Try Again")
            exit()
        print("\nNote: Cars Can Only Be Booked Within One Week Before Your Pickup Date.\n")
        temp = input("Press [B] to Book Cars or [E] to Exit: ")
        if temp == "B" or temp == "b":      # append all booking information into a list if members want to book cars
            booking_info = []
            for info in file:
                book_info = info.split()
                booking_info.append(book_info)
            file.close()
            print()
            car_chosen = input("Enter Car Plate Number of The Car to Book: ")   # asks member to enter car plate number
            car_matched = None
            for car in booking_info:        # check if the car plate number entered is matched in the list
                if car[6] == "AVAILABLE":           # only cars that are available can be booked
                    if car_chosen.upper() == car[1]:    # all car plate numbers are stored in car[1]
                        car_matched = car
            if car_matched == None:       # if no car plate number matches then it returns to the beginning of loop
                print()
                print("Car Number Plate Cannot be Found!\n")
                continue

            print(car_matched)
            try:        # try and except block to prevent invalid date
                pickup_date = input("Please Enter Pick Up Date For The Car by [YYYYMMDD]: ")
                if len(pickup_date) != 8:   # check if the date entered is following our date format
                    print("\nInvalid Input. Please Follow the Date Format Above.\n")
                    continue               # returns to the beginning of loop if date format does not match
                year1 = int(pickup_date[0:4])
                month1 = int(pickup_date[4:6])
                day1 = int(pickup_date[6:8])
                date1 = date(year1, month1, day1)      # converting into date format
                date_today = date.today()               # find today's date
                check_day = date1 - date_today          # check days between today and pickup date by subtracting
                check_days = check_day.days             # convert format into days
                # check if the date is within one week starting from today
                if (check_days < 8) and (check_days > 0):
                    return_date = input("Please Enter Return Date For The Car by [YYYYMMDD]: ")
                    if len(return_date) != 8:
                        print("\nInvalid Input. Please Follow the Date Format Above.\n")
                        continue
                    year2 = int(return_date[0:4])
                    month2 = int(return_date[4:6])
                    day2 = int(return_date[6:8])
                    date2 = date(year2, month2, day2)
                    day_book = date2 - date1       # count booking days by subtracting return date and pickup date
                    booked_days = day_book.days     # convert booking days into days format
                    if booked_days > 0:     # check if booking date is valid (booked for future date)
                        # count the total price by multiplying rental price per day with booking days
                        total_price = int(car_matched[4]) * booked_days
                        print("-" * 7, "Booking Details", "-" * 7)
                        print("Username:", username)
                        print("Car Model:", car_matched[0])
                        print("Car Plate Number:", car_matched[1])
                        print("Pick-up Date:", date1)
                        print("Return Date:", date2)
                        print("Total Days Booked:", booked_days)
                        print("Total Price For Booking (RM):", total_price)
                        print()
                        payment_details = members_payment()    # call function to confirm booking by completing payment
                        booking_list = []
                        booking_list.append(username)           # append all information into a list
                        booking_list.append(car_matched[0])
                        booking_list.append(car_matched[1])
                        booking_list.append(car_matched[5])
                        booking_list.append(str(date1))
                        booking_list.append(str(date2))
                        booking_list.append(str(booked_days))
                        booking_list.append(str(total_price))
                        booking_list.append(payment_details[0])
                        booking_list.append(payment_details[1])
                        booking_list.append(payment_details[2])
                        booking_list.append(payment_details[3])
                        # call function to modify the availability of car when car is booked successfully
                        modify_carAvailability(car_matched, "booking")
                        print()
                        print(car_matched[1], "Booked Successfully!")
                        print("Hope You Enjoy Your Ride. Drive Safe.")
                        return booking_list     # return booking list for saving purposes
                    else:
                        print("\nInvalid Date. Please Try Again\n")
                else:
                    print("\nDate Invalid. Please Book Your Car Within One Week Before Your Pickup Date\n")
            except:
                print("\nInvalid Input. Please enter a valid date.\n")
        else:
            print()
            print("Returning to Member Homepage...")
            break          # break the loop if member wants to exit


# members payment can be done in this function to confirm the car booking
def members_payment():
    from datetime import date       # date is imported from datetime
    while True:     # infinite loop
        print("Please Proceed to Payment to Confirm Your Booking")
        print("-" * 10, "Bank Details", "-" * 10)
        print("Account Number: 601895362451")
        print("Account Name: Super Car Rental")
        print("Bank: MayBank")
        print()
        cont = input("Press any button to continue if payment is done or [E] to exit: ")
        if cont == "E" or cont == "e":
            break           # break the loop when member want to exit
        print("Note: Your Bank Details Are Required For Payment Checking.")
        print("Please Enter Your Bank Details:")
        try:            # try and except block to prevent invalid account number
            payment_date = str(date.today())    # convert today;s date into string
            print("Payment Date: ", payment_date)
            mem_accountNo = int(input("Account Number: "))
            mem_accountName = input("Account Name: ").replace(" ", "_")  # ensure account name does not have blank space
            if mem_accountName == "":      # check if account name is null value
                print("\nAccount Name Cannot Be Null Value. Please Enter Your Account Name.\n")
                continue            # return to the beginning of loop
            mem_bank = input("Bank: ").replace(" ", "")     # ensure bank does not have blank space
            if mem_bank == "":      # check if bank is null value
                print("\nBank Cannot Be Null Value. Please Enter Your Bank.\n")
                continue
            # return payment details
            return str(mem_accountNo), mem_accountName.upper(), mem_bank.upper(), payment_date

        except:
            print("\nInvalid Input. Please enter a valid account number.\n")


# Call menu 
menu()
