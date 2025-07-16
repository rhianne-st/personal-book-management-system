import datetime
import os

# Opening the .txt file to read
with open("books_catalogue.txt", "r") as personal_library:
    library_lines = personal_library.readlines()

# Creating individual lists for the books' information
ISBN = []
author = []
title = []
publisher = []
genre = []
year_published = []
date_purchased = []
status = []

for element in library_lines:
    book_info = element.split('; ')
    # Appends each book category's info to respective lists
    ISBN.append(book_info[0])
    author.append(book_info[1])
    title.append(book_info[2])
    publisher.append(book_info[3])
    genre.append(book_info[4])
    year_published.append(book_info[5])
    date_purchased.append(book_info[6])
    status.append(book_info[7].replace('\n', ''))

# Compiling all individual lists into a nested list
compiled = []
compiled.append(ISBN)
compiled.append(author)
compiled.append(title)
compiled.append(publisher)
compiled.append(genre)
compiled.append(year_published)
compiled.append(date_purchased)
compiled.append(status)


# FUNCTION: Clears output screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# FUNCTION: Prints the main menu
def print_menu():
    print("+––––––––––––––––––––––––––––––––––––+\n"
          "|     [   M A I N    M E N U   ]     |\n"
          "|––––––––––––––––––––––––––––––––––––|\n"
          "|  [1]  Add Book Record(s)           |\n"
          "|  [2]  Delete Book Record(s)        |\n"
          "|  [3]  Update/Edit Book Record(s)   |\n"
          "|  [4]  Display Book Records         |\n"
          "|  [5]  Search for Book(s)           |\n"
          "|  [6]  Exit                         |\n"
          "+––––––––––––––––––––––––––––––––––––+")

# FUNCTION: Check if user input is empty/left blank
def check_empty(user_input, empty_error_message):
    while user_input == '':
        # Handles error if input is left blank
        clear_screen()
        print(f"{empty_error_message} cannot be empty.")
        user_input = str(input(f"Enter {(empty_error_message).lower()}: "))
    return user_input

# FUNCTION: Checks if user input is other than 'Y' and 'N'
def check_cont(cont_var, YN_error_message):
    while cont_var != 'Y' and cont_var != 'N':
        # Re-prompts the continue option if an invalid input is entered
        clear_screen()
        cont_var = str(input(f"{YN_error_message}")).upper()
    return cont_var

# FUNCTION: Return to main menu
def return_to_menu(cont_choice):
    if cont_choice == ('Y'):
        # User chooses to continue the action within the initial [1-5] option
        clear_screen()
    elif cont_choice == ('N' or 'n'):
        # User chooses to exit the action and return to the main menu
        clear_screen()
        print_menu()
    return cont_choice

# FUNCTION: To get delete confirmation in [2] Delete Books part
def get_delete_confirmation():
    while True:
        dlt_cont = input("Do you still want to delete a book? (Y/N): ").upper()
        dlt_cont = check_cont(dlt_cont,"Invalid input. Please enter again.\nDo you want to delete another book? (Y/N): ")
        dlt_cont = return_to_menu(dlt_cont)

        if dlt_cont in ['Y', 'N']:
            return dlt_cont
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

# FUNCTION: wrap text, given text in list and specifying the width to wrap
def wrap_text(text, width):
    wrapped_lines = []
    current_line = ""       # To accumulate the current line being formed
    current_width = 0       # Tracks the current width of the line being formed

    for words in text.split():
        # Splitting the text into a list of words to calculate if the length of the text in within the specified width
        if current_width + len(words) <= width:
            # If adding the current word fits within the specified width
            current_line += words + " "     # The space is added to separate the words
            current_width += len(words) + 1
        else:
            # If the length of the current word exceeds the specified width
            wrapped_lines.append(current_line.rstrip())
            current_line = words + " "      # The space is added to separate the words
            current_width = len(words) + 1

    if current_line:
        wrapped_lines.append(current_line.rstrip())
        # If there is any content left in current_line, it is added to wrapped_line after removing any blank spaces

    return wrapped_lines



