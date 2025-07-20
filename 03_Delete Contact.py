show_contacts(contacts)

def delete_contact(contacts, name):

    #your code here
    for i in range(len(contacts)):
      if contacts[i]['name'] == name:
        contacts.pop(i)



name = input()
delete_contact(contacts, name)

show_contacts(contacts)
