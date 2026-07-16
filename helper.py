y=0
contacts=[]
def create_contact():
    name=input("Enter Name")
    email=input("Enter Email")
    mobile=input("Enter Mobile")
    #print(name+" "+email+" "+mobile)
    contacts.append((name,email,mobile))
def del_contact():
    id=int(input("Enter the ID you want to delete"))
    del contacts[id]
    print("Contact Deleted")
def update_contact():
    id=int(input("Enter the ID you want to update"))
    name=input("Enter Name")
    email=input("Enter Email")
    mobile=input("Enter Mobile")
    contacts[id]=(name,email,mobile)
    print("Contact Updated")
def display_contact():
    #print(contacts)
    for item in contacts:
        print(item[0]+" "+item[1]+" "+item[2])
def menu():
    print("---Menu----")
    print("1->For insert contact")
    print("2->For display contact")
    print("3->For delete contact")
    print("4->For update contact")
    op=int(input("Enter your option"))
    return op