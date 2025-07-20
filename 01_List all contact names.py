## your code here
contacts = [{'name': 'sandesh', "number":11111111111, 'email': 'sandesh@gmail.com' },
            {'name': 'rohit', "number":2222222222, 'email': 'rohit@gmail.com' },
             {'name': 'mahesh', "number":3333333333, 'email': 'mahesh@gmail.com' }]

### List all contact names
Write `show_contacts` function that takes the `contacts` list and prints all the contact names. These names will help us to select the contact later.

def show_contacts(contacts):
    ## your code here
    print(contacts)

#regex patterns
import re
p_name = r'[a-zA-Z]+'
p_email = r'[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]'
p_number = r'[0-9]+{10}'


show_contacts(contacts)
