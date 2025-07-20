def add_contact(contacts):
  c = 0
  name ,number, email = input().split()
  d = {}
  if re.match(p_name, name):
    c += 1
    d['name'] = name

  elif re.match(p_email, name):
    c += 1
    d['name'] = email

  elif re.match(p_number, name):
    c += 1
    d['name'] = number

  if c==3:
    contacts.append(d)

  else:
    print('wrong input, try again')




  



add_contact(contacts)
