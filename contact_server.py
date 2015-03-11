import time
import addressbook_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Contact():

    def AddContact(self, newentry, rpc_controller):
        address_book = addressbook_pb2.AddressBook()
        # Read the existing address book.
        f = open("addressbook.txt", "rb")
        address_book.ParseFromString(f.read())
        f.close()

        # Add an address.
        address_book.person.extend([newentry])

        # Write the new address book back to disk.
        f = open("addressbook.txt", "wb")
        f.write(address_book.SerializeToString())
        f.close()
        message = addressbook_pb2.TextMessage()
        message.text = "Contact added successfully"
        return message

    def ListContacts(self, rpc_controller, message):
        address_book = addressbook_pb2.AddressBook()
        # Read the existing address book.
        f = open("addressbook.txt", "rb")
        address_book.ParseFromString(f.read())
        f.close()
        return address_book

    def FindContact(self, searchmessage, rpc_controller):
        address_book = addressbook_pb2.AddressBook()
        f = open("addressbook.txt", "rb")
        address_book.ParseFromString(f.read())
        f.close()
        for person in address_book.person:
            if (person.name.strip() == searchmessage.text.strip()) :
                return person
        dummy = addressbook_pb2.Person()
        dummy.id = 0
        dummy.name = ""
        return dummy

def serve():
    server = addressbook_pb2.early_adopter_create_Contacts_server(Contact(), 50051, None, None)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop()

if __name__ == '__main__':
    serve()
