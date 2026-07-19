from helper import *
from fileop import *
load_contact()
while y==0:
    opt=menu()
    if(opt==1):
        create_contact()
    if opt==2:
        display_contact()
    if opt==3:
       del_contact()
    if opt==4:
        update_contact()
    y=int(input("Do You wnat to continue? press 0 for yes"))
    if(y!=0):
        c=get_contacts()
        contact_write(c)