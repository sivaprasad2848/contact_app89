def contact_write(contacts):
    fp=open("contact_details","a")
    for item in contacts:
        line=item[0]+"#"+item[1]+"#"+item[2]+"\n"
        fp.write(line)
    fp.close()
def contact_read():
    contacts = []

    with open("contact_details", "r") as file:
        for line in file:
            name, email, mobile = line.strip().split("#")

            contacts.append({
                "name": name,
                "email": email,
                "mobile": mobile
            })

    return contacts

