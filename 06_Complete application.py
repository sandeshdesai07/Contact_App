from IPython.display import clear_output

while True:

    ## show all contacts

    action = input("Press 'a' - add contact, 'o' - open contact, 's' - search contact, 'q' - quit")
    if action == 'a':
      add_contact(contacts)
        ## add contact

    elif action == 'o':
        name = input("Enter name of the contact you want to open. ")
        open_contact(contacts, name)
        ## open contact

    elif action == 'q':
      break
        ## break

    else:
        ## print incorrect choice
        print('print incorrect choice')