### START OF MAIN CODE ###

# Displaying the main menu for user to choose their action
print("                      __.-.\n"
      "   WELCOME       .-. |  | |__\n"
      "   TO YOUR       | |_|  | |  |\n"
      "   BOOK          | | |  | |  |<\\\n"
      "   MANAGEMENT    | | |  | |  | \\\\\n"
      "   SYSTEM        | | |  | |  |  \\\\\n"
      "                 | | |  | |  |   \>\n"
      "======================================")
print_menu()

system_cont = 'Y'
# Action to be executed repeatedly until EXIT is chosen
while system_cont == 'Y':
    try:
        # Prompts for user choice
        action_choice = int(input("What would you like to do? (1-6): "))

    except ValueError:
        # Handling error when input is not an int
        clear_screen()
        print_menu()
        print("Invalid input! Please enter a number.")
    
    else:
        if action_choice not in range(1,7):
            # The accepted input is within the range of 1-6
            # User input other than 1-6 will re-prompt question statement
            clear_screen()
            print_menu()
            print("Choice unavailable! Please choose again.")
        
        
        ### OPTION 1: ADD BOOK RECORD(S)
        if action_choice == 1:
            clear_screen()
            print("You chose to add a new book record!")

            add_cont = 'Y'

            while add_cont.upper() == 'Y':
                while True:
                    try:
                        add_ISBN = int(input("Enter ISBN number: "))

                    except ValueError:
                        # Handling error when ISBN entered is not an int
                        clear_screen()
                        print("ISBN consists of 13-digit numbers.")
                    
                    else:
                        if len(str(add_ISBN)) != 13:
                            # In the case where ISBN entered is not 13-digits long (standard ISBN length)
                            clear_screen()
                            print("ISBN consists of 13-digit numbers.")
                        
                        else:
                            if int(add_ISBN) < 0:
                                # In the case where a 13-digit negative int is entered
                                clear_screen()
                                print("Invalid ISBN input.")
                            
                            else:
                                if str(add_ISBN) in ISBN:
                                    # In the case where the ISBN already exists in the record system
                                    clear_screen()
                                    print("This book already exists in your record.")
                                
                                else:
                                    # If ISBN entered is a positive int, is 13-digits long, does not already exists,
                                    # breaks out of the loop to collect the next information
                                    break

                clear_screen()
                add_author = str(input("Enter author name: "))
                add_author = check_empty(add_author, "Author name")

                clear_screen()
                add_title = str(input("Enter book title: "))
                add_title = check_empty(add_title, "Book title")
                
                clear_screen()
                add_publisher = str(input("Enter publisher: "))
                add_publisher = check_empty(add_publisher, "Publisher")
                
                clear_screen()
                add_genre = str(input("Enter genre: "))
                add_genre = check_empty(add_genre, "Genre")
                
                clear_screen()
                year_format = '%Y'      # The accepted year published format is YYYY
                while True:
                    try:
                        add_year_published = int(input("Enter year published (YYYY): "))     # User enters the year published                        
                        datetime.datetime.strptime(str(add_year_published), year_format)     # Checking for the year formatting
                    
                    except ValueError:
                        # Handling if the year formatting is wrong
                        clear_screen()
                        print("Year format should be YYYY.")

                    else:
                        today = datetime.datetime.now()             # Getting today's date/time info
                        current_year = today.strftime("%Y")         # Today's year in YYYY format

                        if int(add_year_published) > int(current_year):
                            # In the case where user enters the published year that is after today's year (in the future)
                            clear_screen()
                            print("Your book cannot be published in the future.")
                        
                        else:
                            # If no errors, proceed to prompt the next input
                            break
                
                clear_screen()
                date_format = '%d-%m-%Y'    # The accepted date format is DD-MM-YYYY
                while True:
                    try:
                        add_date_purchased = input("Enter purchase date (DD-MM-YYYY): ")    # User enters the date purchased
                        datetime.datetime.strptime(str(add_date_purchased), date_format)         # Checking for the date formatting
                                            
                    except ValueError:
                        # Handling error if the date formatting is wrong
                        clear_screen()
                        print("Date format should be DD-MM-YYYY.")
                    
                    else:
                        year_purchased = add_date_purchased[6:10]       # Extracts only the year in YYYY format
                        current_date = today.strftime("%Y%m%d")         # Today's date in YYYYMMDD format
                        check_date_purchased = add_date_purchased[6:10], add_date_purchased[3:5], add_date_purchased[0:2]
                        check_date = ''.join(check_date_purchased)      # Changing the entered date format to YYYYMMDD
                        
                        if int(year_purchased) < int(add_year_published):
                            # Rejects if the date purchased is before published year, which is impossible to occur
                            clear_screen()
                            print("Date purchased cannot be earlier than year published.")
                        
                        elif int(check_date) > int(current_date):
                            # Rejects if the date purchased entered is after today's date
                            clear_screen()
                            print("Your purchase date is in the future!")
                        
                        else:
                            # If all date formatting/requirements is correct, breaks out of the while loop
                            break
                
                clear_screen()
                add_status = str(input("Enter reading status (to-read/reading/read): "))
                add_status = check_empty(add_status, "Reading status")
                while (add_status != 'to-read') and (add_status != 'reading') and (add_status != 'read'):
                    # If status entered is invalid
                    clear_screen()
                    print("Reading status can only be 'to-read', 'reading', or 'read'.")
                    add_status = str(input("Enter reading status (to-read/reading/read): "))
                    add_status = check_empty(add_status, "Reading status")
                
                # Appends user's input to the record lists in their respective categories
                ISBN.append(str(add_ISBN))
                author.append(add_author)
                title.append(add_title)
                publisher.append(add_publisher)
                genre.append(add_genre)
                year_published.append(str(add_year_published))
                date_purchased.append(str(add_date_purchased))
                status.append(add_status)
                
                # Informs user that a book has been added
                clear_screen()
                print(f"A new book record titled '{add_title}' by {add_author} has been added.")

                # Asks user if they want to add another book
                add_cont = str(input("Would you like to add another book? (Y/N): ")).upper()
                add_cont = check_cont(add_cont, "Invalid input. Please enter again.\nWould you like to add another book? (Y/N): ")
                add_cont = return_to_menu(add_cont)

        

        ### OPTION 2: DELETE BOOK RECORD(S)
        elif action_choice == 2:
            clear_screen()
            print("You chose to delete a book record!")

            dlt_cont = 'Y'
            
            while dlt_cont.upper() == 'Y':
                #while True:
                dlt_title = str(input("Enter book title (case sensitive): "))                
                dlt_author = str(input("Enter author name (case sensitive): "))
        

                # Check if user's inputs match with existing list
                if (dlt_title not in title) or (dlt_author not in author):
                    clear_screen()
                    print("Book does not exist in record!")

                    # Asks user if they still want to delete a book
                    dlt_cont = get_delete_confirmation()
                    
                else:
                    # In the case where inputs exist in list but do not belong to the same book (different index)
                    if author.index(dlt_author) != title.index(dlt_title):
                        clear_screen()
                        print("The author and title does not match!")

                        # Asks user if they still want to delete a book
                        dlt_cont = get_delete_confirmation()

                    else:
                        # If inputs match, prompts a confirmation for deleting book
                        clear_screen()
                        dlt_confirm = str(input(f"Are you sure to delete '{dlt_title}' by '{dlt_author}' from your library? (Y/N): ")).upper()
                        dlt_confirm = check_cont(dlt_confirm, "Invalid confirmation.\nPlease re-enter confirmation (Y/N): ")
                    
                        if dlt_confirm.upper() == 'N':
                            # In the case where user changes their mind (no longer deleting the book)
                            clear_screen()
                            print(f"'{dlt_title}' by '{dlt_author}' will not be deleted.\n")

                            # Asks user if they want to delete another book
                            dlt_cont = get_delete_confirmation()
                        
                        elif dlt_confirm == 'Y':
                            # In the case where user goes through with deleting the book record
                            dlt_book_idx = title.index(dlt_title)
                            for dlt_idx in range(8):    # There are 8 categories/info per book record
                                # Deletes each record from respective lists
                                del compiled[dlt_idx][dlt_book_idx]

                            # Informs user that the book has been deleted
                            clear_screen()
                            print(f"The book record titled '{dlt_title}' by '{dlt_author}' has been deleted.\n")
                            
                            # Asks user if they want to delete another book
                            dlt_cont = get_delete_confirmation()


        # OPTION 3: EDIT BOOK RECORD(S)
        elif action_choice == 3:
            clear_screen()
            print("You chose to update/edit a book record!")

            edit_cont = 'Y'

            while edit_cont.upper() == 'Y':
                # Checks if the book is found; the book is not found in the beginning
                book_found = False
                
                while True:     # Loops the prompt question of how user would like to find the book to edit
                    try:
                        # Prompts user to choose how they want to find the book
                        print("How would you like to find the book?\n"
                              "[1] ISBN\n"
                              "[2] Author and Title")
                        edit_choice = int(input("Enter (1/2): "))
                    
                    except ValueError:
                        clear_screen()
                        print("Invalid input. Please enter 1 or 2.")
                    
                    else:
                        while edit_choice != 1 and edit_choice != 2:
                            # Re-prompt question if user did not choose between 1 or 2
                            clear_screen()
                            print("Invalid input. Please enter 1 or 2.")
                            edit_choice = int(input("Enter (1/2): "))
                        
                        # User finds the book by ISBN number
                        if edit_choice == 1:
                            clear_screen()
                            while True:
                                try:
                                    edit_find_ISBN = int(input("Enter ISBN number: "))

                                except ValueError:
                                    # Handling error when ISBN entered is not an int
                                    clear_screen()
                                    print("ISBN consists of 13-digit numbers.")
                                
                                else:
                                    if len(str(edit_find_ISBN)) != 13:
                                        # In the case where ISBN entered is not 13-digits long (standard ISBN length)
                                        clear_screen()
                                        print("ISBN consists of 13-digit numbers.")
                                    
                                    else:
                                        if int(edit_find_ISBN) < 0:
                                            # In the case where a 13-digit negative int is entered
                                            clear_screen()
                                            print("Invalid ISBN input.")
                                        
                                        else:
                                            if str(edit_find_ISBN) not in ISBN:
                                                # In the case where the ISBN number does not exist in record system
                                                clear_screen()
                                                print("This book is not found in your record.")
                                            
                                            else:
                                                # The book is found
                                                clear_screen()
                                                chosen_book = ISBN.index(str(edit_find_ISBN))
                                                print(f"The book titled '{title[chosen_book]}' by {author[chosen_book]} is found.\n")
                                                book_found = True       # The book is now found
                                                break
                                            

                        # User finds the book by author and title
                        elif edit_choice == 2:
                            clear_screen()
                            while True:
                                edit_find_title = str(input("Enter book title (case sensitive): "))
                                edit_find_author = str(input("Enter author name (case sensitive): "))
                                
                                # Check if user's inputs match with existing list
                                if (edit_find_title not in title) or (edit_find_author not in author):
                                    clear_screen()
                                    print("Book not found! Please enter again.")
                                    
                                else:
                                    # In the case where inputs exist in list but do not belong to the same book (different index)
                                    if title.index(edit_find_title) != author.index(edit_find_author):
                                        clear_screen()
                                        print("The author and title does not match!")

                                    else:
                                        # Inputs match, prompts message that book is found
                                        clear_screen()
                                        chosen_book = author.index(edit_find_author)
                                        print(f"The book titled '{title[chosen_book]}' by {author[chosen_book]} is found.\n")
                                        book_found = True       # The book is now found
                                        break
                    
                    if book_found == True:
                        # Breaks out of the prompt question loop when the book is found, then moves on to the editing step
                        break


                editing_book = 'Y'

                while editing_book.upper() == 'Y':
                    try:
                        # Displays a list of editing options to the user
                        print("Edit Book Record(s):\n"
                          "[1] ISBN\n"
                          "[2] Author\n"
                          "[3] Title\n"
                          "[4] Publisher\n"
                          "[5] Genre\n"
                          "[6] Year published\n"
                          "[7] Date purchased\n"
                          "[8] Reading status")
                        edit_option = int(input("What would you like to edit for this book? (1-8): "))
                        
                        

                    except ValueError:
                        # Handling error when input is not an int
                        clear_screen()
                        print("Invalid input! Please try again.")

                    else:
                        while edit_option not in range(1,9):
                            # The accepted input is within the range of 1-8
                            # User input other than 1-8 will re-prompt question statement
                            clear_screen()
                            print("Invalid input! Please try again.")
                            print("Edit Book Record(s):\n"
                                  "[1] ISBN\n"
                                  "[2] Author\n"
                                  "[3] Title\n"
                                  "[4] Publisher\n"
                                  "[5] Genre\n"
                                  "[6] Year published\n"
                                  "[7] Date purchased\n"
                                  "[8] Reading status")
                            edit_option = int(input("What would you like to edit for this book? (1-8): "))
                            
                        if edit_option == 1:
                            clear_screen()
                            while True:
                                try:
                                    edit_ISBN = int(input("Enter ISBN number: "))

                                except ValueError:
                                    # Handling error when ISBN entered is not an int
                                    clear_screen()
                                    print("ISBN consists of 13-digit numbers.")
                                
                                else:
                                    if len(str(edit_ISBN)) != 13:
                                        # In the case where ISBN entered is not 13-digits long (standard ISBN length)
                                        clear_screen()
                                        print("ISBN consists of 13-digit numbers.")
                                    
                                    elif len(str(edit_ISBN)) == 13:
                                        # Replaces the original ISBN number with newly input ISBN number
                                        clear_screen()
                                        compiled[0][chosen_book] = str(edit_ISBN)
                                        print("ISBN number has been edited.\n")
                                        break


                        elif edit_option == 2:
                            clear_screen()
                            edit_author = str(input("Enter author name: "))
                            edit_author = check_empty(edit_author, "Author name")

                            # Replaces the original author name with newly input author name
                            compiled[1][chosen_book] = str(edit_author)
                            print("Author name has been edited.\n")


                        elif edit_option == 3:
                            clear_screen()
                            edit_title = str(input("Enter book title: "))
                            edit_title = check_empty(edit_title, "Book Title")
                            
                            # Replaces the original book title with newly input book title
                            compiled[2][chosen_book] = str(edit_title)
                            print("Book title has been edited.\n")
                        

                        elif edit_option == 4:
                            clear_screen()
                            edit_publisher = str(input("Enter publisher: "))
                            edit_publisher = check_empty(edit_publisher, "Publisher")

                            # Replaces the original publisher with newly input publisher
                            compiled[3][chosen_book] = str(edit_publisher)
                            print("Publisher has been edited.\n")


                        elif edit_option == 5:
                            clear_screen()
                            edit_genre = str(input("Enter genre: "))
                            edit_genre = check_empty(edit_genre, "Genre")

                            # Replaces the original genre with newly input genre
                            compiled[4][chosen_book] = str(edit_genre)
                            print("Book genre has been edited.\n")


                        elif edit_option == 6:
                            clear_screen()
                            year_format = '%Y'      # The accepted year published format is YYYY
                            while True:
                                try:
                                    edit_year_published = int(input("Enter year published (YYYY): "))     # User enters the year published
                                    datetime.datetime.strptime(str(edit_year_published), year_format)     # Checking for the year formatting

                                except ValueError:
                                    # Handling if the year formatting is wrong
                                    clear_screen()
                                    print("Year format should be YYYY.")
                                
                                else:
                                    today = datetime.datetime.now()
                                    current_year = today.strftime("%Y")
                                    
                                    if int(edit_year_published) > int(current_year):
                                        # Rejects if the year published is in the future
                                        clear_screen()
                                        print("Year published cannot be in the future. Please enter again.")

                                    else:
                                        # Replaces the original year published with newly input year published
                                        clear_screen()
                                        compiled[5][chosen_book] = str(edit_year_published)
                                        print("Year purchased has been edited.\n")
                                        break


                        elif edit_option == 7:
                            clear_screen()
                            date_format = '%d-%m-%Y'    # The accepted date format is DD-MM-YYYY
                            year_published_original = year_published[chosen_book]

                            while True:
                                try:
                                    edit_date_purchased = input("Enter date purchased (DD-MM-YYYY): ")      # User enters the date purchased
                                    datetime.datetime.strptime(edit_date_purchased, date_format)            # Checking for the date formatting
                            
                                except ValueError:
                                    # Handling error if the date formatting is wrong
                                    clear_screen()
                                    print("Date format should be DD-MM-YYYY.")
                                
                                else:
                                    today = datetime.datetime.now()
                                    year_purchased = edit_date_purchased[6:10]      # Extracts only the year in YYYY format
                                    current_date = today.strftime("%Y%m%d")         # Today's date in YYYYMMDD format
                                    check_date_purchased = edit_date_purchased[6:10], edit_date_purchased[3:5], edit_date_purchased[0:2]
                                    check_date = ''.join(check_date_purchased)      # Changing the entered date format to YYYYMMDD
                                
                                    if int(year_purchased) < int(year_published_original):
                                        # Rejects if the date purchased is before published year
                                        clear_screen()
                                        print("Date purchased cannot be earlier than year published. Please enter again.")
                            
                                    elif int(check_date) > int(current_date):
                                        # Rejects if the date purchased entered is after today's date
                                        clear_screen()
                                        print("Your purchase date is in the future! Please enter again.")
                        
                                    else:
                                        # Replaces the original date purchased with newly input date purchased
                                        clear_screen()
                                        compiled[6][chosen_book] = str(edit_date_purchased)
                                        print("Date purchased has been edited.\n")
                                        break


                        elif edit_option == 8:
                            clear_screen()
                            edit_status = str(input("Enter reading status (to-read/reading/read): "))
                            edit_status = check_empty(edit_status, "Reading status")
                            while (edit_status != 'to-read') and (edit_status != 'reading') and (edit_status != 'read'):
                                # If status entered is invalid
                                clear_screen()
                                print("Reading status can only be 'to-read', 'reading', or 'read'.")
                                edit_status = str(input("Enter reading status (to-read/reading/read): "))
                            
                            # Replaces the original reading status with newly input reading status
                            clear_screen()
                            compiled[7][chosen_book] = str(edit_status)
                            print("Book reading status has been edited.\n")


                        # Asks if user wants to edit another info from the same book
                        editing_book = input(f"Do you want to edit another info of the same book? (Y/N): ").upper()
                        editing_book = check_cont(editing_book, "Invalid input. Please enter again (Y/N): ")
                        if editing_book.upper() == 'Y':
                            clear_screen()
                        elif editing_book.upper() == 'N':
                            clear_screen()
                
                # Asks if user wants to edit another book
                edit_cont = str(input("Would you like to edit another book? (Y/N): ")).upper()
                edit_cont = check_cont(edit_cont, "Invalid input. Please enter again.\nWould you like to edit another book? (Y/N): ")
                edit_cont = return_to_menu(edit_cont)



        # OPTION 4: DISPLAY
        elif action_choice == 4:
            while True:
                if not compiled[0]:
                    # If there are no books in the system
                    clear_screen()
                    print("There are no books found in the system!\n")
                    input("Enter any key to return to main menu: ")
                    break
                
                else:
                    clear_screen()

                    # Display column headings
                    headings = ["No.", "ISBN", "Author", "Title", "Publisher", "Genre", "Year Published", "Date Purchased", "Status"]
                    header_line = "|{:^4}|  {:^13}  |  {:^11} |  {:^15}  |  {:^12}  |  {:^13}  |  {:^14}  |  {:^14}  | {:^7} |".format(*headings)
                    print("=" * len(header_line))
                    print(header_line)
                    print("=" * len(header_line))

                    # Wrap text for data that exceed the width of column
                    for i in range(len(compiled[0])):
                        wrapped_author = wrap_text(compiled[1][i], width=11)
                        wrapped_title = wrap_text(compiled[2][i], width=15)
                        wrapped_publisher = wrap_text(compiled[3][i], width=12)
                        wrapped_genre = wrap_text(compiled[4][i], width=13)

                        # Display data for the book (first line for info thats needs text wrapping)
                        data_line = "|{:^4}|  {:^13}  |  {:^11} |  {:^15}  |  {:^12}  |  {:^13}  |  {:^14}  |  {:^14}  | {:^7} |".format(
                            (i + 1), compiled[0][i], wrapped_author[0], wrapped_title[0], wrapped_publisher[0],
                            wrapped_genre[0], compiled[5][i], compiled[6][i], compiled[7][i])
                        print(data_line)

                        # Display the additional wrapped lines
                        for author_line in wrapped_author[1:]:
                            author_line = "|{:^4}|  {:^13}  |  {:^11} |  {:^15}  |  {:^12}  |  {:^13}  |  {:^14}  |  {:^14}  | {:^7} |".format(
                                "", "", author_line, "", "", "", "", "", "")
                            print(author_line)

                        for title_line in wrapped_title[1:]:
                            title_line = "|{:^4}|  {:^13}  |  {:^11} |  {:^15}  |  {:^12}  |  {:^13}  |  {:^14}  |  {:^14}  | {:^7} |".format(
                                "", "", "", title_line, "", "", "", "", "")
                            print(title_line)

                        for publisher_line in wrapped_publisher[1:]:
                            publisher_line = "|{:^4}|  {:^13}  |  {:^11} |  {:^15}  |  {:^12}  |  {:^13}  |  {:^14}  |  {:^14}  | {:^7} |".format(
                                "", "", "", "", publisher_line, "", "", "", "")
                            print(publisher_line)

                        for genre_line in wrapped_genre[1:]:
                            publisher_line = "|{:^4}|  {:^13}  |  {:^11} |  {:^15}  |  {:^12}  |  {:^13}  |  {:^14}  |  {:^14}  | {:^7} |".format(
                                "", "", "", "", "", genre_line, "", "", "")
                            print(publisher_line)

                        # Display a separator line
                        print("–" * len(header_line))

                    print(f"Your current book record consists of {len(title)} books.\n")

                    # Entering any key will bring user back to the main menu after they are done with the display
                    input("Enter any key to return to main menu: ")
                    break
            
            # Clears screen and prints the main menu before returning to the beginning [1-6] options
            clear_screen()
            print_menu()



        # OPTION 5: SEARCH FOR BOOK(S)
        elif action_choice == 5:
            clear_screen()
            print("You chose to search for a book record!")

            search_cont = 'Y'

            while search_cont == 'Y':
                # Prompts user to enter the ISBN number, author, and title of the book

                while True:
                    try:
                        search_ISBN = str(input("Enter ISBN number of book: "))
                    
                    except ValueError:
                        # Handling error when ISBN entered is not an int
                        clear_screen()
                        print("ISBN consists of 13-digit numbers.")

                    else:
                        if len(str(search_ISBN)) != 13:
                            # In the case where ISBN entered is not 13-digits long (standard ISBN length)
                            clear_screen()
                            print("ISBN consists of 13-digit numbers.")
                        
                        else:
                            if int(search_ISBN) < 0:
                                # In the case where a 13-digit negative int is entered
                                clear_screen()
                                print("Invalid ISBN input.")
                            
                            else:
                                # When the ISBN input is valid, breaks out of the loop
                                break                    

                clear_screen()
                search_author = str(input("Enter author name (case sensitive): "))
                
                clear_screen()
                search_title = str(input("Enter book title (case sensitive): "))


                # Validating user's input
                if (search_ISBN not in ISBN) or (search_author not in author) or (search_title not in title):
                    # The input does not exist in record
                    clear_screen()
                    print("Book not found. Please enter a valid ISBN, author, and title of the book.")

                else:
                    # If the input exists in record, check if they are from the same book
                    if ISBN.index(search_ISBN) == author.index(search_author) == title.index(search_title):
                        search_book_idx = ISBN.index(search_ISBN)

                        # Display search result
                        clear_screen()
                        print("Book found.\nHere is the information of your book:\n"
                              f"{'ISBN number':<15}: {ISBN[search_book_idx]}\n"
                              f"{'Author':<15}: {author[search_book_idx]}\n"
                              f"{'Title':15}: {title[search_book_idx]}\n"
                              f"{'Publisher':<15}: {publisher[search_book_idx]}\n"
                              f"{'Year published':<15}: {year_published[search_book_idx]}\n"
                              f"{'Book genre':<15}: {genre[search_book_idx]}\n"
                              f"{'Date purchased':<15}: {date_purchased[search_book_idx]}\n"
                              f"{'Reading status':<15}: {status[search_book_idx]}")
                        
                        # Asks if user wants to search for another book
                        search_cont = str(input("\nDo you want to search for another book? (Y/N): ")).upper()
                        search_cont = check_cont(search_cont, "Invalid input. Please enter again.\nDo you want to search for another book? (Y/N): ")
                        search_cont = return_to_menu(search_cont)
                    
                    else:
                        # If the input exists in record, but is not from the same book
                        clear_screen()
                        print("The details entered do not match to the same book. Please try again.")



        # OPTION 6: EXIT
        elif action_choice == 6:
            # Updates/Rewrites the book data into the txt file
            final_list = len(title)             # Calculating the total number of books in record (list) after making actions
            
            with open("books_catalogue.txt", "w") as edit_library:
                for book_idx in range(final_list):
                    if book_idx != (final_list - 1):
                        # Prints the new book list while adding new line at the end of the information
                        final_book_info = (f"{ISBN[book_idx]}; {author[book_idx]}; {title[book_idx]}; {publisher[book_idx]}; {genre[book_idx]}; {year_published[book_idx]}; {date_purchased[book_idx]}; {status[book_idx]}\n")
                        edit_library.write(final_book_info)
                    else:
                        # (book_idx) counts from 0; the length of (final_list) counts from 1
                        # so, the last (book_idx) will be == (final_list - 1)
                        # If it's the last row of the book list, then will not add new line at the end of the information
                        final_book_info = (f"{ISBN[book_idx]}; {author[book_idx]}; {title[book_idx]}; {publisher[book_idx]}; {genre[book_idx]}; {year_published[book_idx]}; {date_purchased[book_idx]}; {status[book_idx]}")
                        edit_library.write(final_book_info)

                # Closing the updated .txt file
                edit_library.close()

                # Displays final message & exit timestamp to user before the program ends
                clear_screen()
                exit_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print(f"Your book record has been successfully updated at {exit_time}!")

                # Ends the program after user finishes in making changes/updates to the book record
                # No prompting is required as user has explicitly chosen '[6] Exit' to exit/end the program
                system_cont = 'N'