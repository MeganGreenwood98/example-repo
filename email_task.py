"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.


class Email:
    """
        A class representing an email.

    Arguments::
        email_Address (str): The email address of the sender.
        subject_line (str): The subject line of the email
        email_content (str): The contents of the email

    Methods:
        __init__(email_address, subject_line, email_content):
            Initializes a new email
    """
    # Create the 'mark_as_read()' method to change the 'has_been_read'



# Initialise the instance variables for each email.
# Constructor method
    def __init__(self, email_address, subject_line, email_content):
        """Initializes a new email instance."""
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False


    # instance variable for a specific object from False to True.
    # Changes mark_as read to true when it has been read
    def mark_as_read(self):
        self.has_been_read = True

    #Keeps email unread
    def mark_as_unread(self):
        self.has_been_read = False


# --- Functions --- #
# Build out the required functions for your program.


def populate_inbox():
    # Create 3 sample emails and add them to the inbox list.
    megan = Email("megan.g@hotmail.co.uk", "Hello", "How are you?")
    rhys = Email("r.j@live.co.uk", "Decision", "True or False?")
    mum = Email("mum@gmail.com", "Food", "What's for tea?")
    inbox.extend([megan, rhys, mum])


def list_emails():
    # Create a function that prints each email's subject line
    # alongside its corresponding index number,
    # regardless of whether the email has been read.
    for index, name in enumerate(inbox):
        print(f"{index}      {name.subject_line}")


def read_email(index):
    # Create a function that displays the email_address, subject_line,
    # and email_content attributes for the selected email.
    # After displaying these details, use the 'mark_as_read()' method
    # to set its 'has_been_read' instance variable to True.
    email = inbox[index]
    print(f"Email Address: {email.email_address}")
    print(f"Subject Line: {email.subject_line}")
    print(f"Email Content:{email.email_content}")
    email.mark_as_read()
    print(f"\n Email from {email.email_address} marked as read. \n")
    #for index, self in inbox:
    #    print(f"{self.email_address} {self.subject_line}")
    #    self.has_been_read = True


def view_unread_emails():
    # Create a function that displays all unread Email object subject lines
    # along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.
    print("\n Unread emails: ")
    unread_found = False
    for index, name in enumerate(inbox):
        if not name.has_been_read:
            print(f"{index}     {name.subject_line}")
            unread_found = True
    if not unread_found:
        print("No unread emails")


# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.
inbox = []

# Sample emails


# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.

# Display the menu options for each iteration of the loop.
while True:
    user_choice = (
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == "1":
        # Add logic here to read an email
        list_emails()
        try:
            index = int(input("Enter which email you would like to read: "))
            if 0 <= index < len(inbox):
                read_email(index)
            else:
                print("Please enter a valid email number: ")
        except ValueError:
            print("Invalid Input. Enter a number.")

    elif user_choice == "2":
        # Add logic here to view unread emails
        view_unread_emails()

    elif user_choice == "3":
        # Add logic here to quit application.
        break

    else:
        print("Oops - incorrect input.")
