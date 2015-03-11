import addressbook_pb2

_TIMEOUT_SECONDS = 10

# Iterates though all people in the AddressBook and prints info about them.
def ListPeople(address_book):
  for person in address_book.person:
    print "\nPerson ID:", person.id
    print "  Name:", person.name
    if person.HasField('email'):
      print "  E-mail address:", person.email

    for phone_number in person.phone:
      if phone_number.type == addressbook_pb2.Person.MOBILE:
        print "  Mobile phone #:",
      elif phone_number.type == addressbook_pb2.Person.HOME:
        print "  Home phone #:",
      elif phone_number.type == addressbook_pb2.Person.WORK:
        print "  Work phone #:",
      print phone_number.number

# This function fills in a Person message based on user input.
def PromptForAddress(person):
    person.id = int(raw_input("Enter person ID number: "))
    person.name = raw_input("Enter name: ")

    email = raw_input("Enter email address (blank for none): ")
    if email != "":
        person.email = email

    while True:
        number = raw_input("Enter a phone number (or leave blank to finish): ")
        if number == "":
            break
        phone_number = person.phone.add()
        phone_number.number = number

        type = raw_input("Is this a mobile, home, or work phone? ")
        if type == "mobile":
            phone_number.type = addressbook_pb2.Person.MOBILE
        elif type == "home":
            phone_number.type = addressbook_pb2.Person.HOME
        elif type == "work":
            phone_number.type = addressbook_pb2.Person.WORK
        else:
            print "Unknown phone type; leaving as default value."

with addressbook_pb2.early_adopter_create_Contacts_stub('localhost', 50051) as stub:
    message = addressbook_pb2.TextMessage()
    message.text = 'test'

    while True:
        print "\n*** Address Book Contact Management ***"
        print "Options:"
        print "  1) Add a Contact"
        print "  2) List all Contacts"
        option = str(raw_input("Enter 1 or 2, or any other key to quit: "))
        if ("1" == option):
            person = addressbook_pb2.Person()
            PromptForAddress(person)
            response = stub.AddContact(person, _TIMEOUT_SECONDS)
            print response.text
        elif ("2" == option):
            address_book = stub.ListContacts(message, _TIMEOUT_SECONDS)
            ListPeople(address_book)
        else:
            break