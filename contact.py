y=0
contacts=[]
while y==0:
    print("---Menu----")
    print("1->For insert contact")
    print("2->For display contact")
    print("3->For delete contact")
    print("4->For update contact")
    opt=int(input("Enter your option"))
    if(opt==1):
        name=input("Enter Name")
        email=input("Enter Email")
        mobile=input("Enter Mobile")
        #print(name+" "+email+" "+mobile)
        contacts.append((name,email,mobile))
    if opt==2:
        #print(contacts)
        for item in contacts:
            print(item[0]+" "+item[1]+" "+item[2])
    y=int(input("Do You wnat to continue? press 0 for yes"))
