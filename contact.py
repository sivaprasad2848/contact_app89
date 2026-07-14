y=0
contacts=[]
while y==0:
    name=input("Enter Name")
    email=input("Enter Email")
    mobile=input("Enter Mobile")
    #print(name+" "+email+" "+mobile)
    contacts.append((name,email,mobile))
    print(contacts)
    y=int(input("Do You wnat to continue? press 0 for yes"))
