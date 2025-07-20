def update_contact(contacts, name):
  for i in range(len(contacts)):
    if contacts[i]['name'] == name:
      name, number, email = input().split()
      contacts[i]['name'] = name
      contacts[i]['number'] = number
      contacts[i]['email'] = email




name = 'mahesh'
update_contact(contacts, name)
