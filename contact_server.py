from addressbook_pb2 import *

class Contact():

  contacts = []

  def AddContact(self, name, id):
    person = Person()
    person.id = id
    person.name = name

  def ShowContacts(self, name, id):
    for contact in Contact.contacts:
        print "ID:" + contact.id
        print "Name" + contact.name
        print "----"

def serve():
  server = helloworld_pb2.early_adopter_create_Greeter_server(
      Greeter(), 50051, None, None)
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop()

if __name__ == '__main__':
  serve()
