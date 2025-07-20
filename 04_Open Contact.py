def open_contact(contacts, name):
  for i in range(len(contacts)):
    if contacts[i]['name'] == name:
      print(contacts[i])




name = 'sandesh'
open_contact(contacts, name)




We often see *update* & *delete* options after we open a particular contact. It would be great if we can also implement the same.

After opening the contact, the program should wait for user input. The user can press `u` to update & `d` delete contact. Any other key press should be ignored

Write the updated `open_contact` function below

def open_contact(contacts, name):
  ip = input()
  if ip == 'u':
    update_contact(contacts, name)
  elif ip == 'd':
    delete_contact(contacts, name)

 

data = str(contacts)
with open('contacts.txt','w') as f:
  f.write(data)
